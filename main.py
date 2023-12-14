contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Give me name and phone please")
        except TypeError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
        except NameError:
            print("Give me name and phone please")
    return wrapper


def hello():
    return 'Hello how can i help you'


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


@input_error
def show_all():
    #return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contacts


carry = {'show': show_all(), 'number': number, 'change': change, 'add': add, 'hello': hello()}


def parse_command(command):
    parts = command.split(' ')
    if '' in parts:
        parts.remove('')
    if parts[0] in carry and len(parts) == 3:
        return carry[str(parts[0])](parts[1], parts[2])
    elif parts[0] in carry and len(parts) == 2:
        return carry[parts[0]](parts[1])
    elif parts[0] in carry and len(parts) == 1:
        return carry[parts[0]]


def main():

    while True:
        command = input("Enter a command: ")
        if command in ['exit', 'close', 'good bye']:
            print('Good bye!')
            break
        print(parse_command(command))


if __name__ == "__main__":
    main()