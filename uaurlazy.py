#!/usr/bin/python2

import sys
import os
import urllib
import subprocess

if sys.argv[1] == "help":
	print "Usage:"
	print "Parameters:"
	print "		install packagename - installs the package"
	print "		help - displays this useful help file"	
elif sys.argv[1] == "install":
	url = "https://aur.archlinux.org/packages/" + sys.argv[2][0] + sys.argv[2][1] + "/" + sys.argv[2] + "/PKGBUILD"

	httpstatus = urllib.urlopen(url).getcode()	

	if httpstatus == 404:
		print "Package not found"
	elif httpstatus == 500:
		print "Server is down, try again later"
	else:
		print "Changing directory to /tmp for build process"
		os.chdir("/tmp/")

		print "Downloading %s from %s" % (sys.argv[2], url)
		urllib.urlretrieve(url, "PKGBUILD")

		print "Building and installing %s" % sys.argv[2]
		subprocess.call(["makepkg", "-sic"])

		print "Cleaning up"
		subprocess.call(["rm", "PKGBUILD"])
else:
	print "Invalid option, for usage please enter 'uaurlazy help'"
	os.sysexit()
