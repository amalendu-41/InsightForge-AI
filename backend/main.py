from fastapi import FastAPI

from backend.routes.upload_routes import (
    router as upload_router
)

from backend.routes.analytics_routes import (
    router as analytics_router
)

from backend.routes.ai_routes import (
    router as ai_router
)

from backend.database.models import (
    create_tables
)

app = FastAPI()

# Create SQLite tables
create_tables()

app.include_router(upload_router)

app.include_router(analytics_router)

app.include_router(ai_router)