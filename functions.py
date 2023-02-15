def get_todos(filepath='Files/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='Files/todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("when we run this file i need this")
    print("i dont need this if block when this module is used somewhere")

# __name__ is the main file, becoz its main file when we run this file,
# but when we run this in main file, it will give the name of this fiile i.e function

# which means __name__ will always be main for tat particular file,
# hence it will run when executed from that file, if excuted from outside it wont execute that block