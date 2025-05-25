tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def edit_task(task_index, new_task):
    if 0 <= task_index < len(tasks):
        old_task = tasks[task_index]
        tasks[task_index] = new_task
        print(f'Task "{old_task}" edited to "{new_task}".')
    else:
        print("Invalid task index.")
