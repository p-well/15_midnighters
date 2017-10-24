import requests
import datetime
import pytz

def load_database_records():
    all_db_records = []
    url = 'http://devman.org/api/challenges/solution_attempts/'
    pages_count = int(url.json().get('number_of_pages'))
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


    
    
def get_users_info():
    for single_record_content in load_database_records():
        yield {'username': single_record_content['timestamp'] ,
               'timestamp': single_record_content['username'] ,
               'timezone': single_record_content['timezone']}


               
def get_midnighters(database_records):
    devman_owls = []
    for record in database_records:
        devman_server_timestamp = record.get('timestamp')


if __name__ == '__main__':
    pass
