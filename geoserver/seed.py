import requests
import json
import random
import tablib

ENTRY_POINT = 'http://localhost:5000'


def endpoint(resource):
    return '%s/%s/' % (ENTRY_POINT, resource)


def create_parking_record(data):
    return {
        'description': data['Description'],
        'address': data['Address'],
        'location': {
            "type":"Point",
            "coordinates":[
                float(data['Latitude, Longitude'].split(',')[1].strip()) if data['Latitude, Longitude'].strip() else 0.0,
                float(data['Latitude, Longitude'].split(',')[0].strip()) if data['Latitude, Longitude'].strip() else 0.0
            ]
        },
        'entrance': data['Entrance'],
        'phone': data['Phone'],
        'operator': data['Operator'],
        'hourly': data['Hourly'],
        'daily_max': data['Daily Max'],
        'early_bird': data['EarlyBird'],
        'after_hours': data['After Hours(flat rate)'],
        'weekend_rate': data['WeekendRate'],
        'monthly_rate':  data['Monthly Rate'],
        'hours_of_operation': data['Hours of Operation'],
        'indoors_outdoors': data['Indoors/Outdoors'],
        'service_type': data['Service Type'],
        'motorcycles_allowed': data['Motorcyles Allowed'] == "Yes",
        'vehicle_types': data['Vehicle Types'],
        'height_restriction': data['Height Restriction'],
        'note': data['Note']
    }


def post_parking():
    valids = []
    with open("Parking_2015.csv", "rb") as parking_file:
        dataset = tablib.import_set(parking_file.read())
        for data in dataset.dict:
            parking_record = create_parking_record(data)
            print parking_record
            r = perform_post('parkings', json.dumps(parking_record))
            print "'parking' posted", r.status_code

            if r.status_code == 201:
                response = r.json()
                if response['_status'] == 'OK':
                    valids.append(response['_id'])

    return valids


def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(resource), data, headers=headers)


if __name__ == '__main__':
    requests.delete(endpoint('parkings'))
    post_parking()
