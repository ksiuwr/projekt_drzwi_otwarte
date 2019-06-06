#!/bin/bash

cd $DOOR_HOME
screen -X -S worker quit
screen -X -S reader quit
