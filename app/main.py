from fastapi import FastAPI
from app.api.router import router
from app.llm.llm_model import BlueViGptModel
from app.middleware.middleware import CustomMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    blueViGpt = BlueViGptModel()
    app.state.model = blueViGpt
    blueViGpt.load_model()
    yield
    # Shutdown event (currently no specific shutdown actions)
    pass

app = FastAPI(lifespan=lifespan)

app.add_middleware(CustomMiddleware)

app.include_router(router)
