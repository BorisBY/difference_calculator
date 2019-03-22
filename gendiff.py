import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference', usage='gendiff [options] <firstConfig> <secondConfig>')
parser.add_argument('-v', '--version', action='version', version='1.0')
parser.add_argument('-f', '--format ', type=str, version='1.0')



args = vars(parser.parse_args())
