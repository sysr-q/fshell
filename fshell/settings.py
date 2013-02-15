# -*- coding: utf-8 -*-

host = "127.0.0.1"
port = 31337 # ELITE, geddit?

# The absolute path to the database we're storing details in.
database = "/path/to/fshell.db"

# Where you want to bind our "shell" to.
# e.g.: "/shell.php", "/the/gibson/shell.php", "/magic-hacks.phtml"
url = "/shell.php"

# True/False; if it's True, the page <title> will be the shell name.
show_title = False

# Templates available:
#  "greenshell", "c99pro", "login"
template = "greenshell"

## Template variables (Safe to change, for-the-most-part)
template_vars = {
    "v_script": url, # leave this
    "v_hacker": "red_hat",
    "v_shellver": "X1 pr0",
    "v_rooted": True, # True/False, the template might change style based on this

    "s_php_ver": "PHP 5.4.4-11",
    "s_uname_a": "Linux min3152 2.6-32-042stab051.2 #1 SMP x86 GNU/Linux",
    "s_whoami": "nobody",
    "s_perms": "-rwxrw-rw-" # fake script file perms
}

# Don't touch this, all hell could break loose.
schema = """CREATE TABLE IF NOT EXISTS `fshell` (
    `id` INTEGER PRIMARY KEY,
    `method` varchar(16) NOT NULL, -- The HTTP method they use; GET, POST
    `ip` varchar(15) NOT NULL,     -- The IP address of the offender
    `time` INTEGER NOT NULL,       -- UNIX timestamp of request, in form of: int(time.time())
    
    `agent` TEXT NOT NULL,         -- The full useragent.
    `agent_platform` TEXT NOT NULL,-- User-Agent: platform reported by Flask - request.user_agent.platform
    `agent_browser` TEXT NOT NULL, -- User-Agent: browser reported by Flask - request.user_agent.browser
    `agent_version` TEXT NOT NULL, -- User-Agent: version reported by Flask - request.user_agent.version
    `agent_language` TEXT NOT NULL -- User-Agent: language reported by Flask - request.user_agent.language
);"""