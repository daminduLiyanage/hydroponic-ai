import csv
import random

CSV_FILE_PATH   = 'generated_data.csv'
OPEN_MODE       = 'w'
ROUND_OFF_TO    = 2
ENCODE_AS       = 'UTF8'
DELIMITER       = ''

MIN_TEMPERATURE = 24
MAX_TEMPERATURE = 31
MIN_HUMIDITY    = 77
MAX_HUMIDITY    = 83
MIN_EC          = 1.6
MAX_EC          = 2.3
MIN_PH          = 5.5
MAX_PH          = 6

header = ['Temperature', 'Humidity', 'EC', 'pH']
data = []
for _ in range(50):
    data.append([
        round(random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE), ROUND_OFF_TO),
        round(random.uniform(MIN_HUMIDITY, MAX_HUMIDITY), ROUND_OFF_TO),
        round(random.uniform(MIN_EC, MAX_EC), ROUND_OFF_TO),
        round(random.uniform(MIN_PH, MAX_PH), ROUND_OFF_TO)
    ])
with open(CSV_FILE_PATH, OPEN_MODE, encoding=ENCODE_AS, newline=DELIMITER) \
    as opened_file:
    writer = csv.writer(opened_file)
    writer.writerow(header)
    writer.writerows(data)