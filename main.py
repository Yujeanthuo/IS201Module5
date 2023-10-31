from modules import helper_functions
import time 

prompt = "Your options are: Show, Add, Edit, Complete, Exit:"
flag = True

while flag:
    time_now = time.strftime("%b %d,%Y %H:%M:%S")
    print(f"It is now: {time_now}")
    userInput = input(prompt)
    userInput = usrInput.strip().title()
match userInput:
    case "show":
        currentlst = helper_functions.get_current_list()
        filterLst = [item.strip('\n') for item in currentlst]
        for idx, item in enumerate(filterLst):
            print(f"{idx+1}{item}")
        if len(currentlst) <= 0:
            print("None todo items")
    case "Add":
        addtodo = input("Add this to todo list") + "\n"
        currentlst = helper_functions.get_current_list() 
        currentlst.append(addtodo)
        helper_functions.write_current_list(currentlst)
    case "Edit":
        currentlst = helper_functions.get_current_list() 
        editindx = int(input("Edit number: ")) -1
        newTodo = input("New todo item: ") + "\n"
        currentlst[editindx] = newTodo
        helper_functions.write_current_list(currentlst)
    case "Complete":
        currentlst = helper_functions.get_current_list()
        removeTodo = input(" index or todo name to remove")
        if str.isdigit(removeTodo):
            removeTodo = int(removeTodo)
            if removeTodo > len(currentlst) or removeTodo < 1:
                print("Index must between 1 to", len(currentlst))
            else:
                removeTodo = removeTodo -1
                print("Removed:", currentlst.pop(removeTodo))
        else:
            currentlst.remove(removeTodo)
        helper_functions.write_current_list(currentlst)
    case "Exit":
        flag = False

