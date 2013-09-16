#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月16日 星期一 14时56分05秒

def unique(list_, key=lambda x: x):
    """efficient function to uniquify a list preserving item order"""
    seen = {}
    result = []
    for item in list_:
        seenkey = key(item)
        if seenkey in seen: 
            continue
        seen[seenkey] = 1
        result.append(item)
    return result

def main():
    pass

if __name__ == "__main__":
    main()
