file = open("rindas.txt", "w", encoding="UTF-8")

for i in range(1, 100):
    text = f"Rinda {i}\n"
    file.write(text)

file.close



import csv

file_path = 'spotify.csv'
file = open(file_path, mode='r', newline='', encoding='utf-8')
csv_reader = csv.reader(file)

for row in csv_reader:
    print(row)
file.close()



import csv

file_path = 'spotify.csv'

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    total_duration = 0
    track_count = 0
    for row in csv_reader:
        try:
            total_duration += int(row[4])
            track_count += 1
        except:
            continue

    print(f"Average song duration is: {total_duration / track_count} ms")