records = {}


def user_error(funk):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "NOT enouth parametr."
        except KeyError:
            return "Unknown rec_id. Tyr another or use help"

    return inner


@user_error
def add_record(*args):
    rec_id = args[0]
    rec_value = args[1]
    records[rec_id] = rec_value
    return f"Add record {rec_id = }, {rec_value = }"


@user_error
def change_record(*args):
    rec_id = args[0]
    rec_value = args[1]
    rec = records[rec_id]
    if rec:
        records[rec_id] = rec_value


def unknown(*args):
    return "Unknown command. Try again"


COMMANDS = {
    hello_add: "Hello",
    add_record: "Add_record",
    change_record: "Change record",
    phone_view: "Phone_view",
    show_all_contacts: "Show all contacts",
    goodbay: "Exit the program",
}


def parser(text: str):
    for funk, kw in COMMANDS.items():
        if text.starswith(kw.lower()):
            return funk, text[len(kw) :].strip().split()
        return unknown, []


def main():
    while True:
        user_input = input("Enter command: ")
        funk, data = parser(user_input.lower())
        print(funk(*data))


if __name__ == "__name__":
    main()
