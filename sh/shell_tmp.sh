#!/bin/bash

[ "$UID" -ne 0 ] && echo "Please user root exec!" && exit 1

cur_path=$(dirname $(readlink -f $0))
log_file=${cur_path}/shell_tmp.log

function exec_a()
{
    [ -f "${cur_path}/step_dir/exec_a.flag" ] && return 0

    # do something
    
    touch ${cur_path}/step_dir/exec_a.flag
    return 0
}

function exec_b()
{
    [ -f "${cur_path}/step_dir/exec_b.flag" ] && return 0

    # do something

    touch ${cur_path}/step_dir/exec_b.flag
    return 0
}

function main()
{
    echo "Start ..."
    mkdir -p ${cur_path}/step_dir    

    exec_a
    [ $? -ne 0 ] && return 1

    exec_b
    [ $? -ne 0 ] && return 1

    rm -rf ${cur_path}/step_dir
    echo "End ..."
}

main "$@" 2>&1 |tee -a ${log_file}
