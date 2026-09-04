#!/usr/bin/env python3
"""Rebuild the structured parts of the reeftank site, in every language.

Usage, from the directory holding every checkout side by side::

    python3 reeftank/scripts/gen_site.py

What it owns:
  * the three top-level sections (Integrations / Cards / Infrastructure)
  * the ha-reef-maintenance-component section, which did not exist
  * the device tables of the three integrations and of the card
  * the status legend, normalised on the one used by the READMEs
  * the contact section, which used to send every project's users to the
    ha-reefbeat-component tracker

Device statuses come from STATUS_* below and must match the compatibility
tables in the READMEs; that divergence between site and repos is the reason
this script exists. Prose outside the generated blocks is left untouched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LANGS = ["en", "fr", "de", "es", "it", "pl", "pt"]
PAGES = {lang: ("index.md" if lang == "en" else f"{lang}.md") for lang in LANGS}

# --------------------------------------------------------------------------
# Statuses. Single source for the site; keep in sync with the README tables.
# --------------------------------------------------------------------------

OK, WIP, UNTESTED, NO = "ok", "wip", "untested", "no"

# ha-reefbeat-component, per model group.
BEAT_DEVICES = [
    ("ReefATO+", "RSATO+", OK),
    ("ReefControl", "RSCONTROLPRO", OK),
    ("ReefControl", "RSCONTROLLITE", UNTESTED),
    ("ReefControl-Power", "RSPOWER6", OK),
    ("ReefControl-Power", "RSPOWER8", UNTESTED),
    ("ReefDose", "RSDOSE2, RSDOSE4", OK),
    ("ReefLed", "G1 (RSLED50/90/160), G2 (RSLED60/115)", OK),
    ("ReefLed", "G2 (RSLED170)", UNTESTED),
    ("ReefMat", "RSMAT250, RSMAT500, RSMAT1200", OK),
    ("ReefRun", "RSRUN", OK),
    ("ReefWave", "RSWAVE25, RSWAVE45", OK),
]

# ha-aquamedic-component.
AQUA_DEVICES = [
    ("EcoDrift / SmartDrift x.1 / x.3", "wavemaker", OK),
    ("DC Runner x.1 / x.2 / x.3", "return", OK),
    ("DC Runner", "skimmer", OK),
    ("Reefdoser EVO", "dosing", NO),
    ("T-Controller Twin", "temperature", NO),
    ("Aquarius / Spectrus", "lighting", NO),
]

# ha-reef-card. Highlights are per language, see CARD_HIGHLIGHTS.
CARD_DEVICES = [
    ("ReefDose (RSDOSE2/4)", OK, "dose"),
    ("ReefMat (RSMAT250/500/1200)", OK, "mat"),
    ("ReefRun (RSRUN)", OK, "run"),
    ("ReefATO+", OK, "ato"),
    ("ReefControl-Power (RSPOWER6/8)", WIP, "power"),
    ("ReefControl (RSCONTROLPRO/LITE)", NO, "vote"),
    ("ReefLed (G1/G2)", NO, "vote"),
    ("ReefWave", NO, "vote"),
    ("Aqua Medic EcoDrift / SmartDrift", NO, "vote"),
    ("Aqua Medic DC Runner (return, skimmer)", NO, "vote"),
]

VOTE = "https://github.com/Elwinmage/ha-reef-card/discussions/22"
DISCUSS = "https://github.com/Elwinmage/{repo}/discussions"
ISSUES = "https://github.com/Elwinmage/{repo}/issues"

# --------------------------------------------------------------------------
# Translations
# --------------------------------------------------------------------------

T: dict[str, dict[str, str]] = {
    "en": {
        "integrations": "Integrations",
        "cards": "Cards",
        "infrastructure": "Infrastructure",
        "legend": "✅ Supported &nbsp;|&nbsp; 🚧 In progress &nbsp;|&nbsp; 🧪 Untested (may work) &nbsp;|&nbsp; ❌ Not yet supported",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Supported devices:**",
        "device": "Device",
        "models": "Models",
        "status": "Status",
        "highlights": "Highlights",
        "pump": "Pump",
        "wavemaker": "wavemaker",
        "return": "return pump",
        "skimmer": "skimmer pump",
        "dosing": "dosing pump",
        "temperature": "temperature controller",
        "lighting": "lighting",
        "vote": f"[Vote for priority]({VOTE})",
        "ask": "Ask for it",
        "maint_title": "Maintenance tracking for equipment Home Assistant cannot reach.",
        "maint_intro": (
            "Flow pumps, return pumps, skimmers, media reactors — anything you "
            "service by hand. One config entry per brand, one device per piece "
            "of equipment, four entities per task: a button that records the "
            "job, a number for the interval, a switch to mute alerts and a date "
            "to backdate the last intervention."
        ),
        "maint_features": "**Key features:**",
        "maint_f1": "Presets for Tunze, Jebao and generic gear, with manufacturer intervals where one is published",
        "maint_f2": "A shared library of 17 tasks, translated in 8 languages",
        "maint_f3": 'Backdating, so a new piece of equipment does not start from "never done"',
        "maint_f4": "`reef_maintenance.reset` service — stick an NFC tag on the pump and scan it when you are done",
        "maint_f5": "Same `reef_role` contract as the connected integrations, so tasks land in the card's maintenance view",
        "install": "**Installation:**",
        "maint_install": "In HACS, add `https://github.com/Elwinmage/ha-reef-maintenance-component` as a custom repository (Integration).",
        "contact_title": "💬 Contact & Support",
        "contact_q": "**Questions and feature requests:** open a discussion on the project concerned —",
        "contact_b": "**Bug reports:** open an issue on that same project, with the details.",
        "contact_s": "**Support the project:**",
    },
    "fr": {
        "integrations": "Intégrations",
        "cards": "Cartes",
        "infrastructure": "Infrastructure",
        "legend": "✅ Supporté &nbsp;|&nbsp; 🚧 En cours &nbsp;|&nbsp; 🧪 Non testé (peut fonctionner) &nbsp;|&nbsp; ❌ Pas encore supporté",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Appareils supportés :**",
        "device": "Appareil",
        "models": "Modèles",
        "status": "Statut",
        "highlights": "Points forts",
        "pump": "Pompe",
        "wavemaker": "brassage",
        "return": "pompe de remontée",
        "skimmer": "pompe d'écumeur",
        "dosing": "pompe doseuse",
        "temperature": "contrôleur de température",
        "lighting": "éclairage",
        "vote": f"[Voter pour la priorité]({VOTE})",
        "ask": "Demandez-le",
        "maint_title": "Suivi de maintenance pour le matériel que Home Assistant ne voit pas.",
        "maint_intro": (
            "Pompes de brassage, pompes de remontée, écumeurs, réacteurs — tout "
            "ce que vous entretenez à la main. Une entrée par marque, un "
            "appareil par équipement, quatre entités par tâche : un bouton qui "
            "enregistre l'intervention, un nombre pour l'intervalle, un "
            "interrupteur pour couper les alertes et une date pour antidater la "
            "dernière intervention."
        ),
        "maint_features": "**Fonctions principales :**",
        "maint_f1": "Préréglages Tunze, Jebao et matériel générique, avec les intervalles du fabricant quand il en publie",
        "maint_f2": "Une bibliothèque commune de 17 tâches, traduite en 8 langues",
        "maint_f3": "Antidatage, pour qu'un nouvel équipement ne démarre pas à « jamais fait »",
        "maint_f4": "Service `reef_maintenance.reset` — collez un tag NFC sur la pompe et scannez-le une fois le travail terminé",
        "maint_f5": "Même contrat `reef_role` que les intégrations connectées : les tâches arrivent dans la vue maintenance de la carte",
        "install": "**Installation :**",
        "maint_install": "Dans HACS, ajoutez `https://github.com/Elwinmage/ha-reef-maintenance-component` en dépôt personnalisé (Intégration).",
        "contact_title": "💬 Contact & Support",
        "contact_q": "**Questions et demandes de fonctionnalités :** ouvrez une discussion sur le projet concerné —",
        "contact_b": "**Signalement de bugs :** ouvrez une issue sur ce même projet, avec les détails.",
        "contact_s": "**Soutenir le projet :**",
    },
    "de": {
        "integrations": "Integrationen",
        "cards": "Karten",
        "infrastructure": "Infrastruktur",
        "legend": "✅ Unterstützt &nbsp;|&nbsp; 🚧 In Arbeit &nbsp;|&nbsp; 🧪 Ungetestet (könnte funktionieren) &nbsp;|&nbsp; ❌ Noch nicht unterstützt",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Unterstützte Geräte:**",
        "device": "Gerät",
        "models": "Modelle",
        "status": "Status",
        "highlights": "Highlights",
        "pump": "Pumpe",
        "wavemaker": "Strömungspumpe",
        "return": "Rückförderpumpe",
        "skimmer": "Abschäumerpumpe",
        "dosing": "Dosierpumpe",
        "temperature": "Temperaturregler",
        "lighting": "Beleuchtung",
        "vote": f"[Für Priorität abstimmen]({VOTE})",
        "ask": "Anfragen",
        "maint_title": "Wartungsverfolgung für Geräte, die Home Assistant nicht erreicht.",
        "maint_intro": (
            "Strömungspumpen, Rückförderpumpen, Abschäumer, Reaktoren — alles, "
            "was Sie von Hand warten. Ein Eintrag pro Marke, ein Gerät pro "
            "Ausrüstung, vier Entitäten pro Aufgabe: eine Schaltfläche, die die "
            "Arbeit protokolliert, eine Zahl für das Intervall, ein Schalter zum "
            "Stummschalten der Hinweise und ein Datum, um die letzte Wartung "
            "rückwirkend einzutragen."
        ),
        "maint_features": "**Hauptfunktionen:**",
        "maint_f1": "Voreinstellungen für Tunze, Jebao und generische Geräte, mit Herstellerintervallen wo veröffentlicht",
        "maint_f2": "Eine gemeinsame Bibliothek mit 17 Aufgaben, in 8 Sprachen übersetzt",
        "maint_f3": 'Rückdatierung, damit ein neues Gerät nicht bei „nie gemacht" beginnt',
        "maint_f4": "Dienst `reef_maintenance.reset` — NFC-Tag an die Pumpe kleben und nach getaner Arbeit scannen",
        "maint_f5": "Gleicher `reef_role`-Vertrag wie die verbundenen Integrationen: die Aufgaben erscheinen in der Wartungsansicht der Karte",
        "install": "**Installation:**",
        "maint_install": "In HACS `https://github.com/Elwinmage/ha-reef-maintenance-component` als benutzerdefiniertes Repository (Integration) hinzufügen.",
        "contact_title": "💬 Kontakt & Support",
        "contact_q": "**Fragen und Funktionswünsche:** eröffnen Sie eine Diskussion im betreffenden Projekt —",
        "contact_b": "**Fehlerberichte:** eröffnen Sie ein Issue im selben Projekt, mit den Details.",
        "contact_s": "**Projekt unterstützen:**",
    },
    "es": {
        "integrations": "Integraciones",
        "cards": "Tarjetas",
        "infrastructure": "Infraestructura",
        "legend": "✅ Soportado &nbsp;|&nbsp; 🚧 En curso &nbsp;|&nbsp; 🧪 Sin probar (puede funcionar) &nbsp;|&nbsp; ❌ Aún no soportado",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Dispositivos soportados:**",
        "device": "Dispositivo",
        "models": "Modelos",
        "status": "Estado",
        "highlights": "Puntos fuertes",
        "pump": "Bomba",
        "wavemaker": "de movimiento",
        "return": "bomba de retorno",
        "skimmer": "bomba de skimmer",
        "dosing": "bomba dosificadora",
        "temperature": "controlador de temperatura",
        "lighting": "iluminación",
        "vote": f"[Votar por prioridad]({VOTE})",
        "ask": "Solicitarlo",
        "maint_title": "Seguimiento de mantenimiento para equipos que Home Assistant no alcanza.",
        "maint_intro": (
            "Bombas de movimiento, bombas de retorno, skimmers, reactores — todo "
            "lo que limpia a mano. Una entrada por marca, un dispositivo por "
            "equipo, cuatro entidades por tarea: un botón que registra el "
            "trabajo, un número para el intervalo, un interruptor para silenciar "
            "los avisos y una fecha para retrodatar la última intervención."
        ),
        "maint_features": "**Funciones principales:**",
        "maint_f1": "Preajustes para Tunze, Jebao y equipos genéricos, con los intervalos del fabricante cuando los publica",
        "maint_f2": "Una biblioteca común de 17 tareas, traducida a 8 idiomas",
        "maint_f3": "Retrodatación, para que un equipo nuevo no empiece en «nunca hecho»",
        "maint_f4": "Servicio `reef_maintenance.reset` — pegue una etiqueta NFC en la bomba y escanéela al terminar",
        "maint_f5": "Mismo contrato `reef_role` que las integraciones conectadas: las tareas aparecen en la vista de mantenimiento de la tarjeta",
        "install": "**Instalación:**",
        "maint_install": "En HACS, añada `https://github.com/Elwinmage/ha-reef-maintenance-component` como repositorio personalizado (Integración).",
        "contact_title": "💬 Contacto y soporte",
        "contact_q": "**Preguntas y peticiones de funciones:** abra una discusión en el proyecto correspondiente —",
        "contact_b": "**Informes de errores:** abra una issue en ese mismo proyecto, con los detalles.",
        "contact_s": "**Apoyar el proyecto:**",
    },
    "it": {
        "integrations": "Integrazioni",
        "cards": "Schede",
        "infrastructure": "Infrastruttura",
        "legend": "✅ Supportato &nbsp;|&nbsp; 🚧 In corso &nbsp;|&nbsp; 🧪 Non testato (potrebbe funzionare) &nbsp;|&nbsp; ❌ Non ancora supportato",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Dispositivi supportati:**",
        "device": "Dispositivo",
        "models": "Modelli",
        "status": "Stato",
        "highlights": "Punti di forza",
        "pump": "Pompa",
        "wavemaker": "di movimento",
        "return": "pompa di risalita",
        "skimmer": "pompa dello schiumatoio",
        "dosing": "pompa dosatrice",
        "temperature": "controllore di temperatura",
        "lighting": "illuminazione",
        "vote": f"[Vota per la priorità]({VOTE})",
        "ask": "Richiedilo",
        "maint_title": "Tracciamento della manutenzione per le apparecchiature che Home Assistant non raggiunge.",
        "maint_intro": (
            "Pompe di movimento, pompe di risalita, schiumatoi, reattori — tutto "
            "ciò che pulite a mano. Una voce per marca, un dispositivo per "
            "apparecchiatura, quattro entità per attività: un pulsante che "
            "registra il lavoro, un numero per l'intervallo, un interruttore per "
            "silenziare gli avvisi e una data per retrodatare l'ultimo intervento."
        ),
        "maint_features": "**Funzioni principali:**",
        "maint_f1": "Preset per Tunze, Jebao e apparecchiature generiche, con gli intervalli del produttore quando pubblicati",
        "maint_f2": "Una libreria comune di 17 attività, tradotta in 8 lingue",
        "maint_f3": "Retrodatazione, così una nuova apparecchiatura non parte da «mai fatto»",
        "maint_f4": "Servizio `reef_maintenance.reset` — attaccate un tag NFC sulla pompa e scansionatelo a lavoro finito",
        "maint_f5": "Stesso contratto `reef_role` delle integrazioni connesse: le attività compaiono nella vista manutenzione della scheda",
        "install": "**Installazione:**",
        "maint_install": "In HACS, aggiungete `https://github.com/Elwinmage/ha-reef-maintenance-component` come repository personalizzato (Integrazione).",
        "contact_title": "💬 Contatti e supporto",
        "contact_q": "**Domande e richieste di funzionalità:** aprite una discussione sul progetto interessato —",
        "contact_b": "**Segnalazione bug:** aprite una issue sullo stesso progetto, con i dettagli.",
        "contact_s": "**Sostieni il progetto:**",
    },
    "pl": {
        "integrations": "Integracje",
        "cards": "Karty",
        "infrastructure": "Infrastruktura",
        "legend": "✅ Wspierane &nbsp;|&nbsp; 🚧 W trakcie &nbsp;|&nbsp; 🧪 Nieprzetestowane (może działać) &nbsp;|&nbsp; ❌ Jeszcze niewspierane",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Obsługiwane urządzenia:**",
        "device": "Urządzenie",
        "models": "Modele",
        "status": "Status",
        "highlights": "Najważniejsze",
        "pump": "Pompa",
        "wavemaker": "cyrkulacyjna",
        "return": "pompa obiegowa",
        "skimmer": "pompa odpieniacza",
        "dosing": "pompa dozująca",
        "temperature": "sterownik temperatury",
        "lighting": "oświetlenie",
        "vote": f"[Zagłosuj na priorytet]({VOTE})",
        "ask": "Poproś o to",
        "maint_title": "Śledzenie konserwacji sprzętu, do którego Home Assistant nie ma dostępu.",
        "maint_intro": (
            "Pompy cyrkulacyjne, pompy obiegowe, odpieniacze, reaktory — "
            "wszystko, co czyścisz ręcznie. Jeden wpis na markę, jedno "
            "urządzenie na sprzęt, cztery encje na zadanie: przycisk "
            "rejestrujący wykonanie, liczba dla interwału, przełącznik "
            "wyciszający powiadomienia i data do wstecznego wpisania ostatniej "
            "obsługi."
        ),
        "maint_features": "**Główne funkcje:**",
        "maint_f1": "Ustawienia wstępne dla Tunze, Jebao i sprzętu generycznego, z interwałami producenta tam, gdzie są publikowane",
        "maint_f2": "Wspólna biblioteka 17 zadań, przetłumaczona na 8 języków",
        "maint_f3": 'Wsteczne datowanie, aby nowy sprzęt nie zaczynał od „nigdy nie wykonano"',
        "maint_f4": "Usługa `reef_maintenance.reset` — przyklej tag NFC na pompie i zeskanuj go po zakończeniu",
        "maint_f5": "Ten sam kontrakt `reef_role` co integracje podłączone: zadania trafiają do widoku konserwacji karty",
        "install": "**Instalacja:**",
        "maint_install": "W HACS dodaj `https://github.com/Elwinmage/ha-reef-maintenance-component` jako niestandardowe repozytorium (Integracja).",
        "contact_title": "💬 Kontakt i wsparcie",
        "contact_q": "**Pytania i propozycje funkcji:** otwórz dyskusję w odpowiednim projekcie —",
        "contact_b": "**Zgłoszenia błędów:** otwórz issue w tym samym projekcie, ze szczegółami.",
        "contact_s": "**Wesprzyj projekt:**",
    },
    "pt": {
        "integrations": "Integrações",
        "cards": "Cartões",
        "infrastructure": "Infraestrutura",
        "legend": "✅ Suportado &nbsp;|&nbsp; 🚧 Em curso &nbsp;|&nbsp; 🧪 Não testado (pode funcionar) &nbsp;|&nbsp; ❌ Ainda não suportado",
        "ok": "✅",
        "wip": "🚧",
        "untested": "🧪",
        "no": "❌",
        "supported_devices": "**Dispositivos suportados:**",
        "device": "Aparelho",
        "models": "Modelos",
        "status": "Estado",
        "highlights": "Pontos fortes",
        "pump": "Bomba",
        "wavemaker": "de circulação",
        "return": "bomba de retorno",
        "skimmer": "bomba do escumador",
        "dosing": "bomba doseadora",
        "temperature": "controlador de temperatura",
        "lighting": "iluminação",
        "vote": f"[Votar na prioridade]({VOTE})",
        "ask": "Peça-o",
        "maint_title": "Acompanhamento de manutenção para equipamento que o Home Assistant não alcança.",
        "maint_intro": (
            "Bombas de circulação, bombas de retorno, escumadores, reatores — "
            "tudo o que limpa à mão. Uma entrada por marca, um aparelho por "
            "equipamento, quatro entidades por tarefa: um botão que regista o "
            "trabalho, um número para o intervalo, um interruptor para silenciar "
            "os avisos e uma data para retroagir a última intervenção."
        ),
        "maint_features": "**Funções principais:**",
        "maint_f1": "Predefinições para Tunze, Jebao e equipamento genérico, com os intervalos do fabricante quando publicados",
        "maint_f2": "Uma biblioteca comum de 17 tarefas, traduzida em 8 idiomas",
        "maint_f3": "Retroatividade, para que um equipamento novo não comece em «nunca feito»",
        "maint_f4": "Serviço `reef_maintenance.reset` — cole uma etiqueta NFC na bomba e leia-a quando terminar",
        "maint_f5": "Mesmo contrato `reef_role` das integrações ligadas: as tarefas aparecem na vista de manutenção do cartão",
        "install": "**Instalação:**",
        "maint_install": "No HACS, adicione `https://github.com/Elwinmage/ha-reef-maintenance-component` como repositório personalizado (Integração).",
        "contact_title": "💬 Contacto e suporte",
        "contact_q": "**Perguntas e pedidos de funcionalidades:** abra uma discussão no projeto em causa —",
        "contact_b": "**Relatórios de erros:** abra uma issue nesse mesmo projeto, com os detalhes.",
        "contact_s": "**Apoiar o projeto:**",
    },
}

# Card highlights, per device key and language. Short on purpose: the detail
# belongs in the card's own README, the site only says what it is worth.
CARD_HIGHLIGHTS = {
    "en": {
        "dose": "Full scheduling, manual dosing, priming and calibration, supplement management, usage tracking",
        "mat": "Animated roll status, manual/auto/scheduled advance, sensor status, weekly and monthly graphs",
        "run": "Pump speed control, schedule editor, overskimming management",
        "ato": "Water level, leak probe, pump diagnostics, consumption graph, leak buzzer",
        "power": "Per-socket control",
        "vote": None,
    },
    "fr": {
        "dose": "Planification complète, dosage manuel, amorçage et calibration, gestion des suppléments, suivi de l'utilisation",
        "mat": "État du rouleau animé, avance manuelle/auto/programmée, état du capteur, graphiques hebdo et mensuels",
        "run": "Contrôle de la vitesse de pompe, éditeur de programmes, gestion du surécumage",
        "ato": "Niveau d'eau, sonde de fuite, diagnostic pompe, graphe de consommation, buzzer de fuite",
        "power": "Contrôle par prise",
        "vote": None,
    },
    "de": {
        "dose": "Vollständige Planung, manuelle Dosierung, Entlüften und Kalibrieren, Zusatzstoffverwaltung, Verbrauchsverfolgung",
        "mat": "Animierter Rollenstatus, manueller/automatischer/geplanter Vorschub, Sensorstatus, Wochen- und Monatsgrafiken",
        "run": "Pumpendrehzahl, Zeitplan-Editor, Überschäumen-Verwaltung",
        "ato": "Wasserstand, Lecksonde, Pumpendiagnose, Verbrauchsdiagramm, Leck-Summer",
        "power": "Steuerung pro Steckdose",
        "vote": None,
    },
    "es": {
        "dose": "Planificación completa, dosificación manual, cebado y calibración, gestión de suplementos, seguimiento de uso",
        "mat": "Estado del rollo animado, avance manual/automático/programado, estado del sensor, gráficos semanales y mensuales",
        "run": "Control de velocidad de bomba, editor de programas, gestión del sobreespumado",
        "ato": "Nivel de agua, sonda de fugas, diagnóstico de bomba, gráfico de consumo, zumbador de fuga",
        "power": "Control por toma",
        "vote": None,
    },
    "it": {
        "dose": "Pianificazione completa, dosaggio manuale, adescamento e calibrazione, gestione dei supplementi, monitoraggio dei consumi",
        "mat": "Stato del rotolo animato, avanzamento manuale/automatico/programmato, stato del sensore, grafici settimanali e mensili",
        "run": "Controllo della velocità della pompa, editor dei programmi, gestione della sovraschiumazione",
        "ato": "Livello dell'acqua, sonda perdite, diagnostica pompa, grafico dei consumi, buzzer perdite",
        "power": "Controllo per presa",
        "vote": None,
    },
    "pl": {
        "dose": "Pełne harmonogramowanie, dozowanie ręczne, zalewanie i kalibracja, zarządzanie suplementami, śledzenie zużycia",
        "mat": "Animowany stan rolki, przesuw ręczny/automatyczny/zaplanowany, stan czujnika, wykresy tygodniowe i miesięczne",
        "run": "Sterowanie prędkością pompy, edytor harmonogramów, zarządzanie nadmiernym odpienianiem",
        "ato": "Poziom wody, sonda wycieku, diagnostyka pompy, wykres zużycia, buzzer wycieku",
        "power": "Sterowanie per gniazdo",
        "vote": None,
    },
    "pt": {
        "dose": "Planeamento completo, doseamento manual, escorvamento e calibração, gestão de suplementos, acompanhamento do consumo",
        "mat": "Estado do rolo animado, avanço manual/automático/programado, estado do sensor, gráficos semanais e mensais",
        "run": "Controlo da velocidade da bomba, editor de programas, gestão da sobre-escumação",
        "ato": "Nível de água, sonda de fugas, diagnóstico da bomba, gráfico de consumo, buzzer de fuga",
        "power": "Controlo por tomada",
        "vote": None,
    },
}

# Demo videos for the card section. Each entry is (youtube_id, label_key).
# Set youtube_id to None for a placeholder (not yet published).
# To add a new video: append one line here and one label per language below.
CARD_VIDEOS = [
    ("Qee5LH0T9wQ", "demo_dose"),
    ("yyNyUSitb1E", "demo_mat"),
    ("Xxv38OPqiGI", "demo_run"),
    ("Ko46fHonOP4", "demo_maint"),
    ("2R0DHp2eqT4", "demo_ato"),
    # (None, "demo_ato"),  # uncomment when the ReefATO+ video is published
]

VIDEO_LABELS = {
    "en": {
        "demo_dose": "ReefDose demo",
        "demo_mat": "ReefMat demo",
        "demo_run": "ReefRun demo",
        "demo_maint": "Maintenance demo",
        "demo_ato": "ReefATO+ demo",
    },
    "fr": {
        "demo_dose": "Démo ReefDose",
        "demo_mat": "Démo ReefMat",
        "demo_run": "Démo ReefRun",
        "demo_maint": "Démo Maintenance",
        "demo_ato": "Démo ReefATO+",
    },
    "de": {
        "demo_dose": "ReefDose-Demo",
        "demo_mat": "ReefMat-Demo",
        "demo_run": "ReefRun-Demo",
        "demo_maint": "Wartungs-Demo",
        "demo_ato": "ReefATO+-Demo",
    },
    "es": {
        "demo_dose": "Demo ReefDose",
        "demo_mat": "Demo ReefMat",
        "demo_run": "Demo ReefRun",
        "demo_maint": "Demo Mantenimiento",
        "demo_ato": "Demo ReefATO+",
    },
    "it": {
        "demo_dose": "Demo ReefDose",
        "demo_mat": "Demo ReefMat",
        "demo_run": "Demo ReefRun",
        "demo_maint": "Demo Manutenzione",
        "demo_ato": "Demo ReefATO+",
    },
    "pl": {
        "demo_dose": "Demo ReefDose",
        "demo_mat": "Demo ReefMat",
        "demo_run": "Demo ReefRun",
        "demo_maint": "Demo Konserwacja",
        "demo_ato": "Demo ReefATO+",
    },
    "pt": {
        "demo_dose": "Demo ReefDose",
        "demo_mat": "Demo ReefMat",
        "demo_run": "Demo ReefRun",
        "demo_maint": "Demo Manutenção",
        "demo_ato": "Demo ReefATO+",
    },
}

BLUEPRINTS = {
    "en": (
        "Notification blueprints for the whole ecosystem.",
        "Alerts you on your phone about overdue maintenance, found through the shared `reef_role` attribute so every integration is covered, and about devices that went unreachable. Eight languages, one import button each.",
        "**Installation:** import from the repository, one button per language.",
    ),
    "fr": (
        "Blueprints de notification pour tout l'écosystème.",
        "Vous prévient sur votre téléphone des entretiens en retard, trouvés via l'attribut commun `reef_role` afin que toutes les intégrations soient couvertes, et des appareils devenus injoignables. Huit langues, un bouton d'import chacune.",
        "**Installation :** import depuis le dépôt, un bouton par langue.",
    ),
    "de": (
        "Benachrichtigungs-Blueprints für das gesamte Ökosystem.",
        "Meldet auf dem Telefon überfällige Wartungen, über das gemeinsame `reef_role`-Attribut gefunden, sodass jede Integration abgedeckt ist, sowie nicht mehr erreichbare Geräte. Acht Sprachen, je eine Import-Schaltfläche.",
        "**Installation:** Import aus dem Repository, eine Schaltfläche je Sprache.",
    ),
    "es": (
        "Blueprints de notificación para todo el ecosistema.",
        "Le avisa en el móvil de los mantenimientos vencidos, encontrados por el atributo común `reef_role` de modo que todas las integraciones quedan cubiertas, y de los dispositivos que dejaron de responder. Ocho idiomas, un botón de importación cada uno.",
        "**Instalación:** importe desde el repositorio, un botón por idioma.",
    ),
    "it": (
        "Blueprint di notifica per tutto l'ecosistema.",
        "Vi avvisa sul telefono delle manutenzioni scadute, trovate tramite l'attributo comune `reef_role` così che ogni integrazione sia coperta, e dei dispositivi diventati irraggiungibili. Otto lingue, un pulsante di importazione ciascuna.",
        "**Installazione:** importate dal repository, un pulsante per lingua.",
    ),
    "pl": (
        "Blueprinty powiadomień dla całego ekosystemu.",
        "Powiadamia na telefonie o zaległych konserwacjach, znajdowanych przez wspólny atrybut `reef_role`, dzięki czemu objęte są wszystkie integracje, oraz o urządzeniach, które przestały odpowiadać. Osiem języków, po jednym przycisku importu.",
        "**Instalacja:** import z repozytorium, jeden przycisk na język.",
    ),
    "pt": (
        "Blueprints de notificação para todo o ecossistema.",
        "Avisa-o no telemóvel das manutenções em atraso, encontradas pelo atributo comum `reef_role` para que todas as integrações fiquem cobertas, e dos aparelhos que ficaram inacessíveis. Oito idiomas, um botão de importação cada.",
        "**Instalação:** importe do repositório, um botão por idioma.",
    ),
}

START = "<!-- generated:{name}:start -->"
END = "<!-- generated:{name}:end -->"


def block(name: str, body: str) -> str:
    """Wrap generated content in its markers.

    Blank lines around the HTML comments are mandatory: kramdown requires
    tables (and other block elements) to start and end on block boundaries.
    Without them the pipe-table is not recognised and renders as inline text.
    """
    return f"{START.format(name=name)}\n\n{body}\n\n{END.format(name=name)}"


def beat_table(lang: str) -> str:
    t = T[lang]
    lines = [
        t["supported_devices"],
        "",
        f"> {t['legend']}",
        "",
        f"| {t['device']} | {t['models']} | {t['status']} |",
        "|------|------|------|",
    ]
    for name, models, status in BEAT_DEVICES:
        lines.append(f"| **{name}** | {models} | {t[status]} |")
    return "\n".join(lines)


def aqua_table(lang: str) -> str:
    t = T[lang]
    url = DISCUSS.format(repo="ha-aquamedic-component")
    lines = [
        t["supported_devices"],
        "",
        f"> {t['legend']}",
        "",
        f"| {t['device']} | {t['status']} |",
        "|------|------|",
    ]
    for name, kind, status in AQUA_DEVICES:
        cell = t[status]
        if status == NO:
            cell = f"{t[status]} — [{t['ask']}]({url})"
        lines.append(f"| **{name}** ({t[kind]}) | {cell} |")
    return "\n".join(lines)


def card_table(lang: str) -> str:
    t = T[lang]
    hi = CARD_HIGHLIGHTS[lang]
    lines = [
        t["supported_devices"],
        "",
        f"> {t['legend']}",
        "",
        f"| {t['device']} | {t['status']} | {t['highlights']} |",
        "|------|------|------|",
    ]
    for name, status, key in CARD_DEVICES:
        note = hi.get(key) or t["vote"]
        lines.append(f"| **{name}** | {t[status]} | {note} |")
    return "\n".join(lines)


def card_videos(lang: str) -> str:
    """Build the demo-video gallery for the card section.

    Videos are rendered as an HTML table with two columns, wrapping to new
    rows automatically.  Only entries with a non-None youtube_id are shown,
    so uncommenting a line in CARD_VIDEOS is all it takes to publish a new
    video on every language page.
    """
    labels = VIDEO_LABELS[lang]
    active = [(vid, labels[key]) for vid, key in CARD_VIDEOS if vid is not None]
    if not active:
        return ""

    cols = 2
    cells = []
    for vid, label in active:
        thumb = f"https://img.youtube.com/vi/{vid}/0.jpg"
        url = f"https://www.youtube.com/watch?v={vid}"
        cells.append(
            f'<td><a href="{url}">'
            f'<img src="{thumb}" alt="{label}" width="300"/>'
            f"</a><br/><em>{label}</em></td>"
        )

    rows = []
    for i in range(0, len(cells), cols):
        rows.append("<tr>\n" + "\n".join(cells[i : i + cols]) + "\n</tr>")

    return "<table>\n" + "\n".join(rows) + "\n</table>"


def blueprints_section(lang: str) -> str:
    """The shared notification blueprints, filed under Infrastructure.

    Automations, so neither an integration nor a card.
    """
    title, body, install = BLUEPRINTS[lang]
    repo = "https://github.com/Elwinmage/ha-reef-blueprints"
    content = f"""#### 🐬 [ha-reef-blueprints]({repo})

**{title}**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)]({repo}/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

{body}

{install}"""
    return block("blueprints", content)


def maintenance_section(lang: str) -> str:
    t = T[lang]
    repo = "https://github.com/Elwinmage/ha-reef-maintenance-component"
    body = f"""#### 🐙 [ha-reef-maintenance-component]({repo})

**{t["maint_title"]}**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)]({repo}/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)]({repo}/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

{t["maint_intro"]}

{t["maint_features"]}

- {t["maint_f1"]}
- {t["maint_f2"]}
- {t["maint_f3"]}
- {t["maint_f4"]}
- {t["maint_f5"]}

{t["install"]} {t["maint_install"]}"""
    return block("maintenance", body)


def contact_section(lang: str) -> str:
    t = T[lang]
    # Discussions is a per-repo setting: two of them have the tab turned off,
    # so their link would 404. Point those at Issues until the tab is enabled,
    # then move them into the first list.
    with_discussions = [
        "ha-reefbeat-component",
        "ha-aquamedic-component",
        "ha-reef-card",
    ]
    with_issues_only = [
        "ha-reef-maintenance-component",
        "reefbeatEnergyBackup",
    ]
    links = " · ".join(
        [f"[{r}]({DISCUSS.format(repo=r)})" for r in with_discussions]
        + [f"[{r}]({ISSUES.format(repo=r)})" for r in with_issues_only]
    )
    body = f"""## {t["contact_title"]}

- {t["contact_q"]} {links}
- {t["contact_b"]}
- {t["contact_s"]} [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)"""
    return block("contact", body)


def replace_table(text: str, name: str, heading: str, new: str, lang: str) -> str:
    """Swap the supported-devices table that follows one project heading.

    The table is found by its `**Supported devices:**` lead-in and runs to the
    first blank line after the last row, which is how every page is written.
    """
    if START.format(name=name) in text:
        pattern = re.compile(
            re.escape(START.format(name=name))
            + r".*?"
            + re.escape(END.format(name=name)),
            re.DOTALL,
        )
        return pattern.sub(lambda _: block(name, new), text, count=1)

    # Locate the table by its separator row rather than by the translated
    # lead-in: the pages do not all word that line the same way, and a
    # mismatch would silently skip the section.
    at = text.index(heading)
    sep = text.index("|---", at)
    lead = text.rindex("**", 0, text.rindex("**", 0, sep))
    end = text.index("\n\n", sep)
    return text[:lead] + block(name, new) + text[end:]


def restructure(text: str, lang: str) -> str:
    """Move the energy backup out of Integrations and into Infrastructure.

    It is a Raspberry Pi service, not a Home Assistant integration; filing it
    under Integrations was the one classification error on the site.
    """
    t = T[lang]
    if f"## 🔌 {t['infrastructure']}" in text:
        return text

    start = text.index("#### ⚡ [reefbeatEnergyBackup]")
    end = text.index("#### 🌊 [ha-aquamedic-component]")
    backup = text[start:end].rstrip().removesuffix("---").rstrip()

    text = text[:start] + text[end:]

    # Re-file it after the card section, before the 3D models.
    models = re.search(r"^## 📐 ", text, re.MULTILINE)
    assert models, "3D models heading not found"
    header = f"## 🔌 {t['infrastructure']}\n\n---\n\n"
    return (
        text[: models.start()]
        + header
        + backup
        + "\n\n---\n\n"
        + text[models.start() :]
    )


def apply(lang: str) -> None:
    path = Path("reeftank") / PAGES[lang]
    text = path.read_text(encoding="utf-8")
    t = T[lang]

    text = restructure(text, lang)

    text = replace_table(
        text, "beat-devices", "#### 🐠 [ha-reefbeat-component]", beat_table(lang), lang
    )
    text = replace_table(
        text, "aqua-devices", "#### 🌊 [ha-aquamedic-component]", aqua_table(lang), lang
    )
    text = replace_table(
        text, "card-devices", "#### 🪸 [ha-reef-card]", card_table(lang), lang
    )

    # Card demo videos: generated gallery replaces the static HTML table.
    videos_html = card_videos(lang)
    if START.format(name="card-videos") in text:
        pattern = re.compile(
            re.escape(START.format(name="card-videos"))
            + r".*?"
            + re.escape(END.format(name="card-videos")),
            re.DOTALL,
        )
        text = pattern.sub(lambda _: block("card-videos", videos_html), text, count=1)
    else:
        # First run: find the existing static <table> with youtube thumbnails
        # and replace it with the generated block.
        yt_table = re.search(
            r"<table>\s*<tr>\s*<td><a href=\"https://www\.youtube\.com/watch\?v=.*?"
            r"</table>",
            text,
            re.DOTALL,
        )
        if yt_table:
            text = (
                text[: yt_table.start()]
                + block("card-videos", videos_html)
                + text[yt_table.end() :]
            )

    # Maintenance goes last among the integrations, right before the cards.
    if START.format(name="maintenance") in text:
        pattern = re.compile(
            re.escape(START.format(name="maintenance"))
            + r".*?"
            + re.escape(END.format(name="maintenance")),
            re.DOTALL,
        )
        text = pattern.sub(lambda _: maintenance_section(lang), text, count=1)
    else:
        anchor = f"### {t['cards']}\n"
        assert anchor in text, f"{lang}: cards heading not found"
        text = text.replace(
            anchor, maintenance_section(lang) + "\n\n---\n\n" + anchor, 1
        )

    # Blueprints: filed under Infrastructure, before the 3D models.
    if START.format(name="blueprints") in text:
        pattern = re.compile(
            re.escape(START.format(name="blueprints"))
            + r".*?"
            + re.escape(END.format(name="blueprints")),
            re.DOTALL,
        )
        text = pattern.sub(lambda _: blueprints_section(lang), text, count=1)
    else:
        at = re.search(r"^## 📐 ", text, re.MULTILINE)
        assert at, f"{lang}: 3D models heading not found"
        text = (
            text[: at.start()]
            + blueprints_section(lang)
            + "\n\n---\n\n"
            + text[at.start() :]
        )

    # Contact: every project has its own tracker.
    if START.format(name="contact") in text:
        pattern = re.compile(
            re.escape(START.format(name="contact"))
            + r".*?"
            + re.escape(END.format(name="contact")),
            re.DOTALL,
        )
        text = pattern.sub(lambda _: contact_section(lang), text, count=1)
    else:
        at = re.search(r"^## 💬 ", text, re.MULTILINE)
        assert at, f"{lang}: contact heading not found"
        text = text[: at.start()] + contact_section(lang) + "\n"

    path.write_text(text, encoding="utf-8")
    print("updated", path)


def main() -> None:
    for lang in LANGS:
        apply(lang)


if __name__ == "__main__":
    sys.exit(main())
