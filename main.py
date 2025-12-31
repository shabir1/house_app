from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Property
from schemas import PropertyCreate, PropertyResponse

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Property API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Ping endpoint
@app.get("/ping")
def ping():
    return {"message": "pong"}

# 2️⃣ Get data
@app.get("/get_data", response_model=list[PropertyResponse])
def get_data(db: Session = Depends(get_db)):
    return db.query(Property).all()

@app.get("/get_filter_data", response_model=list[PropertyResponse])
def get_filter_data(
    City: str | None = Query(None),
    Floors: int | None = Query(None),
    NumberOfWashrooms: int | None = Query(None),
    NumberOfRooms: int | None = Query(None),
    PropertyType: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Property)

    if City:
        query = query.filter(Property.City.ilike(City))
    if Floors is not None:
        query = query.filter(Property.Floors == Floors)
    if NumberOfWashrooms is not None:
        query = query.filter(Property.NumberOfWashrooms == NumberOfWashrooms)
    if NumberOfRooms is not None:
        query = query.filter(Property.NumberOfRooms == NumberOfRooms)
    if PropertyType:
        query = query.filter(Property.PropertyType.ilike(PropertyType))

    return query.all()

# 3️⃣ Add data
@app.post("/add_data", response_model=PropertyResponse)
def add_data(property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property
