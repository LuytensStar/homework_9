contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Give me name and phone please"
        except TypeError:
            return "Give me name and phone please"
        except ValueError:
            return "Enter user name"
        except NameError:
            return "Give me name and phone please"
    return wrapper


def hello():
    return 'Hello how can i help you'


@input_error
def add(name, phone):
    if phone not in contacts.values() and (name not in contacts.keys()):
        contacts[name] = phone
        return ('Номер телефону додано до контактів.')
    else:
        return ('Цей номер телефону вже є в контактах. Будь ласка, спробуйте інший номер.')
    # if phone in contacts.values():
    #     print('Контакт з таким номер вже існує')
    # contacts[name] = phone
    # return f"{name} has been added as {phone}"


@input_error
def change(name, phone):
    if name in contacts.keys():
        contacts[name] = phone
        return f"Номер телефону контакту {name} успішно змінено на {phone}"
    else:
        return f'Контакту з імям {name} не існує'
    # return f"{name}'s phone number has been updated to {phone}"

@input_error
def phone(name):
    return f"{name}'s phone number is {contacts[name]}"



@input_error
def show_all():
    #return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contacts



carry = {'show_all': show_all(), 'phone': phone, 'change': change, 'add': add, 'hello': hello()}


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