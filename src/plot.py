import json
import matplotlib.pyplot as plt
import os


if os.path.exists("temp.json"):
	f = open('temp.json','r')
	for line in f:
		line = line[:-1]
		obj = json.loads(line)
		fig, ax = plt.subplots()
		ax.plot(obj['x'], obj['y'])
		ax.set(xlabel= obj['xlabel'], ylabel= obj['ylabel'], title= obj['title'])
		ax.set_ylim(ymin=0, ymax= max(obj['y']) + max(obj['y']) - min(obj['y']))
		ax.grid()
		filename = obj['title'].replace(" % ","").replace(" ","_")
		fig.savefig("performance_graphs/" + filename + ".png")
	#os.remove("temp.json")
else:
  print("The file does not exist")
