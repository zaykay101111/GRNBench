"""GRN-Bench HTTP API.

Stage 0: a single health endpoint, so we can prove the service starts
and responds before adding a database, queue, or object storage.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="GRN-Bench",
    version="0.1.0",
    description="Distributed benchmark platform for gene regulatory network inference",
)


class HealthResponse(BaseModel):
    """Shape of the /health response body."""

    status: str = Field(description="Always 'ok' when the process is serving traffic.")


@app.get("/health")
def health() -> HealthResponse:
    """Liveness check. Returns 200 whenever the process is running."""
    return HealthResponse(status="ok")
