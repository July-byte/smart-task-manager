import json
import os
from typing import list
from task_manager.models import Task

DATA_FILE = "data/tasks.json"

def _ensure_life_exists():
  os.makedirs("data", exist_ok=True)
  if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
      json.dump([], f)

def load_tasks() -> List[Task]:
  _ensure_file_exists()
  with open(DATA_FILE, "r") as f:
    data = json.load(f)
    return [Task.from_dict(task) for task in data]

def save_tasks(tasks: List[Task]) -> None:
  with open(DATA_FILE, "w") as f:
    json.dump([task.to_dict() for task in tasks], f, indent=4)

def get_next_id(tasks: List[Task]) -> int:
  if not tasks:
    return 1
  return max(task.id for task in tasks) + 1

