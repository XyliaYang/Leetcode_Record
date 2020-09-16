# 面试题20：表示数值的字符串

import re

def isNumberic(str):
    match1=r'^[+-]?\d+(\.\d*)?([eE][+-]?\d+)?$'
    match2=r'^\.\d+([eE][+1]?\d+)?$'

    if re.match(match1,str) or re.match(match2,str):
        return True
    else:
        return False

if __name__=='__main__':
     str='.3e1'

     if isNumberic(str):
         print('true')
     else:
         print('false')