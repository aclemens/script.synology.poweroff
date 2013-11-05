import xbmc, xbmcgui, xbmcaddon, sys, os


def checkLibrary(module_name):
    try:
        __import__(module_name)
        print "\tLibrary '%s' successfully loaded!" % module_name
        return True
    except ImportError, e:
        print "\tError: Unable to load the library '%s'!" % module_name
        print e
        dialog = xbmcgui.Dialog()
        dialog.ok("Could not find a required library", "Make sure that the python library '%s' is installed on your system." % module_name)
        exit()
        sys.exit(1)


def start():
    __addon__        = xbmcaddon.Addon()
    __addonid__      = __addon__.getAddonInfo('id')
    __addonname__    = __addon__.getAddonInfo('name')
    print "%s: Starting %s" % (__addonid__, __addonname__)


def exit():
    __addon__        = xbmcaddon.Addon()
    __addonid__      = __addon__.getAddonInfo('id')
    __addonname__    = __addon__.getAddonInfo('name')
    print "%s: Closing %s" % (__addonid__, __addonname__)


def log(stream):
    for line in stream:
        print "\t%s" % line


def main(isAutostart=False):    
    start()
    
    # check the required libraries
    checkLibrary('paramiko')
    import paramiko

    # basic settings
    __addon__       = xbmcaddon.Addon()
    hostOrIp        = __addon__.getSetting("hostOrIp")
    username        = __addon__.getSetting("username")
    password        = __addon__.getSetting("password")
    poweroff_cmd    = __addon__.getSetting("poweroff_cmd")

    # call the poweroff command on the (remote) machine
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostOrIp, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(poweroff_cmd)
    log(stdout)
    log(stderr)
    ssh.close()

    exit()
    
    
if __name__ == '__main__':
    main()