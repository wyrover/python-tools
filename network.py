#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月11日 星期三 20时56分44秒
import requests

def get_utf8_body(url):
    response = requests.get(url)
    return response.text

def get_http_body():
    pass

def main():
    pass

def get_redirected(url):
    pass


if __name__ == "__main__":
    main()
