FILEPATH = "todos.txt"
def get_current_list(filepath=FILEPATH):
    with open(filepath, 'r') as todo_file:
        get_current_list = todo_file.readlines()
    return get_current_list

def write_current_list(todo_list, filepath=FILEPATH):
    with open(filepath, 'w') as todoFile:
        todoFile.writelines(todo_list)

if __name__ == "__main__":
    print("debigging purpose")
    print(get_current_list("./todos.txt"))