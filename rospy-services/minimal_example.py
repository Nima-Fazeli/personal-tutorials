import rospy
import std_srvs


class Example:
    def __init__(self):
        # Initialize the ros node
        rospy.init_node("example_server")
        
        # service
        self.exampleSrv = rospy.Service('example', std_srvs.srv.Empty, self.handle_example_server)

    def handle_example_server(self):
        # do something


if __name__ == "__main__":
    try:
        v = Example()
        rospy.loginfo("[Example] - Example service running ...")
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("[Example] - Example service stopped.")
        pass
