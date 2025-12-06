#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray, Float64
import math

class MotorController:
    def __init__(self):
        rospy.init_node('motor_controller')
        
        # 四个电机的发布器
        self.lf_pub = rospy.Publisher('/qtotor/lf_joint_velocity_controller/command', Float64, queue_size=10)
        self.lb_pub = rospy.Publisher('/qtotor/lb_joint_velocity_controller/command', Float64, queue_size=10)
        self.rb_pub = rospy.Publisher('/qtotor/rb_joint_velocity_controller/command', Float64, queue_size=10)
        self.rf_pub = rospy.Publisher('/qtotor/rf_joint_velocity_controller/command', Float64, queue_size=10)
        
        # 订阅统一命令
        rospy.Subscriber('/qtotor/command/motor_speed', Float64MultiArray, self.command_callback)
        
        rospy.loginfo("电机控制器已启动，等待命令...")
        rospy.spin()
    
    def command_callback(self, msg):
        if len(msg.data) >= 4:
            # 发布到各个电机控制器
            self.lf_pub.publish(Float64(msg.data[0]))
            self.lb_pub.publish(Float64(msg.data[1]))
            self.rb_pub.publish(Float64(msg.data[2]))
            self.rf_pub.publish(Float64(msg.data[3]))
            
            rospy.loginfo("设置电机速度: LF=%.1f, LB=%.1f, RB=%.1f, RF=%.1f rad/s", 
                         msg.data[0], msg.data[1], msg.data[2], msg.data[3])
        else:
            rospy.logwarn("需要4个速度值，收到 %d 个", len(msg.data))

if __name__ == '__main__':
    try:
        controller = MotorController()
    except rospy.ROSInterruptException:
        pass