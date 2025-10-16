from datetime import date, datetime, timedelta
from enum import Enum

from pydantic import BaseModel


class TrackingState(Enum):
    STARTED = "started"
    STOPPED = "stopped"


class TrackingHistoryEntry(BaseModel):
    start: datetime
    end: datetime | None = None


class TrackingHistory(BaseModel):
    date: date
    entries: list[TrackingHistoryEntry] = []
    worked: timedelta = timedelta(0)


class Tracking(BaseModel):
    state: TrackingState = TrackingState.STOPPED
    history: list[TrackingHistory] = []
