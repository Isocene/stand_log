from sys import argv
import datetime

output_file = "standing.log"

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


target.close