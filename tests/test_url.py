#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月16日 星期一 14时13分45秒
import sys
import unittest

sys.path.append("../")

from url import get_redirected

class TestURL(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_redirected(self):
        url = "http://finance.sina.com.cn/"
        self.assertEquals(url, get_redirected(url))
        src_url = "http://qq.com/"
        dst_url = "http://www.qq.com/"
        self.assertEquals(dst_url, get_redirected(src_url))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
