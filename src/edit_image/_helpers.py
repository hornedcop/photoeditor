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


def get_file_extension(file_path):
    return file_path.split["."][-1]
