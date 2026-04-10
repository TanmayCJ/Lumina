# Lumina

<p align="center">
	<img src="assets/lumina-logo.png" alt="Lumina Logo" width="420" />
</p>

Lumina is an AI-based star guide designed to help users explore astronomy with structure, clarity, and beautiful interaction.
It combines curated celestial datasets, guided explanation logic, and a premium web experience to make learning the night sky feel modern, elegant, and practical.

## Overview

Lumina is being built in milestones. The current milestone delivers a complete user-facing loop:

1. User enters a star or celestial object
2. Frontend sends a request to the guide API
3. Backend looks up curated local dataset records
4. Lumina returns structured facts and an educational explanation adapted to user level

This gives a real product foundation you can demo today while keeping the architecture clean for future AI and data growth.

## What Lumina Includes Right Now

- FastAPI backend with production-style modular architecture
- Curated local astronomy datasets for stars and celestial objects
- Guided explanation endpoint with beginner/intermediate/advanced tone support
- Next.js + TypeScript frontend with polished dark-space visual design
- One-command local startup workflow through VS Code task: Run Lumina

## Tech Stack

### Backend

- Python + FastAPI
- Pydantic schemas for strict request/response contracts
- Local JSON dataset loaders (stars and celestial objects)
- Swagger/OpenAPI docs for endpoint testing

### Frontend

- Next.js (App Router) + React + TypeScript
- Tailwind CSS for design system and responsive styling
- Framer Motion for subtle transitions and section reveals
- Lucide icons for clean UI iconography

## Current Datasets

Lumina currently loads curated JSON datasets from apps/api/src/data.

| Domain | File | Purpose |
|---|---|---|
| Stars | apps/api/src/data/stars.json | Star identity, constellation, distance, magnitude, spectral class, description |
| Celestial Objects | apps/api/src/data/objects.json | Galaxy/nebula/cluster metadata and sky context |

Included examples currently cover well-known entities such as:

- Stars: Sirius, Betelgeuse, Polaris, Vega, Proxima Centauri, Rigel
- Objects: Andromeda Galaxy, Orion Nebula, Pleiades, Ring Nebula, Sombrero Galaxy

## Current API Surface

Base URL: http://127.0.0.1:8000

- GET /health
- GET /api/v1/stars
- GET /api/v1/stars/{star_id}
- POST /api/v1/stars/search
- GET /api/v1/objects
- GET /api/v1/objects/{object_id}
- POST /api/v1/objects/search
- POST /api/v1/guide/explain

Guide endpoint supports:

- category: star, object, or omitted for auto-detect
- user level: beginner, intermediate, advanced
- include_scientific_facts toggle

## UI Milestone (Current)

The frontend currently includes:

- A polished astronomy-inspired hero section
- Main Lumina explorer form (name, category, user level, scientific facts toggle)
- Quick prompt chips for fast testing
- Rich response card showing:
	- object identity and category
	- structured facts
	- guided explanation
	- key fact list
- Clean empty/loading/error/not-found states
- Responsive layout optimized for laptop and desktop demos

## Run Locally

### Recommended (single command)

1. Open VS Code Command Palette.
2. Run Tasks: Run Task.
3. Select Run Lumina.

This starts:
- Backend: http://127.0.0.1:8000
- Frontend: http://localhost:3000

### Manual option

- Backend dependencies: pip install -r apps/api/requirements.txt
- Frontend dependencies: npm --prefix apps/web install
- Backend start: .venv/Scripts/python.exe -m uvicorn apps.api.src.main:app --reload
- Frontend start: npm --prefix apps/web run dev

### Verify services

- Backend docs: http://127.0.0.1:8000/docs
- Frontend app: http://localhost:3000

## Product Direction

Lumina is being built as a scalable AI-first astronomy platform with clear separation across data, API, AI guidance logic, and user experience layers.

Current milestone focus:

- Deliver one complete polished feature from input to explanation
- Ensure strong backend/frontend integration and testability
- Establish a visual and architectural quality baseline for future releases

Near-term expansion (next milestones):

- Broader dataset coverage and richer metadata
- Additional explorer flows built on existing API foundations
- More advanced guided learning experiences