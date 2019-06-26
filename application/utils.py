import csv

from datetime import date, datetime

def update_csv(file_name, data):
    data_array = list(data.values())
    with open(f'{file_name}.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(data_array)


def csv_view(file_name):
    with open(f'{file_name}.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_data = []
        for row in reversed(list(csv_reader)):
            csv_data.append(', '.join(row))
        return csv_data


def remove_dashes(input):
    output = input.replace('-', ' ').capitalize()
    return output


def csv_dict(file_name, index_number=None):
    with open(f'{file_name}.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        array = []
        for row in reader:
            array.append(row)
        if index_number is not None:
            return array[index_number - 1]
        else:
            return array


def convert_ordered_dicts_for_dl(data):
    data_list = []
    for x, y in data.items():
        if x != 'csrf_token':
            key = remove_dashes(x)
            data_list.append([key, y])
    return data_list


def json_serialiser(form_data):
    """JSON serializer for objects not serializable by default json code"""

    entry_data = {}
    for k, v in form_data.items():
        if isinstance(v, (datetime, date)):
            entry_data[k] = v.isoformat()
        else:
            entry_data[k] = v
    return entry_data
