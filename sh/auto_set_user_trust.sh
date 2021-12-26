#!/bin/bash

remotehost=$1
password=$2

cd ~
[ -f ".ssh/id_rsa*" ] || echo -e "\n" |ssh-keygen -t rsa -P ''

expect -c "
spawn ssh-copy-id -i .ssh/id_rsa.pub ${remotehost}
expect {
    \"*yes/no*\" { send \"yes\n\"; exp_continue }
    \"*assword*\" { send \"${password}\n\"; exp_continue }
    eof { send_user \"eof\" }
}
"
