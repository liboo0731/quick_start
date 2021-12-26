#!/bin/bash

[root@localhost liboo]# bash echoip.sh
192.168.1.2
[root@localhost liboo]# ssh root@192.168.1.3 -C "/bin/bash" < echoip.sh
root@192.168.1.3's password:
192.168.1.3
[root@localhost liboo]#


# Reference link
https://backreference.org/2011/08/10/running-local-script-remotely-with-arguments/
