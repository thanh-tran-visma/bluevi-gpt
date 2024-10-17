from fastapi import FastAPI
from app.api.router import router
from app.llm.llm_model import BlueViGptModel
from contextlib import asynccontextmanager

blueViGpt = BlueViGptModel()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    app.state.model = blueViGpt
    blueViGpt.load_model()
    yield
    # Shutdown event (currently no specific shutdown actions)
    pass

app = FastAPI(lifespan=lifespan)

app.include_router(router)
