#
#
import os
import sys
import rospy
from std_msgs.msg import Int16

sys.path.append(os.path.dirname(__file__)+"../")
import vl53l0x

class tof_vl53:
  def __init__(self):
    self.tof=vl53l0x.VL53L0X()
    self.pub_ = rospy.Publisher('tof_distance', Int16, queue_size=10)
    self.tof.start_ranging(1)

  def get_distance(self):
    return self.tof.get_distance()

  def publish(self, val):
    msg=Int16(data=val)
    self.pub_.publish(msg)
    return

if __name__ == '__main__':
  rospy.init_node("vl53")
  node=tof_vl53()

  r=rospy.Rate(19)
  while not rospy.is_shutdown():
    distance = node.get_distance()
    node.publish(distance)
    r.sleep()
  

