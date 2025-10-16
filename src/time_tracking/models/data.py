from pydantic import BaseModel

from .tracking import Tracking


class Data(BaseModel):
    tracking: Tracking = Tracking()
