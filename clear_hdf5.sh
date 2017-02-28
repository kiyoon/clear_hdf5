#!/bin/bash

ls *.hdf5 -l | awk '{print $9}' >> result.log
hdf5=$(find . -name "*.hdf5")

max_val_acc=0
max_file=''
while read line
do
	val_acc=$(echo "$line" | awk -F- '{print $5}' | awk -F_ '{print $1}' | sed -e 's/\.//')
	if [ "$val_acc" -gt "$max_val_acc" ]
	then
		max_val_acc="$val_acc"
		max_file="$line"
	elif [ "$val_acc" -eq "$max_val_acc" ]
	then
		max_file="$max_file
$line"
	fi
done <<< "$hdf5"

echo "Remove hdf5 files except:"
echo "$max_file"

read -p "Are you sure? (y/n) " -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
	remove="$hdf5"
	while read line
	do
		remove=$(echo "$remove" | grep -v "$line")
	done <<< "$max_file"

	echo "$remove" | xargs rm
fi
