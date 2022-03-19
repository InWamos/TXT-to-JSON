import json
import sys

# Creates JSON file
try:
    with open('./result.json', 'x'):
        pass
except:
    pass

# Opens JSON file
with open('./result.json', 'r') as json_file:
    data = json.loads(json_file.read())

# Opens TXT
try:
    file = open('text.txt', encoding='utf-8')
    file_list = file.readlines()
except:
    sys.exit('Please, create text.txt in an appropriate way')

round = 0
for i in file_list:
    NEC = i.split(' ')
    NEC[len(NEC) - 1] = NEC[len(NEC) - 1].replace('\n', '')
    data[f'card{round}'] = {
        'card_number' : NEC[0],
        'expires' : NEC[1],
        'cvv' : NEC[2]
    }
    round += 1

with open('./result.json', 'w') as json_file:
    json_file.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))