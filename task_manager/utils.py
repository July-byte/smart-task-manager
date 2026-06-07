from datetime import datetime
from task_manager.exceptions import InvalidDateFormatError

def validate_due_date(date_str: str) -> str:
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    return date_str
  except ValueError:
    raise InvalidDateFormatError(
      "Invalid date format. Use YYYY-MM-DD."
    )
