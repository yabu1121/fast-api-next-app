from typing import Optional
from pydantic import BaseModel, Field


# BaseModelを継承してTaskBaseを作っている。
class TaskBase(BaseModel):
  # Optionalは指定した型、もしくはNoneを許容する。
  # typing.Unionは複数の型を指定可能。
  # typingライブラリは型付けのライブラリである。
  title: Optional[str] = Field(None, example = "クリーニングを取りに行く")
    

class TaskCreate(TaskBase):
  pass

class TaskCreateResponse(TaskCreate):
  id: int
  class Config:
    orm_mode = True

# TaskBaseを継承してTaskを作っている。
class Task(TaskBase):
  # int の型ヒント
  id: int
  # Optional[str] という型ヒント
  # Fieldはフィールドに関する付加情報を加える。第一引数は初期値、第二引数は値の例
  # bool という型ヒント
  done: bool = Field(False, description = "完了フラグ")
  class Config:
    orm_mode = True