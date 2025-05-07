import json
import os 

def check_file():
    if(os.path.exists("tasks.json")):
        with open ("tasks.json", "r") as file:
            return json.load(file)
    return []
def save_file(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks ,file, indent=4)


def add_task(tasks):
    task=input("please enter the task :\n")
    task_id=len(tasks)+1
    tasks.append({"Task ID" : task_id, "Task"  :task , "Task Status" : False})
    save_file(tasks)
    print("task added successfully")

def view_task(tasks):
    if not tasks:
        print("your to do list is empty!")
    else:
        for task in tasks:
            if(task["Task Status"]!=False):
                status="✔"
            else:
                status="❌"
            print(f"{task["Task ID"]}  {task["Task"]}  {status}")

def complete_task(tasks):
    if not tasks:
        print("your to do list is empty!")
    else:
        id=int(input("please enter the task id = "))
        for task in tasks:
            if(id==task["Task ID"]):
                task["Task Status"]=True
                save_file(tasks)
                print("marked complete ")
                return
        print(f"task with {id} was not found!")

def delete_task(tasks):
    if not tasks:
        print("your to do list is empty!")
    else:
        id=int(input("please enter the taks id = "))
        for task in tasks:
            if(id==task["Task ID"]):
                tasks.remove(task)
                for i , t in enumerate(tasks):
                    t["Task ID"]=i+1
                save_file(tasks)
                print("deleted task")
                return
        print(f"task with {id} was not found!")

def menu():
    print("_____MENU____")
    print("1. ADD A TASK")
    print("2. VIEW ALL TASK")
    print("3. COMPLETE A TASK")
    print("4. DELETE A TASK")
    print("5. PRINT THE MENU")
    print("6. EXIT")


tasks=check_file()

menu()

while True:
    opt=int(input("please enter your option = "))
    if(opt==1):
        add_task(tasks)
    elif(opt==2):
        view_task(tasks)
    elif(opt==3):
        complete_task(tasks)
    elif(opt==4):
        delete_task(tasks)
    elif(opt==5):
        menu()
    elif(opt==6):
        print("exiting..")
        break

    else:
        print("please enter the correct option from the menu..")    
