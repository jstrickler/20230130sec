import sys

if len(sys.argv) < 2:
    print("Please put folder on command line")
    exit(1)

folder = sys.argv[1]   # must put folder
print("processing folder: ", folder)
