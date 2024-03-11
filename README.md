# CIDRs - CIDR block utility

This is a simple utility to work with CIDR blocks. It can be used to check if an IP address is in a CIDR block, or to generate a list of IP addresses in a CIDR block.

## Installation

- Install Python 3.x

## Usage

- Create a list of CIDR blocks.
  - Both IP address and CIDR block styles are also supported.
  - Both IPv4 and IPv6 are supported.
  - Refer to the `example.txt` file for an example of the input file format.

- To summarize the CIDR blocks, execute the following command:
    ```sh
    cat example.txt | python summarize.py
    ```

### Detailed execution demonstration

Create a list of CIDR blocks.

```sh
(cat << EOF
192.168.0
2001::db8::2

172.16.0.0
2001:db8::

172.17.0.0/24
172.17.1.0/24
2001:db8:dead::/64
2001:db8:dead:1::/64

172.18.0.1
172.18.0.0/24
2001:db8:face::1
2001:db8:face::/64
EOF
) > demo.txt
```

Execute the following command:

```sh
cat demo.txt | python summarize.py
```

The output will be:

```sh

Input Warnings:
'192.168.0' does not appear to be an IPv4 or IPv6 network
'2001::db8::2' does not appear to be an IPv4 or IPv6 network
'' does not appear to be an IPv4 or IPv6 network
'' does not appear to be an IPv4 or IPv6 network
'' does not appear to be an IPv4 or IPv6 network

Summarized CIDRs:
172.16.0.0/32
172.17.0.0/23
172.18.0.0/24
2001:db8::/128
2001:db8:dead::/63
2001:db8:face::/64
```

NOTE: The input warnings are due to the fact that the input file contains invalid CIDR blocks or blank lines.  You can remove them from the input file and then will get clean results.

## Testing

- Install pytest
    ```sh
    pip install pytest
    ```

- Execute
    ```sh
    pytest
    ```