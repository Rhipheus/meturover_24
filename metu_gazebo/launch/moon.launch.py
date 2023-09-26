import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_path = get_package_share_directory("metu_gazebo")

    gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_path, "launch", "gazebo.launch.py")
        ),
        launch_arguments={"world": os.path.join(
            pkg_path, "worlds", "moon.world"),
            #"initial_pose_x":"-11.0",
            #"initial_pose_y":"-11.5",
            #"initial_pose_z":"0.3",
            #"initial_pose_yaw": "3.1"
            }.items()
    )

    ld = LaunchDescription()
    ld.add_action(gazebo_cmd)

    return ld
