# Lumina

<p align="center">
	<img src="assets/lumina-logo.png" alt="Lumina Logo" width="220" />
</p>

Lumina is an AI-based star guide designed to help users explore astronomy with structure, clarity, and beautiful interaction.
It combines curated celestial datasets, a guided explanation engine, and a premium frontend experience to make learning the night sky feel modern and intuitive.

## What Lumina Includes Right Now

- FastAPI backend with production-style modular architecture
- Curated local astronomy datasets for stars and celestial objects
- Guided explanation endpoint with beginner/intermediate/advanced tone support
- Next.js + TypeScript frontend with polished dark-space visual design
- One-command local startup workflow through VS Code task: Run Lumina

## Current Datasets

Lumina currently loads curated JSON datasets from apps/api/src/data.

| Domain | File | Purpose |
|---|---|---|
| Stars | apps/api/src/data/stars.json | Star identity, constellation, distance, magnitude, spectral class, description |
| Celestial Objects | apps/api/src/data/objects.json | Galaxy/nebula/cluster metadata and sky context |

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

## Product Direction

Lumina is being built as a scalable AI-first astronomy platform with clear separation across data, API, AI guidance logic, and user experience layers.
Milestone 1 focuses on a complete, demo-ready core loop: ask about a celestial entity and receive structured facts plus educational guidance.