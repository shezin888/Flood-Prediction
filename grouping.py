import csv

result = {}
with open('/home/shezin/Desktop/Flood Estimation/srm/csv/lat_lon_data.csv', mode='rU') as f:
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        print(row)
        if not n:
            # Skip header row (n = 0).
            continue  
        id, long, lat, data = row
        if data not in result:
            result[data] = list()
        result[data].append((long, lat))

print(result)

with open('/home/shezin/Desktop/Flood Estimation/srm/csv/dict.csv','w') as f:
    w = csv.writer(f)
    w.writerow(result.keys())
    w.writerow(result.values())

