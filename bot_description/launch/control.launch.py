from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Path to spawn.launch.py
    spawn_launch_path = PathJoinSubstitution(
        [FindPackageShare('bot_description'), 'launch', 'spawn.launch.py']
    )
    teleop_keyboard=ExecuteProcess(
            cmd=[
                'gnome-terminal', '--', 
                'ros2', 'run', 'teleop_twist_keyboard', 'teleop_twist_keyboard',
            ],
            output='screen'
        )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(spawn_launch_path)
        ),
        
        teleop_keyboard,
    ])
