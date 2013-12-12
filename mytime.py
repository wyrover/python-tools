#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年10月14日 星期一 10时49分14秒
import time
import datetime
import re
"""this module defines usually used time func"""

def time2str(timestamp):
    pass

def date2str(timestamp, data_format=""):
    pass


"""
this module detecets date in url
only concerns years between 1900 -- 2099
before 1900 there is no url :(
and 100 years enough :)
"""

pattern = re.compile("|".join([
    "\D(19\d\d|20\d\d)-[0,1]\d-[0-3]\d\D",  # "[not number]2013-11-12[not number]"
    "\D(19\d\d|20\d\d)-[0,1]\d/[0-3]\d\D",  # "[not number]2013-11/12[not number]"
    "\D(19\d\d|20\d\d)/[0,1]\d/[0-3]\d\D",  # "[not number]2013/11/12[not number]"
    "\D(19\d\d|20\d\d)/[0,1]\d-[0-3]\d\D",  # "[not number]2013/11-12[not number]"
    "\D(19\d\d|20\d\d)/[0,1]\d_[0-3]\d\D",  # "[not number]2013/11_12[not number]"
    "\D(19\d\d|20\d\d)_[0,1]\d_[0-3]\d\D",  # "[not number]2013_11_12[not number]"
    "\D(19\d\d|20\d\d)-[0,1]\d[0-3]\d\D",  # "[not number]2013-1112[not number]"
    "\D(19\d\d|20\d\d)/[0,1]\d[0-3]\d\D",  # "[not number]2013/1112[not number]"
    "\D(19\d\d|20\d\d)[0,1]\d[0-3]\d\D",  # "[not number]20121112[not number]"
    "\D(19\d\d|20\d\d)[0,1]\d\D",  # "[not number]200609[not number]"
    "\D(19\d\d|20\d\d)/[0,1]\d\D",  # "[not number]2013/11[not number]"
    "\D(19\d\d|20\d\d)/\d\D",  # "[not number]2013/7[not number]"
    "\D(19\d\d|20\d\d)-[0,1]\d\D",  # "[not number]2013-11[not number]"
    "\D(19\d\d|20\d\d)-\d\D",  # "[not number]2013-7[not number]"
    "\D(19\d\d|20\d\d)_[0,1]\d\D",  # "[not number]2013_11[not number]"
    "\D(19\d\d|20\d\d)_\d\D",  # "[not number]2013_7[not number]"
    "\D[0,1]\d\/(19\d\d|20\d\d)\D",  # "[not number]11/2013[not number]"
    "\D\d\/(19\d\d|20\d\d)\D",  # "[not number]7/2013[not number]"
    "\D[0,1]\d/[0-3]\d/(19\d\d|20\d\d)\D",  # "[not number]11/21/2013[not number]"
    "\D[0,1]\d[0-3]\d/(19\d\d|20\d\d)\D",  # "[not number]1121/2013[not number]"
]))


def contains_date(url):
    return bool(pattern.search(url))


def main():
    pass


if __name__ == "__main__":
    main()                   
