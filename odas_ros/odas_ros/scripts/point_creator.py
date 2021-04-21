#!/usr/bin/env python

import rospy
from odas_msgs.msg import Tracked_source
from odas_msgs.msg import Tracked_sources
from geometry_msgs.msg import PointStamped


class PointCreator(object):
    def __init__(self):
        self.goal = None

        rospy.init_node('point_creator')
        self.odas_sub = rospy.Subscriber('sounds/tracked_sources', Tracked_sources, self.odas_cb)
        self.point_pubs = [
            rospy.Publisher('point1', PointStamped, queue_size=1),
            rospy.Publisher('point2', PointStamped, queue_size=1),
            rospy.Publisher('point3', PointStamped, queue_size=1),
            rospy.Publisher('point4', PointStamped, queue_size=1)]
        rospy.spin()

    def odas_cb(self, odas_msg):
        point_msg = PointStamped()
        point_msg.header = odas_msg.header
        point_msg.header.frame_id = "odas"

        for i in range(4):
            point_msg.point.x = odas_msg.sources[i].x
            point_msg.point.y = odas_msg.sources[i].y
            point_msg.point.z = odas_msg.sources[i].z
            
            self.point_pubs[i].publish(point_msg)

if __name__ == "__main__":
    PointCreator()
