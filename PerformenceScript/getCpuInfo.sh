#!/usr/bin/env bash

init_data(){
    if [[ ! -d ${OUTPUT} ]]; then
        mkdir -p ${OUTPUT}
    fi
    if [[ ! -d ${CURRENT_OUTPUT} ]]; then
        mkdir -p ${CURRENT_OUTPUT}
    fi
    if [[ ! -d ${TEMP_FILE} ]]; then
        mkdir -p ${TEMP_FILE}
    fi
}

WORKSPACE=`pwd`
OUTPUT=${WORKSPACE}/output_cpuinfo
CURRENT_TIME=`date +%Y%m%d%H%M`
# 输出文件夹
CURRENT_OUTPUT=${OUTPUT}/${CURRENT_TIME}
# 临时文件夹
TEMP_FILE=${CURRENT_OUTPUT}/temp

init_data

packageName=${1}

function getPid() {
    adb shell ps | grep ${1} | tr -d $'\r' | awk '{print $2}' | head -n 1
}

function getCpuKer() {
    adb shell cat /proc/cpuinfo | grep "processor" > ${TEMP_FILE}/processor_count
    cpu_ker_count=`awk 'END{print NR}' ${TEMP_FILE}/processor_count`
    echo ${cpu_ker_count}
#    rm -r ${TEMP_FILE}/processor_count
}

function processCpuTime() {
    adb shell cat /proc/${1}/stat > ${TEMP_FILE}/process_cpu_time
    utime=$(cat ${TEMP_FILE}/process_cpu_time | awk '{print $14}')
    stime=$(cat ${TEMP_FILE}/process_cpu_time | awk '{print $15}')
    cutime=$(cat ${TEMP_FILE}/process_cpu_time | awk '{print $16}')
    cstime=$(cat ${TEMP_FILE}/process_cpu_time | awk '{print $17}')
    result=`expr ${utime} + ${stime} + ${cutime} + ${cstime}`
    echo ${result}
#    rm -r ${TEMP_FILE}/process_cpu_time
}

function totalCpuTime() {
    adb shell cat /proc/stat > ${TEMP_FILE}/total_cpu_time
    cat ${TEMP_FILE}/total_cpu_time | grep "cpu" | head -n 1 > ${TEMP_FILE}/total_cpu
    user=$(cat ${TEMP_FILE}/total_cpu | awk '{print $2}')
    nice=$(cat ${TEMP_FILE}/total_cpu | awk '{print $3}')
    system=$(cat ${TEMP_FILE}/total_cpu | awk '{print $4}')
    idle=$(cat ${TEMP_FILE}/total_cpu | awk '{print $5}')
    iowait=$(cat ${TEMP_FILE}/total_cpu | awk '{print $6}')
    irq=$(cat ${TEMP_FILE}/total_cpu | awk '{print $7}')
    softirq=$(cat ${TEMP_FILE}/total_cpu | awk '{print $8}')
    result=`expr ${user} + ${nice} + ${system} + ${idle} + ${iowait} + ${irq} + ${softirq}`
    echo ${result}
}

pid=`getPid ${packageName}`
echo ${pid}

cpu_ker=`getCpuKer`
echo ${cpu_ker}

#process_cpu_time=`processCpuTime ${pid}`
#echo ${process_cpu_time}
#
#totalCpuTime=`totalCpuTime`
#echo ${totalCpuTime}
#sleep 1
#totalCpuTime=`totalCpuTime`
#echo ${totalCpuTime}

function getCpuRate() {
    process_cpu_time1=`processCpuTime ${1}`
    total_cpu_time1=`totalCpuTime`
    sleep 1s
    process_cpu_time2=`processCpuTime ${1}`
    total_cpu_time2=`totalCpuTime`
    process_cpu_time3=$(( ${process_cpu_time2} - ${process_cpu_time1} ))
    total_cpu_time3=$(( ${total_cpu_time2} - ${total_cpu_time1} ))
    cpu_rate=$(bc <<< "scale=3;(${process_cpu_time3}/${total_cpu_time3})*${2}*100")
    result=$(echo "scale=0;${cpu_rate}/1" | bc -l)
    echo "cpu rate"
    echo ${result}
}

#cpu_rate=`getCpuRate ${pid} ${cpu_ker}`
#echo ${cpu_rate}

getCpuRate ${pid} ${cpu_ker}
