from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create the FastAPI application used by the template project."""
    app = FastAPI(title="agent-harness-template")

    @app.get("/health", summary="Health Check")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
