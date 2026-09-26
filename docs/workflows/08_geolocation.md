# Geolocation & Spatial Verification Workflow

## Objective
Step-by-step methodology for determining the precise physical coordinates of an event, photograph, or incident using open-source geospatial datasets, satellite imagery, and environmental analysis.

---

## Intelligence Lifecycle

```
TARGET
  │  [Visual Clue / Imagery / Reference Landmark / Video Clip]
  ▼
DISCOVERY
  │  Identify regional clues (language, signage, vehicle styles, driving side)
  ▼
ENUMERATION
  │  Isolate distinctive physical landmarks, road geometry, and building architecture
  ▼
CORRELATION
  │  Match features against satellite imagery, street view services, and GIS data
  ▼
VERIFICATION
  │  Confirm line-of-sight angles, shadows, solar positioning, and topographic elevation
  ▼
DOCUMENTATION
     Record precise coordinates (lat/long), map overlay, and validation proof
```

---

### Phase 1: Macro-Location (Region & Country)
1. **Traffic & Road Infrastructure**:
   - Driving side (left vs right).
   - License plate aspect ratios, color schemes, and registration marks.
   - Road sign design, font, guardrail designs, and utility pole styles.
2. **Language & Culture**:
   - Alphabets, official scripts, regional dialects on storefronts.
3. **Environment & Geography**:
   - Climate zone, biome, flora, mountain profiles, soil coloration.

### Phase 2: Micro-Location (City & Neighborhood)
1. **Commercial & Civic Signage**:
   - Phone area codes, postal codes, business names, bus stop route numbers.
2. **Distinctive Architecture**:
   - Church steeples, religious architecture, unique roof structures, high-voltage pylons.
3. **Linear Infrastructure**:
   - Railway lines, bridges, canal systems, coastline contours.

### Phase 3: Spatial Correlation (Satellite & Street-Level)
1. **Satellite Comparison**:
   - Google Earth Pro (utilize historical imagery slider to track structural changes).
   - Sentinel Hub / Copernicus (recent multispectral satellite passes).
2. **Street-Level Verification**:
   - Google Street View, Mapillary (crowdsourced street photos), KartaView.

### Phase 4: Rigorous Triangulation & Verification
1. **Sight-Line Triangulation**:
   - Draw perspective lines from camera viewpoint to two prominent foreground/background objects.
2. **Chronolocation (Sun Angle)**:
   - Use SunCalc / NOAA solar calculators to match shadow angle with claimed time and date.

### Phase 5: Documentation
1. Output decimal coordinates (e.g., `51.5007° N, 0.1246° W`).
2. Attach side-by-side comparison images with highlighted matching anchor points.

---

## Ethical & Legal Boundaries
- Do not use geolocation tradecraft for real-time stalking, harassment, or doxxing individuals.
