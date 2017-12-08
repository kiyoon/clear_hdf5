#!/bin/bash

# clear the hdf5 model except lowest training loss and hightest training accuracy

ls *.hdf5 -l | awk '{print $9}' >> result.log
hdf5=$(find . -mindepth 1 -maxdepth 1 -name "*.hdf5")

min_loss=999999
max_acc=0
exclude_file_acc=''
exclude_file_loss=''
while read line
do
	loss=$(echo "$line" | awk -F- '{print $2}' | awk -F_ '{print $1}' | sed -e 's/\.//')
	acc=$(echo "$line" | awk -F- '{print $3}' | awk -F_ '{print $1}' | sed -e 's/\.//')
	if [ "$acc" -gt "$max_acc" ]
	then
		max_acc="$acc"
		exclude_file_acc="$line"
	elif [ "$acc" -eq "$max_acc" ]
	then
		exclude_file_acc="$exclude_file_acc
$line"
	fi

	if [ "$loss" -lt "$min_loss" ]
	then
		min_loss="$loss"
		exclude_file_loss="$line"
	elif [ "$loss" -eq "$min_loss" ]
	then
		exclude_file_loss="$exclude_file_loss
$line"
	fi
done <<< "$hdf5"

echo "Remove hdf5 files except:"
echo "$exclude_file_acc"
echo
echo "$exclude_file_loss"

read -p "Are you sure? (y/n) " -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
	remove="$hdf5"
	while read line
	do
		remove=$(echo "$remove" | grep -v "$line")
	done <<< "$exclude_file_acc"

	while read line
	do
		remove=$(echo "$remove" | grep -v "$line")
	done <<< "$exclude_file_loss"

	echo "$remove" | xargs rm
fi
