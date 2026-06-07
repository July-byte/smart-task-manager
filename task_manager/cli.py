import argparse
from task_manager import service
from task_manager.exceptions import (
TaskNotFoundError,
InvalidPriorityError,
InvalidDateFormatError,
)

def run():
  parser = argparse.ArgumentParser(description="Smart Task Manager CLI")
  subparses = parser.add_subparsers(dest="command")

#add
  add_parser = subparsers.add_parser("add")
  add_parser.add_argument("title")
  add_parser.add_argument("--priority", required=True)
  add_parser.add_argument("--due", required=True)

#list
  list_parser = subparsers.add_parser("list")
  list_parser.add_argument("--status", choices=["completed", "pending"])
  list_parser.add_argument("--priority")

#complete
  complete_parser = subparsers.add_parser("complete")
  complete_parser.add_argument("id", type=int)

#delete
  delete_parser = subparsers.add_parser("delete")
  delete_parser.add_argument("id", type=int)

  args = parser.parse_args()

  try:
    if args.command == "add":
      tasks = service.add_task(args.title, args.priority, args.due)
      print(f"Task added: {task.title}")

elif args.command == "list":
tasks = service.list_tasks(args.status, args.priority)
  for task in tasks:
    status = "Ok" if task.completed else " "
    
    print(f"[{status}] {task.id}.{task.title} ")
    print(f"(Priority: {task.priority}, Due: {task.due_date})
    
   elif args.command == "complete":
    servive.complete_task(args.id)
    print("Task completed")

  elif args.command == "delete":
      servive.delete_task(args.id)
      print("Task deleted")

  else:
    parser.print_help()
  
  except(TaskNotFoundError, InvalidPriorityErroe, InvalidDateFormatError) as e:
    print(f"Error: {e}")

    
