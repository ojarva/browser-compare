Browser upgrade detection
=========================

This small library detects browser downgrades and major changes,
including OS/browser family changes. It could be used as an indicator
of user browser authenticity: if authentication cookies are used
on downgraded browser, it might be restored from a backup.

Similarly, cookie that appears on completely different platform
or browser is probably either stolen or copied. This check is not
foolproof, as attacker can easily spoof user-agent too.

Example usage:

::

  from browser_compare import *

  old_ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0'
  new_ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'
  another_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0'

  bc = BrowserCompare(old_ua, new_ua)
  print bc.compare() # True

  bc = BrowserCompare(new_ua, old_ua)
  print bc.compare() # raises UADowngradedException

  bc = BrowserCompare(old_ua, another_ua)
  print bc.compare() # raises UAChangedException

Use ``UAException`` to catch any problems with user-agents, if you don't
care why it was rejected. Additional information is available in 
``exception.msg``.

License
-------

Licensed under MIT license:

Copyright (c) 2014 Olli jarva olli@jarva.fi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
