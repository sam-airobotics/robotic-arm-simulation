from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import Command
from launch.substitutions import PathJoinSubstitution

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Package Name
    package_name = "robotic-arm_description"

    # Robot Description Path
    robot_description_path = PathJoinSubstitution([
        FindPackageShare(package_name),
        "urdf",
        "robotic-arm.xacro"
    ])

    # Robot Description
    robot_description = Command([
        "xacro ",
        robot_description_path
    ])

    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{
            "robot_description": robot_description
        }]
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    # RViz Config Path
    rviz_config_path = PathJoinSubstitution([
        FindPackageShare(package_name),
        "rviz",
        "robotic-arm.rviz"
    ])

    # RViz Node
    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_path]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz2
    ])