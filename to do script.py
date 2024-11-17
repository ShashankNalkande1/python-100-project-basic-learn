def task_manager():
    task = []
    print('Welcome to the Task Management App')

    total_task = int(input("Enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f'Enter task {i}: ')
        task.append(task_name)
        print(f'Today\'s tasks are:\n{task}')

    while True:
        try:
            operation = int(input("\nEnter:\n1 - Add Task\n2 - Update Task\n3 - Delete Task\n4 - View Tasks\n5 - Exit/Stop\n"))

            if operation == 1:
                add = input("Enter the task you want to add: ")
                task.append(add)
                print(f'Task "{add}" has been successfully added.')

            elif operation == 2:
                updated_val = input("Enter the task name you want to update: ")
                if updated_val in task:
                    up = input("Enter the new task: ")
                    ind = task.index(updated_val)
                    task[ind] = up
                    print(f'Updated task "{updated_val}" to "{up}".')
                else:
                    print('Task not found.')

            elif operation == 3:
                del_val = input("Enter the task you want to delete: ")
                if del_val in task:
                    ind = task.index(del_val)
                    del task[ind]
                    print(f'Task "{del_val}" has been deleted.')
                else:
                    print('Task not found.')

            elif operation == 4:
                print(f'Total tasks: {task}')

            elif operation == 5:
                print('Closing the program. Goodbye!')
                break

            else:
                print('Invalid input. Please enter a number from 1 to 5.')

        except ValueError:
            print('Invalid input. Please enter a valid number.')

task_manager()
