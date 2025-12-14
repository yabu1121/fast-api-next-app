from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    # int の型ヒント
    id: int
    # Optional[str] という型ヒント
    # Fieldはフィールドに関する付加情報を加える。第一引数は初期値、第二引数は値の例
    title: Optional[str] = Field(None, example = "クリーニングを取りに行く")
    # bool という型ヒント
    done: bool = Field(False, description = "完了フラグ")
