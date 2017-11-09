from datetime import datetime
from pytz import timezone
import requests


def load_database_records():
    all_db_records = []
    pages_amount = 1
    page_number = 1
    while page_number <= pages_amount:
        url = 'http://devman.org/api/challenges/solution_attempts/'
        payload = {'page': page_number}
        timeout_seconds = 3.05  # http://docs.python-requests.org/en/master/user/advanced/#timeouts
        response_content = requests.get(url, params=payload,
                                    timeout=timeout_seconds).json()
        pages_amount = response_content['number_of_pages']
        records_on_page = response_content['records']
        for record in records_on_page:
            all_db_records.append(record)
        page_number += 1
    return all_db_records
     
    
def get_midnighters(database_records):
    devman_owls = set()
    night_stop_time = 6
    for record in database_records:
        devman_server_timestamp = record['timestamp']
        local_tz = timezone(record['timezone'])
        local_time = datetime.fromtimestamp(devman_server_timestamp,
                                            tz=local_tz)
        if local_time.hour < night_stop_time:
            devman_owls.add(record['username'])
    return devman_owls


if __name__ == '__main__':
    print('\nRetrieving midnight users from Devman.org database...\n')
    devman_owls = get_midnighters(load_database_records())
    if devman_owls:
        print('Done! Here is a list of devman owls:\n')
        for user_count, user in enumerate(devman_owls, start=1):
            print('{}. {}'.format(user_count, user))
    else:
        print('Looks like Devman students prefer sleep at night!')
