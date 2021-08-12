from collections import namedtuple, defaultdict
from datetime import datetime


import csv
from itertools import islice


#Goal 1
def cast(data_type, value):
    '''This function returns the value after casting it to the expected data type
        Input parameters:
            1. Data Type: Type to be converted to
            2. Value: Value which needs to be converted
    '''
    if data_type == int:
        return int(value)
    elif data_type == datetime:
        new_format = "%Y-%m-%d"
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').strftime(new_format)
    else:
        return str(value)

def cast_row(data_types, data_row):
    '''This function returns a list of values after casting each of the list elements
        to the corresponding expected data type
        1. Data Types: An array of data types
        2. Data Row: An array of values
    '''
    return [cast(data_type, data_value) for data_type, data_value in list(zip(data_types, data_row))]


def get_headers(file_name):
    #rows = get_rows(file_name)
    with open(file_name, encoding='latin-1') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        #header_row = yield from rows
        header = islice(rows,1)
        header_row = next(iter(header))
        #Employment = namedtuple('Employment', header_row)
        data = islice(rows,2)
        data_row = next(iter(data))
        data_types = []
        for column in data_row:
            if column.isdigit():
                data_types.append(int)
            else:
                try:
                    datetime.strptime(column, '%Y-%m-%dT%H:%M:%SZ')
                    data_types.append(datetime)
                except:
                    data_types.append(str)
    return header_row, data_row, data_types

    
#To extract data
def get_iterators(file_name):
    '''This function iterates through all the data rows in the csv
        and yields a named tuple after converting each item in the
        tuple to its corresponding data type.
        Note: 1 row had a "," within the data which was removed.
    '''
    get_headers(file_name)
    header_row, data_row, data_types = get_headers(file_name)
    with open(file_name, encoding='latin-1') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        next(rows)
        for row in rows:
            if file_name == "employment.csv":
                Employment = namedtuple('Employment', header_row)
                
                emp_data = cast_row(data_types, row)
                yield Employment(*emp_data)
            elif file_name == "personal_info.csv":
                Personal_info = namedtuple('Personal_info', header_row)
                personal_data = cast_row(data_types, row)
                yield Personal_info(*personal_data)
            elif file_name == "update_status.csv":
                Update_status = namedtuple('Update_status', header_row)
                update_data = cast_row(data_types, row)
                yield Update_status(*update_data)
            elif file_name == "vehicles.csv":
                Vehicles = namedtuple('Vehicles', header_row)
                Vehicle_data = cast_row(data_types, row)
                yield Vehicles(*Vehicle_data)        
            #Skip header row
            # next(iter(f))
            # for line in f:
            #     rows = csv.reader(f, delimiter=',', quotechar='"')
            #     data = cast_row(data_types, line.strip('\n').split(','))
            #     yield Ticket(*data)
def merge_iterators():
    get_emp_iterator = iter(get_iterators('employment.csv'))
    get_personal_iterator = iter(get_iterators('personal_info.csv'))
    get_update_status_iterator = iter(get_iterators('update_status.csv'))
    get_vehicle_iterator = iter(get_iterators('vehicles.csv'))
    emp_fields = next(get_emp_iterator)._fields
    personal_fields = next(get_personal_iterator)._fields
    status_fields = next(get_update_status_iterator)._fields
    vehicle_fields = next(get_vehicle_iterator)._fields

    combined_data = []
    All_list = list(set(emp_fields+personal_fields+status_fields+vehicle_fields))
    All_details = namedtuple('All_details', All_list) 

    get_emp_iterator = iter(get_iterators('employment.csv'))
    get_personal_iterator = iter(get_iterators('personal_info.csv'))
    get_update_status_iterator = iter(get_iterators('update_status.csv'))
    get_vehicle_iterator = iter(get_iterators('vehicles.csv'))

    i = 0
    try:
        while True:
            emp_row = next(get_emp_iterator)
            personal_row = next(get_personal_iterator)
            status_row = next(get_update_status_iterator)
            vehicle_row = next(get_vehicle_iterator)

            All_detailsparam = All_details(ssn = personal_row.ssn,
            first_name=personal_row.first_name,
            last_name=personal_row.last_name,
            gender = personal_row.gender,
            language = personal_row.language,
            employee_id = emp_row.employee_id,
            department = emp_row.department,
            employer = emp_row.employer,
            vehicle_make = vehicle_row.vehicle_make,
            vehicle_model = vehicle_row.vehicle_model,
            model_year = vehicle_row.model_year,
            last_updated = status_row.last_updated,
            created = status_row.created)

            combined_data.append(All_detailsparam)
            #print(combined_data[i])
            i = i + 1
    except StopIteration:       
        return combined_data
    return combined_data


def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict