---
layout: default
title: Elwinmage - Projets Reef Tech
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷] / [🇩🇪](de.md) / [🇪🇸](es.md) / [🇮🇹](it.md) / [🇵🇱](pl.md) / [🇵🇹](pt.md)

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

Gérez vos appareils Red Sea ReefBeat **localement** (sans cloud) : ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun et ReefWave.

> ⚠️ Ceci n'est pas un dépôt officiel Red Sea. Utilisation à vos risques et périls.

**Fonctionnalités clés :**
- **Contrôle 100% local** — aucune dépendance au cloud pour la plupart des appareils
- Détection automatique des appareils sur le réseau local (avec mode manuel et support sous-réseau)
- Icônes personnalisées pour tous les appareils ReefBeat
- Notifications de mise à jour du firmware (via Cloud API optionnelle)
- Mode de mise à jour en temps réel de la configuration
- Support multilingue

**Appareils supportés :**

| Appareil | Modèles | Statut |
|----------|---------|--------|
| **ReefATO+** | RSATO+ | ✅ Testé |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Testé |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Testé |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Testé |
| **ReefRun** | RSRUN | ✅ Testé |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Pas encore — [contactez-moi](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**Spécificités ReefWave :** Le ReefWave est le seul appareil lié au cloud ReefBeat. Trois modes de fonctionnement sont disponibles — Cloud, Local et Hybride — pour choisir l'équilibre entre contrôle local total et synchronisation avec l'application mobile ReefBeat.

**Installation :** Disponible directement dans [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — recherchez "redsea" ou "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Contrôle des pompes Aqua Medic via Home Assistant grâce à l'API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Contrôlez vos pompes Aqua Medic depuis Home Assistant via l'API cloud Gizwits (même backend que l'application officielle Aqua Medic).

**Appareils supportés :**

| Appareil | Statut |
|----------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (brassage) | ✅ Supporté |
| **DC Runner x.1 / x.2 / x.3** (pompe de remontée) | 🧪 Non testé |
| **Reefdoser EVO** (pompe doseuse) | ❌ Pas encore — [contactez-moi](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (contrôleur de température) | ❌ Pas encore — [contactez-moi](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (éclairage) | ❌ Pas encore — [contactez-moi](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

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

**Appareils supportés :**

| Appareil | Statut | Points forts |
|----------|--------|--------------|
| **ReefDose** (RSDOSE2/4) | ✅ Implémenté | Planification complète, dosage manuel, amorçage/calibration, gestion des suppléments, suivi de l'utilisation |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implémenté | État du rouleau animé, avance manuelle/auto/programmée, état du capteur, graphiques hebdo/mensuels |
| **ReefRun** (RSRUN) | ☑️ En cours | Contrôle de la vitesse de pompe, gestion du surécumage |
| **ReefATO+** | ❌ Prévu | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Prévu | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Prévu | [Voter pour la priorité](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

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

---

## 💬 Contact & Support

- **Questions & demandes de fonctionnalités :** Utilisez l'onglet [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) de chaque projet
- **Signaler un bug :** Ouvrez une [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) avec les détails
- **Soutenir le projet :** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
