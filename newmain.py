import csv




def read_playerData(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == "George Pickens":
                print(row)


def main():
    print("hello")
    read_playerData("playerData.csv")
    

if __name__ == "__main__":
    main()