# https://docs.python.org/3/library/ipaddress.html
import ipaddress

class CIDRs:
    def __init__(self, lst):
        self.cidrs = []
        self.errors = []
        for _ in lst:
            try:
                self.cidrs.append(ipaddress.ip_network(_, strict=True))
            except ValueError as e:
                self.errors.append(str(e))

    def get_errors(self):
        return self.errors

    def get_ipv4_cidrs(self):
        return [c for c in self.cidrs if c.version == 4]

    def get_ipv6_cidrs(self):
        return [c for c in self.cidrs if c.version == 6]

    def get_cidrs(self):
        return self.get_ipv4_cidrs() + self.get_ipv6_cidrs()

    def collapse_ipv4_cidrs(self):
        return ipaddress.collapse_addresses(self.get_ipv4_cidrs())

    def collapse_ipv6_cidrs(self):
        return ipaddress.collapse_addresses(self.get_ipv6_cidrs())

    def summarize_cidrs(self):
        return [_ for _ in self.collapse_ipv4_cidrs()] + [_ for _ in self.collapse_ipv6_cidrs()]