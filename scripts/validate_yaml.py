import argparse
import os
from os import listdir
from os.path import isfile, join
from linkml.validator import validate_file

"""
This script validates YAML files against a specified schema using the LinkML validator.
Usage: python validate_yaml.py -y <directory> -s <schema_file> [-c <target_class>]
- `-y` or `--directory`: Path to the directory containing YAML files.
- `-s` or `--schema`: Path to the schema file to validate against.
- `-c` or `--target-class`: Optional target class to validate against.
  If not provided, it validates all classes in the schema.
The script will print any validation errors found in the YAML files.

Examples:
  python ./validate_yaml.py -y ../yaml/20250701_r12/bc -s ../model/cosmos_bc_model.yaml -c BiomedicalConcept
  python ./validate_yaml.py -y ../yaml/20250701_r12/sdtm -s ../model/cosmos_sdtm_model.yaml -c SDTMGroup
  python ./validate_yaml.py -y ../yaml/20251231_draft/bc -s ../model/cosmos_crf_model.yaml -c CRFGroup
"""


def validate_yaml(f, SCHEMA, target_class=None):
    try:
        report = validate_file(f, SCHEMA, target_class)
        if report.results:
            print(f)
            for result in report.results:
                print("ERROR: " + result.message)
    except Exception as e:
        print(f"Error validating {f}: {e}")


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--directory", required=True, help="Input folder with YAML files", dest="directory")
    parser.add_argument("-s", "--schema", required=True, help="Schema file to validate against", dest="schema_file")
    parser.add_argument(
        "-c", "--target-class",
        required=False,
        help="Target class to validate against",
        dest="target_class",
        default=None
    )
    args = parser.parse_args()
    return args


def main():

    args = set_cmd_line_args()

    directory = args.directory
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return

    schema = args.schema_file
    if not os.path.isfile(schema):
        print(f"Schema file {schema} does not exist.")
        return

    target_class = args.target_class

    files = [
        join(directory, f)
        for f in listdir(directory)
        if isfile(join(directory, f)) and os.path.splitext(f)[1] == '.yaml'
    ]
    print(
        f"\nValidating {len(files)} YAML files from {directory}\n"
        f"using schema {schema} and target class "
        f"{target_class if target_class else 'None'}\n"
    )

    for f in files:
        validate_yaml(f, schema, target_class)


if __name__ == "__main__":
    main()
