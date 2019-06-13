#!/bin/bash

function run_module {
    module_name=$1
    rm -f /tmp/${module_name}
    nohup python3 ${module_name}.py > ${module_name}.out &
}

curr_dir=$(pwd)
cd $DOOR_HOME

run_module worker
run_module reader

cd curr_dir