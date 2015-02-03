#!/usr/bin/env python


import sys


def getRouter(rtr,field):

    router1 = {'os_version':'3.1.1','hostname':'sjc_router1','model':'nexus 9396','domain':'cisco.com','mgmt_ip':'10.1.50.11'}
    router2 = {'os_version':'3.1.1','hostname':'rtp_router2','model':'nexus 9396','domain':'cisco.com','mgmt_ip':'10.1.50.12'}
    router3 = {'os_version':'3.3.1','hostname':'lab_router3','model':'nexus 9504','domain':'lab.cisco.com','mgmt_ip':'10.1.50.13'}
    router_list = [router1,router2,router3]

    for router in router_list:

        if rtr == router['hostname'] and router.has_key(field) == True:
            return ('Hostname: ' + router['hostname'] + ', ' + field + ": " + router[field])

    return "Incorrect router name or data field."


def main():

    result = getRouter(sys.argv[1],sys.argv[2])

    print result


if __name__ == "__main__":

    main()

