from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    return await service.get_students(db)

@router.get('/students/id')
async def get_students_id( id: int , db: Session = Depends(get_db)):
    return await service.get_students_id(db , id)

@router.post('/students/')
async def post_students( id: int, user_name: str , db: Session = Depends(get_db)):
    return await service.post_students(db , id, user_name)

@router.put('/students/id/')
async def put_students_id( id: str, user_name: str , db: Session = Depends(get_db)):
    return await service.put_students_id(db , id, user_name)

@router.delete('/students/id')
async def delete_students_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_students_id(db , id)

