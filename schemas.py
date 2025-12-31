from pydantic import BaseModel

class PropertyCreate(BaseModel):
    PropertyType: str
    City: str
    Location: str
    NumberOfRooms: int
    NumberOfWashrooms: int
    Floors: int
    Price: float
    AreaSQFT: float
    TagLine: str
    Contact: str

class PropertyResponse(PropertyCreate):
    id: int

    class Config:
        from_attributes = True
