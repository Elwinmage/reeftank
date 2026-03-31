---
layout: default
title: Elwinmage - Progetti Reef Tech
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷](fr.md) / [🇩🇪](de.md) / [🇪🇸](es.md) / [🇮🇹] / [🇵🇱](pl.md) / [🇵🇹](pt.md)

# I miei strumenti ReefTank

Benvenuto nella documentazione dei miei progetti per acquari di barriera.

<video src="assets/videos/logo_v1.mp4" 
       poster="image-de-remplacement.jpg"
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Integrazioni e schede Home Assistant

---

### Integrazioni

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Integrazione locale per l'ecosistema Red Sea ReefBeat.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Gestisci i tuoi dispositivi Red Sea ReefBeat **localmente** (senza cloud): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun e ReefWave.

> ⚠️ Questo non è un repository ufficiale Red Sea. Uso a proprio rischio.

**Funzionalità principali:**
- **Controllo 100% locale** — nessuna dipendenza dal cloud per la maggior parte dei dispositivi
- Rilevamento automatico dei dispositivi sulla rete locale (con modalità manuale e supporto sottoreti)
- Icone personalizzate per tutti i dispositivi ReefBeat
- Notifiche di aggiornamento firmware (con Cloud API opzionale)
- Modalità di aggiornamento configurazione in tempo reale
- Supporto multilingue

**Dispositivi supportati:**

| Dispositivo | Modelli | Stato |
|-------------|---------|-------|
| **ReefATO+** | RSATO+ | ✅ Testato |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Testato |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Testato |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Testato |
| **ReefRun** | RSRUN | ✅ Testato |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Non ancora — [contattami](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**Specificità ReefWave:** ReefWave è l'unico dispositivo legato al cloud ReefBeat. Tre modalità operative sono disponibili — Cloud, Locale e Ibrida — per scegliere l'equilibrio tra controllo locale completo e sincronizzazione con l'app mobile ReefBeat.

**Installazione:** Disponibile direttamente in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — cerca "redsea" o "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Controllo delle pompe Aqua Medic tramite Home Assistant via API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controlla le tue pompe Aqua Medic da Home Assistant tramite l'API cloud Gizwits (stesso backend dell'app ufficiale Aqua Medic).

**Dispositivi supportati:**

| Dispositivo | Stato |
|-------------|-------|
| **EcoDrift / SmartDrift x.1 / x.3** (pompa di movimento) | ✅ Supportato |
| **DC Runner x.1 / x.2 / x.3** (pompa di risalita) | 🧪 Non testato |
| **Reefdoser EVO** (pompa dosatrice) | ❌ Non ancora — [contattami](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controllore di temperatura) | ❌ Non ancora — [contattami](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (illuminazione) | ❌ Non ancora — [contattami](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

**Funzionalità EcoDrift / SmartDrift:**
- Accensione/spegnimento, tipo d'onda (Impulso/Marea), modalità alimentazione, timer, modalità controllo 0-10V
- Modalità onda: Classica, Sinusoidale, Casuale, Flusso costante
- Collegamento: Indipendente, Master, Slave
- Controllo portata, frequenza e durata alimentazione
- Sensori diagnostici completi (sovracorrente, sovratensione, surriscaldamento, rotore bloccato, marcia a secco, UART)

**Funzionalità DC Runner:**
- Accensione/spegnimento, modalità alimentazione (pausa 10 min), modalità controllo 0-10V
- Controllo portata (30–100%)
- Sensori diagnostici (marcia a secco, rotore bloccato, tensione)

**Installazione:** In HACS, aggiungi `https://github.com/Elwinmage/ha-aquamedic-component` come repository personalizzato (Integrazione), poi cerca "Aqua Medic".

---

### Schede

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Scheda Lovelace personalizzata per dashboard di barriera.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

La **Reef Card** per Home Assistant ti aiuta a gestire il tuo acquario di barriera direttamente dalla dashboard. Combinata con [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component), rileva e supporta automaticamente i tuoi dispositivi Red Sea (ReefBeat).

> I dispositivi non-Redsea possono essere supportati — [richiedilo qui](https://github.com/Elwinmage/ha-reef-card/discussions/2).

**Dispositivi supportati:**

| Dispositivo | Stato | Punti di forza |
|-------------|-------|----------------|
| **ReefDose** (RSDOSE2/4) | ✅ Implementato | Pianificazione completa, dosaggio manuale, adescamento/calibrazione, gestione integratori, monitoraggio utilizzo |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implementato | Stato del rullo animato, avanzamento manuale/auto/programmato, stato sensore, grafici settimanali/mensili |
| **ReefRun** (RSRUN) | ☑️ In corso | Controllo velocità pompa, gestione sovraschiumazione |
| **ReefATO+** | ❌ Pianificato | [Vota la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Pianificato | [Vota la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Pianificato | [Vota la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

**Punti di forza ReefDose:**
- Scheda a 6 zone: config/WiFi, stati, dosaggio manuale con scorciatoie, pianificazione per testina con progresso circolare, gestione integratori con immagini di marca, e coda delle prossime dosi
- Supporto flussi di adescamento e calibrazione
- Libreria integratori con immagini per Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest e altri

**Punti di forza ReefMat:**
- Scheda a 7 zone con sfondo animato che cambia in base all'utilizzo del rullo (0%–100%)
- Info in tempo reale del rullo: lunghezza residua, media giornaliera, giorni rimanenti stimati
- Controlli di avanzamento manuale, automatico e programmato
- Visualizzazione stato sensore di livello (connesso, disconnesso, sporco)
- Grafici di consumo settimanali e mensili

**Installazione:** Disponibile direttamente in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — cerca "reef-card".

**Configurazione:** Senza il parametro `device`, la scheda rileva automaticamente tutti i dispositivi ReefBeat e ti permette di scegliere. Imposta il parametro `device` per forzare un dispositivo specifico.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
</table>

---

## 📐 Modelli 3D

### ReefRun DC Skimmer
#### 📦 [*Strumento per girante skimmer DC Red Sea*](https://www.thingiverse.com/thing:7313258)


<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Chiave Red Sea 3D"
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

## 💬 Contatti e supporto

- **Domande e richieste di funzionalità:** Usa la scheda [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) di ogni progetto
- **Segnalare un bug:** Apri un [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) con i dettagli
- **Supporta il progetto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
