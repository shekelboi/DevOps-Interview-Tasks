import datetime as dt
import string
from random import randint
import json

WORDS_FROM = 5
WORDS_TO = 15
WORD_LENGTH_MIN = 3
WORD_LENGTH_MAX = 10
FROM = dt.datetime(year=2024, month=8, day=1)
TO = dt.datetime(year=2024, month=8, day=31)
LOG_LENGTH = 1000
LOG_LEVELS = ['WARNING', 'ERROR', 'DEBUG', 'INFO']
SERVICE_NAMES = ['apache', 'nginx', 'chrome', 'xampp']


def generate_word(minimum=WORD_LENGTH_MIN, maximum=WORD_LENGTH_MAX):
    return ''.join(
        chr(randint(0, len(string.ascii_lowercase) - 1)
            + ord('a')) for i in range(randint(minimum, maximum)))


def generate_message(minimum=WORDS_FROM, maximum=WORDS_TO):
    return ' '.join(generate_word() for i in range(randint(minimum, maximum)))


def generate_timestamp(minimum=FROM, maximum=TO):
    return dt.datetime.fromtimestamp(
        randint(minimum.timestamp(),
                maximum.timestamp())).isoformat()


with open('out.txt', 'w') as file:
    for i in range(LOG_LENGTH):
        r = randint(1, 10)

        # Weighted log levels
        log_level = ''
        # 10%
        if r <= 1:
            log_level = 'ERROR'
        # 50 %
        elif r <= 6:
            log_level = 'INFO'
        # 20%
        elif r <= 8:
            log_level = 'DEBUG'
        # 20%
        else:
            log_level = 'WARNING'

        d = {
            'timestamp': generate_timestamp(),
            'log_level': log_level,
            'service_name': SERVICE_NAMES[randint(0, len(SERVICE_NAMES) - 1)],
            'message': generate_message()
        }
        file.write(json.dumps(d) + '\n')
