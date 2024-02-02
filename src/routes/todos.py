from fastapi import APIRouter
from src.models.todos import Todo
from src.databases.mongodb import collection_name
from src.schemas.todos import serialize_todos
from bson import ObjectId

router = APIRouter(
  prefix="/todos",
  tags=["Todos"],
)

# GET request method
@router.get("")
async def get_todos():
  todos = serialize_todos(collection_name.find())
  return todos

#POST request method
@router.post("")
async def post_todo(todo: Todo):
  collection_name.insert_one(dict(todo))

#PUT request method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
  collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

#DELETE request method
@router.delete("/{id}")
async def delete_todo(id: str):
  collection_name.find_one_and_delete({"_id": ObjectId(id)})