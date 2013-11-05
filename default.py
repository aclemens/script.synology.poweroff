
import xbmc, xbmcgui, xbmcaddon
import subprocess 

def main(isAutostart=False):
	
	print 'script.synology.poweroff: Starting Synology DiskStation Power Off script'
	
	####### Read Settings
	settings = xbmcaddon.Addon( id="script.synology.poweroff" )
	language  = settings.getLocalizedString
	
	# basic settings
	hostOrIp = settings.getSetting("hostOrIp")
	username = settings.getSetting("username")
	password = settings.getSetting("password")
	poweroff_cmd = settings.getSetting("poweroff_cmd")

	command = "sshpass -p \"%s\" ssh -o StrictHostKeyChecking=no %s@%s %s" % (
		password, username, hostOrIp, poweroff_cmd)

	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output,stderr = process.communicate()
	status = process.poll()
	print output

	print 'script.synology.poweroff: Closing Synology DiskStation Power Off script'
	return
	
if __name__ == '__main__':
	main()