#!/bin/bash

# See http://wiki.ros.org/melodic/Installation/Ubuntu for details
set -e;
sudo apt update;
sudo apt install curl;
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list';


curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -;

sudo apt update;

sudo apt install ros-melodic-desktop-full;

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc;
source ~/.bashrc;

source /opt/ros/melodic/setup.bash;

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential;

sudo apt install python-rosdep;

sudo rosdep init;
rosdep update;

printenv | grep ROS;
# should print something like :
# ROS_ETC_DIR=/opt/ros/melodic/etc/ros
# ROS_ROOT=/opt/ros/melodic/share/ros
# ROS_MASTER_URI=http://localhost:11311
# ROS_VERSION=1
# ROS_PYTHON_VERSION=2
# ROS_PACKAGE_PATH=/opt/ros/melodic/share
# ROSLISP_PACKAGE_DIRECTORIES=
# ROS_DISTRO=melodic
