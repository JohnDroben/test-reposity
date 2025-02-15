# Менеджер задач
#Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from _datetime import datetime
from typing import List


class Task:
    def  __init__(self, description:str, deadline:datetime, status:bool=False):
        self.description = description             # Описание задачи
        self.deadline = deadline       # Срок выполнения задачи
        self.status = status           # Статус (bool)


    def mark_status(self):
        """Пометить задачу как выполненную"""
        self.status = True

    def __repr__(self):
        return f"Task('{self.description}', {self.deadline.strftime('%Y-%m-%d')}, {self.status})"

def add_task(tasks: List[Task], description: str, deadline: str) -> None:
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            tasks.append(Task(description, deadline_date))
        except ValueError:
            print(f"Некорректный формат даты: {deadline}. Используйте YYYY-MM-DD")

def print_pending_tasks(tasks: List):
       """Вывести список невыполненных задач"""
       print("\nТекущие задачи:")
       pending = [t for t in tasks if not t.status]
       for i, task in enumerate(pending, 1):
           print(f"{i}. {task.description} (до {task.deadline.strftime('%d.%m.%Y')})")
           if tasks:
                    tasks[0].mark_status()
           else:
                    print("Список задач пуст!")

# Проверяем работу:

if __name__ == "__main__":
    tasks: List[Task] = []

    # Добавляем задачи
add_task (tasks, "Купить продукты", "2024-03-20")
add_task (tasks, "Сделать презентацию", "2024-03-25")
add_task (tasks, "Записаться к врачу", "2024-03-18")

    # Отмечаем одну задачу выполненной
tasks[0].mark_status()

    # Выводим текущие задачи
print_pending_tasks(tasks)

    # Вывод в консоли:
    # Текущие задачи:
    # 1. Сделать презентацию (до 25.03.2024)
    # 2. Записаться к врачу (до 18.03.2024)