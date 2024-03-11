import ipaddress
from src.cidrs import CIDRs

# '192.168.0.1' などIPアドレス形式を受け取れる
def test_ipv4addr():
    cidrs = CIDRs(['192.168.0.1'])
    assert cidrs.get_ipv4_cidrs() == [ipaddress.IPv4Network('192.168.0.1/32')]

# '192.168.0.0/30' などCIDR形式を受け取れる
def test_ipv4cidr():
    cidrs = CIDRs(['192.168.0.0/30'])
    assert cidrs.get_ipv4_cidrs() == [ipaddress.IPv4Network('192.168.0.0/30')]

# '192.168.0.1/30' などCIDR形式ではホスト部を受け取れない
def test_invalid_ipv4cidr_with_host_bits():
    cidrs = CIDRs(['192.168.0.1/30'])
    assert cidrs.get_errors() == ['192.168.0.1/30 has host bits set']

# 無効な形式の入力を受け取った場合にエラーを返す
def test_invalid_input():
    cidrs = CIDRs(['192.168.0'])
    assert cidrs.get_errors() == ["'192.168.0' does not appear to be an IPv4 or IPv6 network"]

# IPv4 を集約できる
def test_summarize_ipv4():
    cidrs = CIDRs(['192.168.0.0', '192.168.0.1', '192.168.0.2'])
    assert cidrs.summarize_cidrs() == [ipaddress.IPv4Network('192.168.0.0/31'), ipaddress.IPv4Network('192.168.0.2/32')]

# IPv6 を集約できる
def test_summarize_ipv6():
    cidrs = CIDRs(['2001:db8::', '2001:db8::1', '2001:db8::2'])
    assert cidrs.summarize_cidrs() == [ipaddress.IPv6Network('2001:db8::/127'), ipaddress.IPv6Network('2001:db8::2/128')]

# IPv4 と IPv6 を混在させて集約できる
def test_summarize_mixed():
    cidrs = CIDRs(['2001:db8::', '192.168.0.0', '2001:db8::2', '192.168.0.2', '2001:db8::1', '192.168.0.1'])
    assert cidrs.summarize_cidrs() == [ipaddress.IPv4Network('192.168.0.0/31'), ipaddress.IPv4Network('192.168.0.2/32'), ipaddress.IPv6Network('2001:db8::/127'), ipaddress.IPv6Network('2001:db8::2/128')]
