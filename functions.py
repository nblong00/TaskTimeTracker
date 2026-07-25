import csv
import datetime
from dateutil import relativedelta


def minutes_output(start, end):
    diff_now_end = relativedelta.relativedelta(end, 
                                               start)
    diff_total_minutes = (diff_now_end.hours * 60) + diff_now_end.minutes
    diff_minutes_output = f'{diff_total_minutes} minutes'
    return diff_minutes_output


def standardized_format(point):
    return datetime.datetime.strftime(point, "%I:%M%p %Y-%m-%d")


def start_tracking(current_obj):
    start = datetime.datetime.now()
    start_time = standardized_format(start)

    print("\n=========================")
    print("Press ENTER to stop recording time...")
    print("=========================")
    input('\n')

    end = stop_tracking()
    end_time = standardized_format(end)

    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([current_obj, start_time, end_time,
                         minutes_output(start, end)])


def stop_tracking():
    now = datetime.datetime.now()
    return now
