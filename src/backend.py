import os
import pickle
from datetime import datetime

DB_PATH = "./USER.DATA"


def db_exists():
    return os.path.exists(DB_PATH)


def get_designer_name():
    while True:
        designer_name = input("Hello Graphic Designer, What's your name?: ")

        # INVALID INPUT ERROR HANDLING
        if not all(char.isalpha() or char.isspace() for char in designer_name):
            print("Names don't contain numbers or symbols, just alphabets and spaces. Let's try that again.")
            continue
        else:
            return designer_name


def is_valid_date(designer_dob):
    fields = designer_dob.split("/")
    contains_all_fields = len(fields) == 3
    all_fields_are_int = all([f.isdecimal() for f in fields])
    has_valid_format = contains_all_fields and all_fields_are_int

    if not has_valid_format:
        return False

    day, month, year = [int(field) for field in fields]
    day_exists, month_exists = 0 < day < 32, 0 < month < 13
    current_year = datetime.now().year
    year_exists = 1900 < year < current_year

    if day_exists and month_exists and year_exists:
        return True


def get_designer_dob():
    while True:
        designer_dob = input(
            "We'd like to wish you happy birthday, when is it? (dd/mm/yyyy): "
        )

        if is_valid_date(designer_dob):
            fields = designer_dob.split("/")
            return [int(field) for field in fields]

        print("The dob you entered, isn't quite right. Let's try that again.")
        continue


def create_db():
    print("Hey there stranger,",
          "Looks like You are using this photo editor for the first time.",
          "Let's get you started, we'd like to store some info about you.", sep="\n")

    data = {
        "name": get_designer_name(),
        "dob": get_designer_dob()
    }

    db = open(DB_PATH, "wb")
    pickle.dump(data, db)
    db.close()


def get_db():
    if db_exists():
        db = open(DB_PATH, "rb")
        data = pickle.load(db)
        db.close()
        return data
    else:
        create_db()
        return get_db()

