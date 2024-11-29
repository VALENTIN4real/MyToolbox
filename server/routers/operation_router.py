from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlmodel import Session, select
from ..models.operation_model import Operation
from ..database.config import get_session

router = APIRouter()

@router.get("/operations", response_model=List[Operation])
def get_operations(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        operations = session.exec(select(Operation).offset(offset).limit(limit)).all()
        if not operations:
            raise HTTPException(status_code=404, detail="No operations found.")
        return operations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/operations/{operation_id}", response_model=Operation)
def get_operation_by_id(operation_id: int, session: Session = Depends(get_session)):
    try:
        operation = session.get(Operation, operation_id)
        if not operation:
            raise HTTPException(status_code=404, detail="Operation not found")
        return operation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/operations", response_model=Operation)
def create_operation(operation: Operation, session: Session = Depends(get_session)):
    try:
        session.add(operation)
        session.commit()
        session.refresh(operation)
        return operation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/operations/{operation_id}", response_model=Operation)
def update_operation(operation_id: int, operation: Operation, session: Session = Depends(get_session)):
    try:
        db_operation = session.get(Operation, operation_id)
        if not db_operation:
            raise HTTPException(status_code=404, detail="Operation not found")
        for key, value in operation.dict().items():
            setattr(db_operation, key, value)
        session.add(db_operation)
        session.commit()
        session.refresh(db_operation)
        return db_operation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/operations/{operation_id}")
def delete_operation(operation_id: int, session: Session = Depends(get_session)):
    try:
        operation = session.get(Operation, operation_id)
        if not operation:
            raise HTTPException(status_code=404, detail="Operation not found")
        session.delete(operation)
        session.commit()
        return {"message": "Operation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))