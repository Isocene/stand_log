from sys import argv
import datetime

output_file = "standing.log"

current_time = str(datetime.datetime.now())

target = open(output_file, 'a')

target.write(current_time)
target.write("\n")
target.close