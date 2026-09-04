---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: it
---

{% include language-selector.html %}

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

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


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

Gestisci i tuoi dispositivi Red Sea ReefBeat **localmente** (senza cloud): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun e ReefWave.

> ⚠️ Questo non è un repository ufficiale Red Sea. Uso a proprio rischio.

**Funzionalità principali:**
- **Controllo 100% locale** — nessuna dipendenza dal cloud per la maggior parte dei dispositivi
- Rilevamento automatico dei dispositivi sulla rete locale (con modalità manuale e supporto sottoreti)
- Icone personalizzate per tutti i dispositivi ReefBeat
- Notifiche di aggiornamento firmware (con Cloud API opzionale)
- Modalità di aggiornamento configurazione in tempo reale
- Supporto multilingue

<!-- generated:beat-devices:start -->

**Dispositivi supportati:**

> ✅ Supportato &nbsp;|&nbsp; 🚧 In corso &nbsp;|&nbsp; 🧪 Non testato (potrebbe funzionare) &nbsp;|&nbsp; ❌ Non ancora supportato

| Dispositivo | Modelli | Stato |
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

**Specificità ReefWave:** ReefWave è l'unico dispositivo legato al cloud ReefBeat. Tre modalità operative sono disponibili — Cloud, Locale e Ibrida — per scegliere l'equilibrio tra controllo locale completo e sincronizzazione con l'app mobile ReefBeat.

**Installazione:** Disponibile direttamente in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — cerca "redsea" o "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Controllo delle pompe Aqua Medic tramite Home Assistant via API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controlla le tue pompe Aqua Medic da Home Assistant tramite l'API cloud Gizwits (stesso backend dell'app ufficiale Aqua Medic).

<!-- generated:aqua-devices:start -->

**Dispositivi supportati:**

> ✅ Supportato &nbsp;|&nbsp; 🚧 In corso &nbsp;|&nbsp; 🧪 Non testato (potrebbe funzionare) &nbsp;|&nbsp; ❌ Non ancora supportato

| Dispositivo | Stato |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (di movimento) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (pompa di risalita) | ✅ |
| **DC Runner** (pompa dello schiumatoio) | ✅ |
| **Reefdoser EVO** (pompa dosatrice) | ❌ — [Richiedilo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controllore di temperatura) | ❌ — [Richiedilo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (illuminazione) | ❌ — [Richiedilo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

<!-- generated:aqua-devices:end -->

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

<!-- generated:maintenance:start -->

#### 🐙 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Tracciamento della manutenzione per le apparecchiature che Home Assistant non raggiunge.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Pompe di movimento, pompe di risalita, schiumatoi, reattori — tutto ciò che pulite a mano. Una voce per marca, un dispositivo per apparecchiatura, quattro entità per attività: un pulsante che registra il lavoro, un numero per l'intervallo, un interruttore per silenziare gli avvisi e una data per retrodatare l'ultimo intervento.

**Funzioni principali:**

- Preset per Tunze, Jebao e apparecchiature generiche, con gli intervalli del produttore quando pubblicati
- Una libreria comune di 17 attività, tradotta in 8 lingue
- Retrodatazione, così una nuova apparecchiatura non parte da «mai fatto»
- Servizio `reef_maintenance.reset` — attaccate un tag NFC sulla pompa e scansionatelo a lavoro finito
- Stesso contratto `reef_role` delle integrazioni connesse: le attività compaiono nella vista manutenzione della scheda

**Installazione:** In HACS, aggiungete `https://github.com/Elwinmage/ha-reef-maintenance-component` come repository personalizzato (Integrazione).

<!-- generated:maintenance:end -->

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

<!-- generated:card-devices:start -->

**Dispositivi supportati:**

> ✅ Supportato &nbsp;|&nbsp; 🚧 In corso &nbsp;|&nbsp; 🧪 Non testato (potrebbe funzionare) &nbsp;|&nbsp; ❌ Non ancora supportato

| Dispositivo | Stato | Punti di forza |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Pianificazione completa, dosaggio manuale, adescamento e calibrazione, gestione dei supplementi, monitoraggio dei consumi |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Stato del rotolo animato, avanzamento manuale/automatico/programmato, stato del sensore, grafici settimanali e mensili |
| **ReefRun (RSRUN)** | ✅ | Controllo della velocità della pompa, editor dei programmi, gestione della sovraschiumazione |
| **ReefATO+** | ✅ | Livello dell'acqua, sonda perdite, diagnostica pompa, grafico dei consumi, buzzer perdite |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Controllo per presa |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Vota per la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Vota per la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Vota per la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Vota per la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Vota per la priorità](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

<!-- generated:card-devices:end -->

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

<!-- generated:card-videos:start -->

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=Xxv38OPqiGI"><img src="https://img.youtube.com/vi/Xxv38OPqiGI/0.jpg" alt="Demo ReefRun" width="300"/></a><br/><em>Demo ReefRun</em></td>
<td><a href="https://www.youtube.com/watch?v=Ko46fHonOP4"><img src="https://img.youtube.com/vi/Ko46fHonOP4/0.jpg" alt="Demo Manutenzione" width="300"/></a><br/><em>Demo Manutenzione</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=2R0DHp2eqT4"><img src="https://img.youtube.com/vi/2R0DHp2eqT4/0.jpg" alt="Demo ReefATO+" width="300"/></a><br/><em>Demo ReefATO+</em></td>
</tr>
</table>

<!-- generated:card-videos:end -->

---

## 🔌 Infrastruttura

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Sistema autonomo di backup a batteria per acquari di barriera Red Sea.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Mantieni ReefWave, ReefRun e DC Skimmer in funzione durante le interruzioni di corrente con una batteria LiFePO₄ 24V, un Raspberry Pi e una riduzione intelligente delle pompe.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Funzionalità principali:**
- **Monitoraggio batteria** via INA226 (I2C) + caricabatterie Victron BLE opzionale
- **Rilevamento istantaneo** delle interruzioni tramite relè 230V su GPIO
- **Riduzione progressiva** delle pompe — livelli SoC calcolati da un'autonomia target
- **Failover rete a 3 livelli** — Ethernet → Wi-Fi → hotspot mirror autonomo
- **Failover 4G/LTE** — notifiche e accesso cloud ReefBeat via modem USB o tethering
- **Notifiche push** via [ntfy.sh](https://ntfy.sh) (gratuito, senza account)
- **Integrazione Home Assistant** — auto-discovery MQTT, entità aggiornamento, blueprint test batteria
- **Auto-aggiornamento** — controlla GitHub, pulsante "Installa" in HA

**Livelli hardware:**

| Livello | Cosa ottieni | Budget |
|---------|-------------|--------|
| **1 — Base** | Batteria + cavi, backup passivo | ~290 € |
| **2 — Normale** *(consigliato)* | + RPi + INA226 + relè, monitoraggio & automazione | ~402 € |
| **3 — Avanzato** | + Caricabatterie Victron BLE, interruttore smart, modem 4G | ~627 € |

**Installazione:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Funziona autonomamente o come complemento a [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) per una gestione completa dell'acquario.

---

<!-- generated:blueprints:start -->

#### 🐬 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Blueprint di notifica per tutto l'ecosistema.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Vi avvisa sul telefono delle manutenzioni scadute, trovate tramite l'attributo comune `reef_role` così che ogni integrazione sia coperta, e dei dispositivi diventati irraggiungibili. Otto lingue, un pulsante di importazione ciascuna.

**Installazione:** importate dal repository, un pulsante per lingua.

<!-- generated:blueprints:end -->

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

**Dimostrazione video:**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->

## 💬 Contatti e supporto

- **Domande e richieste di funzionalità:** aprite una discussione sul progetto interessato — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Segnalazione bug:** aprite una issue sullo stesso progetto, con i dettagli.
- **Sostieni il progetto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
