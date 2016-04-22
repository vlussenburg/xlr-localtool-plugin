#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.xebialabs.xlrelease.plugin.overthere import OverthereSession


def apply_task_options():
    if username:
        host.setProperty('username', username)
        host.setProperty('password', password)
    if privateKeyFile:
        host.setProperty('privateKeyFile', privateKeyFile)
        host.setProperty('passphrase', passphrase)    
    if connectionOptions:
        host_options = host.getProperty("connectionOptions")
        for key, value in connectionOptions.iteritems():
            host_options.put(key, value)


host = task.pythonScript.getProperty("host")
script = "%s %s \"%s %s.%s %s '%s'\"" % (host.getProperty("executablePath"), host.getProperty("server"), action, client, service, duration, message)
apply_task_options()
session = OverthereSession(host)
response = session.execute(script, None)


# set variables
output = response.stdout
error = response.stderr

if response.rc == 0:
    print "```"
    print output
    print "```"
else:
    print "Exit code: "
    print response.rc
    print
    print "#### Output:"
    print "```"
    print output
    print "```"

    print "----"
    print "#### Error stream:"
    print "```"
    print error
    print "```"
    print

    sys.exit(response.rc)