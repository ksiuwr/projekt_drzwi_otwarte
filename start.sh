#!/bin/bash

# no idea why, but people on stack say so...
script /dev/null 

cd $DOOR_HOME
rm -f /tmp/worker
rm -f /tmp/adder
screen -S worker -d -m python3 worker.py
screen -S reader -d -m python3 reader.py
