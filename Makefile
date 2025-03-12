setup:
	uv sync

shell:
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" uv run quart shell

dbshell:
	docker-compose exec database psql -U psplanner

dev:
	uv run alembic upgrade head
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" uv run python3 app.py

prod:
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" .uv run uvicorn app:app --host 0.0.0.0 --port 5000

up:
	docker-compose up -d
