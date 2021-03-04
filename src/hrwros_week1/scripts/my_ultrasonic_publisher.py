#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Node to publish to a string topic.

import rospy
from std_msgs.msg import String

# import new message
from hrwros_msgs.msg import UltrasonicSensor

# import ulitilies
from hrwros_utilities.sim_sensor_data import distSensorData as getSensorData

def simplePublisher():
    ult_publish = rospy.Publisher('ultrasonic', UltrasonicSensor, queue_size = 10)
    rospy.init_node('ultrasonic_publisher', anonymous=False)
    rate = rospy.Rate(1)

    # create a new ultrasonic object
    ultrasonic_info = UltrasonicSensor()

    # fill the header of range data type, http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Range.html
    ultrasonic_info.sensor_data.header.stamp = rospy.Time.now()
    ultrasonic_info.sensor_data.header.frame_id = 'distance_sensor_frame'

    # fill the range data type information
    ultrasonic_info.sensor_data.radiation_type = ultrasonic_info.sensor_data.ULTRASOUND
    ultrasonic_info.sensor_data.field_of_view = 0.5
    ultrasonic_info.sensor_data.min_range = 0.002
    ultrasonic_info.sensor_data.max_range = 5.000

    # fill the info about ultrasonic that we defined
    ultrasonic_info.maker_name = "Zero-Inside"
    ultrasonic_info.part_number = 00000
    ultrasonic_info.sensor_type = "Analog"

    while not rospy.is_shutdown():

        # feed .range to fake sensor data function
        ultrasonic_info.sensor_data.range = getSensorData(ultrasonic_info.sensor_data.radiation_type,
                                                          ultrasonic_info.sensor_data.min_range,
                                                          ultrasonic_info.sensor_data.max_range)

        ult_publish.publish(ultrasonic_info)
        rospy.loginfo("publish new message!")
        rospy.loginfo(ultrasonic_info)
        rate.sleep()

if __name__ == '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
