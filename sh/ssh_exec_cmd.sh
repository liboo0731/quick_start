#!/usr/bin/expect

set timeout 600
set username [lindex $argv 0]
set remotehost [lindex $argv 1]
set command [lindex $argv 2]

spawn ssh -q -n -o StrictHostKeyChecking=no ${username}@${remotehost} "${command}"
expect {
    
}
