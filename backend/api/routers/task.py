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

# create_task関数の引数にtask_bodyというのを入れて、dictに変換して、
# **をつけることでキーワード引数として展開する
# これはdictをkey/valueわたしをするから、数が多くなってきたときに役立つ
@router.post("/tasks", response_model = task_schema.TaskCreateResponse)
async def create_task(task_body : task_schema.TaskCreate):
  return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put("/tasks/{task_id}", task_schema.TaskCreateResponse)
async def update_tasks(task_id: int , task_body : task_schema.TaskCreate):
  return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}")
async def delete_tasks(task_id: int):
  return 