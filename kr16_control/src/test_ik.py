from get_ik import GetIK
from geometry_msgs.msg import PoseStamped

gik = GetIK("kr16_arm")
ps = PoseStamped()
ps.header.frame_id = 'base_link'
ps.pose.position.x = 0.1
ps.pose.orientation.w = 1.0
print (gik.get_ik(ps))