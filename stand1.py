from sys import argv
import datetime
import sys

output_file = "standing.log"
os_version = sys.platform

current_time = str(datetime.datetime.now())

target = open(output_file, 'a')

print "Standing up!"
target.write(current_time)
target.write("|")
print "Hit enter when sitting down"
wait = raw_input()
end_time = str(datetime.datetime.now())
target.write(end_time)
target.write("\n")

# Play a sound if it is on Windows or OSX
if os_version == "win32":
	import winsound
	winsound.PlaySound("C:\drum.wav", 1)
else:
  sys.stdout.write('\a')
  sys.stdout.flush()

target.close