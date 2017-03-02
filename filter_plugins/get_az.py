def get_az_compute(hostname):
    '''
    This plugin will receive a Hostname from Produban infra and will return
    in which AZ are located based on the Compute Hostname
    '''
    import re
    az = re.findall('\d+', hostname)

    return abs(int(az[1]))

def get_az_controller_master(hostname):
    '''
    This plugin will receive a Hostname from Produban infra and will return
    master if the node is the third in a group of 3, else will return slave.
    The use case is for controllers and Cinder, you dont know in which AZ are
    a controller.
    '''
    import re
    node = re.findall('\d+', hostname)[1]
    if int(node) % 3 == 0:
        return 'master'
    else:
        return 'slave'

def get_az_controller_master_name(hostname):
    '''
    This plugin will receive a Hostname from Produban infra and will return
    the name of the master node.
    '''
    import re
    node = hostname.split('.')
    return "%s03.%s" % (node[0][:-2],'.'.join(node[1:]))

def get_az_controller(hostname):
    '''
    This plugin will receive a Hostname from Produban infra and will return
    the AZ where is located the controller node based on groups of 3 nodes
    starting from 01
    '''
    import re
    node = re.findall('\d+', hostname)[1]
    group = float(node) / 3
    if group > abs(int(node) / 3):
        return int(group + 1)
    else:
        return int(group)

def get_controller(hostname):
    '''
    This plugin will receive a Hostname from Produban infra and will return
    the position inside of cluster (1|2|3)
    return 3 when controller is the third, return 2 when is the second...
    '''
    import re
    node = re.findall('\d+', hostname)[1]
    if int(node) % 3 == 0:
        return 3
    else:
        return int(node) % 3

class FilterModule(object):
    def filters(self):
        return {
            "get_az_compute": get_az_compute,
            "get_az_controller_master": get_az_controller_master,
            "get_az_controller_master_name": get_az_controller_master_name,
            "get_az_controller": get_az_controller,
            "get_controller": get_controller,
        }
