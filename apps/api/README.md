# Lumina API (FastAPI)

Backend service for Lumina's astronomy assistant.

## What Is Included

- FastAPI app with OpenAPI/Swagger docs
- Versioned REST routes under `/api/v1`
- Modular routers: health, stars, objects, exoplanets, guide
- Dataset-driven service layer with local JSON loaders
- Pydantic request/response schemas with examples
- Filtering, pagination, and ID-based detail endpoints
- Fallback in-memory records when dataset files are missing

## Project Structure

```text
apps/api
|-- README.md
|-- requirements.txt
`-- src
	|-- main.py
	|-- api
	|   |-- __init__.py
	|   `-- routers
	|       |-- __init__.py
	|       |-- exoplanets.py
	|       |-- guide.py
	|       |-- health.py
	|       |-- objects.py
	|       `-- stars.py
	|-- core
	|   |-- __init__.py
	|   |-- config.py
	|   `-- exceptions.py
	|-- data
	|   |-- exoplanets.json
	|   |-- objects.json
	|   `-- stars.json
	|-- models
	|   |-- __init__.py
	|   |-- common.py
	|   |-- exoplanets.py
	|   |-- guide.py
	|   |-- health.py
	|   |-- objects.py
	|   `-- stars.py
	`-- services
		|-- __init__.py
		|-- data_loader.py
		|-- exoplanets_service.py
		|-- guide_service.py
		|-- objects_service.py
		|-- stars_service.py
		`-- utils.py
```

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r apps/api/requirements.txt
```

3. Start the API server from repository root:

```bash
uvicorn apps.api.src.main:app --reload
```

4. Open docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Minimum Test Routes

- `GET /health`
- `GET /api/v1/stars`
- `GET /api/v1/stars/{star_id}`
- `POST /api/v1/stars/search`
- `GET /api/v1/objects`
- `GET /api/v1/objects/{object_id}`
- `POST /api/v1/objects/search`
- `GET /api/v1/exoplanets`
- `GET /api/v1/exoplanets/{planet_id}`
- `POST /api/v1/exoplanets/search`
- `POST /api/v1/guide/explain`

## Notes

- No authentication is enabled yet.
- No database is required yet; services read local dataset files.
- Service layer is intentionally isolated for future DB/vector-store integration.
