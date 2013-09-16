#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月11日 星期三 20时55分00秒
import urllib2
import cookielib

def get_redirected(url):
    jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
    f = opener.open(url)
    return f.geturl()

def main():
    pass

if __name__ == "__main__":
    main()
