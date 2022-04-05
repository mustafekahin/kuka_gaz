from get_fk import GetFK
from sensor_msgs.msg import JointState
gfk = GetFK("kr16_arm")
js = JointState()

js.header.frame_id = 'baselink'

print (gfk.get_fk(js))
print(js)