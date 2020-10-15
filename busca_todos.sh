#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
for file in Entries/*
do
    echo ""
    echo "$file"
    echo ""
    python3 __main__.py "-algoritmo" $1 "-entrada" $file
done