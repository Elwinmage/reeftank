---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: fr
---

{% include language-selector.html %}

# Mes outils ReefTank

Bienvenue sur la documentation de mes projets pour aquarium récifal.

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

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Intégrations et cartes Home Assistant

---

### Intégrations

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Intégration locale pour l'écosystème Red Sea ReefBeat.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Gérez vos appareils Red Sea ReefBeat **localement** (sans cloud) : ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun et ReefWave.

> ⚠️ Ceci n'est pas un dépôt officiel Red Sea. Utilisation à vos risques et périls.

**Fonctionnalités clés :**
- **Contrôle 100% local** — aucune dépendance au cloud pour la plupart des appareils
- Détection automatique des appareils sur le réseau local (avec mode manuel et support sous-réseau)
- Icônes personnalisées pour tous les appareils ReefBeat
- Notifications de mise à jour du firmware (via Cloud API optionnelle)
- Mode de mise à jour en temps réel de la configuration
- Support multilingue

<!-- generated:beat-devices:start -->
**Appareils supportés :**

> ✅ Supporté &nbsp;|&nbsp; 🚧 En cours &nbsp;|&nbsp; 🧪 Non testé (peut fonctionner) &nbsp;|&nbsp; ❌ Pas encore supporté

| Appareil | Modèles | Statut |
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

**Spécificités ReefWave :** Le ReefWave est le seul appareil lié au cloud ReefBeat. Trois modes de fonctionnement sont disponibles — Cloud, Local et Hybride — pour choisir l'équilibre entre contrôle local total et synchronisation avec l'application mobile ReefBeat.

**Installation :** Disponible directement dans [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — recherchez "redsea" ou "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Contrôle des pompes Aqua Medic via Home Assistant grâce à l'API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Contrôlez vos pompes Aqua Medic depuis Home Assistant via l'API cloud Gizwits (même backend que l'application officielle Aqua Medic).

<!-- generated:aqua-devices:start -->
**Appareils supportés :**

> ✅ Supporté &nbsp;|&nbsp; 🚧 En cours &nbsp;|&nbsp; 🧪 Non testé (peut fonctionner) &nbsp;|&nbsp; ❌ Pas encore supporté

| Appareil | Statut |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (brassage) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (pompe de remontée) | ✅ |
| **DC Runner** (pompe d'écumeur) | ✅ |
| **Reefdoser EVO** (pompe doseuse) | ❌ — [Demandez-le](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (contrôleur de température) | ❌ — [Demandez-le](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (éclairage) | ❌ — [Demandez-le](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
<!-- generated:aqua-devices:end -->

**Fonctionnalités EcoDrift / SmartDrift :**
- Marche/arrêt, type de vague (Pulse/Marée), mode nourrissage, minuterie, mode contrôle 0-10V
- Modes de vagues : Classique, Sinusoïdale, Aléatoire, Flux constant
- Liaison : Indépendant, Maître, Esclave
- Contrôle du débit, de la fréquence et de la durée de nourrissage
- Capteurs de diagnostic complets (surintensité, surtension, surchauffe, rotor bloqué, marche à sec, UART)

**Fonctionnalités DC Runner :**
- Marche/arrêt, mode nourrissage (pause 10 min), mode contrôle 0-10V
- Contrôle du débit (30–100%)
- Capteurs de diagnostic (marche à sec, rotor bloqué, tension)

**Installation :** Dans HACS, ajoutez `https://github.com/Elwinmage/ha-aquamedic-component` comme dépôt personnalisé (Intégration), puis recherchez "Aqua Medic".

---

<!-- generated:maintenance:start -->
#### 🧰 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Suivi de maintenance pour le matériel que Home Assistant ne voit pas.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Pompes de brassage, pompes de remontée, écumeurs, réacteurs — tout ce que vous entretenez à la main. Une entrée par marque, un appareil par équipement, quatre entités par tâche : un bouton qui enregistre l'intervention, un nombre pour l'intervalle, un interrupteur pour couper les alertes et une date pour antidater la dernière intervention.

**Fonctions principales :**

- Préréglages Tunze, Jebao et matériel générique, avec les intervalles du fabricant quand il en publie
- Une bibliothèque commune de 17 tâches, traduite en 8 langues
- Antidatage, pour qu'un nouvel équipement ne démarre pas à « jamais fait »
- Service `reef_maintenance.reset` — collez un tag NFC sur la pompe et scannez-le une fois le travail terminé
- Même contrat `reef_role` que les intégrations connectées : les tâches arrivent dans la vue maintenance de la carte

**Installation :** Dans HACS, ajoutez `https://github.com/Elwinmage/ha-reef-maintenance-component` en dépôt personnalisé (Intégration).
<!-- generated:maintenance:end -->

---

### Cartes

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Carte Lovelace personnalisée pour les tableaux de bord récifaux.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

La **Reef Card** pour Home Assistant vous aide à gérer votre aquarium récifal directement depuis votre tableau de bord. Combinée avec [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component), elle détecte et supporte automatiquement vos appareils Red Sea (ReefBeat).

> Les appareils non-Redsea peuvent aussi être supportés — [demandez ici](https://github.com/Elwinmage/ha-reef-card/discussions/2).

<!-- generated:card-devices:start -->
**Appareils supportés :**

> ✅ Supporté &nbsp;|&nbsp; 🚧 En cours &nbsp;|&nbsp; 🧪 Non testé (peut fonctionner) &nbsp;|&nbsp; ❌ Pas encore supporté

| Appareil | Statut | Points forts |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Planification complète, dosage manuel, amorçage et calibration, gestion des suppléments, suivi de l'utilisation |
| **ReefMat (RSMAT250/500/1200)** | ✅ | État du rouleau animé, avance manuelle/auto/programmée, état du capteur, graphiques hebdo et mensuels |
| **ReefRun (RSRUN)** | ✅ | Contrôle de la vitesse de pompe, éditeur de programmes, gestion du surécumage |
| **ReefATO+** | ✅ | Niveau d'eau, sonde de fuite, diagnostic pompe, graphe de consommation, buzzer de fuite |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Contrôle par prise |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
<!-- generated:card-devices:end -->

**Points forts ReefDose :**
- Carte 6 zones : config/WiFi, états, dosage manuel avec raccourcis, planification par tête avec progression circulaire, gestion des suppléments avec images de marques, et file d'attente des prochaines doses
- Support des flux d'amorçage et de calibration
- Bibliothèque de suppléments avec images pour Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest, et plus

**Points forts ReefMat :**
- Carte 7 zones avec fond animé qui change selon l'utilisation du rouleau (0%–100%)
- Infos en temps réel du rouleau : longueur restante, moyenne journalière, jours restants estimés
- Contrôles d'avance manuelle, automatique et programmée
- Affichage de l'état du capteur de niveau (connecté, déconnecté, encrassé)
- Graphiques de consommation hebdomadaire et mensuelle

**Installation :** Disponible directement dans [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — recherchez "reef-card".

**Configuration :** Sans le paramètre `device`, la carte détecte automatiquement tous les appareils ReefBeat et vous laisse choisir. Définissez le paramètre `device` pour forcer un appareil spécifique.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Démo ReefDose" width="300"/></a><br/><em>Démo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Démo ReefMat" width="300"/></a><br/><em>Démo ReefMat</em></td>
</tr>
</table>

---

## 🔌 Infrastructure

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Système autonome de secours batterie pour aquariums récifaux Red Sea.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Maintenez vos ReefWave, ReefRun et DC Skimmer en fonctionnement pendant les coupures de courant grâce à une batterie LiFePO₄ 24V, un Raspberry Pi et une dégradation intelligente des pompes.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Fonctionnalités clés :**
- **Monitoring batterie** via INA226 (I2C) + chargeur Victron BLE optionnel
- **Détection instantanée** des coupures via relais 230V sur GPIO
- **Dégradation progressive** des pompes — niveaux SoC calculés à partir d'une autonomie cible
- **Failover réseau 3 niveaux** — Ethernet → Wi-Fi → hotspot miroir autonome
- **Failover 4G/LTE** — notifications et accès cloud ReefBeat via modem USB ou tethering smartphone
- **Notifications push** via [ntfy.sh](https://ntfy.sh) (gratuit, sans compte)
- **Intégration Home Assistant** — auto-discovery MQTT, entité de mise à jour, blueprint de test batterie
- **Mise à jour automatique** — vérifie GitHub, bouton "Installer" dans HA

**Niveaux matériels :**

| Niveau | Ce que vous obtenez | Budget |
|--------|-------------------|--------|
| **1 — Basique** | Batterie + câbles, secours passif | ~290 € |
| **2 — Normal** *(recommandé)* | + RPi + INA226 + relais, monitoring & automatisation | ~402 € |
| **3 — Avancé** | + Chargeur Victron BLE, disjoncteur connecté, modem 4G | ~627 € |

**Installation :**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

Un assistant interactif configure tout : scan des appareils, capacité batterie, niveaux SoC, MQTT, notifications, 4G, reboot programmé.

> Fonctionne seul ou en complément de [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) pour un setup récifal entièrement intégré.

---

<!-- generated:blueprints:start -->
#### 🔔 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Blueprints de notification pour tout l'écosystème.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Vous prévient sur votre téléphone des entretiens en retard, trouvés via l'attribut commun `reef_role` afin que toutes les intégrations soient couvertes, et des appareils devenus injoignables. Huit langues, un bouton d'import chacune.

**Installation :** import depuis le dépôt, un bouton par langue.
<!-- generated:blueprints:end -->

---

## 📐 Modèles 3D

### ReefRun DC Skimmer
#### 📦 [*Outil pour rotor d'écumeur DC Red Sea*](https://www.thingiverse.com/thing:7313258)




<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Clé Red Sea 3D"
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
    console.log("Modèle chargé, dimensions détectées :", width, "x", height);
    if (width === 0 || height === 0) {
        modelViewer.style.width = "100%";
        modelViewer.style.height = "500px";
    }
  });
</script>

**Vidéo de démonstration :**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->
## 💬 Contact & Support

- **Questions et demandes de fonctionnalités :** ouvrez une discussion sur le projet concerné — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Signalement de bugs :** ouvrez une issue sur ce même projet, avec les détails.
- **Soutenir le projet :** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
<!-- generated:contact:end -->
