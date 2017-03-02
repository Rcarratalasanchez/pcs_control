def get_last(path, separator):
    '''
    This plugin will receive a path of a file and will return the
    filename of it using a custom separator
    '''
    return path.split(separator)[-1]

def get_region(domain):
    '''
    This plugin will receive a domain name and return the region
    which it belongs
    '''
    return domain.split('-')[0]

class FilterModule(object):
    def filters(self):
        return {
            "get_last": get_last,
            "get_region": get_region,
        }
