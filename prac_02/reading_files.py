import json

file_data = open('some_file.txt', 'r')
headers = file_data.readline()
headers = headers.strip('\n').split(',')
print(headers)

guitar_data = list()

for line in file_data:
    # print(line.strip('\n'))
    line = line.strip('\n').split(',')
    line[1] = int(line[1])
    line[2] = float(line[2])
    guitar_data.append(line)
    # print(line)

print(guitar_data)

guitar_json = []
print(guitar_json)

outfile = open('output.jsn', 'w')

for guitars in guitar_data:
    guitar = {headers[i]:row for i, row in enumerate(guitar)}
    json.dump(g, outfile, indent=4)

outfile.close()