# Lumina

An AI-based astronomy assistant focused on learning, exploration, and guided understanding of stars, celestial objects, and exoplanets.

Lumina is designed as a modular, AI-first platform with a clean backend foundation, local dataset support, and a scalable architecture for future LLM orchestration, vector search, and production deployment.

---

## Highlights

- Modern FastAPI backend with OpenAPI/Swagger docs
- Dataset-driven API layer for stars, deep-sky objects, and exoplanets
- Modular architecture ready for AI orchestration and vector database integration
- Local JSON dataset loading with graceful fallback behavior
- Clear separation of routers, schemas, services, and data assets

---

## Datasets Included (Current)

Lumina currently uses local dataset files under `apps/api/src/data`.

| Domain | File | Purpose |
|---|---|---|
| Stars | `apps/api/src/data/stars.json` | Star identity, spectral class, distance, magnitude, constellation |
| Celestial Objects | `apps/api/src/data/objects.json` | Nebula/galaxy/cluster metadata and constellation linkage |
| Exoplanets | `apps/api/src/data/exoplanets.json` | Host star, discovery method, orbital and habitability-related fields |

Planned future sources include curated stellar catalogs, object metadata repositories, and expanded exoplanet archives.

---

## API Surface (v1)

Base URL: `http://127.0.0.1:8000`

### Health

- `GET /health`

### Stars

- `GET /api/v1/stars`
- `GET /api/v1/stars/{star_id}`
- `POST /api/v1/stars/search`

Supported filter/search fields:
- `name`
- `spectral_type`
- `min_distance`
- `max_distance`
- `min_magnitude`
- `max_magnitude`
- `constellation`
- `page`
- `page_size`

### Celestial Objects

- `GET /api/v1/objects`
- `GET /api/v1/objects/{object_id}`
- `POST /api/v1/objects/search`

Supported filter/search fields:
- `name`
- `object_type`
- `constellation`
- `page`
- `page_size`

### Exoplanets

- `GET /api/v1/exoplanets`
- `GET /api/v1/exoplanets/{planet_id}`
- `POST /api/v1/exoplanets/search`

Supported filter/search fields:
- `name`
- `host_star`
- `discovery_method`
- `page`
- `page_size`

### Sky Guide

- `POST /api/v1/guide/explain`

Request body input fields:
- `name`
- `category`
- `user_level`
- `include_scientific_facts`
- `context`

---

## Run Locally

1. Install dependencies:

```bash
pip install -r apps/api/requirements.txt
```

2. Start the backend server:

```bash
uvicorn apps.api.src.main:app --reload
```

3. Open API docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI spec: `http://127.0.0.1:8000/openapi.json`

---

## Architecture Direction

Lumina is structured for modular growth across:
- Frontend experience layer
- Backend API services
- AI orchestration and prompt systems
- Astronomy data ingestion and processing
- Future vector retrieval and semantic search
- Production-grade monitoring and deployment

---

## Status

Current stage: backend foundation complete and Swagger-testable.

Next stage: expand dataset coverage, add retrieval-enhanced guide logic, and connect frontend experience.