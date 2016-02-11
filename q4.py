import requests

RUN_TIMES = 0

def get_next_num(num):
    req = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(num))
    return req.text.split()[-1]

for i in range(200):
    initial_num = 0
    if RUN_TIMES == 0:
        next_num = get_next_num(initial_num)
    else:
        next_num = get_next_num(next_num)
        
    RUN_TIMES += 1
    
    print(next_num, RUN_TIMES)