from sqlalchemy import Column, Integer, String, Float
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    PropertyType = Column(String)
    City = Column(String)
    Location = Column(String)
    NumberOfRooms = Column(Integer)
    NumberOfWashrooms = Column(Integer)
    Floors = Column(Integer)
    Price = Column(Float)
    AreaSQFT = Column(Float)
    TagLine = Column(String)
    Contact = Column(String)
