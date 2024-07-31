import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import getpass

def check_rdp_connection(ip, username, password, ntlm_hash):
    
    if ntlm_hash:
        command = [
            './xfreerdp_expect.sh',
            ip,
            username,
            '',
            ntlm_hash
        ]
    else:
        command = [
            './xfreerdp_expect.sh',
            ip,
            username,
            password,
            ''
        ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return f"{ip}: Connection timeout"

def main(ip_list_file, username, password, ntlm_hash):
    # IP listesini oku
    with open(ip_list_file, 'r') as file:
        ip_addresses = [line.strip() for line in file.readlines()]

    # Thread havuzu oluştur
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Her IP için bağlantı kontrolü yap
        futures = [executor.submit(check_rdp_connection, ip, username, password, ntlm_hash) for ip in ip_addresses]

        # Sonuçları sırayla yazdır
        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multiple RDP connection check with xfreerdp')
    parser.add_argument('-i', '--iplist', required=True, help='IPs file path')
    parser.add_argument('-u', '--username', required=True, help='Username')
    parser.add_argument('-p', '--password', help='Password')
    parser.add_argument('--ntlm', help='NTLM Hash')

    args = parser.parse_args()

    if not args.password and not args.ntlm:
        args.password = getpass.getpass("Password: ")

    main(args.iplist, args.username, args.password, args.ntlm)
