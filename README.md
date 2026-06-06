# Smart Task Manager
CLI приложение для управленич задачами с использованием чистой архитектуры.

## Возможности
* Добавление задач
* Приоритеты
* Дедлайны
* Фильтрация
* Сортировка
* JSON-хранилище
* Чистая архитектура

## Технологии
- Python 3.12
- Dataclasses
- Argparse
- OOP
- Clean architecture

## Установка
git clone https://July-byte/smart-task-manager
cd smart-task-manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Использование
python main.py add "Buy milk" --priority high --due 2026-05-20
python main.py list
python main.py complete 1
python main.py delete 2

## Архитектура

## Цель проекта
Проект был создан для демонстрации навыков:
- Проектирования архитектуры
- Разделения ответственности
- Работы с CLI
- Обработки ошибок
- Чистой структуры кода
