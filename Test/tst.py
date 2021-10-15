import sys

#Python check my module in following directory
sys.path.insert(1, '/MyUtils')
from MyUtilsForEveryDays.file import touch, count_lines, count_lines_exclude_blank_lines

res = touch('test1.txt','test2.txt')
print(res)

lines = count_lines('/MyUtils/MyUtilsForEveryDays/Test/file.txt')
print(lines)

lines = count_lines_exclude_blank_lines('/MyUtils/MyUtilsForEveryDays/Test/file.txt')
print(lines)
