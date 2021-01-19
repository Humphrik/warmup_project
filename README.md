# CMSC 206 Warmup Project Writeup

## Part 1: Driving in a Square.
#### High-Level Approach
For this section of the project, the code proved to relatively straightforward, aside from the challenge of turning 90 degrees. Originally, I intended to utilize the odometer built into the turtle, as such a sensor would accurately keep track of the robot's turning position. However, I eventually decided to simply turn for a specific amount of time, as will be discussed shortly. Once a simple way of turning and moving the robot was implemented, the behavior was only a matter of alternating between straight movement and LH turns in a loop.
#### Code Structure
The structure of "move_in_square.py" is somewhat similar to the object oriented files developed during lecture two of class. It consists of a primary class, titled ROS, which contains the entire behavior of the robot. The program utilizes a single publisher on topic cmd_vel, and has no subscribers.
The run() function of ROS consists primarily of a loop, which alternates between sleeping (via rospy.sleep()) and moving (via a custom function named move().) The move() function in ROS takes two Vector3 arguments and simply publishes new Twist arguments (position and rotation respectively) to the cmd_vel topic.
#### Gif of Behavior
![Put gif here!](move_in_square.gif)
(I'll make it a little smaller next time.)
#### Challenges
As mentioned previously, the largest challenge faced in the program was reliably turning 90 degrees so to make a square pattern. However, this matter was somewhat simplified upon the discovery that the robot's rotational velocity is given in radians per second. Therefore, rotating pi/2 radians could be done by setting the z-axis rotational velocity to pi/2/x, where x is the duration of the turn. Ideally, x should be high to minimize the time spent accelerating by the robot.
Another problem faced during this section of the project was the "skidding" of the robot whenever it stopped to turn. Initially, my turn command set the linear velocity of the robot to 0 before increasing its rotational velocity. However, this sudden brake and turn proved to be unreliable, and could cause the robot to turn too much or too little. To solve this matter, I ensured that the linear x velocity remained constant throughout the behavior, resulting in wider, but more accurate turns.
#### Future Improvements
In the future, I would like to utilize the odometer to increase the precision of my robots linear and rotational movements. While I was able to gain some understanding of how the odometer transfers data to the odom topic, the process was simply too time consuming for this project. Namely, the move_in_square behavior would need to collect the z-axis rotational position of the robot, convert it into radians (inverse sine function?) and calculate the new target position for after the turn. Still, I expect that the odometer will play a critical role in future projects.
#### Key Takeaways
As the name "warmup_project" implies, I am still getting used to the ROS process and the interactions between simulator and code. In a way, this project is a lesson on the more fundamental aspects of ROS.
