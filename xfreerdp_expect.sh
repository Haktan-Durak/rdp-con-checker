#!/usr/bin/expect -f

set timeout -1
set ip [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
set ntlm_hash [lindex $argv 3]

if { $ntlm_hash != "" } {
    set cmd "xfreerdp /u:$username /pth:$ntlm_hash /v:$ip +clipboard +sec-nla"
} else {
    set cmd "xfreerdp /u:$username /p:$password /v:$ip +clipboard +sec-nla"
}

spawn {*}$cmd
expect {
    "Do you trust" { send "yes\r"; exp_continue }
    "connected to" { puts "$ip: Connection success"; exit 0 }
    "Authentication failure" { puts "$ip: Authentication failed"; exit 1 }
    "unable to connect" { puts "$ip: Connection failed"; exit 1 }
    eof { puts "$ip: Unknown error"; exit 1 }
}
