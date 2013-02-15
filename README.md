fshell
======

fshell is a fake honeypot shell.php script, written in Python using Flask.  
It's really just there to mess with skiddies who think they're cool by using prefabricated tools.  

Features
--------

+ Stores logs in an sqlite db.
+ A few templates to choose from. (or make your own!)
+ Doesn't actually do anything with POST data - __100% safe__.
+ Guaranteed to make some skiddies mad.

Dependencies
------------

+ `Python 2.7.x`
+ `sqlite3` (comes with Python)
+ `Flask` (`pip install flask`)
+ `pysqlw>=1.3.0` (`pip install pysqlw`)
+ `mattdaemon>=1.1.0` (`pip install mattdaemon`)

Notes
-----

+ It's unlikely to happen, but skiddies may attempt to throw packets at your website in an attempt to take your fshell down.
    + You take full liability for this, I in no way can help you there.

Running / Usage
---------------

+ git clone the fshell repo
+ Edit the settings to your liking, in `settings.py`.
+ fshell uses my [mattdaemon](https://github.com/plausibility/mattdaemon) daemonizer, so usage is simple:
    + `python fshell.py start`
    + `python fshell.py stop`
    + `python fshell.py status` (is the daemon already running?)
    + You should be in the same directory as fshell for the initial run, or else it won't find `schema.sql`
+ Forward connections to the honeypot using nginx, your httpd of choice, iptables, whatever.

Author
------

+ [plausibility](https://github.com/plausibility)
