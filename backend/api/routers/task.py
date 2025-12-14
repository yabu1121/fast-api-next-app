from fastapi import APIRouter
from typing import List
import api.schemas.task as task_schema
router = APIRouter()


# C : post 
# R : get
# U : put
# D : delete
@router.get("/tasks", response_model = List[task_schema.Task])
async def list_tasks():
  return [task_schema.Task(id=1, title="1つ目のtodoタスク")]

@router.post("/tasks")
async def create_tasks():
  pass

@router.put("/tasks/{task_id}")
async def update_tasks():
  pass

@router.delete("/tasks/{task_id}")
async def delete_tasks():
  pass