#!/usr/bin/env python

import getopt
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient
from relay_sdk import Interface, Dynamic as D

relay = Interface()

options = {
    'token': relay.get(D.sysdig.connection.token),
    'alert_list': relay.get(D.alert_name).split(','),
}

initialize(**options)


#
# Instantiate the SDC client
#
sdclient = SdcClient(options['token'])

ok, res = sdclient.get_alerts()
if not ok:
    print(res)
    sys.exit(1)

alert_found = False
for alert in res['alerts']:
    if alert['name'] in options['alert_list']:
        alert_found = True
        print("Updating \'" + alert['name'] + "\'. Enabled status before change:")
        print(alert['enabled'])
        alert['enabled'] = False
        ok, res_update = sdclient.update_alert(alert)

        if not ok:
            print(res_update)
            sys.exit(1)

        # Validate and print the results
        print('Alert status after modification:')
        print(alert['enabled'])
        print(' ')

if not alert_found:
    print('Alert to be updated not found')
    sys.exit(1)
