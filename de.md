---
layout: default
title: Elwinmage - Reef Tech Projekte
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
- Automatische Geräteerkennung im lokalen Netzwerk
- Benutzerdefinierte Icons für alle ReefBeat-Geräte
- Firmware-Update-Benachrichtigungen
- Live-Konfigurationsaktualisierung für Echtzeit-Überwachung
- Mehrsprachige Unterstützung

**Installation:** Direkt in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) verfügbar.

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Autonomes Batterie-Backup-System für Red Sea Riffaquarien.**

Halten Sie Ihre ReefWave, ReefRun und DC Skimmer bei Stromausfällen mit einer 24V LiFePO₄-Batterie, einem Raspberry Pi und intelligenter Pumpen-Drosselung am Laufen.

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Steuerung von Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API.**

Steuern Sie Ihre Aqua Medic Pumpen über Home Assistant mittels der Gizwits Cloud API (dasselbe Backend wie die offizielle Aqua Medic App).

---

### Karten

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Benutzerdefinierte Lovelace-Karte für Riff-Dashboards.**

Die **Reef Card** für Home Assistant hilft Ihnen, Ihr Riffaquarium direkt vom Dashboard aus zu verwalten.

---

## 💬 Kontakt & Support

- **Fragen & Feature-Anfragen:** Nutzen Sie den [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions)-Tab jedes Projekts
- **Fehler melden:** Öffnen Sie ein [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) mit Details
- **Projekt unterstützen:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
