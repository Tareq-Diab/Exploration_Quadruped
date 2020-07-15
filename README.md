# Inroduction
A quadruped that uses 8 sg90 servos , the robot body itself was 3d printed from an opensource design on thingvese , the controlling program was written using micropython on an esp8266 which has a wifi interface that was used to communicate with a laptop in order to use it's interface to controll the robot movement . 
In the robot layer subroutine was written for all the movements , which was 1-moving forward  2-turning left 3-turning write and a motor check routine was written to ensure that all motors are conected and caliprated corectly.

On the pc part the interfacing is done using pygame keyboard interface that listen to arrow key strockes and sends the corresponding command via a tcp connection using Socket liberary.
