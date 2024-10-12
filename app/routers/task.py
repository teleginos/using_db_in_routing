from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    pass


@router.get("/task_id")
async def task_by_id():
    pass


@router.post("/create")
async def create_user():
    pass


@router.put("/update")
async def update_user():
    pass


@router.delete("/delete")
async def delete_users():
    pass
