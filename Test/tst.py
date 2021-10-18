import sys
import openpyxl as xls

from openpyxl.styles.fonts import Font

#Python check my module in following directory
sys.path.insert(1, '/MyUtils')
from MyUtilsForEveryDays.file import touch, count_lines_with_blank_lines, count_lines_without_blank_lines
from MyUtilsForEveryDays.excel import get_max_rows,get_max_cols, rename_excel_sheet, remove_excel_sheet, change_style_cells

COLOR_YELLOW = 'FFFF00'
COLOR_BLACK = '000000'
COLOR_RED = 'FF0000'

excel_filename = '/MyUtils/MyUtilsForEveryDays/Test/Test.xlsx'
wrkbk = xls.load_workbook(excel_filename)

#res = touch('test1.txt','test2.txt')
#print(res)

#lines = count_lines_with_blank_lines('/MyUtils/MyUtilsForEveryDays/Test/file.txt')
#print(lines)

#lines = count_lines_without_blank_lines('/MyUtils/MyUtilsForEveryDays/Test/file.txt')
#print(lines)


num_rows = get_max_rows(wrkbk,'Pluto1')
print(num_rows)

num_cols = get_max_cols(wrkbk,'Pluto1')
print(num_cols)


#rename_excel_sheet(wrkbk,'Pippo','Pluto')

#remove_excel_sheet(wrkbk,'Popo')

lst_cells_to_change_font_style = ['A1','A3','D6']
change_style_cells(wrkbk,lst_cells_to_change_font_style, 'Pluto1', COLOR_YELLOW, bold=True,size=30, name='Comic Sans MS')

wrkbk.save(excel_filename)
wrkbk.close()