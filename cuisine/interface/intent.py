from enum import Enum


class Intent(Enum):
    CREATE_NEW_RECIPE = "new"
    IMPROVE_EXISTING = "improve"
    RECYCLE_RECIPE = "delete"
