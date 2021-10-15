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

def count_lines(file_to_read) -> int:
    """
    Read the number of lines in the file
    
    Args:
        file_to_read : path + filename 

    Returns:
        int: Returns the number of lines of which the file is composed
    """
    try:
        lines = []        
        with open(file_to_read, "r") as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError as e:
        print('Check file exsit', e.filename)
        return -1
    except PermissionError as e:
        print('Permission denied!' , e.filename)
        return -1

def count_lines_exclude_blank_lines(file_to_read) -> int:
    """
    Read the number of lines in the file excluded blank lines
    
    Args:
        file_to_read : path + filename 

    Returns:
        int: Returns the number of lines of which the file is composed
    """
    try:
        count = 0
        lines = []
        with open(file_to_read, "r") as f:
            lines = f.readlines()
            for l in lines:
                if(l != "\n"):
                    count = count + 1
        return count
    except FileNotFoundError as e:
        print('Check file exsit', e.filename)
        return -1
    except PermissionError as e:
        print('Permission denied!' , e.filename)
        return -1
