from sys import argv
from json import load, dump

#commands
commands = ['create', 'incomplete' , 'complete', 'inprogress',
            'printall', 'printcomp', 'printprog']

#data
tasks = {commands[0]: [],
         commands[1]: [],
         commands[2]: [],
         commands[3]: []}

#load the saved data form the json file
try:
    with open('tasks.json', 'r') as file:
        tasks = load(file)
except FileNotFoundError:
    pass

if len(argv) >= 3 and argv[1] in commands:


    #getting a single task string form user input
    task = []
    for i in range(2, len(argv)):
        task.append(argv[i])
    
    #checking which command user types
    if argv[1] == commands[0]:
        tasks[commands[0]].append(" ".join(task))
        tasks[commands[1]].append(" ".join(task))
        print(f"Task '{" ".join(task)}' created!")
    
    elif argv[1] == commands[2]:
        tasks[commands[2]].append(" ".join(task))
        tasks[commands[1]].remove(" ".join(task))
        print(f"Task '{" ".join(task)}' completed!")
    
    elif argv[1] == commands[3]:
        tasks[commands[3]].append(" ".join(task))
        print(f"Task '{" ".join(task)}' is in progress!")

#check if user type print commands
elif len(argv) >= 2 and argv[1] in commands:
        
    if argv[1] == commands[4]:
        print("\nALL TASKS:-----\n")
        for index, task in enumerate(tasks[commands[0]]):
            print(f"{index + 1}. {task}.")
        print("\n")

    elif argv[1] == commands[5]:
        print("\nCOMPLETED TASKS:-----\n")
        for index, task in enumerate(tasks[commands[2]]):
            print(f"{index + 1}. {task}.")
        print("\n")

    elif argv[1] == commands[6]:
        print("\nTASK IN PROGRESS:-----\n")
        for index, task in enumerate(tasks[commands[3]]):
            print(f"{index + 1}. {task}.")
        print("\n")

#write the user's data to the json file
with open('tasks.json', 'w') as file:
    dump(tasks, file, indent=4)
        

#if user's input does not meeet the commands
if len(argv) <= 1 or len(argv) >= 3 and argv[1] not in commands:
    print("Please type a appropiate commands!")
    print("Commands: ", end= " ")
    for i in range(len(commands)):
        print(f"{commands[i]},", end= " ")
    print("\n")

