---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: de
---

{% include language-selector.html %}

# Meine ReefTank-Werkzeuge

Willkommen zur Dokumentation meiner Riffaquarium-Projekte.

<video src="assets/videos/logo_v1.mp4" 
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Home Assistant Integrationen und Karten

---

> Seit Home Assistant 2026.11 ist HACS als **Marketplace** Teil von Home Assistant (*Einstellungen > Marketplace*). Bei einem älteren Home Assistant funktionieren dieselben Schritte in HACS.

### Integrationen

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Lokale Integration für das Red Sea ReefBeat-Ökosystem.**

[![Marketplace Badge](https://img.shields.io/badge/Marketplace-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Verwalten Sie Ihre Red Sea ReefBeat-Geräte **lokal** (kein Cloud erforderlich): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun und ReefWave.

> ⚠️ Dies ist kein offizielles Red Sea Repository. Nutzung auf eigene Gefahr.

**Hauptfunktionen:**
- **100% lokale Steuerung** — keine Cloud-Abhängigkeit für die meisten Geräte
- Automatische Geräteerkennung im lokalen Netzwerk (mit manuellem Modus und Subnetz-Unterstützung)
- Benutzerdefinierte Icons für alle ReefBeat-Geräte
- Firmware-Update-Benachrichtigungen (mit optionaler Cloud API)
- Live-Konfigurationsaktualisierung für Echtzeit-Überwachung
- **Dosierregelung** für die ReefDose: assistierte Dosierung anhand Ihrer Testergebnisse, auf die Salinität geregelte Salzlösung
- **Poseidon-Modus** (experimentell): ein lokales Relais, das den Großteil der Abfragen durch das ersetzt, was die Geräte senden, mit dem Dosierverlauf und den Gerätealarmen als Home-Assistant-Ereignisse
- Mehrsprachige Unterstützung

<!-- generated:beat-devices:start -->

**Unterstützte Geräte:**

> ✅ Unterstützt &nbsp;|&nbsp; 🚧 In Arbeit &nbsp;|&nbsp; 🧪 Ungetestet (könnte funktionieren) &nbsp;|&nbsp; ❌ Noch nicht unterstützt

| Gerät | Modelle | Status |
|------|------|------|
| **ReefATO+** | RSATO+ | ✅ |
| **ReefControl** | RSCONTROLPRO | ✅ |
| **ReefControl** | RSCONTROLLITE | 🧪 |
| **ReefControl-Power** | RSPOWER6 | ✅ |
| **ReefControl-Power** | RSPOWER8 | 🧪 |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115) | ✅ |
| **ReefLed** | G2 (RSLED170) | 🧪 |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ |
| **ReefRun** | RSRUN | ✅ |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ |

<!-- generated:beat-devices:end -->

**ReefWave-Besonderheiten:** ReefWave ist das einzige Gerät, das an die ReefBeat-Cloud gebunden ist. Drei Betriebsmodi stehen zur Verfügung — Cloud, Lokal und Hybrid — damit Sie die Balance zwischen voller lokaler Steuerung und Synchronisation mit der ReefBeat-App wählen können.

**Installation:** Direkt im [Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) verfügbar — suchen Sie nach "redsea" oder "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Steuerung von Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API.**

[![Marketplace Badge](https://img.shields.io/badge/Marketplace-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Steuern Sie Ihre Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API (dasselbe Backend wie die offizielle Aqua Medic App).

<!-- generated:aqua-devices:start -->

**Unterstützte Geräte:**

> ✅ Unterstützt &nbsp;|&nbsp; 🚧 In Arbeit &nbsp;|&nbsp; 🧪 Ungetestet (könnte funktionieren) &nbsp;|&nbsp; ❌ Noch nicht unterstützt

| Gerät | Status |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (Strömungspumpe) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (Rückförderpumpe) | ✅ |
| **DC Runner** (Abschäumerpumpe) | ✅ |

<!-- generated:aqua-devices:end -->

**EcoDrift / SmartDrift Funktionen:**
- Ein/Aus, Wellentyp (Puls/Gezeiten), Fütterungsmodus, Timer, 0-10V Steuerungsmodus
- Wellenmodi: Klassisch, Sinus, Zufällig, Konstanter Fluss
- Kopplung: Unabhängig, Master, Slave
- Durchfluss-, Frequenz- und Fütterungsdauer-Steuerung
- Zeitfensterprogramm, bis zu 48 Zeitfenster
- Vollständige Diagnose-Fehlersensoren (Überstrom, Überspannung, Übertemperatur, blockierter Rotor, Trockenlauf, UART)

**DC Runner Funktionen:**
- Ein/Aus, Fütterungsmodus (1–60 Min. Pause), 0-10V Steuerungsmodus
- Durchflusssteuerung (30–100%)
- Zeitfensterprogramm, bis zu 48 Zeitfenster
- Diagnose-Fehlersensoren (Trockenlauf, blockierter Rotor, Spannung, Überstrom, Übertemperatur, UART)

**Installation:** Suchen Sie in *Einstellungen > Marketplace* nach „Aqua Medic“.

---

<!-- generated:maintenance:start -->

#### 🐙 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Wartungsverfolgung für Geräte, die Home Assistant nicht erreicht.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Strömungspumpen, Rückförderpumpen, Abschäumer, Reaktoren — alles, was Sie von Hand warten. Ein Eintrag pro Marke, ein Gerät pro Ausrüstung, vier Entitäten pro Aufgabe: eine Schaltfläche, die die Arbeit protokolliert, eine Zahl für das Intervall, ein Schalter zum Stummschalten der Hinweise und ein Datum, um die letzte Wartung rückwirkend einzutragen.

**Hauptfunktionen:**

- Voreinstellungen für Tunze, Jebao und generische Geräte, mit Herstellerintervallen wo veröffentlicht
- Eine gemeinsame Bibliothek mit 22 Aufgaben, in 8 Sprachen übersetzt
- Rückdatierung, damit ein neues Gerät nicht bei „nie gemacht" beginnt
- Dienst `reef_maintenance.reset` — NFC-Tag an die Pumpe kleben und nach getaner Arbeit scannen
- Gleicher `reef_role`-Vertrag wie die verbundenen Integrationen: die Aufgaben erscheinen in der Wartungsansicht der Karte

**Installation:** Suchen Sie in *Einstellungen > Marketplace* nach "reef-maintenance".

<!-- generated:maintenance:end -->

---

<!-- generated:reeftank:start -->

#### 🐟 [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component)

**Ein lebendiges Bild Ihres Aquariums auf dem Dashboard.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reeftank-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reeftank-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reeftank-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reeftank-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

<p align="center"><img src="https://raw.githubusercontent.com/Elwinmage/ha-reeftank-component/main/doc/img/preview.webp" width="70%" alt="ReefTank"/></p>

Die Integration hinter der Aquariumkarte von ha-reef-card: Ihr Foto, das Wasser beleuchtet von Ihren echten Lampen, animierte Fische und Korallen und Ihre Geräte und Entitäten darauf. Sie speichert die Aquarien, ihre Bilder und ihren Besatz und protokolliert die Fütterungen.

**Hauptfunktionen:**

- Wasser, Sand und Steine auf Ihrem eigenen Foto umranden — oder das Becken mit Stein- und Sandtexturen zeichnen
- Fische im Schwarm, im Freiwasser, auf dem Sand oder aus ihrer Höhle schauend, die sich nachts hinter den Steinen verstecken
- Wasser in der Farbe Ihrer Lampen (ReefLED oder jedes Licht), Korallen, die sich mit den Pumpen wiegen
- Fütterungen von Futterautomaten, Kurzbefehlen oder einem Dienst; Fisch- und Korallenzahl als Sensoren; pH und ORP werden mit dem eigenen Verlauf des Beckens verglichen
- Arten aus dem [reeftank-catalog](https://github.com/Elwinmage/reeftank-catalog), automatisch aktuell gehalten

**Installation:** Suchen Sie in *Einstellungen > Marketplace* nach "ReefTank" und installieren Sie ha-reef-card für die Karte.

<!-- generated:reeftank:end -->

---

### Karten

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Benutzerdefinierte Lovelace-Karte für Riff-Dashboards.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

Die **Reef Card** für Home Assistant hilft Ihnen, Ihr Riffaquarium direkt vom Dashboard aus zu verwalten. In Kombination mit [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) erkennt und unterstützt sie automatisch Ihre Red Sea (ReefBeat) Geräte.

> Nicht-Redsea-Geräte können ebenfalls unterstützt werden — [hier anfragen](https://github.com/Elwinmage/ha-reef-card/discussions/2).

<!-- generated:card-devices:start -->

**Unterstützte Geräte:**

> ✅ Unterstützt &nbsp;|&nbsp; 🚧 In Arbeit &nbsp;|&nbsp; 🧪 Ungetestet (könnte funktionieren) &nbsp;|&nbsp; ❌ Noch nicht unterstützt

| Gerät | Status | Highlights |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Vollständige Planung, manuelle Dosierung, Entlüften und Kalibrieren, Zusatzstoffverwaltung, Verbrauchsverfolgung, Dosierregelung (assistiert, Salzlösung), Dosierverlauf |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Animierter Rollenstatus, manueller/automatischer/geplanter Vorschub, Sensorstatus, Wochen- und Monatsgrafiken |
| **ReefRun (RSRUN)** | ✅ | Pumpendrehzahl, Zeitplan-Editor, Überschäumen-Verwaltung |
| **ReefATO+** | ✅ | Wasserstand, Lecksonde, Pumpendiagnose, Verbrauchsdiagramm, Leck-Summer |
| **ReefControl (RSCONTROLPRO)** | ✅ | Sonden mit Pegelbalken, Trends und 7-Tage-Verlauf, geführte pH/EC/ORP/Temperatur-Kalibrierung, 12V-Ports, ATO, Summer, gekoppelte Steckdosenleiste |
| **ReefControl (RSCONTROLLITE)** | 🧪 | Sonden mit Pegelbalken, Trends und 7-Tage-Verlauf, geführte pH/EC/ORP/Temperatur-Kalibrierung, 12V-Ports, ATO, Summer, gekoppelte Steckdosenleiste |
| **ReefControl-Power (RSPOWER6)** | ✅ | Steuerung pro Steckdose, Modi Ein/Aus/Zeitplan/Sonde, verknüpfte Geräte, lokale Temperatursonde oder ReefControl-Verbindung |
| **ReefControl-Power (RSPOWER8)** | 🧪 | Steuerung pro Steckdose, Modi Ein/Aus/Zeitplan/Sonde, verknüpfte Geräte, lokale Temperatursonde oder ReefControl-Verbindung |
| **ReefLed (G1)** | ✅ | Himmel mit Sonne und Mond, Lichtkegel mit dem Tagesprogramm, Regler für Intensität/Farbe oder Weiß/Blau, Programm-Editor (Kelvin oder Weiß/Blau, Wolken), Wettermodus, Gruppen mit versetztem Sonnenaufgang, Akklimatisierung |
| **ReefLed (G2)** | 🧪 | Himmel mit Sonne und Mond, Lichtkegel mit dem Tagesprogramm, Regler für Intensität/Farbe oder Weiß/Blau, Programm-Editor (Kelvin oder Weiß/Blau, Wolken), Wettermodus, Gruppen mit versetztem Sonnenaufgang, Akklimatisierung |
| **ReefWave (RSWAVE25/45)** | ✅ | Animierte Pumpenansicht, Geschwindigkeit und Richtung, Wellenbibliothek, Zeitplan-Editor mit Zeitfenstern, Pumpengruppen |
| **Aqua Medic EcoDrift / SmartDrift** | ✅ | Pumpendrehzahl im Bild, Störungen, Fütterungspause, Zeitfenster-Programm-Editor |
| **Aqua Medic DC Runner (return, skimmer)** | ✅ | Ansicht als Förder- oder Abschäumerpumpe je nach Rolle in der Integration, Drehzahl, Störungen, Zeitfenster-Programm-Editor |
| **Energy Backup (reefbeatEnergyBackup)** | ✅ | Energieflüsse von Netz, Batterie und Pumpen, gezeichnet mit Power Flow Card Plus |
| **VSON fish feeder (hacked, ESPHome)** | ✅ | Lebendiges Bild des Automaten, Fütterungsplätze, Vorratswarnung, Jetzt füttern |
| **Aquarium view (ha-reeftank-component)** | ✅ | Das Foto Ihres Beckens mit Live-Geräten und -Entitäten, vom Licht Ihrer Lampen getöntes Wasser, animierte Fische und Korallen, Szeneneditor mit sieben Reitern |

<!-- generated:card-devices:end -->

**ReefDose-Highlights:**
- 6-Zonen-Karte: Config/WiFi, Zustände, manuales Dosieren mit Shortcuts, Kopfplanung mit kreisförmigem Fortschritt, Supplement-Verwaltung mit Markenbildern und Warteschlange für bevorstehende Dosen
- Unterstützung von Priming- und Kalibrierungsabläufen
- Dialoge der Dosierregelung: assistierte Dosierung, Salzlösung mit Salinitätsdiagramm
- Supplement-Bibliothek mit Bildern für Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest und mehr

**ReefMat-Highlights:**
- 7-Zonen-Karte mit animiertem Hintergrund, der sich je nach Rollenverbrauch ändert (0%–100%)
- Echtzeit-Rolleninfo: Restlänge, Tagesdurchschnitt, geschätzte verbleibende Tage
- Manuelle, automatische und geplante Vorschubsteuerung
- Anzeige des Füllstandsensorstatus (verbunden, getrennt, verschmutzt)
- Wochen- und Monatsverbrauchsdiagramme

**Aquarienansicht:** Eine zweite Karte, `custom:reef-aquarium-card`, zeigt ein lebendiges Bild Ihres Beckens. Sie benötigt [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component).

**Installation:** Direkt im [Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) verfügbar — suchen Sie nach "reef-card".

**Konfiguration:** Ohne den Parameter `device` erkennt die Karte automatisch alle ReefBeat-Geräte und lässt Sie wählen. Setzen Sie den Parameter `device`, um ein bestimmtes Gerät zu erzwingen.

<!-- generated:card-videos:start -->

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="ReefDose-Demo" width="300"/></a><br/><em>ReefDose-Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="ReefMat-Demo" width="300"/></a><br/><em>ReefMat-Demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=Xxv38OPqiGI"><img src="https://img.youtube.com/vi/Xxv38OPqiGI/0.jpg" alt="ReefRun-Demo" width="300"/></a><br/><em>ReefRun-Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=Ko46fHonOP4"><img src="https://img.youtube.com/vi/Ko46fHonOP4/0.jpg" alt="Wartungs-Demo" width="300"/></a><br/><em>Wartungs-Demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=2R0DHp2eqT4"><img src="https://img.youtube.com/vi/2R0DHp2eqT4/0.jpg" alt="ReefATO+-Demo" width="300"/></a><br/><em>ReefATO+-Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=voFobfc7Slk"><img src="https://img.youtube.com/vi/voFobfc7Slk/0.jpg" alt="ReefControl- & ReefControl-Power-Demo" width="300"/></a><br/><em>ReefControl- & ReefControl-Power-Demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=pA49z8QjTN4"><img src="https://img.youtube.com/vi/pA49z8QjTN4/0.jpg" alt="ReefLed-Demo" width="300"/></a><br/><em>ReefLed-Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=sYVeE0zV3eo"><img src="https://img.youtube.com/vi/sYVeE0zV3eo/0.jpg" alt="ReefWave-Demo" width="300"/></a><br/><em>ReefWave-Demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=9Gh4YE6Ck9g"><img src="https://img.youtube.com/vi/9Gh4YE6Ck9g/0.jpg" alt="Aqua-Medic-Demo" width="300"/></a><br/><em>Aqua-Medic-Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=ZtYobmQZf9k"><img src="https://img.youtube.com/vi/ZtYobmQZf9k/0.jpg" alt="Aquarienansicht-Demo" width="300"/></a><br/><em>Aquarienansicht-Demo</em></td>
</tr>
</table>

<!-- generated:card-videos:end -->

---

## 🔌 Infrastruktur

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Autonomes Batterie-Backup-System für Red Sea Riffaquarien.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Halten Sie Ihre ReefWave, ReefRun und DC Skimmer bei Stromausfällen mit einer 24V LiFePO₄-Batterie, einem Raspberry Pi und intelligenter Pumpen-Drosselung am Laufen.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Hauptfunktionen:**
- **Batterieüberwachung** via INA226 (I2C) + optionaler Victron BLE Lader
- **Sofortige Ausfallserkennung** via 230V-Relais am GPIO
- **Progressive Pumpendrosselung** — SoC-basierte Stufen berechnet aus einer Zielautonomie
- **3-stufiges Netzwerk-Failover** — Ethernet → Wi-Fi → autonomer Mirror-Hotspot
- **4G LTE Failover** — Benachrichtigungen und ReefBeat-Cloud-Zugang über USB-Modem oder Smartphone-Tethering
- **Push-Benachrichtigungen** via [ntfy.sh](https://ntfy.sh) (kostenlos, kein Konto erforderlich)
- **Home Assistant Integration** — MQTT Auto-Discovery, Update-Entity, Batterie-Test-Blueprint
- **Poseidon-Watchdog** — überwacht das MQTT-Relais von ha-reefbeat-component und schaltet die Geräte in den Normalmodus zurück, wenn es ausfällt
- **Auto-Update** — prüft GitHub auf neue Versionen, HA Update-Entity mit "Installieren"-Button

**Hardware-Stufen:**

| Stufe | Was Sie bekommen | Budget |
|-------|-----------------|--------|
| **1 — Basis** | Batterie + Kabel, passives Backup | ~290 € |
| **2 — Normal** *(empfohlen)* | + RPi + INA226 + Relais, volles Monitoring & Automatisierung | ~402 € |
| **3 — Erweitert** | + Victron BLE Lader, Smart-Schutzschalter, 4G-Modem | ~664 € |

**Installation:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Funktioniert eigenständig oder als Ergänzung zu [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) für ein vollständig integriertes Riff-Management-Setup.

---

<!-- generated:blueprints:start -->

#### 🐬 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Automatisierungs-Blueprints für das gesamte Ökosystem.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Benachrichtigt Sie auf dem Telefon über überfällige Wartungen, gefunden über das gemeinsame Attribut `reef_role`, sodass jede Integration abgedeckt ist, und über nicht mehr erreichbare Geräte. Testet Ihre Heizer einzeln und warnt Sie, wenn ein Relais aus ist, sein Gerät aber noch Strom zieht. Acht Sprachen, je eine Import-Schaltfläche.

**Installation:** Import aus dem Repository, eine Schaltfläche je Sprache.

<!-- generated:blueprints:end -->

---

## 📐 3D-Modelle

### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer Impeller-Werkzeug*](https://www.thingiverse.com/thing:7313258)

**Videodemonstration:**
<video width="100%" height="auto" controls style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  Your browser does not support the video tag.
</video>


<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Red Sea Schlüssel 3D"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<script>
  const modelViewer = document.querySelector("#aquarium-model");
  modelViewer.addEventListener("load", () => {
    const width = modelViewer.clientWidth;
    const height = modelViewer.clientHeight;
    if (width === 0 || height === 0) {
        modelViewer.style.width = "100%";
        modelViewer.style.height = "500px";
    }
  });
</script>


<!-- generated:skimmer-risers:start -->

#### 📦 [*Fußerhöhungen für den Red Sea DC Skimmer*](https://www.thingiverse.com/thing:7420525)

Erhöhungen für die Füße des Red Sea DC Abschäumers, um seine Höhe im Technikbecken einzustellen. Vier Versionen: 80, 70, 60 und 50 mm.

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer src="assets/models/redsea-skimmer-risers.glb"
                alt="Fußerhöhungen für den Red Sea DC Skimmer"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

### Wassertests

#### 📦 [*Organizer für Red Sea Riffaquarium-Tests*](https://www.thingiverse.com/thing:7429899)

Ein Aufbewahrungssystem für die Red Sea Wassertests fürs Riffaquarium.

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer src="assets/models/redsea-tests-organizer.glb"
                alt="Organizer für Red Sea Riffaquarium-Tests"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<!-- generated:skimmer-risers:end -->

---

<!-- generated:contact:start -->

## 💬 Kontakt & Support

- **Fragen und Funktionswünsche:** eröffnen Sie eine Diskussion im betreffenden Projekt — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component/issues) · [reeftank-catalog](https://github.com/Elwinmage/reeftank-catalog/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues) · [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints/issues)
- **Fehlerberichte:** eröffnen Sie ein Issue im selben Projekt, mit den Details.
- **Projekt unterstützen:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
