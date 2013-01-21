#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

import mattdaemon

class FshellDaemon(mattdaemon.daemon):
    def run(self):
        from fsh import main
        main()

if __name__ == "__main__":
    args = {
        "pidfile": "/tmp/fshell-daemon.pid",
        "stdout": "/tmp/fshell-daemon.log",
        "stderr": "/tmp/fshell-daemon.log"
    }
    daem = FshellDaemon(**args)

    for arg in sys.argv[1:]:
        arg = arg.lower()
        if arg in ('-h', '--help'):
            print 'python', sys.argv[0], 'start|stop|restart|status'

        elif arg in ('start'):
            daem.start()

        elif arg in ('start-no-daemon'):
            # For easy debugging.
            daem.start(daemonize=False)

        elif arg in ('stop'):
            daem.stop()

        elif arg in ('restart'):
            daem.restart()

        elif arg in ('status'):
            if daem.status():
                print 'fshell daemon currently running! :)'
            else:
                print 'fshell daemon not running! :('

        elif arg in ('--requires-root'):
            # Just ignore this, since it's for the superuser check.
            continue

        else:
            print 'Unknown arg:', arg