# HamRadio360_SWR_analyzer_control_KB5EZ.py
# Sample HR360 build project SWR analyzer interface 

# by Rob Suggs/KB5EZ 18 Jan 2017, modified 23 Jan 2017
# open source and free to use as you wish

# info on Serial package at http://pyserial.readthedocs.io/en/latest/examples.html 
# pyserial 2.7 download at https://pypi.python.org/pypi/pyserial/2.7 
# installation instructions http://pyserial.readthedocs.io/en/latest/pyserial.html#installation
# other packages bundled with Python(X,Y) distribution

import serial # serial interface package
import numpy as np # numerical analysis package
import matplotlib.pyplot as plt # plotting package

ser = serial.Serial('/dev/ttyACM0', baudrate = 115200)
# ser port (my COM10) is the Arduino virtual serial port
# change port to /dev/ttyACM0 for Linux
# baud rate is set in the Arduino sketch

band = 20 # pick the band of interest

comment = 'mMA5B_HR360_analyzer' # this will be in figure title and file name

num_steps = 100 # number of samples across the band, 1 more for upper band edge

# band edges
# HR360 Analyzer expects the numbers in Hz
start = {10:28000000,12:24890000,15:21001000,17:18068000,20:14000000,
         30:10100000,40:7000000,80:3500000,160:1800000}
         
end   = {10:29700000,12:24990000,15:21450000,17:18168000,20:14350000,
         30:10150000,40:7300000,80:4000000,160:2000000}     

# build the commands for the SWR analyzer

start_freq = "%08d" % start[band] + "A"
end_freq   = "%08d" % end[band]   + "B"
steps      = "%04d" % num_steps   + "N"

# for single freq - not implemented
#freq    = "%08d" % freq_single + "C"

print 'Commands ', start_freq, end_freq, steps

ser.write(start_freq) # set start frequency
ser.write(end_freq)   # set end freq
ser.write(steps)      # set number of steps
ser.write("S")        # start sweep

for i in range(num_steps): # setup loop over number of points
    in_string = ser.readline() # read a line from the Arduino
#    print 'index =',i, "string = ",in_string # check the read

# parse the input string to obtain freq and swr, convert to MHz and swr
# these values could be loaded in arrays for fancy plot and analysis
    freq_swr_string = in_string.split(",") # break the comma-separated input string
    freq_cur = np.float(freq_swr_string[0])/1.e6
    vswr     = np.float(freq_swr_string[1])/1.e3 # voltage readings are 2 and 3
    print "Freq = ", freq_cur, "  VSWR = ",vswr

# Plot the SWR
    plt.plot(freq_cur,vswr,'ro') # plot the SWR as a red dot (r o)

# you could read the min SWR and freq or compute them in Python

ser = serial.Serial.close # close the  port

# finish the plot and save it
plt.title('SWR '+str(band)+'m band '+comment) # concatenate some strings for title
plt.xlabel('Freq MHz') # X axis label
plt.ylabel('SWR')      # Y axis label
plt.ylim(1.,5.)        # set the Y axis limits from SWR = 1 to 5
plt.savefig(str(band)+comment+'.png',format='png') # build a filename and save the figure
plt.show()  # display the figure in the console
# end of program
#==============================================================================
