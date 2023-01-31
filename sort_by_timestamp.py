import sys
from dateutil.parser import parse
import csv
import pytz

TIME_REGIONS = {
    'bst': pytz.timezone("Europe/London"),
    'pdt': pytz.timezone("US/Pacific"),
    'est': pytz.timezone("US/Eastern"),
}

def main(args):
    output_filename = args.pop(0)
    records = []
    for arg in args:
        file_name, time_zone = arg.split(':')
        with open(file_name) as file_in:
            rdr = csv.reader(file_in)
            for *other_fields, timestamp in rdr:
                naive_ts = parse(timestamp)
                ts = TIME_REGIONS[time_zone].localize(naive_ts)
                record = other_fields + [ts, time_zone.upper()]
                records.append(record)

    with open(output_filename, "w") as file_out:
        wtr = csv.writer(file_out)
        for record in sorted(records, key=by_time):
            wtr.writerow(record)

def by_time(record):
    return record[2]

john_info = """
jstrickler@gmail.com
John Strickler
"""

if __name__ == '__main__':
    main(sys.argv[1:])
