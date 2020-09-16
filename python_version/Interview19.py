# 面试题19：正则表达式匹配

def match(str,pattern):
    if str is None or pattern is None:
        return False
    return matchCore(str,0,pattern,0)

def matchCore(str,str_index,pattern,pat_index):
    len_str=len(str)
    len_pat=len(pattern)

    # 成功：字符串和模式都到尽头
    if str_index==len_str and pat_index==len_pat:
        return True
    # 失败：一个到底另一个没有到底
    if str_index==len_str and pat_index!=len_pat or pat_index==len_pat and str_index!=len_str:
        return False
    # 模式第二个字符为*
    if pat_index+1<len_pat and pattern[pat_index+1]=='*':
        if pattern[pat_index]==str[str_index]:
            return matchCore(str,str_index+1,pattern,pat_index)
        else:
            return matchCore(str,str_index,pattern,pat_index+2)
    else:
        if pattern[pat_index]==str[str_index] or pattern[pat_index]=='.':
            return matchCore(str,str_index+1,pattern,pat_index+1)
        else:
            return False


if __name__=='__main__':
    str=None
    pattern=None
    print(match(str,pattern))
