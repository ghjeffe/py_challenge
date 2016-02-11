import os   
import re
import zipfile
import requests

ZF = None

def get_zip_file():
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    local_file = os.path.basename(url)
    zip_stream = requests.get(url, stream=True)
    with open(local_file, mode='wb') as fh:
        for chunk in zip_stream.iter_content(chunk_size=1024):
            if chunk:
                fh.write(chunk)
    return local_file

def extract_num(filename='readme.txt'):
    global ZF
    re_initial = re.compile('start from (\d+)$')
    re_secondary = re.compile('Next nothing is (\d+)$')
    match = None
    with ZF.open(filename) as fh:
        for line in fh:
            line = line.decode('utf8')
            match = re_secondary.search(line)
            if not match:
                match = re_initial.search(line)
            if match:
                return match.group(1)
    
def main():
    global ZF
    comments = []
    ZF = zipfile.PyZipFile(get_zip_file())
    next_num = extract_num()
    while next_num:
        comments.append(ZF.getinfo('{}.txt'.format(next_num)).comment)
        print(next_num)
        next_num = extract_num('{}.txt'.format(next_num))
    print(''.join(comment.decode('utf8') for comment in comments))
        
main()