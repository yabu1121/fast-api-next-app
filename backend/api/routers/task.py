from fastapi import APIRouter

router = APIRouter()


# C : post 
# R : get
# U : put
# D : delete
@router.get("/tasks")
async def list_tasks():
  pass

@router.post("/tasks")
async def create_tasks():
  pass

@router.put("/tasks/{task_id}")
async def update_tasks():
  pass

@router.delete("/tasks/{task_id}")
async def delete_tasks():
  pass