import os

FILE_PATH = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")
