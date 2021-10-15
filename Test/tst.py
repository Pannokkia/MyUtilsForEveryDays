import sys

sys.path.insert(1, '../MyUtils')
from MyUtilsForEveryDays.file import touch

res = touch('test1.txt','test2.txt')
print(res)





