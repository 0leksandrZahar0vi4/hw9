records = {}


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown rec_id. Try another or use help."
        except TypeError:
            return "How can I help you?"
        except NameError:
            return "There is no such number in the dict"

    return inner


@user_error
def hello(*args):
    for func, kw in COMMANDS.items():
        if "hello":
            return f"How can I help you?"


@user_error
def add_record(*args):
    rec_id = args[0]
    rec_value = args[1]
    records[rec_id] = rec_value
    return f"Add record {rec_id = }, {rec_value = }"


@user_error
def change_record(*args):
    rec_id = args[0]
    new_value = args[1]
    rec = records[rec_id]
    if rec:
        records[rec_id] = new_value
        return f"Change record {rec_id = }, {new_value = }"


@user_error
def phone_number(*args):
    for func, kw in COMMANDS.items():
        if "phone":
            contact = input("Enter number: ")
            return f"{records[contact]=}"


@user_error
def show_all(*args):
    for func, kw in COMMANDS.items():
        if "show all":
            return f"{records}"


@user_error
def goodbay(*args):
    for func, kw in COMMANDS.items():
        if ("exit", "good bay", "close"):
            break
    return f"Good bay!"


def unknown(*args):
    return "Unknown command. Try again."


COMMANDS = {
    hello: "hello",
    add_record: "add record",
    change_record: "change record",
    phone_number: "phone",
    show_all: "show all",
    goodbay: ("exit", "good bay", "close"),
}


def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw) :].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input("Enter text: ")

        func, data = parser(user_input.lower())
        print(func(*data))


if __name__ == "__main__":
    main()
