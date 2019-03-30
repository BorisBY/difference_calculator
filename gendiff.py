import argparse
from jsondiff import diff
import json


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference', usage='gendiff [options] <firstConfig> <secondConfig>')
parser.add_argument('-v', '--version', action='version', version='1.0')
parser.add_argument('-f', '--format ', type=str)
args = vars(parser.parse_args())


# with open('file1.json') as f1:
#     json1 = json.load(f1)

with open('file1.json') as f1, open('file2.json') as f2:
    json1 = json.load(f1)
    json2 = json.load(f2)

temp = diff(json1, json2)
print(temp)
pass
