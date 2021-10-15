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
    