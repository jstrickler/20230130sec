import csv

DATA_FILE = 'DATA/primeministers.txt'
OUTPUT_FILE = 'ministers.csv'

with open(DATA_FILE) as pm_in:
    with open(OUTPUT_FILE, 'w') as pm_out:
        with open('pm_info.txt', 'w') as pm_out2:
            wtr = csv.writer(pm_out)
            for raw_record in pm_in:
                record = raw_record.rstrip()
                fields = record.split(':')
                wtr.writerow(fields)
                fields[1] = fields[1].replace("Sir ", "")
                pm_out2.write(f"{fields[0]}\t{fields[1]}\t{fields[2]}\n")
