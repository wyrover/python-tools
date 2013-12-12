#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2013年09月11日 星期三 20时55分15秒
import chardet

def valid_XML_char_ordinal(i):
    return ( # conditions ordered by presumed frequency
            0x20 <= i <= 0xD7FF 
            or i in (0x9, 0xA, 0xD)
            or 0xE000 <= i <= 0xFFFD
            or 0x10000 <= i <= 0x10FFFF
    )

def uniform(text):
    """filter none xml characters"""
    return ''.join(
        c for c in text if
        valid_XML_char_ordinal(ord(c))
   )

def uni_to_utf8(json_obj):
    """encoding key/value of json object to utf8
    for json.loads defaultly loads value to unicode
    """
    if isinstance(json_obj, unicode):
        result = json_obj.encode('UTF-8')
    elif isinstance(json_obj, list):
        result = []
        for key in json_obj:
            result.append(uni_to_utf8(key))
    elif isinstance(json_obj, dict):
        result = {}
        for key in json_obj:
            result[key.encode('UTF-8')] = uni_to_utf8(json_obj.get(key))
    elif isinstance(json_obj, str):
        result = json_obj
    else:
        result = str(json_obj)
    return result

def get_encode(doc):
    d = chardet.detect(doc)
    enc = d['encoding']
    confidence = d['confidence']
    return enc, confidence

def str2uni(text, encoding=None, errors='strict'):

    if encoding is None:
        encoding = 'utf-8'
    if isinstance(text, str):
        return text.decode(encoding, errors)
    elif isinstance(text, unicode):
        return text
    else:
        raise TypeError('str_to_unicode must receive a str or unicode object, got %s' % type(text).__name__)

def uni2str(text, encoding=None, errors='strict'):

    if encoding is None:
        encoding = 'utf-8'
    if isinstance(text, unicode):
        return text.encode(encoding, errors)
    elif isinstance(text, str):
        return text
    else:
        raise TypeError('requires a unicode or str, got %s' % type(text).__name__)

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def main():
    pass

if __name__ == "__main__":
    main()
