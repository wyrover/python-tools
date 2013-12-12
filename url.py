#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月11日 星期三 20时55分00秒
import cookielib
import re
import types
import urllib2
import urlparse

import hashlib


from unicode import uni2str
from libs.TLDs.regDomain import getRegisteredDomain
from libs.TLDs.effectiveTLDs import tldTree

ip_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

def get_domain(url):

    host = urlparse.urlparse(url).hostname
    domain = host

    if host:
        #ip
        if ip_pattern.match(host):
            domain = host
        else:
            """
                use 3rd lib to parse domain
            """
            domain = getRegisteredDomain(host, tldTree)
    return domain

def get_redirected(url):
    jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
    f = opener.open(url)
    return f.geturl()

def get_uid(url):
    """
        get the uid of the url
        algorithm:
        1) get 16 bytes (128 bits) md5, encoded by hex
        2) split the first 8 bytes and the last 8 bytes
        3) convert the two 8 bytes into int
        4) XOR the two 8 bytes
        5) encode the result by hex
    """
    # convert unicode to str (with encode utf-8)
    # this function is str safe, without double encode error
    url = uni2str(url)
    
    if isinstance(url, types.StringType):
        # md5 is a string represents a 32bytes hex number
        md5 = hashlib.new("md5", url).hexdigest()
        first_half_bytes = md5[:16]
        last_half_bytes = md5[16:]
        
        # get the two long int
        first_half_int = int(first_half_bytes, 16)
        last_half_int = int(last_half_bytes, 16)
        
        # XOR the two long int, get a long int
        xor_int = first_half_int ^ last_half_int
        
        # convert to a hex string
        uid = "%x" % xor_int
        
        return uid

def get_digest(url):
    return url

def main():
    pass

if __name__ == "__main__":
    main()
