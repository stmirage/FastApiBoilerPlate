from fastapi import FastAPI, APIRouter

app = FastAPI(title="BoilerPlate API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """ Root path """

    return {"msg": "Hello World"}

app.include_router(api_router)

if __name__ == "main":
    # использовать только для отладки
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", log_level="debug")