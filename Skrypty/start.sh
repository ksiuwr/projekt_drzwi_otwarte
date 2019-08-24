#!/bin/bash

function run_module {
    module_name=$1
    rm -f /tmp/${module_name}
    nohup python3 ${module_name}.py > ${module_name}.out 2> ${module_name}.err &
}

curr_dir=$(pwd)
cd $DOOR_HOME/Kod

run_module worker
run_module reader

cd $curr_dir