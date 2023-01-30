import sys

print(sys.argv)

data_to_process = sys.argv[1]
print(f"data_to_process: {data_to_process}")

file_name, time_zone = data_to_process.split(':')

print(f"file_name: {file_name}")
print(f"time_zone: {time_zone}")

