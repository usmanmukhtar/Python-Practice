import pandas

def main():
    data = pandas.read_csv('squirrel_data.csv')

    grey_color = data[data["Primary Fur Color"] == 'Gray']["Primary Fur Color"].count()
    red_color = data[data["Primary Fur Color"] == 'Cinnamon']["Primary Fur Color"].count()
    black_color = data[data["Primary Fur Color"] == 'Black']["Primary Fur Color"].count()

    new_data = {
        "Fur Color": ["Gray", "Red", "Black"],
        "Count": [grey_color, red_color, black_color]
    }

    new_data = pandas.DataFrame(new_data)
    new_data.to_csv('squirrel_data_new.csv')


if __name__ == "__main__":
    main()