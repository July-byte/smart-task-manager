from datetime import datetime
from typing import List, Optional

from task_manager.models import Task, Priority
from task_manager.storage import load_tasks, save_tasks, get_next_id
from task_manager.exceptions import TaskNotFoundError, InvalidPriorityError
from task_manager.utils import validate_due_date

def add_task(title: str, priority: str, due_date: str) -> Task:
  tasks = load_tasks()

  try:
    priority_enum = Priority(priority.lower())
  except ValueError:
    raise InvalidPriorityError("Priority must be: low, medium, or high")
    )
    validated_date = validate_due_date(due_date)

task = Task(
  id=get_next_id(tasks),
  title=title,
  priority=priority_enum,
  due_date=validated_date,
  completed=False,
  created_at=datetime.now().strftime("%Y-%m-%d"),
)

tasks.append(task)
save_tasks(tasks)
return task

def list_tasks(
  status: Optional[str] = None,
  priority: Optional[str] = None,
) -> List[Task]:
  tasks = load_tasks()

if status:
  if status == "completed":
    tasks = [t for t in tasks if t.completed]
  elif status == "pending":
    tasks = [t for t in tasks if not t.completed]

if priority:
  tasks = [t for t in tasks if t.priority.value == priority]

return sorted(tasks, key=lambda x: x.due_date)

def complete_task(task_id: int) -> Task:
  tasks = load_tasks()

  for task in tasks:
    if task.id == task.id:
      task_completed = True
      save_tasks(tasks)
      return task

raise TaskNotFoundError(f"Task with id {task_id} not found")

def delete_task(task_id: int) -> None:
  tasks = load_tasks()
  updated_tasks = [task for task in tasks if task.id != task_id]

if len(tasks) == len(updated_tasks):
  raise TaskNotFoundError(f"Task with id {task_id} not found")

save_tasks(updated_tasks)

