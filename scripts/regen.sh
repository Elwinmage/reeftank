#!/bin/bash
#
# Regenerate every generated file of the ReefTech ecosystem.
#
# Run from the directory holding every checkout side by side:
#
#     bash reeftank/scripts/regen.sh
#
# It ends by listing what changed and offering to commit and push each
# repository on its current branch. Only the paths the generators own are
# staged; anything else that is dirty is named but left alone. Set
# REGEN_MESSAGE to preset the commit message. Piped or run from cron, it
# reports and stops without committing.
#
# Two families of generators, and that is what dictates the order:
#
#   * Per-repo generators rewrite whole files, from their own repository root.
#   * Cross-repo generators inject blocks between markers into files spread
#     across several repositories, from the parent directory.
#
# Per-repo first: a file created here for a language that did not exist yet
# would otherwise miss its shared block until the next run.
#
# Since the gen_readme.py scripts preserve an existing ecosystem block, a
# single one can be re-run on its own; the order only matters on a first
# generation.
#
# Not run here: ha-reef-maintenance-component/scripts/gen_translations.py,
# which regenerates the *integration* strings rather than documentation. Run
# it after touching the task library.

set -euo pipefail

# Every repository this script writes into. Checked up front so a missing
# checkout is reported before anything is half-written.
REPOS=(
  ha-reef-blueprints
  ha-reef-maintenance-component
  ha-reefbeat-component
  ha-aquamedic-component
  ha-reef-card
  reefbeatEnergyBackup
  reeftank
)

missing=()
for repo in "${REPOS[@]}"; do
  [ -d "$repo" ] || missing+=("$repo")
done
if [ ${#missing[@]} -gt 0 ]; then
  echo "Missing checkouts: ${missing[*]}" >&2
  echo "Run this from the directory holding every repository." >&2
  exit 1
fi

step() { printf '\n=== %s\n' "$1"; }

# ---------------------------------------------------------------------------
# 1. Per-repo generators
# ---------------------------------------------------------------------------

step "Blueprints (8 languages)"
(cd ha-reef-blueprints && python3 scripts/gen_blueprints.py)

step "Blueprints README (8 languages)"
(cd ha-reef-blueprints && python3 scripts/gen_readme.py)

step "Maintenance README (8 languages)"
(cd ha-reef-maintenance-component && python3 scripts/gen_readme.py)

# ---------------------------------------------------------------------------
# 2. Cross-repo generators
# ---------------------------------------------------------------------------

step "Documentation site (7 pages)"
python3 reeftank/scripts/gen_site.py

step "Related projects block (40 files, 6 repositories)"
python3 reeftank/scripts/gen_ecosystem.py

# ---------------------------------------------------------------------------
# 3. Checks and formatting
# ---------------------------------------------------------------------------

step "Validate the blueprints"
(cd ha-reef-blueprints && python3 scripts/check_blueprints.py)

# ha-reef-card is the only repository whose markdown is under prettier, and
# the injected block leaves it non-conforming. Skipped when npx is absent so
# the script still works without a Node toolchain.
if command -v npx >/dev/null 2>&1; then
  step "Format the card markdown"
  (cd ha-reef-card && npx --yes prettier --write README.md doc/*/README.*.md >/dev/null)
else
  printf '\n=== Skipping prettier: npx not found\n' >&2
  echo "    Run it in ha-reef-card before committing." >&2
fi

# ---------------------------------------------------------------------------
# 4. Report and offer to push
# ---------------------------------------------------------------------------

# Paths these generators own. Only these are staged: sweeping everything with
# `git add -A` would drag work in progress into a documentation commit.
generated_paths() {
  local repo="$1" candidates existing=""
  case "$repo" in
    reeftank)
      candidates="index.md fr.md de.md es.md it.md pl.md pt.md _config.yml" ;;
    ha-reef-blueprints)
      candidates="README.md doc blueprints/automation" ;;
    *)
      candidates="README.md README.fr.md doc" ;;
  esac
  # Only the paths that exist: `git add` fails on a missing pathspec, and not
  # every repository has a doc/ directory or a French README.
  for path in $candidates; do
    [ -e "$repo/$path" ] && existing="$existing $path"
  done
  echo "$existing"
}

commit_message="${REGEN_MESSAGE:-docs: regenerate}"
interactive=1
[ -t 0 ] || interactive=0

printf '\n'
changed_repos=()
for repo in "${REPOS[@]}"; do
  [ -d "$repo/.git" ] || continue
  # Resolved here, in the parent: inside the subshell below the cwd is the
  # repository, and the existence test in generated_paths would look for
  # "<repo>/<repo>/..." and come back empty -- staging nothing at all.
  paths=$(generated_paths "$repo")
  [ -n "$paths" ] || continue
  status=$(cd "$repo" && git status --porcelain -- $paths 2>/dev/null || true)
  # -x: whole-line match. Without it a path that is a substring of another
  # would wrongly be treated as already listed and never reported.
  other=$(cd "$repo" && git status --porcelain | grep -vxF "$status" 2>/dev/null || true)

  [ -n "$status" ] || continue
  changed_repos+=("$repo")

  branch=$(cd "$repo" && git rev-parse --abbrev-ref HEAD)
  printf '=== %s (branch %s)\n' "$repo" "$branch"
  echo "$status" | sed 's/^/    /'

  # Anything else that is dirty is named but never staged, so it cannot be
  # swept into the commit without the user noticing.
  if [ -n "$other" ] && [ "$other" != "$status" ]; then
    printf '    -- not staged (outside the generated paths):\n'
    echo "$other" | sed 's/^/       /'
  fi
  printf '\n'
done

if [ ${#changed_repos[@]} -eq 0 ]; then
  echo "Nothing changed."
  exit 0
fi

if [ "$interactive" -eq 0 ]; then
  echo "Not a terminal: stopping without committing."
  exit 0
fi

read -r -p "Commit and push these to their current branch? [y/N] " answer
case "$answer" in
  [yY]|[yY][eE][sS]) ;;
  *) echo "Left uncommitted."; exit 0 ;;
esac

read -r -p "Commit message [${commit_message}]: " typed
[ -n "$typed" ] && commit_message="$typed"

failed=()
for repo in "${changed_repos[@]}"; do
  branch=$(cd "$repo" && git rev-parse --abbrev-ref HEAD)
  if [ "$branch" = "HEAD" ]; then
    echo "$repo: detached HEAD, skipped." >&2
    continue
  fi
  paths=$(generated_paths "$repo")
  printf '\n=== %s -> %s\n' "$repo" "$branch"
  # One repository failing -- no remote, rejected push, nothing staged -- must
  # not stop the others, so the subshell result is reported and swallowed.
  if (
    cd "$repo"
    git add -- $paths
    git commit -m "$commit_message"
    git push origin "$branch"
  ); then
    :
  else
    echo "$repo: not pushed, see the error above." >&2
    failed+=("$repo")
  fi
done

if [ ${#failed[@]} -gt 0 ]; then
  printf '\nDone, but these were not pushed: %s\n' "${failed[*]}" >&2
  exit 1
fi

printf '\nDone.\n'
