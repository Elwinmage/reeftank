---
layout: default
title: Elwinmage - Reef Tech Projekte
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷](fr.md) / [🇩🇪] / [🇪🇸](es.md) / [🇮🇹](it.md) / [🇵🇱](pl.md) / [🇵🇹](pt.md)

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

Verwalten Sie Ihre Red Sea ReefBeat-Geräte **lokal** (kein Cloud erforderlich): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun und ReefWave.

> ⚠️ Dies ist kein offizielles Red Sea Repository. Nutzung auf eigene Gefahr.

**Hauptfunktionen:**
- **100% lokale Steuerung** — keine Cloud-Abhängigkeit für die meisten Geräte
- Automatische Geräteerkennung im lokalen Netzwerk (mit manuellem Modus und Subnetz-Unterstützung)
- Benutzerdefinierte Icons für alle ReefBeat-Geräte
- Firmware-Update-Benachrichtigungen (mit optionaler Cloud API)
- Live-Konfigurationsaktualisierung für Echtzeit-Überwachung
- Mehrsprachige Unterstützung

**Unterstützte Geräte:**

| Gerät | Modelle | Status |
|-------|---------|--------|
| **ReefATO+** | RSATO+ | ✅ Getestet |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Getestet |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Getestet |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Getestet |
| **ReefRun** | RSRUN | ✅ Getestet |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Noch nicht — [kontaktieren Sie mich](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**ReefWave-Besonderheiten:** ReefWave ist das einzige Gerät, das an die ReefBeat-Cloud gebunden ist. Drei Betriebsmodi stehen zur Verfügung — Cloud, Lokal und Hybrid — damit Sie die Balance zwischen voller lokaler Steuerung und Synchronisation mit der ReefBeat-App wählen können.

**Installation:** Direkt in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) verfügbar — suchen Sie nach "redsea" oder "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Steuerung von Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Steuern Sie Ihre Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API (dasselbe Backend wie die offizielle Aqua Medic App).

**Unterstützte Geräte:**

| Gerät | Status |
|-------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (Strömungspumpe) | ✅ Unterstützt |
| **DC Runner x.1 / x.2 / x.3** (Rückförderpumpe) | 🧪 Ungetestet |
| **Reefdoser EVO** (Dosierpumpe) | ❌ Noch nicht — [kontaktieren Sie mich](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (Temperaturregler) | ❌ Noch nicht — [kontaktieren Sie mich](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (Beleuchtung) | ❌ Noch nicht — [kontaktieren Sie mich](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

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

**Unterstützte Geräte:**

| Gerät | Status | Highlights |
|-------|--------|------------|
| **ReefDose** (RSDOSE2/4) | ✅ Implementiert | Vollständige Planung, manuelles Dosieren, Priming/Kalibrierung, Supplement-Verwaltung, Nutzungsverfolgung |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implementiert | Animierter Rollenstatus, manuelle/auto/geplante Vorschub, Sensorstatus, Wochen-/Monatsdiagramme |
| **ReefRun** (RSRUN) | ☑️ In Arbeit | Pumpengeschwindigkeitssteuerung, Überschäumungsverwaltung |
| **ReefATO+** | ❌ Geplant | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Geplant | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Geplant | [Für Priorität abstimmen](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

**ReefDose-Highlights:**
- 6-Zonen-Karte: Config/WiFi, Zustände, manuelles Dosieren mit Shortcuts, Kopfplanung mit kreisförmigem Fortschritt, Supplement-Verwaltung mit Markenbildern und Warteschlange für bevorstehende Dosen
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

## 📐 3D-Modelle

### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer Impeller-Werkzeug*](https://www.thingiverse.com/thing:7313258)


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

## 💬 Kontakt & Support

- **Fragen & Feature-Anfragen:** Nutzen Sie den [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions)-Tab jedes Projekts
- **Fehler melden:** Öffnen Sie ein [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) mit Details
- **Projekt unterstützen:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
