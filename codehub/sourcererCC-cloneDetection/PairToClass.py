#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""created by fwk
   2018/06/20
   to transform clone pair to clone group 
"""

import sys
# set max recursion depth
sys.setrecursionlimit(100000)

data = [{1,2},{3,6},{4,7},{7,5},{3,1},{1,3},{0,4}]

def pairToGroup(grouplist, result):
    if len(grouplist) == 0:
        return result
    firstGroup = grouplist[0]
    flag = 0
    for i,v in enumerate(grouplist[1:]):
        # ru guo you jiaoji
        if firstGroup & v:
            flag = i+1
            break
    if flag:
        # qiu bing ji
        grouplist[0] = grouplist[0] | grouplist[flag]
        grouplist.pop(flag)
        # print grouplist
        pairToGroup(grouplist, result)
    else:
        result.append(grouplist[0])
        pairToGroup(grouplist[1:], result)
        

if __name__ == "__main__":
    result = []
    pairToGroup(data, result)
    print result
