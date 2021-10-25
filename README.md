# R3-SoftwareTask2-DixPaulson

Both the program files are incomplete. There were problems trying to send the real time data from keyboard to the server program continuosly. I had issues tryin to come up with the server program as well.
The idea was to gather input from the user through keyboard. The first set of input determines the speed of the motors raging from 0 to 5
For example a speed setting of 1 would mean a value of 51 incrementing by 51 to a maximum value of 255

Once that input is recieved using the keys a,s,w,d the rover is controlled continuously. The client program sends the input received from the user to the server program

The server program interprets the input received and sends the output to the motors. When the server program recieves an input corresponding to the speed setting, it converts the output using pulse width modulation. For example, a speed setting of 1 would be changed to a value of 51 and it increments by a value of 51.

speed setting 0 = 0

speed setting 1 = 51

speed setting 2 = 102

speed setting 3 = 153

speed setting 4 = 204

speed setting 5 = 255

Then depending on the input received from the client server, the direction of the motors are determined. When the input 'w' is received, all the motors are in forward motion, while the input 's' turns them all in the reverse direction. 'a' turns the left 2 motors in the reverse direction and the two right motors in the forward direction. 'd'  turns the two left motors in the forward direction and the two right motors in the reverse direction.
