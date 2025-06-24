
 
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

 
def generate_launch_description():
 
  # Constants for paths to different files and folders
  world_file_name = 'simple.world'


  # Pose where we want to spawn the robot
 
 
  ############ You do not need to change anything below this line #############
 
  # Set the path to different files and folders.  
  pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')   

 
  world_path = os.path.join(
    get_package_share_directory('limo_gazebosim'), 
    'worlds',
    world_file_name
  )

  gazebo_models_path = os.path.join(
    get_package_share_directory('limo_gazebosim'), 
    'models'
  )
  os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path

 

  headless = LaunchConfiguration('headless')
 
  use_simulator = LaunchConfiguration('use_simulator')
  world = LaunchConfiguration('world')
  declare_world_cmd = DeclareLaunchArgument(
    name='world',
    default_value=world_path,
    description='Full path to the world model file to load')
  declare_simulator_cmd = DeclareLaunchArgument(
    name='headless',
    default_value='False',
    description='Whether to execute gzclient')
  declare_use_simulator_cmd = DeclareLaunchArgument(
    name='use_simulator',
    default_value='True',
    description='Whether to start the simulator')
 
  # Start Gazebo server
  start_gazebo_server_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
    condition=IfCondition(use_simulator),
    launch_arguments={'world': world}.items())
 
  # Start Gazebo client    
  start_gazebo_client_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')),
    condition=IfCondition(PythonExpression([use_simulator, ' and not ', headless])))
 
  # Launch the robot

 
  # Create the launch description and populate
  ld = LaunchDescription()
  ld.add_action(declare_world_cmd)
  ld.add_action(declare_simulator_cmd)
  ld.add_action(declare_use_simulator_cmd)
  # Add any actions
  ld.add_action(start_gazebo_server_cmd)
  ld.add_action(start_gazebo_client_cmd)

 
  return ld