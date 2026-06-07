from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import Dict

class Priority(str, Enum):
  LOW = "low"
  MEDIUM = "medium"
  HIGH = "high"

@dataclass
class Task:
  id: int
  title: str
  priority: Priority
  due_date: str
  completed: bool
  created_at: str

  def to_dict(self) -> Dict:
  return {
    "id": self.id,
    "title": self.title,
    "priority": self.priority,
    "due_date": self.due_date,
    "completed": self.completed,
    "created_at": self.created_at,
  }

@staticmethod
def from_dict(data: Dict) -> "Task":
  return Task(
    id=data["id"],
    title=data["title"],
    priority=Priority(data["priority"]),
    due_date=data["due_date"],
    completed=data["completed"],
    created_at=data["created_at"],
    }

    
    
  
