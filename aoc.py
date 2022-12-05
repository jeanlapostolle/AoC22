import argparse
import traceback

from code import day1, day2, day3, day4, day5
import tomllib


parser = argparse.ArgumentParser(
    prog= 'aoc.py',
    description= 'Compute days for Advent of Code'
)

parser.add_argument('-d','--day', type= int, choices= range(1,25))
parser.add_argument('-t', '--test', action='store_true')
parser.add_argument('-p', '--part', type=int, choices=range(1,3))
parser.add_argument('-a', '--all', action='store_true')

args = parser.parse_args()


def compute_day_by_part(x):
    if not args.part:
        result_part1 = globals()[f"day{x}"].compute(f"input/input_{x}")
        result_part2 = globals()[f"day{x}"].compute_2(f"input/input_{x}")
        print(f"Jour {x} (p1): {result_part1} \t (p2): {result_part2}")
    elif args.part == 1:
        result_part1 = globals()[f"day{x}"].compute(f"input/input_{x}")
        print(f"Jour {x} (p1): {result_part1}")
    else:
        result_part2 = globals()[f"day{x}"].compute_2(f"input/input_{x}")
        print(f"Jour {x} (p2): {result_part2}")


def compute_day_by_part_test(x):
    with open("test.toml", 'rb') as f:
        test = tomllib.load(f)

    if not args.part:
        result_part1 = globals()[f"day{x}"].compute(f"test_input/input_{x}")
        check_result_part_1 = "✔" if (result_part1 == test[f"day{x}"]["part1"]) else "✘"
        result_part2 = globals()[f"day{x}"].compute_2(f"test_input/input_{x}")
        check_result_part_2 = "✔" if (result_part2 == test[f"day{x}"]["part2"]) else "✘"
        print(
            f"Jour {x} (test) (p1): {result_part1} {check_result_part_1} \t (p2): {result_part2} {check_result_part_2}")
    elif args.part == 1:
        result_part1 = globals()[f"day{x}"].compute(f"test_input/input_{x}")
        check_result_part_1 = "✔" if (result_part1 == test[f"day{x}"]["part1"]) else "✘"
        print(f"Jour {x} (test) (p1): {result_part1} {check_result_part_1}")
    else:
        result_part2 = globals()[f"day{x}"].compute_2(f"test_input/input_{x}")
        check_result_part_2 = "✔" if (result_part2 == test[f"day{x}"]["part2"]) else "✘"
        print(f"Jour {x} (test) (p2): {result_part2} {check_result_part_2}")

def compute_day(x):
    try:
        if not args.test:
            compute_day_by_part(x)
        else:
            compute_day_by_part_test(x)
    except KeyError as Error:
        if not args.all:
            print("This day is not yet implemented.")
            print(traceback.format_exc())
        return False
    else:
        return True



if not args.all:
    compute_day(args.day)
else:
    i = 1
    while compute_day(i):
        i += 1