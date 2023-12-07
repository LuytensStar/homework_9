contacts = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
    return wrapper()

@input_error
def add(name, phone):
    contacts[name] = phone
    return f"{name} has been added as {phone}"

@input_error
def change(name, phone):
    contacts[name] = phone
    return f"{name}'s phone number has been updated to {phone}"

@input_error
def number(name):
    return f"{name}'s phone number is {contacts[name]}"

def show_all():
    if not contacts:
        return "You have no contacts saved"
    else:
        return "\n".join([f"{name}: {contacts[name]}" for name in contacts])

def main():
    while True:
        command = input("Enter a command: ")
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            name, phone = command.split()[1:]
            print(add(name, phone))
        elif command.startswith("change"):
            name, phone = command.split()[1:]
            print(change(name, phone))
        elif command.startswith("phone"):
            name = command.split()[1]
            print(number(name))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
