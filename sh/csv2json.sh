#!/bin/bash

csv_file=$1

title_arr=($(cat ${csv_file} |awk 'NR==1{gsub(/,/," ");print}'))
csv_val=$(cat ${csv_file} |awk 'NR>1{print}')

for row_str in ${csv_val}
do
	row_arr=(${row_str//,/ })
	kv_str=""
	for i in ${!title_arr[@]}
	do
	kv_str="${kv_str}\"${title_arr[${i}]}\":\"${row_arr[${i}]}\","
	done
	json_str="${json_str}{${kv_str%,}},"
done
echo "[${json_str%,}]"

