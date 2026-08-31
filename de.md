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
       poster="image-de-remplacement.jpg"
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

### Integrationen

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Lokale Integration für das Red Sea ReefBeat-Ökosystem.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
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

**Installation:** Direkt in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) verfügbar — suchen Sie nach "redsea" oder "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Steuerung von Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
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
| **Reefdoser EVO** (Dosierpumpe) | ❌ — [Anfragen](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (Temperaturregler) | ❌ — [Anfragen](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (Beleuchtung) | ❌ — [Anfragen](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
<!-- generated:aqua-devices:end -->

**EcoDrift / SmartDrift Funktionen:**
- Ein/Aus, Wellentyp (Puls/Gezeiten), Fütterungsmodus, Timer, 0-10V Steuerungsmodus
- Wellenmodi: Klassisch, Sinus, Zufällig, Konstanter Fluss
- Kopplung: Unabhängig, Master, Slave
- Durchfluss-, Frequenz- und Fütterungsdauer-Steuerung
- Vollständige Diagnose-Fehlersensoren (Überstrom, Überspannung, Übertemperatur, blockierter Rotor, Trockenlauf, UART)

**DC Runner Funktionen:**
- Ein/Aus, Fütterungsmodus (10 Min. Pause), 0-10V Steuerungsmodus
- Durchflusssteuerung (30–100%)
- Diagnose-Fehlersensoren (Trockenlauf, blockierter Rotor, Spannung)

**Installation:** In HACS fügen Sie `https://github.com/Elwinmage/ha-aquamedic-component` als benutzerdefiniertes Repository (Integration) hinzu und suchen dann nach "Aqua Medic".

---

<!-- generated:maintenance:start -->
#### 🧰 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Wartungsverfolgung für Geräte, die Home Assistant nicht erreicht.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Strömungspumpen, Rückförderpumpen, Abschäumer, Reaktoren — alles, was Sie von Hand warten. Ein Eintrag pro Marke, ein Gerät pro Ausrüstung, vier Entitäten pro Aufgabe: eine Schaltfläche, die die Arbeit protokolliert, eine Zahl für das Intervall, ein Schalter zum Stummschalten der Hinweise und ein Datum, um die letzte Wartung rückwirkend einzutragen.

**Hauptfunktionen:**

- Voreinstellungen für Tunze, Jebao und generische Geräte, mit Herstellerintervallen wo veröffentlicht
- Eine gemeinsame Bibliothek mit 17 Aufgaben, in 8 Sprachen übersetzt
- Rückdatierung, damit ein neues Gerät nicht bei „nie gemacht" beginnt
- Dienst `reef_maintenance.reset` — NFC-Tag an die Pumpe kleben und nach getaner Arbeit scannen
- Gleicher `reef_role`-Vertrag wie die verbundenen Integrationen: die Aufgaben erscheinen in der Wartungsansicht der Karte

**Installation:** In HACS `https://github.com/Elwinmage/ha-reef-maintenance-component` als benutzerdefiniertes Repository (Integration) hinzufügen.
<!-- generated:maintenance:end -->

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
| **ReefDose (RSDOSE2/4)** | ✅ | Vollständige Planung, manuelle Dosierung, Entlüften und Kalibrieren, Zusatzstoffverwaltung, Verbrauchsverfolgung |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Animierter Rollenstatus, manueller/automatischer/geplanter Vorschub, Sensorstatus, Wochen- und Monatsgrafiken |
| **ReefRun (RSRUN)** | ✅ | Pumpendrehzahl, Zeitplan-Editor, Überschäumen-Verwaltung |
| **ReefATO+** | ✅ | Wasserstand, Lecksonde, Pumpendiagnose, Verbrauchsdiagramm, Leck-Summer |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Steuerung pro Steckdose |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
<!-- generated:card-devices:end -->

**ReefDose-Highlights:**
- 6-Zonen-Karte: Config/WiFi, Zustände, manuales Dosieren mit Shortcuts, Kopfplanung mit kreisförmigem Fortschritt, Supplement-Verwaltung mit Markenbildern und Warteschlange für bevorstehende Dosen
- Unterstützung von Priming- und Kalibrierungsabläufen
- Supplement-Bibliothek mit Bildern für Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest und mehr

**ReefMat-Highlights:**
- 7-Zonen-Karte mit animiertem Hintergrund, der sich je nach Rollenverbrauch ändert (0%–100%)
- Echtzeit-Rolleninfo: Restlänge, Tagesdurchschnitt, geschätzte verbleibende Tage
- Manuelle, automatische und geplante Vorschubsteuerung
- Anzeige des Füllstandsensorstatus (verbunden, getrennt, verschmutzt)
- Wochen- und Monatsverbrauchsdiagramme

**Installation:** Direkt in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) verfügbar — suchen Sie nach "reef-card".

**Konfiguration:** Ohne den Parameter `device` erkennt die Karte automatisch alle ReefBeat-Geräte und lässt Sie wählen. Setzen Sie den Parameter `device`, um ein bestimmtes Gerät zu erzwingen.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="ReefDose Demo" width="300"/></a><br/><em>ReefDose Demo</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="ReefMat Demo" width="300"/></a><br/><em>ReefMat Demo</em></td>
</tr>
</table>

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
- **Auto-Update** — prüft GitHub auf neue Versionen, HA Update-Entity mit "Installieren"-Button

**Hardware-Stufen:**

| Stufe | Was Sie bekommen | Budget |
|-------|-----------------|--------|
| **1 — Basis** | Batterie + Kabel, passives Backup | ~290 € |
| **2 — Normal** *(empfohlen)* | + RPi + INA226 + Relais, volles Monitoring & Automatisierung | ~402 € |
| **3 — Erweitert** | + Victron BLE Lader, Smart-Schutzschalter, 4G-Modem | ~627 € |

**Installation:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Funktioniert eigenständig oder als Ergänzung zu [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) für ein vollständig integriertes Riff-Management-Setup.

---

<!-- generated:blueprints:start -->
#### 🔔 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Benachrichtigungs-Blueprints für das gesamte Ökosystem.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Meldet auf dem Telefon überfällige Wartungen, über das gemeinsame `reef_role`-Attribut gefunden, sodass jede Integration abgedeckt ist, sowie nicht mehr erreichbare Geräte. Acht Sprachen, je eine Import-Schaltfläche.

**Installation:** Import aus dem Repository, eine Schaltfläche je Sprache.
<!-- generated:blueprints:end -->

---

## 📐 3D-Modelle

### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer Impeller-Werkzeug*](https://www.thingiverse.com/thing:7313258)

**Videodemonstration:**
<video width="100%" height="auto" controls style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
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

---

<!-- generated:contact:start -->
## 💬 Kontakt & Support

- **Fragen und Funktionswünsche:** eröffnen Sie eine Diskussion im betreffenden Projekt — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Fehlerberichte:** eröffnen Sie ein Issue im selben Projekt, mit den Details.
- **Projekt unterstützen:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
<!-- generated:contact:end -->
