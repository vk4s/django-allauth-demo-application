
def get_allowed_hosts(hosts, separator=','):
    allowed_hosts = []
    for host in hosts.split(separator):
        if host:
            allowed_hosts.append(host.strip())
    return allowed_hosts


