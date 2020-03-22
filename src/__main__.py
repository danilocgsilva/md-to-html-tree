
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input",
    "-i", 
    type=str, 
    required=True, 
    help="just to test parser"
)

args = parser.parse_args()
input_value = args.input
print("The input value from input is " + input_value)

