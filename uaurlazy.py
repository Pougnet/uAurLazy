#!/usr/bin/python

import sys
import urllib
import subprocess

url = "https://aur.archlinux.org/packages/" + sys.argv[1][0] + sys.argv[1][1] + "/" + sys.argv[1] + "/PKGBUILD"
print "Downloading %s from %s" % (sys.argv[1], url)
urllib.urlretrieve(url, "PKGBUILD")

print "Building and installaing %s" % sys.argv[1]
subprocess.call(["makepkg", "-sic"])

print "Cleaning up"
subprocess.call(["rm", sys.argv[1]+"*", "PKGBUILD"])
