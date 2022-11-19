import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):

    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(my_date):
    months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    day = my_date[8]+my_date[9]
    year = my_date[0]+my_date[1]+my_date[2]+my_date[3]
    mes = str(months[int(my_date[5]+my_date[6])])
    day2 = int(my_date[8]+my_date[9])
    year2 = int(my_date[0]+my_date[1]+my_date[2]+my_date[3])
    mes2 = int(my_date[5]+my_date[6])
    dayoftheweek = datetime(year2,mes2,day2)
    dayoftheweek2 = datetime.weekday(dayoftheweek) 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    datefinal = days[dayoftheweek2]+' '+day+' '+mes+' '+year
    return(datefinal)

pass


def convert_f_to_c(temp_in_farenheit):
    temp_in_c = (float(temp_in_farenheit)-32)*5/9
    temp = round(temp_in_c, 1)
    return(temp)

pass


def calculate_mean(weather_data):
    new_list = []
    for item in weather_data:
        new_list.append(float(item))
    mean = (sum(new_list))/(len(new_list))
    return(mean)

pass


def load_data_from_csv(csv_file):
    
    with open(csv_file) as f:
        reader = csv.reader(f)
        next(reader)
        list = []
        for row in reader:
            if len(row) >0:
                date = row[0]
                min = int(row[1])
                max = int(row[2])
                list.append([date, min, max])
    return(list)

pass


def find_min(weather_data):

    if len(weather_data) >0:
        min_t = float(weather_data[0])
        min_t_position = 0
        for i in range(len(weather_data)):
            if float(weather_data[i]) <= min_t:
                min_t = float(weather_data[i])
                min_t_position = i
        
        return (min_t,min_t_position)
    else: 
        return ()
        
pass


def find_max(weather_data):

    if len(weather_data) >0:
        max_t = float(weather_data[0])
        max_t_position = 0
        for i in range(len(weather_data)):
            if float(weather_data[i]) >= max_t:
                max_t = float(weather_data[i])
                max_t_position = i
        
        return (max_t,max_t_position)
    else: 
        return ()

pass


def generate_summary(weather_data): 
    days = len(weather_data)
    min = find_min([el[1] for el in weather_data])
    min_temperature = convert_f_to_c(min[0]) 
    max = find_max([el[2] for el in weather_data])
    max_temperature = convert_f_to_c(max[0])
    sum_min = 0
    sum_max = 0
    for el in weather_data:
        sum_min = sum_min + el[1]
        sum_max = sum_max + el[2]
    average_l = sum_min/days
    average_low = convert_f_to_c(average_l)
    average_h = sum_max/days
    average_high = convert_f_to_c(average_h)

    a = f'{days} Day Overview\n  The lowest temperature will be {str(format_temperature(min_temperature))}, and will occur on {convert_date(weather_data[min[1]][0])}.\n  The highest temperature will be {str(format_temperature(max_temperature))}, and will occur on {convert_date(weather_data[max[1]][0])}.\n  The average low this week is {str(format_temperature(average_low))}.\n  The average high this week is {str(format_temperature(average_high))}.\n'
    return(a)
pass


def generate_daily_summary(weather_data):

    daily_sum = ""
    
    for info in weather_data:
        date = convert_date(info[0])
        daily_min_temp = convert_f_to_c(info[1])
        daily_max_temp = convert_f_to_c(info[2])
    
        date_ready = f"---- {date} ----\n"
        daily_min_temp_ready = f"  Minimum Temperature: {format_temperature(daily_min_temp)}\n"
        daily_max_temp_ready = f"  Maximum Temperature: {format_temperature(daily_max_temp)}\n\n"
        daily_sum = daily_sum+date_ready+daily_min_temp_ready+daily_max_temp_ready
        
    return(daily_sum)
