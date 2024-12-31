from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_students(db: Session):

    students_all = db.query(models.Students).all()
    res = {
        'students_all': students_all,
    }
    return res

async def get_students_id(db: Session, id: int):

    students_one = db.query(models.Students).filter(models.Students.id == id).first()
    res = {
        'students_one': students_one,
    }
    return res

async def post_students(db: Session, id: int, user_name: str):

    record_to_be_added = {'id': id, 'user_name': user_name}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students

    aman = db.query(models.Students).filter(models.Students.id == students_inserted_record.id).first()

    name = db.query(models.Students).all()

    user = db.query(models.Students).filter(models.Students.id == students_inserted_record.id).first()
    for key, value in {'id': students_inserted_record.id, 'user_name': user_name}.items():
          setattr(user, key, value)
    db.commit()
    db.refresh(user)
    user = user


    # output
    user_age: int = id

    res = {
        'students_inserted_record': students_inserted_record,
    }
    return res

async def put_students_id(db: Session, id: str, user_name: str):

    students_edited_record = db.query(models.Students).filter(models.Students.id == id).first()
    for key, value in {'id': id, 'user_name': user_name}.items():
          setattr(students_edited_record, key, value)
    db.commit()
    db.refresh(students_edited_record)
    students_edited_record = students_edited_record

    res = {
        'students_edited_record': students_edited_record,
    }
    return res

async def delete_students_id(db: Session, id: int):

    students_deleted = None
    record_to_delete = db.query(models.Students).filter(models.Students.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          students_deleted = record_to_delete
    res = {
        'students_deleted': students_deleted,
    }
    return res

