# Robotics-II-Control-Modeling-and-Learning-Labs

## Prerequisites

These packages depend on other simulation and moveit configuration files that are present in the following packages. Therefore, clone following repositories in your `catkin_workspace`:

* https://github.com/arebgun/dynamixel_motor
* https://github.com/fenixkz/ros_snake_robot.git


Moreover, install ROS Control:
```
$ sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-kinetic-ros-controllers
```
and [MoveIt](https://ros-planning.github.io/moveit_tutorials/doc/setup_assistant/setup_assistant_tutorial.html):

```
$ sudo apt install ros-melodic-moveit
```

### Laboratory 4 execution
```
$ roslaunch gazebo_robot moveit_gazebo.launch 
$ roslaunch moveit_arm_new moveit_planning_execution.launch 
```

Then run any desired script for execution:

```
$ rosrun laboratory-4 move_straight 
```
```
$ rosrun laboratory-4 draw_square 
```
```
$ rosrun laboratory-4 draw_circle 
```

Demo video is available [here](https://youtu.be/esYCAj7T4GI)


