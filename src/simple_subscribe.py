## Node to subscribe to a string and print the string on terimnal

import rospy
from std_msgs.msg import String


# define callback function
def string_listener_callback(data):
    rospy.loginfo("The contents of topics {}".format(data.data))


def string_listener():
    # init node
    rospy.init_node("node_2", anonymous=False)

    # define subscriber
    rospy.Subscriber("topic_2", String, string_listener_callback)

    # keeps program from exiting unttil this node is stropped
    rospy.spin()


if __name__ == '__main__':
    string_listener()
