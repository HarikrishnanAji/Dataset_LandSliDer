import csv


with open("records.csv",'r') as file:
	datas = csv.reader(file)
	value = [data for data in datas]


res = []

for i in range(1, len(value)):

	slope = float(value[i][0])
	vib = float(value[i][1])
	moist = float(value[i][2])

	if (slope < 45) and (vib < 1) and (moist < 65):
		res.append([slope, vib, moist, 1])
	else:
		res.append([slope, vib, moist, 0])


with open("test.csv", "w",newline='') as f:
	cw = csv.writer(f)
	cw.writerow(["slope", "vibration", "moisture", "status"])
	cw.writerows(res)