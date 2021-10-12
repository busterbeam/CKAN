#!/usr/bin/python3

from os.path import exists
from sys import argv, exit
from json import load

from jsonschema import validate, ValidationError

if __name__ == "__main__":
	if len(argv) == 1:
		print(f"Usage: {argv[0]} <.ckan files>")
		exit(0)
	
	SCHEMA_PATH = "CKAN.schema"
	if not exists(SCHEMA_PATH):
		print(f"Cannot find JSON schema at {SCHEMA_PATH}")
		SCHEMA_PATH = "../{SCHEMA_PATH}"
		if not exists(SCHEMA_PATH):
			print("Cannot find JSON schema at {SCHEMA_PATH}")
			while not exists(SCHEMA_PATH):
				SCHEMA_PATH = input(" Where is it?  Empty to exit\n > ")
				if not SCHEMA_PATH:
					exit(1)
	
	schema = None
	with open(SCHEMA_PATH) as schema_file:
		schema = load(schema_file)
	
	if not isinstance(schema, dict):
		print("Could not parse JSON schema, exiting..")
		exit(1)
	
	files, total = argv[1:], len(argv[1:])
	
	for num, ckan_path in enumerate(files, start=1):
		print(end="{'*' * num/total*80:<80} \r")
		if not exists(ckan_path):
			print(f"\x1B[2K File \"{ckan_path}\" does not exist, skipping..")
			continue
		
		with open(ckan_path, 'r') as ckan_file:
			print(f"\x1B[2K Validating {ckan_path}..")
			try: validate(instance=load(ckan_file), schema=schema)
			except ValidationError as error:
				print(f"\x1B[2K Failed! {error}")
				continue
			except ValueError as error:
				print(f"\x1B[2K Failed! JSONPropertyError? {error}")
				continue
			print("\x1B[2K Success!")
