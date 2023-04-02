# import csv


# def main():
#     tempratures = []
#     with open('weather_data.csv') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             print(row)
#             if row[1] != 'temp':
#                 tempratures.append(float(row[1]))
#                 print(tempratures)


import pandas
def main():
    #read weather data from pandas
    data = pandas.read_csv('weather_data.csv')

    #convert dataframe to dictionary
    data_dict = data.to_dict()
    print(data_dict)

    #convert series to list
    temp_list = data['temp'].to_list()
    print(temp_list)

    #calculate average temperature from temp list
    avg = sum(temp_list)/len(temp_list)
    print(avg)

    #alternative to calculate avg using pandas
    mean = data['temp'].mean()
    print(mean)

    #get max temperature using pandas series function
    max_temp = data['temp'].max()
    print(max_temp)

    #another way to select columns
    conditions = data.condition
    print(conditions)

    #get data in row
    print(data[data.day == "Monday"])
    #get max data in row
    print(data[data.temp == data.temp.max()])

    monday = data[data.day == "Monday"]
    print(monday.condition)

    #Challenge: convert temperature from celcius to fahrenheit
    fahrenheit = (int(monday.temp) * 9/5) + 32
    print(f"{fahrenheit = }")

    #create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "John", "Usman"],
        "scores": [73, 23, 45]
    }

    data = pandas.DataFrame(data_dict)
    data.to_csv('new_data.csv')
    print(data)

if __name__ == '__main__':
    main()