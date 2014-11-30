import math

# Speed of Light in m/s
c = 299792458

# Elapsed Time (given acceleration and proper time)
def terraTime1(accel, properTime):
	return c/accel * math.sinh(a*properTime/c)

# Elapsed Time (given acceleration and distance)
def terraTime2(accel, dist):
	return math.sqrt(math.pow(dist/c, 2) + (2*dist/a))

# Distance Travelled (given acceleration and proper time)
def dist1(accel, properTime):
	return math.pow(c, 2)/accel * (math.cosh(accel*properTime/c) - 1)

# Distance Travelled (given acceleration and terra time)
def dist2(accel, terraTime):
	return math.pow(c, 2)/accel * (math.sqrt((1 + math.pow((accel*terraTime/c), 2)) - 1))

# Final Velocity (given acceleration and proper time)
def vFinal1(accel, properTime):
	return c * math.tanh(accel * properTime/c)

# Final Velocity (given acceleration and terra time)
def vFinal2(accel, terraTime):
	return (accel * terraTime) / math.sqrt(1 + math.pow(a*terraTime/c, 2))