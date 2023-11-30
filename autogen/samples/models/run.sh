#!/bin/bash
# Read each line from 'list.txt' and execute the command
while IFS= read -r directory; do
  echo $directory
done < list.txt
