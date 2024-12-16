#!/usr/bin/env bash

# Ensure uncompyle6 is installed and in PATH before running:
# pip install uncompyle6

# Loop through all .pyc files in the current directory
for pyc_file in *.pyc; do
    # Check if the file actually exists (in case no .pyc files are found)
    if [ -f "$pyc_file" ]; then
        # Extract the base name by removing the .pyc extension
        base_name="${pyc_file%.pyc}"

        # Run uncompyle6 and redirect output to a .py file
        uncompyle6 "$pyc_file" > "${base_name}.py"

        # Optional: Print a message indicating that the file was processed
        echo "Decompiled $pyc_file to ${base_name}.py"
    fi
done

