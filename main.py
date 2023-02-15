import functions as f
import time
now = time.strftime("%b %Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add,show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = f.get_todos()
        todos.append(todo)
        f.write_todos(todos)

    elif user_action.startswith("show"):
        todos = f.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}.){item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = f.get_todos()
            todos[number] = input("Enter the new todo:") + '\n'
            f.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = f.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            f.write_todos(todos)
            message = f"Todo '{todo_to_remove}' has been removed from the todo"
            print(message)
        except IndexError:
            print("Index is out of range ")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid")

print('bye')
