from fastapi import FastAPI, APIRouter, HTTPException, Query
from .data.mock_data import TEST_DATA
from .schemas.record import Record, RecordSearchResults, RecordCreate
from typing import Optional

app = FastAPI(title="BoilerPlate API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """ Root path """

    return {"msg": "Hello World"}


@api_router.get("/record/{record_id}", status_code=200, response_model = Record)
def get_record(*, record_id: int) -> dict:
    """ get single record by id"""
    
    result = [record for record in TEST_DATA if record["id"] == record_id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Record not found")


@api_router.get("/search/", status_code=200)
def search_records(
    keyword: Optional[str] = Query(None, max_length=3, example="label"), 
    max_results: Optional[int] = 10
) -> dict:
    """ default searching records method"""

    if not keyword:
        return {"results": TEST_DATA[:max_results]}
    
    results = list(filter(lambda record: keyword.lower() in record["label"].lower(), TEST_DATA))
    
    return results[:max_results]

@api_router.post("/record/", status_code=201, response_model = Record)
def create_record(*, record_in: RecordCreate) -> dict:
    """create new record (in memory only"""
    new_entry_id = len(TEST_DATA) + 1
    record_entry = Record(
        id = new_entry_id,
        label = record_in.label,
        source = record_in.source,
        url = record_in.url
    )

    TEST_DATA.append(record_entry.dict)

    return record_entry

app.include_router(api_router)

if __name__ == "main":
    # использовать только для отладки
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", log_level="debug")