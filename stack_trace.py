#!/usr/bin/env python2.6
# encoding: utf-8
# Author: guodongdong <dd.guo@foxmail.com>
# Created Time: 2014年05月28日 星期三 16时38分19秒
# pystack

import signal
import sys
import time
import traceback
import threading

class PYStackThread(threading.Thread):
    def __init__(self, interval):
        self.interval = interval
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            pystack()
            time.sleep(self.interval)

def pystack():
    for tid, stack in sys._current_frames().items():
        info = []
        t = _get_thread(tid)
        info.append('"%s" tid=%d' % (t.name, tid))
        for filename, lineno, _, line in traceback.extract_stack(stack):
            info.append('    at %s(%s:%d)' % (line,
                filename.split("/")[-1], lineno))
        print '\r\n'.join(info)
        print  ''

def _get_thread(tid):
    for t in threading.enumerate():
        if t.ident == tid:
            return t
    return None

def _pystack(sig, frame):
    pystack()

def enable_pystack(interval=None):
    """
      print stack trace 
      if interval set, then print every interval secs
      else only print when receive SIGUSR1 signal
    """
    if not interval:
        signal.signal(signal.SIGUSR1, _pystack)
    else:
        thread = PYStackThread(interval)
        thread.setDaemon(True)
        thread.start()

def main():
    enable_pystack(3)
    time.sleep(5)
    print "finish"

if __name__ == "__main__":
    main()
