import csv
def auto_gen():
    header = ['name', 'area', 'country_code2', 'country_code3']
    data = ['Afghanistan', 652090, 'AF', 'AFG']

    with open('countries.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

    # write the header
        writer.writerow(header)

    # write the data
        writer.writerow(data)

if __name__ == "__main__":
    print("good here")
    auto_gen()