# Airplanes.live

> Community-driven, unfiltered live ADS-B flight tracking platform providing global aircraft telemetry and route histories.

---

## Purpose
Airplanes.live is an open, community-powered flight tracking service created by the original developers of ADS-B Exchange. It aggregates raw ADS-B radio signals from a global volunteer receiver network to provide completely unfiltered, unblocked tracking of civil, commercial, private, government, and military aircraft.

## Category
- **Primary**: Aviation & Flight Tracking (`aviation`)
- **Secondary**: Maps & Geospatial Intelligence (`maps`), Geolocation & Terrain (`geolocation`)

## Interface
- **Web**
- **API**

## Language & Runtime
- **Platform**: Web, Cross-platform (JSON REST API)

## Usage

```bash
# Open interactive global flight radar
# Visit: https://airplanes.live

# Query aircraft telemetry by ICAO hex code via API
curl -s "https://api.airplanes.live/v2/hex/a1b2c3" | jq .

# Query all aircraft within a geographic radius (lat, lon, nautical miles)
curl -s "https://api.airplanes.live/v2/point/37.7749/-122.4194/50" | jq .
```

## Common Use Cases
1. **Executive & VIP Movement Tracking**: Monitoring corporate jet tail numbers and flight patterns during corporate OSINT investigations.
2. **Military & Government Aircraft Tracking**: Tracking unblocked state aircraft, VIP transports, and reconnaissance flights.
3. **Flight Path Historical Analysis**: Correlating aircraft positions with ground events, maritime movements, or news reports.

## Input
- Tail number, ICAO 24-bit hex code, callsign, or geographic coordinates.

## Output
- Live radar map, real-time altitude/airspeed/squawk telemetry, and historical flight tracks.

## Requirements
- **Dependencies**: Web browser or curl.
- **API Keys**: None required for standard queries.

## Source
- **Official Website**: [https://airplanes.live](https://airplanes.live)
- **API Documentation**: [https://airplanes.live/api](https://airplanes.live/api)

## Status
- **Status**: Active

## RAVEN Notes
Unlike commercial flight tracking platforms (e.g. FlightRadar24) that censor military, government, or private aircraft upon owner request, Airplanes.live provides completely unfiltered raw ADS-B telemetry, making it the premier aviation OSINT data source in RAVEN.
