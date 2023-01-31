import sys
from datetime import datetime
import random
import csv


def main(args: list[str]):
    """
    Program entry point
    """
    file_name, items = args
    items = int(items)
    start_time = datetime(2023, 1, 1, 10)
    end_time = datetime(2023,1,10,23, 30)
    timestamps = get_random_timestamps(items, start_time, end_time)
    words = get_random_words(items)
    ints = get_random_integers(items, 1, 100)

    with open(file_name, 'w') as file_out:
        wtr = csv.writer(file_out)
        wtr.writerows(zip(ints, words, timestamps))

def get_random_timestamps(count, start_time: datetime, end_time: datetime):
    """
    Create a series of random datetime objects between start_time
    and end_time.

    :param count: number of datetime objects to make
    :param start_time: starting time as datetime
    :param end_time: ending time as datetime
    :return: list of random datetimes
    """
    start_timestamp = datetime.timestamp(start_time)
    end_timestamp = datetime.timestamp(end_time)

    elapsed_time = int(end_timestamp - start_timestamp)

    timestamps = []
    for _ in range(count):
        timestamp_offset = random.randint(
            1, elapsed_time
        )
        new_timestamp = start_timestamp + timestamp_offset
        timestamps.append(datetime.fromtimestamp(new_timestamp))

    return sorted(timestamps)

def get_random_words(count):
    all_words = open('DATA/words.txt').read().splitlines()
    return random.sample(all_words, count)

def get_random_integers(count, start, stop):
    return [random.randint(start, stop) for _ in range(count)]

if __name__ == '__main__':
    main(sys.argv[1:])

