#!/bin/sh

MOTION_TARGET_DIR=/var/lib/motion
DIR_NAME=`date "+%Y%m%d-%H%M%S"`

mkdir ${MOTION_TARGET_DIR}/${DIR_NAME}
mv ${MOTION_TARGET_DIR}/*.jpg ${MOTION_TARGET_DIR}/${DIR_NAME}
