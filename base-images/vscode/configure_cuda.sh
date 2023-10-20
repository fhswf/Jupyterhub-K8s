#!/bin/bash
#########
# checks gpu availabilty and sets env CUDA_VISBILE_DEVICE to use most sutiable device in case more are avaiable 
##########
kicluster_configure_cmd=nvidia-smi
if [[ $(type -P "$kicluster_configure_cmd") ]] ; then
    kicluster_configure_mode=(`nvidia-smi --format=csv --query-gpu=mig.mode.current | tail --lines=+2`)
    if  [ ${#mode[@]} == 0 ] ; then
       echo "WARNING: no cuda devices found";
    else
        ## mig modes for cuda devices can be: [Disabled|Enabled]
        kicluster_configure_migs=(`nvidia-smi --format=csv --query-gpu=mig.mode.current,uuid | tail --lines=+2 | grep Enabled | awk '{print $2}'`);
        kicluster_configure_gpus=(`nvidia-smi --format=csv --query-gpu=mig.mode.current,uuid | tail --lines=+2 | grep Disabled | awk '{print $2}'`);
        kicluster_configure_uuids=();
        for kicluster_configure_mig in "${kicluster_configure_migs[@]}" 
        do
          kicluster_configure_uuid=(`nvidia-smi -L | cat - <(echo "EOF")  | grep -A10  "${kicluster_configure_mig}" | tail --lines=+2 |  grep  -B10 -E 'GPU|EOF' --max-count=1 | head --lines=-1 | awk '{print substr($6, 1, length($6)-1)}'`);
          kicluster_configure_uuids+=("${kicluster_configure_uuid[@]}")
        done;
        kicluster_configure_uuids+=("${kicluster_configure_gpus[@]}")
        # pip install nvidia-ml-py
        kicluster_configure_target_device=`python -c "  
import sys
ids = sys.argv[1:]
import pynvml as nv
import operator
nv.nvmlInit()
lst={}
for id in ids:
    d = nv.nvmlDeviceGetHandleByUUID(id)
    m = nv.nvmlDeviceGetMemoryInfo(d)
    n = nv.nvmlDeviceGetName(d)
    i = nv.nvmlDeviceGetIndex(d)
    m.total
    m.used
    m.free   
    lst[i] = (m.used/1024)/1024
s_lst = dict(sorted(lst.items(), key=operator.itemgetter(1)))
for k,v in s_lst.items():
    print(str(k))
    break
" ${kicluster_configure_uuids[@]} `
    # sorted list
    fi
    echo "Setting CUDA Device to $kicluster_configure_target_device"
    export CUDA_VISIBLE_DEVICES=$kicluster_configure_target_device
fi;

