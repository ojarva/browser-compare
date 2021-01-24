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

Licensed under MIT license: see LICENSE.txt for full details.
