from sys import argv
import datetime
import sys

output_file = "standing.log"
os_version = sys.platform

def stand_up():
	print "Standing up!"
	current_time = str(datetime.datetime.now())
	print "Hit enter when sitting down"
	wait = raw_input()
	end_time = str(datetime.datetime.now())
	output_line = "%s|%s" % (current_time, end_time)
	return output_line

def write_file(output_line):
	target = open(output_file, 'a')
	target.write(output_line)
	target.write("\n")
	target.close

line = stand_up()
write_file(line)

# Play a sound if it is on Windows or OSX
if os_version == "win32":
	import winsound
	winsound.PlaySound("C:\drum.wav", 1)
else:
  sys.stdout.write('\a')
  sys.stdout.flush()

