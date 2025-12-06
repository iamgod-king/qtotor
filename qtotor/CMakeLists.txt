cmake_minimum_required(VERSION 3.0.2)
project(qtotor)

# 查找catkin和相关包
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	geometry_msgs
	sensor_msgs
	nav_msgs
	tf
	controller_manager
	joint_state_controller
	robot_state_publisher
	xacro
	urdf
)

# 添加Gazebo依赖
find_package(gazebo REQUIRED)
find_package(Boost REQUIRED COMPONENTS thread system)

# 设置包含目录
include_directories(
	include
	${catkin_INCLUDE_DIRS}
	${GAZEBO_INCLUDE_DIRS}
	${Boost_INCLUDE_DIRS}
)

# 链接库目录
link_directories(
	${catkin_LIBRARY_DIRS}
	${GAZEBO_LIBRARY_DIRS}
)

# catkin包配置
catkin_package(
  CATKIN_DEPENDS 
    roscpp 
    rospy 
    std_msgs 
    geometry_msgs 
    sensor_msgs 
    nav_msgs 
    tf
    controller_manager
    joint_state_controller
    robot_state_publisher
    xacro
    urdf
	LIBRARIES ${PROJECT_NAME}
	DEPENDS 
		Boost
)

# 安装Python脚本
catkin_install_python(PROGRAMS 
	scripts/motor_controller.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


# 安装配置文件
install(DIRECTORY 
	launch/
	config/
	urdf/
	meshes/
	rviz/
	worlds/
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# 安装可执行文件
install(PROGRAMS 
	scripts/motor_controller.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)