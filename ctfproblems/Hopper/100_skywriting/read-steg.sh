#!/bin/bash
for filename in static/*.wav; do
    echo "----------------------------------------------------------------------"
    echo $filename
    ent -b "$filename"
done
