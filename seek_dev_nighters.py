import requests
from datetime import datetime
from pytz import timezone

def load_database_records():
    all_db_records = []
    url = 'http://devman.org/api/challenges/solution_attempts/'
    try:
        pages_count = requests.get(url).json().get('number_of_pages')
    except requests.exceptions.RequestException as error:
        records_responce = None
        print(error)
    for page_number in range(1, pages_count + 1):
        payload = {'page':page_number}
        try:
            records_responce = requests.get(url, params = payload).json().get('records')
        except requests.exceptions.RequestException as error:
            records_responce = None
            print(error)
        if records_responce is not None:
            for user in records_responce:
                all_db_records.append(user)
    return all_db_records
   
def get_midnighters(database_records):
    devman_owls = []
    night_start, night_stop = 0,6
    for record in database_records:
        devman_server_timestamp = record.get('timestamp')
        local_tz = timezone(record.get('timezone'))
        local_time = datetime.fromtimestamp(devman_server_timestamp, tz = local_tz)
        if local_time.hour in range (night_start, night_stop + 1):
            devman_owls.append(record.get('username'))
    return devman_owls

if __name__ == '__main__':
    print('\nRetrieving midnight users from Devman.org database. Please wait.\n') 
    devman_owls = get_midnighters(load_database_records())
    if devman_owls:
        print('Done! Here is a list of devman owls:\n')
        for user_count, user in enumerate(devman_owls, start = 1):
            print('{}. {}'.format(user_count, user))
    else:
         print('Looks like Devman.org students prefer sleep at night!')
