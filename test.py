import csv 

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

# print(load_data_from_csv('tests/data/example_one.csv'))
weatherlist = load_data_from_csv('tests/data/example_three.csv')
print(weatherlist)

min_t = weatherlist[0][1]
min_t_position = 0

temperatures = [49, 57, 56, 55, 53, 49]

for i in range(len(temperatures)):
    #print(f'position: {i} min_t: {weatherlist[i][1]}')
    if temperatures[i][1] <= min_t:
        min_t = weatherlist[i][1]
        min_t_position = i
    
    print(f'position: {i} min_t_list: {weatherlist[i][1]} min_t: {min_t}') 