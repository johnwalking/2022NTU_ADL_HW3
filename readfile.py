import json

f= open('./data/sample_test.jsonl', encoding= 'utf-8')
k = f.readlines()
for data in k:
    print(json.loads(data))

f.close()

