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
