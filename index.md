---
layout: default
title: Home - Reef Tech Projects
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸] / [🇫🇷](fr.md)

# My ReefTank tools

Welcome to the documentation of my reef tank projects.

<video src="assets/videos/logo_v1.mp4" 
       poster="image-de-remplacement.jpg"
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;">
</video>

---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Home Assitant Integrations and Cards

### Integrations
#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)
**Local Integration for Red Sea ReefBeat ecosystem.**
Supports ReefAto+, ReefDose, ReefLed, ReefMat, ReefRun and ReefWave.

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)
**Control for Aqua Medic wavemakers and return pumps.**
Supports SmartDrift and DC Runner.

### Cards
####  🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)
**Custom Lovelace card for reef dashboards.**

---
## 📐 3D Models
### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer impeller tool*](https://www.thingiverse.com/thing:7313258)


<!-- 1. Chargement du script (si pas déjà fait en haut de page) -->
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<!-- 2. Conteneur avec dimensions forcées -->
<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Support Red Sea Key 3D"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<!-- 3. Script de secours pour corriger le "Zero Size" -->
<script>
  const modelViewer = document.querySelector("#aquarium-model");
  modelViewer.addEventListener("load", () => {
    // Force le moteur 3D à recalculer la taille du conteneur
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

