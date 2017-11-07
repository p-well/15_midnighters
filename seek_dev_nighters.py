from datetime import datetime
from pytz import timezone
import requests


def load_database_records():
    all_db_records = []
    url = 'http://devman.org/api/challenges/solution_attempts/'
    timeout_seconds = 3.05
    response = requests.get(url, timeout = timeout_seconds)
    pages_count = response.json().get('number_of_pages')
    for page_number in range(1, pages_count + 1):
        payload = {'page':page_number}
        page_content = requests.get(url, params = payload,
                                    timeout = timeout_seconds)
        records = page_content.json().get('records')
        for user in records:
            all_db_records.append(user) 
    return all_db_records

   
def get_midnighters(database_records):
    devman_owls = set()
    night_start = 0 
    night_stop = 6
    for record in database_records:
        devman_server_timestamp = record.get('timestamp')
        local_tz = timezone(record.get('timezone'))
        local_time = datetime.fromtimestamp(devman_server_timestamp,
                                            tz = local_tz)
        if local_time.hour in range (night_start, night_stop + 1):
            devman_owls.add(record.get('username'))
    return devman_owls


if __name__ == '__main__':
    print('\nRetrieving midnight users from Devman.org database...\n') 
    devman_owls = get_midnighters(load_database_records())
    if devman_owls:
        print('Done! Here is a list of devman owls:\n')
        for user_count, user in enumerate(devman_owls, start = 1):
            print('{}. {}'.format(user_count, user))
    else:
        print('Looks like Devman students prefer sleep at night!')
