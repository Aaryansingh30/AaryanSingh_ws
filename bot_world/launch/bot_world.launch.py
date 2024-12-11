import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription , ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    world_name="bot_world"
    robot_name="AaryanSingh_bot"
    package_name="bot_description"

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rviz.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Launch Gazebo 
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': os.path.join(get_package_share_directory(world_name), 'worlds', 'bot_world.world')}.items()
    )

    # Spawn robot into Gazebo 
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', robot_name,
            '-topic', '/robot_description'
        ],
        output='screen'
    )

        #Run the teleop_keyboard in new terminal
    teleop_keyboard =  ExecuteProcess(
            cmd=['gnome-terminal', '--','ros2', 'run', 'teleop_twist_keyboard', 'teleop_twist_keyboard',
            ],
            output='screen'
        )

    return LaunchDescription([
        rviz_launch,
        gazebo_launch,
        spawn_entity,
        teleop_keyboard,
    ])
