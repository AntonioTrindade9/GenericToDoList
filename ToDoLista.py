def Menu():
    print("\n-----To-Do-List-----")
    print("1. Show tasks to do")
    print("2. Add tasks")
    print("3. Complete tasks")
    print("4. Delete tasks")
    print("5. Exit")

def ToDo():
    #List of the tasks
    tasks = [
    {
        "task": "Study Python",
        "Done": False
    },
    {
        "task": "Go to gym",
        "Done": True
    }
]
    
    while True:
        Menu()
        choice = input ("\nChoose an option (1-5): ").strip()
        #Menu to choose which option do you want
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                #Shows each tasks you have
                #The ENUMERATE fucntion shows each task in order from 1 to x
                #Status show if the task is alredy done by seeing if its True or False
                print("\nYOUR TASKS:")
                for index, item in enumerate(tasks, 1):
                    status = "Done" if item["Done"] else "Not Done"
                    print(f"{index}. [{status}] {item['task']}")

        elif choice == "2":
            #Add a new task
            new_task = input("Add a new task: ")

            tasks.append({
                "task": new_task,
                "Done": False
            })
        
        elif choice == "3":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYOUR TASKS:")
                for index, item in enumerate(tasks, 1):
                    status = "Done" if item["Done"] else "Not Done"
                    print(f"{index}. [{status}] {item['task']}")
                #Choose a task to mark as complete
                #The tasks are a list that each item is treated as a hashmap
                #[state of the task (Done/Not Done)] : [name of the task]
                try:
                    choose_task = int(
                        input(f"Choose a task to complete (1-{len(tasks)}): ")
                    )

                    if 1 <= choose_task <= len(tasks):
                        tasks[choose_task - 1]["Done"] = True
                        print("Task completed!")
                    else:
                        print("Error: Task does not exist")

                except ValueError:
                    print("Error: Please enter a valid whole number")

        elif choice == "4":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYOUR TASKS:")
                for index, item in enumerate(tasks, 1):
                    status = "Done" if item["Done"] else "Not Done"
                    print(f"{index}. [{status}] {item['task']}")

                try:
                    choose_task = int(
                        input(f"Choose a task to complete (1-{len(tasks)}): ")
                    )
                    #Get the choosed task and delete it of the list
                    if 1 <= choose_task <= len(tasks):
                        tasks.pop(choose_task - 1)
                    else:
                        print("Error: Task does not exist")
                except ValueError:
                    print("Error: Please enter a valid whole number")
        elif choice == "5":
            print("Goodbye!")
            break
ToDo()

               