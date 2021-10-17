import openpyxl as xls

def get_max_rows(excel_filename, sheet_name = 'Sheet1') -> int:
    """
        Count the maximum number of occupied rows

    Arguments: 
        
      excel_filename: excel file to process
      sheet_name: exchel sheet name to check.If sheet name not set, default is Sheet1

    Returns:
        int: Return max number occupied rows
    """

    try:
        wrkbk = xls.load_workbook(excel_filename)
        wrkbk.active = wrkbk[sheet_name]
        return wrkbk[sheet_name].max_row
    except KeyError as e:
        print("Error:", e)
        return -1
   except FileNotFoundError as e:
        print('Check path and filename!' , e.filename)
        return -1
    except PermissionError as e:
        print("Error:", e)
        return -1

def get_max_cols(excel_filename, sheet_name = 'Sheet1') -> int:
    """
        Count the maximum number of occupied columns

    Arguments: 
        
        excel_filename: excel file to process
        sheet_name: exchel sheet name to check.If sheet name not set, default is Sheet1

    Returns:
        int: Return max number occupied columns
    """
    try:
        wrkbk = xls.load_workbook(excel_filename)
        wrkbk.active = wrkbk[sheet_name]
        return wrkbk[sheet_name].max_column
    except KeyError as e:
        print("Error:", e)
        return -1
    except FileNotFoundError as e:
        print('Check path and filename!' , e.filename)
        return -1 
    except PermissionError as e:
        print("Error:", e)
        return -1

def rename_excel_sheet(excel_filename, old_sheet_name, new_sheet_name) -> None:
    """
        Rename Sheet on excel file

    Arguments: 

        excel_filename: excel file to process
        old_excel_sheet_name: old name of ecel sheet
        new_sheet_name: new name of excel sheet

    Returns:
        None
    """
    try:
        wrkbk = xls.load_workbook(excel_filename)
        sh = wrkbk[old_sheet_name]
        sh.title = new_sheet_name
        wrkbk.save(excel_filename)
    except KeyError as e:
        print("Error:", e)
    except FileNotFoundError as e:
        print('Check path and filename!' , e.filename)
    except PermissionError as e:
        print("Error:", e)
