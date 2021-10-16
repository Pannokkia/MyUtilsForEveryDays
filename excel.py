import openpyxl as xls


def get_max_rows(excel_filename) -> int:
    """
        Count the maximum number of occupied rows

    Returns:
        int: Return mac number occupied rows
    """

    try:
        wrkbk = xls.load_workbook(excel_filename)
        sh = wrkbk.active
        return sh.max_row
    except Exception as e:
        print("Error on get_max_rows!", e)
        return -1

def get_max_cols(excel_filename) -> int:
    """
        Count the maximum number of occupied columns

    Returns:
        int: Return mac number occupied columns
    """
    try:
        wrkbk = xls.load_workbook(excel_filename)
        sh = wrkbk.active
        return sh.max_column
    except Exception as e:
        print("Error on get_max_cols!", e)
        return -1