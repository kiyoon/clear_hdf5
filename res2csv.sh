#!/bin/bash

cmd='paste -d ,'
while read line
do
	out_path=$(dirname "$line")
	out_path="$out_path/val_acc.csv"

	cat "$line" | awk -F- '{print $NF}' | awk -F_ '{print $1}' > "$out_path"

	cmd="$cmd '$out_path'"
done <<< "$(find . -name "result.log" | sort)"

cmd="$cmd > val_accs.csv"
echo "$cmd"
eval "$cmd"

