from typing import List

from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema
from starlette.requests import Request
from starlette.responses import Response

router = APIRouter()

import json
from datetime import datetime, timedelta

@router.post("/ticket")
async def ticket(scope, request: Request):
    print(await request.json())
    return {"status": True}

@cbv(router)
class SummaryView:
    @router.post("/", response_model=SummaryResponseSchema, status_code=201)
    async def create_summary(self, payload: SummaryPayloadSchema) -> SummaryResponseSchema:
        summary_id = await crud.post(payload)
        response_object = {
            "id": summary_id,
            "url": payload.url
        }
        return response_object


    @router.get("/{id}/", response_model=SummarySchema, status_code=200)
    async def read_summary(self, id: int) -> SummarySchema:
        summary = await crud.get(id)
        if not summary:
            raise HTTPException(status_code=404, detail="Summary not found")
        return summary


    @router.get("/", response_model=List[SummarySchema])
    async def read_all_summaries(self) -> List[SummarySchema]:
        return await crud.get_all()
