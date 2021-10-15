def touch(*files) -> bool:

    """ 
    Create several empty files.
    :param files: The list of file paths to create.
    :return: The list of created files.

    """

    try:
        for file in files:
            open(file, 'w').close()       
        return True
    except FileNotFoundError as e:
        print('Check path exist!' , e.filename)
        return False
    except PermissionError as e:
        print('Permission denied!' , e.filename)
        return False

def lines_count(file_to_read) -> int:
    """
    Read the number of lines in the file
    
    Args:
        file_to_read : path + filename 

    Returns:
        int: Returns the number of lines of which the file is composed
    """
    try:
        lines = []
        print(file_to_read)
        f = open(file_to_read, "r")
        lines = f.readlines()
        return len(lines)
    except FileNotFoundError as e:
        print('Check file exsit', e.filename)
        return -1
    except PermissionError as e:
        print('Permission denied!' , e.filename)
        return False