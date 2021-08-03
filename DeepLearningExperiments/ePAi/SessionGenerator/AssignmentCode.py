from collections import namedtuple, defaultdict
from datetime import datetime

file_name = 'nyc_parking_tickets_extract-1.csv'

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
        return datetime.strptime(value, '%m/%d/%Y')
    else:
        return str(value)

def cast_row(data_types, data_row):
    '''This function returns a list of values after casting each of the list elements
        to the corresponding expected data type
        1. Data Types: An array of data types
        2. Data Row: An array of values
    '''
    return [cast(data_type, data_value) for data_type, data_value in list(zip(data_types, data_row))]

#To extract column names and data types
with open(file_name, encoding='latin-1') as f:
    headers = f.readline().strip('\n').replace(' ', '_').split(',')
    datarow = f.readline().strip('\n').split(',')
    data_types = []
    for column in datarow:
        if column.isdigit():
            data_types.append(int)
        else:
            try:
                datetime.strptime(column, '%m/%d/%Y')
                data_types.append(datetime)
            except:
                data_types.append(str)
    Ticket = namedtuple('Ticket', headers)

#To extract data
def get_tickets():
    '''This function iterates through all the data rows in the csv
        and yields a named tuple after converting each item in the
        tuple to its corresponding data type.
        Note: 1 row had a "," within the data which was removed.
    '''
    with open(file_name, encoding='latin-1') as f:
        #Skip header row
        next(iter(f))
        for line in f:
            data = cast_row(data_types, line.strip('\n').split(','))
            yield Ticket(*data)

get_ticket = iter(get_tickets())

print(next(get_ticket))
print('\n')
print(next(get_ticket))
print('\n')
print(next(get_ticket))

#Goal 2
violations = defaultdict(int)
for ticket in get_tickets():
    violations[ticket.Vehicle_Make] += 1
print('\n')
print(violations)