# RDP Connection Checker

## Description

The RDP Connection Checker project is designed to automate the process of connecting to a remote desktop using RDP (Remote Desktop Protocol) and verifying the connection. It uses a combination of Python and an Expect script to facilitate the connection process.

## How to use

This tool can be used to:

1. Automatically connect to multiple remote desktop using RDP.
2. Verify if the connection was successful, failed due to authentication, or failed due to connection issues.

## Requirements

- Python 3.x
- `expect` (Install via `sudo apt-get install expect`)
- `xfreerdp` (Install via `sudo apt-get install freerdp2-x11`)

## Setup

1. Ensure the `xfreerdp_expect.sh` script has execute permissions:

    ```sh
    chmod +x xfreerdp_expect.sh
    ```

2. Run the main script with the these arguments:

    ```sh
    usage: main.py [-h] -i IPLIST -u USERNAME [-p PASSWORD] [--ntlm NTLM]

    Multiple RDP connection check with xfreerdp

    optional arguments:
      -h, --help            show this help message and exit
      -i IPLIST, --iplist IPLIST
                            IPs file path
      -u USERNAME, --username USERNAME
                            Username
      -p PASSWORD, --password PASSWORD
                            Password
      --ntlm NTLM           NTLM Hash
    ```

    - `<ip>`: The IP address of the remote desktop.
    - `<username>`: The username for the remote desktop.
    - `<password>`: The password for the remote desktop. Leave empty if using NTLM hash. (optional) 
    - `<ntlm_hash>`: The NTLM hash for the remote desktop authentication. Leave empty if using a password. (optional)

## Example

Password authentication:

```sh
python3 main.py -i ip_list_file.txt -u myusername
python3 main.py -i ip_list_file.txt -u myusername -p mypassword
python3 main.py -i ip_list_file.txt -u myusername --ntlm myntlm
```
