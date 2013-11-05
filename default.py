import xbmc, xbmcgui, xbmcaddon, sys


def checkLibrary(module_name):
    try:
        __import__(module_name)
        print "\tLibrary '%s' successfully loaded!" % module_name
        return True
    except ImportError:
        print "\tError: Unable to load the library '%s'!" % module_name
        dialog = xbmcgui.Dialog()
        dialog.ok("Could not find a required library", "Make sure that the python library '%s' is installed on your system." % module_name)
        exit()
        sys.exit(1)


def start():
    print 'script.synology.poweroff: Starting Synology DiskStation Power Off script'


def exit():
    print 'script.synology.poweroff: Closing Synology DiskStation Power Off script'


def log(stream):
    for line in stream:
        print "\t%s" % line


def main(isAutostart=False):    
    start()

    checkLibrary('paramiko')
    import paramiko
    
    ####### Read Settings
    settings = xbmcaddon.Addon( id="script.synology.poweroff" )
    language  = settings.getLocalizedString
    
    # basic settings
    hostOrIp = settings.getSetting("hostOrIp")
    username = settings.getSetting("username")
    password = settings.getSetting("password")
    poweroff_cmd = settings.getSetting("poweroff_cmd")

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