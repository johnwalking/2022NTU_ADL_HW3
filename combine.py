f = open('./generated_predictions.txt')
results = f.readlines()
#for result in results:
#    print(result)
#    print("---------")
f.close


import json
import sys
ids = []
f = open(sys.argv[1])
datas = f.readlines()
for data in datas:
    tmp = json.loads(data)
    ids.append(tmp['id'])
#print(ids)

print(len(results), len(ids))
assert len(results) == len(ids)


import jsonlines

with jsonlines.open(sys.argv[2], 'w') as writer:
    for i, title in zip(ids, results):
        writer.write({
            "title": title,
            "id": i
        })
print("finish writing file.")
