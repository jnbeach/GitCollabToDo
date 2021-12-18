todos = []


def add(todo):
    todos.append(todo)


def update(old_todo, new_todo):
    for i, todo in enumerate(todos):
        if todo == old_todo:
            todos[i] = new_todo


def delete(todo):
    todos.remove("banana")


def main():
    print("This a todo list")


if __name__ == "__main__":
    main()
