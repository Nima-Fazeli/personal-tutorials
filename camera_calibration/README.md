# How to calibrate two sets of 3D poses:

Assume you have 2 sets of 3D poses (can be from a camera and a robot, or two cameras for example).

Let's call these sets A and B. If we want to find the rigid transformation between the two we can call `rigid_transformation_3D.py`.

We can collect this data from Apriltags for example.

# TODO:

Write python script to read apriltag or apriltag board and store the data in 3xN matrix/matrices. This will be used in the calibration of camera w.r.t. robot or two cameras.
