# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 31337 # ELITE, geddit?

# The absolute path to the database we're storing details in.
database = "/path/to/fshell.db"

# Where you want to bind our "shell" to.
# e.g.: "/shell.php", "/the/gibson/shell.php", "magic-hacks.phtml"
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