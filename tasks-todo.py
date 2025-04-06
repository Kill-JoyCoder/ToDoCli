import mysql.connector as mc # or from mysql import connector
# TF = "Todo.json"
connection = mc.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="todo_list"
)
mycursor = connection.cursor()

def fetch_last_task() -> int:
    mycursor.execute("SELECT task_id from todo_list order by task_id desc limit 1;")
    task_id = mycursor.fetchone()

    if task_id == None:
        return None
    return task_id[0]

# def show_task():
        
def add_task(task_name: str):
    task_id = fetch_last_task()
    task_name = str(input("Enter task name"))
    if task_id != None:
        task_id+=1
    elif task_id == None:
        task_id =1
    mycursor.execute(f"insert into todo_list values({task_id}, \"{task_name}\");")
    connection.commit()
    print(f"Task \"{task_name}\" added successfully")

def view_tasks() -> list[tuple]:
    """Returns the list of tasks."""
    mycursor.execute("Select * from todo_list")
    tasks = mycursor.fetchall()
    return tasks

# Step 6: Delete a Task
def delete_task(task_id: int):
    """Deletes a Task from the list of tasks."""
    mycursor.execute(f"delete from todo_list where task_id = {task_id};")
    connection.commit()
    print(f"Task with ID {task_id} deleted successfully.\n")

# Step 8: get task ids
def get_task_ids() -> list[int]:
    """Returns a list of task ids"""
    mycursor.execute("Select task_id from todo_list")
    task_ids = mycursor.fetchall()
    final_task_ids = []
    for task_id in task_ids:
        final_task_ids.append(task_id[0])
    return final_task_ids

# Step 7: Create a Menu for user to interact with
def main():
    while True:
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Quit")
        choice = input("Enter Your Choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid choice!")
            continue
        if choice == 1:
            task = input("Enter a Task: ")
            add_task(task)
            
        elif choice == 2:
            tasks = view_tasks()
            if tasks == []:
                print("\nNo Tasks\n")
                continue
            print()
            print("Task Id, Task Name")
            for task in tasks:
                print(f"{task[0]}, {task[1]}")
            print()
        elif choice == 3:
            tasks = view_tasks()
            if tasks == []:
                print("\nNo Tasks To Delete\n")
                continue
            print()
            print("Task Id, Task Name")
            for task in tasks:
                print(f"{task[0]}, {task[1]}")
            print()
            task_id = input("Enter the task's id: ")
            try:
                task_id = int(task_id)
            except ValueError:
                print("Enter a valid task id!")
                continue
            # Step 8: get task ids
            ids = get_task_ids()
            if task_id in ids:
                delete_task(task_id)
            else:
                print("Enter a valid task id!")
        elif choice == 4:
            print("Thanks For Using!!")
            break
        else:
            print("Please enter a valid choice!")

if __name__ == "__main__":
    main()


