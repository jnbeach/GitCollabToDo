todos = []


def main():
    print("hey there")  # Using the special variable  # __name__
    print("This is some more changes.")


if __name__ == "__main__":
    main()


def hello():
    print("hello")


def hello2():
    print("Bonjour")


def add(todo):
    todos.append(todo)


def update(old_todo, new_todo):
    for i, todo in enumerate(todos):
        if todo == old_todo:
            todos[i] = new_todo
