"""
    find missing runs

    given a folder marks each run number found, then based off highest number checks for any missing
"""
import os, csv

BASE_DIR = "/home/wsk4/code/fish-energy-tradeoff-vensim" # needed
RUN_FOLDER = os.path.join(BASE_DIR, "results_csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "MissingRunRecords_070219_2.csv")
INPUT_FILE = os.path.join(BASE_DIR, "RunRecords.csv")

highest_run_number = -1


# find existing
run_numbers = []
for filename in os.listdir(RUN_FOLDER):
    if filename.endswith('.csv'):
        run_number = int(filename.replace('fish-energy-run-','').replace('.csv',''))
        run_numbers.append(run_number)
        if run_number > highest_run_number:
            highest_run_number = run_number


# find missing
print("check for missing: (highest: {})".format(highest_run_number))
missing_run_numbers = []
for i in range(1, highest_run_number):
    if i not in run_numbers:
        #print("found missing: {}".format(i))
        missing_run_numbers.append(i)


# print output
print("-"*80)
print("Results for Missing Run Numbers: (length: {})".format(len(missing_run_numbers)))
print("-"*80)
#for number in missing_run_numbers:
#    print number


# iterate RunRecords to form MissingRunRecords
linecount = 1 # starts at line 1 as there is no header
with open(INPUT_FILE, 'rb') as infile, open(OUTPUT_FILE, 'w+') as outfile:
    reader = csv.reader(infile, delimiter=',', quoting = csv.QUOTE_MINIMAL)
    writer = csv.writer(outfile, delimiter=',', quoting = csv.QUOTE_MINIMAL)
    for line in reader:
        if linecount in missing_run_numbers:
            writer.writerow(line)
        linecount += 1

