#!/usr/bin/env python3
"""Build the interactive project flower of the site, and its README image.

This file is the single source for the flower: the projects, their order,
links, relations and short texts. It provides:

  * site_html(), injected into the pages by gen_site.py;
  * README_IMAGE, shown above the Related projects table by gen_ecosystem.py;
  * the static assets of assets/flower/, when run as a script.

Usage, from the directory holding every checkout side by side::

    python3 reeftank/scripts/gen_flower.py

Adding a project: add it to PROJECTS, then give it a text in every language of
FLOWER_TEXT. gen_ecosystem.py refuses to run when its REPOS and PROJECTS differ.

The CSS and JS live in _includes/ecosystem-flower.html.
"""

from __future__ import annotations

import math
import sys
from html import escape
from pathlib import Path

GH = "https://github.com/Elwinmage/{repo}"
ASSETS = Path("assets/flower")

# Served from main: an image shared by eight repositories cannot be relative.
# A new version therefore only shows in the READMEs once merged.
README_IMAGE = (
    "https://raw.githubusercontent.com/Elwinmage/reeftank/main/"
    "assets/flower/ecosystem-flower.png"
)
README_IMAGE_ALT = "ReefTech project ecosystem"
README_IMAGE_WIDTH = 480

# Distance from the center to an icon, in % of the flower. Larger would push
# the labels of the bottom petals out of the box.
RADIUS = 36.0

THUMB_SIZE = 192

# White label text sits on these: keep a contrast of at least 4.5:1.
COLORS = {
    "display": "#0f7f47",
    "integration": "#1e6bb8",
    "infrastructure": "#a86a00",
    "content": "#c8431f",
}

# Clockwise from the top. Families stay contiguous, and neighbours are related
# where possible, so the ring reads as a map rather than a list. "url" is the
# click target: point it at a site anchor to keep visitors on the site.
PROJECTS: dict[str, dict[str, str]] = {
    "ha-reef-card": {"label": "Reef Card", "family": "display"},
    "ha-reefbeat-component": {"label": "ReefBeat", "family": "integration"},
    "ha-aquamedic-component": {"label": "Aqua Medic", "family": "integration"},
    "ha-reef-maintenance-component": {
        "label": "Maintenance",
        "family": "integration",
    },
    "ha-reef-blueprints": {"label": "Blueprints", "family": "infrastructure"},
    "reefbeatEnergyBackup": {"label": "Energy Backup", "family": "infrastructure"},
    "reeftank-catalog": {"label": "Catalog", "family": "content"},
    "ha-reeftank-component": {"label": "ReefTank", "family": "content"},
}
for _repo, _project in PROJECTS.items():
    _project.setdefault("url", GH.format(repo=_repo))

# Which projects light up together. Undirected: mirrors the "Works with"
# column of the Related projects table.
RELATIONS = [
    ("ha-reef-card", "ha-reefbeat-component"),
    ("ha-reef-card", "ha-aquamedic-component"),
    ("ha-reef-card", "ha-reef-maintenance-component"),
    ("ha-reef-card", "ha-reeftank-component"),
    ("ha-reef-card", "reefbeatEnergyBackup"),
    ("ha-reefbeat-component", "ha-reef-blueprints"),
    ("ha-aquamedic-component", "ha-reef-blueprints"),
    ("ha-reef-maintenance-component", "ha-reef-blueprints"),
    ("ha-reefbeat-component", "reefbeatEnergyBackup"),
    ("ha-reeftank-component", "reeftank-catalog"),
]

# A page gets its flower once its language is listed here.
FLOWER_TEXT: dict[str, dict[str, str]] = {
    "en": {
        "title": "ReefTech",
        "hint": "Eight projects that fit together. Each one also works on its own.",
        "open": "Open project",
        "nav": "ReefTech projects",
        "ha-reef-card": (
            "Interactive view of every device on your dashboard, and the only "
            "way to edit advanced schedules."
        ),
        "ha-reefbeat-component": (
            "Red Sea ReefBeat devices in Home Assistant, controlled locally "
            "with no cloud."
        ),
        "ha-aquamedic-component": (
            "Aqua Medic wavemakers, return and skimmer pumps in Home "
            "Assistant, through the Gizwits cloud API."
        ),
        "ha-reef-maintenance-component": (
            "Cleaning and wear tracking for the equipment Home Assistant "
            "cannot talk to."
        ),
        "ha-reef-blueprints": (
            "Shared notifications for overdue maintenance and for devices "
            "that went unreachable."
        ),
        "reefbeatEnergyBackup": (
            "Battery backup for outages, slowing your pumps progressively as "
            "the charge drops."
        ),
        "reeftank-catalog": (
            "Fish, corals and textures of the aquarium card, kept up to date "
            "automatically."
        ),
        "ha-reeftank-component": (
            "A living picture of your tank: your photo, your real lamps, "
            "animated fish and corals."
        ),
    },
}


def related(repo: str) -> list[str]:
    """Every project lit together with this one."""
    out = [b for a, b in RELATIONS if a == repo]
    out += [a for a, b in RELATIONS if b == repo]
    return out


def angle(index: int) -> float:
    """Clockwise angle of a petal, in degrees, 0 being the top."""
    return index * 360 / len(PROJECTS)


def center_of(index: int) -> tuple[float, float]:
    """Center of an icon, in % of the flower."""
    rad = math.radians(angle(index))
    return 50 + RADIUS * math.sin(rad), 50 - RADIUS * math.cos(rad)


def site_html(lang: str) -> str | None:
    """Render the flower for one page, or None if it has no texts yet."""
    t = FLOWER_TEXT.get(lang)
    if t is None:
        return None

    lines = [
        "{% include ecosystem-flower.html %}",
        "",
        f'<nav class="eco-flower" aria-label="{escape(t["nav"])}"'
        f' data-open="{escape(t["open"])}" data-hint="{escape(t["hint"])}">',
        '  <div class="eco-center">',
        f"    <strong>{escape(t['title'])}</strong>",
        f"    <span>{escape(t['hint'])}</span>",
        "  </div>",
    ]
    for index, (repo, project) in enumerate(PROJECTS.items()):
        x, y = center_of(index)
        src = f"{{{{ '/assets/flower/{repo}.webp' | relative_url }}}}"
        style = (
            f"--a:{angle(index):g}deg;--x:{x:.2f}%;--y:{y:.2f}%;"
            f"--c:{COLORS[project['family']]}"
        )
        lines += [
            f'  <a class="eco-petal" href="{escape(project["url"])}"'
            f' data-repo="{repo}" data-links="{" ".join(related(repo))}"'
            f' style="{style}">',
            f'    <img src="{src}" width="{THUMB_SIZE}" height="{THUMB_SIZE}"'
            ' alt="" loading="lazy" />',
            f'    <span class="eco-name">{escape(project["label"])}</span>',
            f'    <span class="eco-text"><strong>{repo}</strong>'
            f"<span>{escape(t[repo])}</span></span>",
            "  </a>",
        ]
    lines.append("</nav>")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Static assets. Pillow is imported here so that gen_site.py and
# gen_ecosystem.py keep working without it.
# --------------------------------------------------------------------------


def load_font(size: int):
    from PIL import ImageFont

    for name in (
        "DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "LiberationSans-Bold.ttf",
        "arialbd.ttf",
        "Arial Bold.ttf",
    ):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def rounded_icon(path: Path, size: int):
    """Load an icon cropped to its circle.

    Some icons are transparent outside the circle, others are opaque: the
    mask gives them all the same outline.
    """
    from PIL import Image, ImageDraw

    icon = Image.open(path).convert("RGBA")
    scale = 4
    mask = Image.new("L", (size * scale, size * scale), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * scale - 1, size * scale - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    icon = icon.resize((size, size), Image.LANCZOS)
    alpha = Image.composite(icon.getchannel("A"), Image.new("L", icon.size, 0), mask)
    icon.putalpha(alpha)
    return icon


def thumbnails(root: Path, out: Path) -> None:
    for repo in PROJECTS:
        target = out / f"{repo}.webp"
        rounded_icon(root / repo / "icon.png", THUMB_SIZE).save(
            target, "WEBP", quality=82, method=6
        )
        print("updated", target)


def readme_image(root: Path, out: Path) -> None:
    """Draw the flower as one transparent PNG.

    Labels sit on their own colored pills and the center on a white disc, so
    the image reads on the light and dark themes of GitHub alike.
    """
    from PIL import Image, ImageColor, ImageDraw

    final = 960
    scale = 2
    size = final * scale
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # Petals, drawn pointing up from the center and rotated in place.
    pw, ph = int(size * 0.21), int(size * 0.47)
    for index, project in enumerate(PROJECTS.values()):
        color = ImageColor.getrgb(COLORS[project["family"]])
        layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        left = (size - pw) // 2
        top = size // 2 - ph
        ImageDraw.Draw(layer).ellipse(
            (left, top, left + pw, size // 2 + pw // 4), fill=(*color, 70)
        )
        layer = layer.rotate(-angle(index), Image.BICUBIC)
        canvas = Image.alpha_composite(canvas, layer)

    draw = ImageDraw.Draw(canvas)
    icon_size = int(size * 0.18)
    ring = int(size * 0.007)
    label_font = load_font(int(size * 0.0235))
    for index, (repo, project) in enumerate(PROJECTS.items()):
        x, y = center_of(index)
        cx, cy = int(size * x / 100), int(size * y / 100)
        half = icon_size // 2
        color = COLORS[project["family"]]
        draw.ellipse(
            (cx - half - ring, cy - half - ring, cx + half + ring, cy + half + ring),
            fill=color,
        )
        icon = rounded_icon(root / repo / "icon.png", icon_size)
        canvas.alpha_composite(icon, (cx - half, cy - half))

        # Labels overlap the bottom of the icon: at this size there is no room
        # below it, and the icons look alike without them.
        label = project["label"]
        box = draw.textbbox((0, 0), label, font=label_font)
        tw, th = box[2] - box[0], box[3] - box[1]
        pad_x, pad_y = int(size * 0.012), int(size * 0.006)
        top = cy + half - th // 2 - pad_y
        draw.rounded_rectangle(
            (
                cx - tw // 2 - pad_x,
                top,
                cx + tw // 2 + pad_x,
                top + th + 2 * pad_y,
            ),
            radius=(th + 2 * pad_y) // 2,
            fill=color,
        )
        draw.text(
            (cx - tw // 2 - box[0], top + pad_y - box[1]),
            label,
            font=label_font,
            fill="white",
        )

    half = int(size * 0.14)
    mid = size // 2
    draw.ellipse(
        (mid - half, mid - half, mid + half, mid + half),
        fill="white",
        outline="#dce6f0",
        width=scale * 2,
    )
    title = "ReefTech"
    title_font = load_font(int(size * 0.042))
    box = draw.textbbox((0, 0), title, font=title_font)
    draw.text(
        (mid - (box[2] - box[0]) // 2 - box[0], mid - (box[3] - box[1]) // 2 - box[1]),
        title,
        font=title_font,
        fill="#155799",
    )

    target = out / "ecosystem-flower.png"
    canvas.resize((final, final), Image.LANCZOS).save(target, optimize=True)
    print("updated", target)


def main() -> int:
    root = Path(".")
    out = root / "reeftank" / ASSETS
    try:
        import PIL  # noqa: F401
    except ImportError:
        print("skipped flower assets: Pillow is not installed")
        return 0
    missing = [r for r in PROJECTS if not (root / r / "icon.png").is_file()]
    if missing:
        print(f"skipped flower assets: no icon.png for {', '.join(missing)}")
        return 0
    out.mkdir(parents=True, exist_ok=True)
    thumbnails(root, out)
    readme_image(root, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
