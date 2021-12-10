# generated by datamodel-codegen:
#   filename:  schema/type/usageDetails.json
#   timestamp: 2021-12-04T12:57:16+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, confloat, conint

from . import basic


class UsageStats(BaseModel):
    class Config:
        extra = Extra.forbid

    count: conint(ge=0) = Field(
        ..., description='Usage count of a data asset on the start date.'
    )
    percentileRank: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None, description='Optional daily percentile rank data asset use when relevant.'
    )


class TypeUsedToReturnUsageDetailsOfAnEntity(BaseModel):
    dailyStats: UsageStats = Field(
        ..., description='Daily usage stats of a data asset on the start date.'
    )
    weeklyStats: Optional[UsageStats] = Field(
        None,
        description='Weekly (last 7 days) rolling usage stats of a data asset on the start date.',
    )
    monthlyStats: Optional[UsageStats] = Field(
        None,
        description='Monthly (last 30 days) rolling usage stats of a data asset on the start date.',
    )
    date: basic.Date = Field(..., description='Date in UTC.')