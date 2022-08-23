import csv

fieldnames = ['sku', 'make', 'model', 'color']

with open("test.csv", 'r') as f:
    isFirst = True
    for l in f:
        if isFirst:
            isFirst = False
            continue
        data = l.strip('\n').split(',')
        res = ""
        for i, field in enumerate(fieldnames):
            res = f"{res}, {field}:{data[i]}" if res else f"{field}:{data[i]}"
        print(res)


data_source = {"sku":"45781", "make":"adidas", "model":"gazelle", "color":"green"}

# with open("test.csv", 'a') as f:
#     f.write(','.join([data_source[name] for name in fieldnames]))



# using the CSV module

with open("test.csv", 'r') as f:
    reader = csv.reader(f)
    isFirst = True
    for data in reader:
        if isFirst:
            isFirst = False
            continue
        print(data)
        res = ""
        for i, field in enumerate(fieldnames):
            res = f"{res}, {field}:{data[i]}" if res else f"{field}:{data[i]}"
        print(res)

# with open("test.csv", 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(data_source.values())

with open("test.csv", 'r') as f:
    reader = csv.DictReader(f, fieldnames)
    isFirst = True
    for data in reader:
        if isFirst:
            isFirst = False
            continue
        print(','.join([f"{name}:{data[name]}" for name in fieldnames]))

# with open("test.csv", 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames)
#     writer.writeheader()
#     writer.writerow(data_source)
