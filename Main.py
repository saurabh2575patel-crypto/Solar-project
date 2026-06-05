import argparse
from src.scheduler import run_scheduler
parser=argparse.ArgumentParser()
parser.add_argument('--demo',action='store_true')
args=parser.parse_args()
run_scheduler(args.demo)

