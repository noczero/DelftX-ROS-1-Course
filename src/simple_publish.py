import rospy
from std_msgs.msg import String


def simple_publisher():
    # init publisher
    pub = rospy.Publisher('topic_1', String, queue_size=10)

    # init node
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(10)  # 10 Hz

    # define msg
    topic1_content = "My first ROS topic!"

    # Do looping while rospy is not shutdown
    while not rospy.is_shutdown():
        # start publish message
        pub.publish(topic1_content)
        # give delay
        rate.sleep()


if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInternalException:
        pass
