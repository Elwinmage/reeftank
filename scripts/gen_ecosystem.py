#!/usr/bin/env python3
"""Generate the shared "Related projects" block in every README, every language.

One source, twenty files. Blocks are delimited by ecosystem:start/end markers
so re-running updates them in place -- same convention as the
maintenance-section markers already used in ha-aquamedic-component.

Usage, from the directory holding every checkout side by side::

    python3 reeftank/scripts/gen_ecosystem.py

Edit PROJECTS and T here, never the generated blocks in the READMEs: a hand
edit in one file is exactly the drift this script exists to prevent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAW = "https://raw.githubusercontent.com/Elwinmage/{repo}/main/icon.png"
GH = "https://github.com/Elwinmage/{repo}"
SITE = "https://elwinmage.github.io/reeftank/"

# Icon size, and the width reserved for the column holding it.
#
# The table is emitted as HTML rather than markdown for this single reason: a
# markdown table sizes its columns from their content, which overrides the
# img width and shrinks the icons. Only a <th width> pins the column, and
# markdown has no way to express one.
#
# COLUMN_WIDTH must stay comfortably above ICON_WIDTH, or the column collapses
# back onto the image and the icons shrink again.
ICON_WIDTH = 64
COLUMN_WIDTH = "100px"

BLUEPRINT_BADGE = (
    "[![Open your Home Assistant instance and show the blueprint import dialog"
    " with a specific blueprint pre-filled.]"
    "(https://my.home-assistant.io/badges/blueprint_import.svg)]"
    "(https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url="
    "https://raw.githubusercontent.com/Elwinmage/ha-reefbeat-component/refs/"
    "heads/main/blueprints/automation/redsea_alerts.en.yaml)"
)

REPOS = [
    "ha-reefbeat-component",
    "ha-aquamedic-component",
    "ha-reef-maintenance-component",
    "ha-reef-card",
    "ha-reef-blueprints",
    "reefbeatEnergyBackup",
]

EMOJI = {
    "ha-reefbeat-component": "🐠",
    "ha-aquamedic-component": "🌊",
    "ha-reef-maintenance-component": "🐙",
    "ha-reef-card": "🪸",
    "ha-reef-blueprints": "🐬",
    "reefbeatEnergyBackup": "⚡",
}

# --------------------------------------------------------------------------
# Translations. "d_<repo>" is the description cell for that project.
# --------------------------------------------------------------------------

T: dict[str, dict[str, str]] = {
    "en": {
        "title": "Related projects",
        "intro": (
            "The ReefTech projects fit together: the integrations bring your "
            "equipment into Home Assistant, the card displays and drives it, "
            "and the backup keeps it running through an outage. Each one also "
            "works on its own."
        ),
        "h_project": "Project",
        "h_what": "What it does",
        "h_with": "Works with",
        "this": "(this repository)",
        "footer": f"All of them are documented together on the [ReefTech project page]({SITE}).",
        "d_ha-reefbeat-component": (
            "Red Sea ReefBeat devices, controlled locally with no cloud: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun and ReefWave.<br />"
            "alert blueprint for abnormal modes, calibrations and low "
            "battery. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Aqua Medic pumps through the Gizwits cloud API: EcoDrift and "
            "SmartDrift wavemakers, DC Runner return and skimmer pumps."
        ),
        "d_ha-reef-maintenance-component": (
            "Cleaning and wear tracking for the equipment Home Assistant "
            "cannot talk to: flow pumps, return pumps, skimmers, media "
            "reactors, anything you service by hand."
        ),
        "d_ha-reef-card": (
            "Interactive graphical view of each device on your dashboard, and "
            "the only way to edit advanced schedules. Reads the three "
            "integrations above through the shared `reef_role` contract, with "
            "no card-side configuration."
        ),
        "d_ha-reef-blueprints": (
            "Notification blueprints shared by the whole ecosystem: "
            "overdue maintenance found through the `reef_role` contract, "
            "and devices that went unreachable. Eight languages."
        ),
        "d_reefbeatEnergyBackup": (
            "Battery backup for power outages. A 24V LiFePO\u2084 pack driven "
            "by a Raspberry Pi, with pump speed degraded progressively "
            "according to the state of charge."
        ),
        "w_integrations": "all three integrations",
        "w_card": "ha-reef-card",
        "w_alone": "standalone, or alongside ha-reefbeat-component",
    },
    "fr": {
        "title": "Projets liés",
        "intro": (
            "Les projets ReefTech s'articulent entre eux : les intégrations "
            "font entrer votre matériel dans Home Assistant, la carte "
            "l'affiche et le pilote, et le secours le maintient en marche "
            "pendant une coupure. Chacun fonctionne aussi seul."
        ),
        "h_project": "Projet",
        "h_what": "Rôle",
        "h_with": "Fonctionne avec",
        "this": "(ce dépôt)",
        "footer": f"L'ensemble est documenté sur la [page du projet ReefTech]({SITE}).",
        "d_ha-reefbeat-component": (
            "Appareils Red Sea ReefBeat, pilotés en local sans cloud : "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun et ReefWave.<br />"
            "blueprint d'alertes pour les modes anormaux, les calibrations "
            "et les batteries faibles. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Pompes Aqua Medic via l'API cloud Gizwits : brasseurs EcoDrift et "
            "SmartDrift, pompes DC Runner de remontée et d'écumeur."
        ),
        "d_ha-reef-maintenance-component": (
            "Suivi du nettoyage et de l'usure du matériel que Home Assistant "
            "ne peut pas interroger : pompes de brassage, pompes de remontée, "
            "écumeurs, réacteurs, tout ce que vous entretenez à la main."
        ),
        "d_ha-reef-card": (
            "Vue graphique interactive de chaque appareil sur votre tableau de "
            "bord, et seul moyen d'éditer les programmes avancés. Lit les "
            "trois intégrations ci-dessus via le contrat `reef_role` commun, "
            "sans configuration côté carte."
        ),
        "d_ha-reef-blueprints": (
            "Blueprints de notification communs à tout l'écosystème : "
            "entretiens en retard trouvés via le contrat `reef_role`, et "
            "appareils devenus injoignables. Huit langues."
        ),
        "d_reefbeatEnergyBackup": (
            "Secours sur batterie en cas de coupure. Pack 24V LiFePO\u2084 "
            "piloté par un Raspberry Pi, avec dégradation progressive de la "
            "vitesse des pompes selon l'état de charge."
        ),
        "w_integrations": "les trois intégrations",
        "w_card": "ha-reef-card",
        "w_alone": "seul, ou avec ha-reefbeat-component",
    },
    "de": {
        "title": "Verwandte Projekte",
        "intro": (
            "Die ReefTech-Projekte greifen ineinander: die Integrationen "
            "bringen Ihre Geräte in Home Assistant, die Karte zeigt und "
            "steuert sie, und das Backup hält sie bei einem Stromausfall am "
            "Laufen. Jedes funktioniert auch für sich allein."
        ),
        "h_project": "Projekt",
        "h_what": "Funktion",
        "h_with": "Arbeitet mit",
        "this": "(dieses Repository)",
        "footer": f"Alle zusammen sind auf der [ReefTech-Projektseite]({SITE}) dokumentiert.",
        "d_ha-reefbeat-component": (
            "Red Sea ReefBeat-Geräte, lokal gesteuert ohne Cloud: ReefATO+, "
            "ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, "
            "ReefRun und ReefWave.<br />"
            "Alarm-Blueprint für abweichende Modi, Kalibrierungen und "
            "niedrigen Akkustand. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Aqua Medic-Pumpen über die Gizwits-Cloud-API: EcoDrift- und "
            "SmartDrift-Strömungspumpen, DC Runner Rückförder- und "
            "Abschäumerpumpen."
        ),
        "d_ha-reef-maintenance-component": (
            "Reinigungs- und Verschleißverfolgung für Geräte, die Home "
            "Assistant nicht erreicht: Strömungspumpen, Rückförderpumpen, "
            "Abschäumer, Reaktoren, alles was von Hand gewartet wird."
        ),
        "d_ha-reef-card": (
            "Interaktive grafische Ansicht jedes Geräts auf Ihrem Dashboard "
            "und der einzige Weg, erweiterte Zeitpläne zu bearbeiten. Liest "
            "die drei Integrationen über den gemeinsamen `reef_role`-Vertrag, "
            "ohne Konfiguration auf Kartenseite."
        ),
        "d_ha-reef-blueprints": (
            "Benachrichtigungs-Blueprints für das gesamte Ökosystem: "
            "überfällige Wartungen, über den `reef_role`-Vertrag gefunden, "
            "und nicht mehr erreichbare Geräte. Acht Sprachen."
        ),
        "d_reefbeatEnergyBackup": (
            "Batterie-Backup bei Stromausfall. Ein 24V LiFePO\u2084-Pack, "
            "gesteuert von einem Raspberry Pi, mit schrittweiser Reduzierung "
            "der Pumpendrehzahl je nach Ladezustand."
        ),
        "w_integrations": "alle drei Integrationen",
        "w_card": "ha-reef-card",
        "w_alone": "eigenständig oder zusammen mit ha-reefbeat-component",
    },
    "es": {
        "title": "Proyectos relacionados",
        "intro": (
            "Los proyectos ReefTech encajan entre sí: las integraciones traen "
            "tu equipo a Home Assistant, la tarjeta lo muestra y lo controla, "
            "y el respaldo lo mantiene en marcha durante un corte. Cada uno "
            "funciona también por su cuenta."
        ),
        "h_project": "Proyecto",
        "h_what": "Función",
        "h_with": "Funciona con",
        "this": "(este repositorio)",
        "footer": f"Todos están documentados juntos en la [página del proyecto ReefTech]({SITE}).",
        "d_ha-reefbeat-component": (
            "Dispositivos Red Sea ReefBeat, controlados localmente sin cloud: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun y ReefWave.<br />"
            "blueprint de alertas para modos anómalos, calibraciones y "
            "batería baja. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Bombas Aqua Medic a través de la API cloud Gizwits: bombas de "
            "movimiento EcoDrift y SmartDrift, bombas DC Runner de retorno y "
            "de skimmer."
        ),
        "d_ha-reef-maintenance-component": (
            "Seguimiento de limpieza y desgaste del equipo que Home Assistant "
            "no puede consultar: bombas de movimiento, bombas de retorno, "
            "skimmers, reactores, todo lo que mantienes a mano."
        ),
        "d_ha-reef-card": (
            "Vista gráfica interactiva de cada dispositivo en tu panel, y la "
            "única forma de editar programaciones avanzadas. Lee las tres "
            "integraciones mediante el contrato `reef_role` común, sin "
            "configuración del lado de la tarjeta."
        ),
        "d_ha-reef-blueprints": (
            "Blueprints de notificación comunes a todo el ecosistema: "
            "mantenimientos vencidos encontrados por el contrato `reef_role`, "
            "y dispositivos que dejaron de responder. Ocho idiomas."
        ),
        "d_reefbeatEnergyBackup": (
            "Respaldo por batería ante cortes de luz. Un pack 24V LiFePO\u2084 "
            "gobernado por una Raspberry Pi, con degradación progresiva de la "
            "velocidad de las bombas según el estado de carga."
        ),
        "w_integrations": "las tres integraciones",
        "w_card": "ha-reef-card",
        "w_alone": "por su cuenta, o junto a ha-reefbeat-component",
    },
    "it": {
        "title": "Progetti correlati",
        "intro": (
            "I progetti ReefTech si incastrano tra loro: le integrazioni "
            "portano la tua attrezzatura in Home Assistant, la scheda la "
            "mostra e la pilota, e il backup la mantiene in funzione durante "
            "un blackout. Ognuno funziona anche da solo."
        ),
        "h_project": "Progetto",
        "h_what": "Ruolo",
        "h_with": "Funziona con",
        "this": "(questo repository)",
        "footer": f"Sono tutti documentati insieme sulla [pagina del progetto ReefTech]({SITE}).",
        "d_ha-reefbeat-component": (
            "Dispositivi Red Sea ReefBeat, pilotati in locale senza cloud: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun e ReefWave.<br />"
            "blueprint di allerta per modalità anomale, calibrazioni e "
            "batteria scarica. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Pompe Aqua Medic tramite l'API cloud Gizwits: pompe di movimento "
            "EcoDrift e SmartDrift, pompe DC Runner di risalita e dello "
            "schiumatoio."
        ),
        "d_ha-reef-maintenance-component": (
            "Tracciamento di pulizia e usura per l'attrezzatura che Home "
            "Assistant non può interrogare: pompe di movimento, pompe di "
            "risalita, schiumatoi, reattori, tutto ciò che curi a mano."
        ),
        "d_ha-reef-card": (
            "Vista grafica interattiva di ogni dispositivo sulla tua "
            "dashboard, e unico modo per modificare le programmazioni "
            "avanzate. Legge le tre integrazioni tramite il contratto "
            "`reef_role` comune, senza configurazione lato scheda."
        ),
        "d_ha-reef-blueprints": (
            "Blueprint di notifica comuni a tutto l'ecosistema: "
            "manutenzioni scadute trovate tramite il contratto `reef_role`, "
            "e dispositivi diventati irraggiungibili. Otto lingue."
        ),
        "d_reefbeatEnergyBackup": (
            "Backup a batteria in caso di blackout. Un pacco 24V LiFePO\u2084 "
            "gestito da un Raspberry Pi, con degrado progressivo della "
            "velocità delle pompe in base allo stato di carica."
        ),
        "w_integrations": "tutte e tre le integrazioni",
        "w_card": "ha-reef-card",
        "w_alone": "da solo, o insieme a ha-reefbeat-component",
    },
    "nl": {
        "title": "Verwante projecten",
        "intro": (
            "De ReefTech-projecten grijpen in elkaar: de integraties brengen uw "
            "apparatuur in Home Assistant, de kaart toont en bedient ze, en de "
            "back-up houdt alles draaiend tijdens een stroomuitval. Elk werkt "
            "ook op zichzelf."
        ),
        "h_project": "Project",
        "h_what": "Rol",
        "h_with": "Werkt samen met",
        "this": "(deze repository)",
        "footer": f"Alles staat samen gedocumenteerd op de [ReefTech-projectpagina]({SITE}).",
        "d_ha-reefbeat-component": (
            "Red Sea ReefBeat-apparaten, lokaal aangestuurd zonder cloud: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun en ReefWave.<br />"
            "blueprint met meldingen voor afwijkende modi, kalibraties en "
            "lage accu. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Aqua Medic-pompen via de Gizwits-cloud-API: EcoDrift- en "
            "SmartDrift-stromingspompen, DC Runner opvoer- en "
            "afschuimerpompen."
        ),
        "d_ha-reef-maintenance-component": (
            "Schoonmaak- en slijtageopvolging voor apparatuur die Home "
            "Assistant niet kan uitlezen: stromingspompen, opvoerpompen, "
            "eiwitafschuimers, reactoren, alles wat u met de hand onderhoudt."
        ),
        "d_ha-reef-card": (
            "Interactieve grafische weergave van elk apparaat op uw dashboard, "
            "en de enige manier om geavanceerde schema's te bewerken. Leest de "
            "drie integraties via het gedeelde `reef_role`-contract, zonder "
            "configuratie aan de kaartzijde."
        ),
        "d_ha-reef-blueprints": (
            "Meldings-blueprints voor het hele ecosysteem: achterstallig "
            "onderhoud gevonden via het `reef_role`-contract, en apparaten "
            "die onbereikbaar zijn geworden. Acht talen."
        ),
        "d_reefbeatEnergyBackup": (
            "Accuback-up bij stroomuitval. Een 24V LiFePO\u2084-pakket "
            "aangestuurd door een Raspberry Pi, met de pompsnelheid die "
            "geleidelijk zakt met de laadtoestand."
        ),
        "w_integrations": "alle drie de integraties",
        "w_card": "ha-reef-card",
        "w_alone": "zelfstandig, of samen met ha-reefbeat-component",
    },
    "pl": {
        "title": "Powiązane projekty",
        "intro": (
            "Projekty ReefTech uzupełniają się: integracje wprowadzają sprzęt "
            "do Home Assistant, karta go wyświetla i steruje nim, a zasilanie "
            "awaryjne utrzymuje go w ruchu podczas przerwy w zasilaniu. Każdy "
            "działa również samodzielnie."
        ),
        "h_project": "Projekt",
        "h_what": "Rola",
        "h_with": "Współpracuje z",
        "this": "(to repozytorium)",
        "footer": f"Wszystkie są udokumentowane razem na [stronie projektu ReefTech]({SITE}).",
        "d_ha-reefbeat-component": (
            "Urządzenia Red Sea ReefBeat, sterowane lokalnie bez chmury: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun i ReefWave.<br />"
            "blueprint alertów dla nietypowych trybów, kalibracji i "
            "niskiego poziomu baterii. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Pompy Aqua Medic przez chmurowe API Gizwits: pompy cyrkulacyjne "
            "EcoDrift i SmartDrift, pompy DC Runner obiegowe i do odpieniacza."
        ),
        "d_ha-reef-maintenance-component": (
            "Śledzenie czyszczenia i zużycia sprzętu, do którego Home "
            "Assistant nie ma dostępu: pompy cyrkulacyjne, pompy obiegowe, "
            "odpieniacze, reaktory, wszystko co obsługujesz ręcznie."
        ),
        "d_ha-reef-card": (
            "Interaktywny widok graficzny każdego urządzenia na pulpicie i "
            "jedyny sposób edycji zaawansowanych harmonogramów. Odczytuje trzy "
            "integracje przez wspólny kontrakt `reef_role`, bez konfiguracji "
            "po stronie karty."
        ),
        "d_ha-reef-blueprints": (
            "Blueprinty powiadomień wspólne dla całego ekosystemu: zaległe "
            "konserwacje znajdowane przez kontrakt `reef_role` oraz "
            "urządzenia, które przestały odpowiadać. Osiem języków."
        ),
        "d_reefbeatEnergyBackup": (
            "Zasilanie awaryjne na wypadek przerw w zasilaniu. Pakiet 24V "
            "LiFePO\u2084 sterowany przez Raspberry Pi, ze stopniowym "
            "obniżaniem prędkości pomp zależnie od stanu naładowania."
        ),
        "w_integrations": "wszystkie trzy integracje",
        "w_card": "ha-reef-card",
        "w_alone": "samodzielnie lub razem z ha-reefbeat-component",
    },
    "pt": {
        "title": "Projetos relacionados",
        "intro": (
            "Os projetos ReefTech encaixam-se entre si: as integrações trazem "
            "o seu equipamento para o Home Assistant, o cartão mostra-o e "
            "comanda-o, e o backup mantém-no a funcionar durante um corte. "
            "Cada um funciona também sozinho."
        ),
        "h_project": "Projeto",
        "h_what": "Função",
        "h_with": "Funciona com",
        "this": "(este repositório)",
        "footer": f"Estão todos documentados em conjunto na [página do projeto ReefTech]({SITE}).",
        "d_ha-reefbeat-component": (
            "Aparelhos Red Sea ReefBeat, comandados localmente sem cloud: "
            "ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, "
            "ReefMat, ReefRun e ReefWave.<br />"
            "blueprint de alertas para modos anómalos, calibrações e "
            "bateria fraca. " + BLUEPRINT_BADGE
        ),
        "d_ha-aquamedic-component": (
            "Bombas Aqua Medic através da API cloud Gizwits: bombas de "
            "circulação EcoDrift e SmartDrift, bombas DC Runner de retorno e "
            "do escumador."
        ),
        "d_ha-reef-maintenance-component": (
            "Acompanhamento da limpeza e do desgaste do equipamento que o Home "
            "Assistant não consegue interrogar: bombas de circulação, bombas "
            "de retorno, escumadores, reatores, tudo o que trata à mão."
        ),
        "d_ha-reef-card": (
            "Vista gráfica interativa de cada aparelho no seu painel, e a "
            "única forma de editar os programas avançados. Lê as três "
            "integrações através do contrato `reef_role` comum, sem "
            "configuração do lado do cartão."
        ),
        "d_ha-reef-blueprints": (
            "Blueprints de notificação comuns a todo o ecossistema: "
            "manutenções em atraso encontradas pelo contrato `reef_role`, e "
            "aparelhos que ficaram inacessíveis. Oito idiomas."
        ),
        "d_reefbeatEnergyBackup": (
            "Backup por bateria em caso de corte. Um pack 24V LiFePO\u2084 "
            "comandado por um Raspberry Pi, com degradação progressiva da "
            "velocidade das bombas conforme o estado de carga."
        ),
        "w_integrations": "as três integrações",
        "w_card": "ha-reef-card",
        "w_alone": "sozinho, ou a par do ha-reefbeat-component",
    },
}

WORKS_WITH = {
    "ha-reefbeat-component": "w_card",
    "ha-reef-blueprints": "w_integrations",
    "ha-aquamedic-component": "w_card",
    "ha-reef-maintenance-component": "w_card",
    "ha-reef-card": "w_integrations",
    "reefbeatEnergyBackup": "w_alone",
}

START = "<!-- ecosystem:start -->"
END = "<!-- ecosystem:end -->"

# Anchors for files that carry no section yet: the block is inserted before
# the named heading.
ANCHORS = {
    ("ha-aquamedic-component", "en"): "## Supported Devices",
    ("ha-aquamedic-component", "fr"): "## Appareils compatibles",
    ("ha-aquamedic-component", "de"): "## Unterstützte Geräte",
    ("ha-aquamedic-component", "es"): "## Dispositivos compatibles",
    ("ha-aquamedic-component", "it"): "## Dispositivi supportati",
    ("ha-aquamedic-component", "pl"): "## Obsługiwane urządzenia",
    ("ha-aquamedic-component", "pt"): "## Dispositivos suportados",
    ("ha-reef-blueprints", "en"): "## Why a separate repository",
    ("ha-reef-blueprints", "fr"): "## Pourquoi un dépôt séparé",
    ("ha-reef-blueprints", "de"): "## Warum ein eigenes Repository",
    ("ha-reef-blueprints", "es"): "## Por qué un repositorio aparte",
    ("ha-reef-blueprints", "it"): "## Perché un repository separato",
    ("ha-reef-blueprints", "nl"): "## Waarom een aparte repository",
    ("ha-reef-blueprints", "pl"): "## Dlaczego osobne repozytorium",
    ("ha-reef-blueprints", "pt"): "## Porquê um repositório separado",
    ("ha-reef-maintenance-component", "en"): "## With ha-reef-card",
    ("ha-reef-maintenance-component", "fr"): "## Avec ha-reef-card",
    ("ha-reef-maintenance-component", "de"): "## Mit ha-reef-card",
    ("ha-reef-maintenance-component", "es"): "## Con ha-reef-card",
    ("ha-reef-maintenance-component", "it"): "## Con ha-reef-card",
    ("ha-reef-maintenance-component", "nl"): "## Met ha-reef-card",
    ("ha-reef-maintenance-component", "pl"): "## Z ha-reef-card",
    ("ha-reef-maintenance-component", "pt"): "## Com o ha-reef-card",
    ("reefbeatEnergyBackup", "en"): "## \u26a1 Features",
    ("reefbeatEnergyBackup", "fr"): "## \u26a1 Fonctionnalités",
}

# Hand-written sections to delete: they duplicate the generated block under a
# different heading, so the marker-based replacement never finds them.
LEGACY_HEADINGS = [
    "## 🔗 Related projects",
    "## 🔗 Projets liés",
]


def targets() -> list[tuple[Path, str, str]]:
    """Every file to write, as (path, repo, language)."""
    out: list[tuple[Path, str, str]] = [
        (Path(f"{repo}/README.md"), repo, "en") for repo in REPOS
    ]
    out.append(
        (Path("reefbeatEnergyBackup/README.fr.md"), "reefbeatEnergyBackup", "fr")
    )
    for lang in ["fr", "de", "es", "it", "pl", "pt"]:
        for repo in ["ha-reefbeat-component", "ha-reef-card", "ha-aquamedic-component"]:
            out.append((Path(f"{repo}/doc/{lang}/README.{lang}.md"), repo, lang))
    # These two are translated into Dutch as well.
    for repo in ["ha-reef-maintenance-component", "ha-reef-blueprints"]:
        for lang in ["fr", "de", "es", "it", "nl", "pl", "pt"]:
            out.append((Path(f"{repo}/doc/{lang}/README.{lang}.md"), repo, lang))
    return out


def md_to_html(text: str) -> str:
    """Convert the inline markdown used in the cells to HTML.

    GitHub does not process markdown inside an HTML block, so a cell written
    as markdown would render its asterisks and brackets literally.
    """
    # Badge: a linked image, [![alt](src)](href). Must run before the plain
    # link rule, which would otherwise match its inner part.
    text = re.sub(
        r"\[!\[([^\]]*)\]\(([^)]+)\)\]\(([^)]+)\)",
        r'<a href="\3"><img src="\2" alt="\1" /></a>',
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def build_block(current: str, lang: str) -> str:
    """Render the block for one repo in one language."""
    t = T[lang]
    lines = [
        START,
        "",
        f"## {t['title']}",
        "",
        t["intro"],
        "",
        "<table>",
        "  <tr>",
        f'    <th width="{COLUMN_WIDTH}"></th>',
        f"    <th>{t['h_project']}</th>",
        f"    <th>{t['h_what']}</th>",
        f"    <th>{t['h_with']}</th>",
        "  </tr>",
    ]

    for repo in REPOS:
        icon = (
            f'<img src="{RAW.format(repo=repo)}" width="{ICON_WIDTH}" alt="{repo}" />'
        )
        if repo == current:
            emoji = EMOJI.get(repo, "")
            label = f"{emoji}<br /><b>{repo}</b><br /><i>{t['this']}</i>"
        else:
            emoji = EMOJI.get(repo, "")
            label = f'{emoji}<br /><a href="{GH.format(repo=repo)}"><b>{repo}</b></a>'
        lines += [
            "  <tr>",
            f"    <td>{icon}</td>",
            f"    <td>{label}</td>",
            f"    <td>{md_to_html(t['d_' + repo])}</td>",
            f"    <td>{md_to_html(t[WORKS_WITH[repo]])}</td>",
            "  </tr>",
        ]

    lines += ["</table>", "", t["footer"], "", END]
    return "\n".join(lines)


def drop_legacy(text: str) -> str:
    """Remove a hand-written duplicate left under another heading."""
    for heading in LEGACY_HEADINGS:
        while heading in text:
            start = text.index(heading)
            after = text[start + len(heading) :]
            nxt = re.search(r"^#{1,3} ", after, re.MULTILINE)
            end = start + len(heading) + (nxt.start() if nxt else len(after))
            text = text[:start] + text[end:]
    return text


def apply(path: Path, repo: str, lang: str) -> str:
    """Insert or refresh the block in one README."""
    text = drop_legacy(path.read_text(encoding="utf-8"))
    block = build_block(repo, lang)

    if START in text:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
        return pattern.sub(lambda _: block, text, count=1)

    # Hand-written section under the localised heading: replace it whole, up
    # to the next heading of the same or higher level.
    heading = f"## {T[lang]['title']}"
    if heading in text:
        start = text.index(heading)
        after = text[start + len(heading) :]
        nxt = re.search(r"^#{1,2} ", after, re.MULTILINE)
        end = start + len(heading) + (nxt.start() if nxt else len(after))
        return text[:start] + block + "\n\n" + text[end:]

    anchor = ANCHORS.get((repo, lang))
    if anchor is None or anchor not in text:
        raise SystemExit(f"{path}: no marker, no section, and no usable anchor")
    return text.replace(anchor, block + "\n\n" + anchor, 1)


def main() -> None:
    for path, repo, lang in targets():
        if not path.exists():
            print("skipped (missing)", path)
            continue
        path.write_text(apply(path, repo, lang), encoding="utf-8")
        print("updated", path)


if __name__ == "__main__":
    sys.exit(main())
