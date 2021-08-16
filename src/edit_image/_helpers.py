import os.path


def auto_renamed_writable_file(file_path, recursive_index=1):
    """
    RETURNS THE ORIGINAL FILE PATH IF IT DOES NOT EXIST,
    IF THE FILE PATH EXISTS, AUTO RENAMES THE PATH AND RETURNS NEW NON-EXISTENT PATH
    """
    if not os.path.isfile(file_path):
        return open(file_path, "w")
    else:
        new_file_path = file_path.split(".")
        new_file_path[-2] += f"({recursive_index})"
        new_file_path = ".".join(new_file_path)
        if os.path.isfile(new_file_path):
            return auto_renamed_writable_file(file_path, recursive_index + 1)
        else:
            return open(new_file_path, "w")


def get_percentage_of(value, prompt):
    while True:
        try:
            percentage = float(input(prompt))
            if not (0 <= percentage <= 100):
                raise ValueError
            break
        except ValueError:
            print('\033[31m' + 'INVALID INPUT' + '\033[0m')

    abs_value = round((percentage / 100) * value)
    return abs_value
