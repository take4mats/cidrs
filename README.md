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

## Testing

- Install pytest
    ```sh
    pip install pytest
    ```

- Execute
    ```sh
    pytest
    ```