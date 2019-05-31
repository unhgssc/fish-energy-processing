
BASE_DIR = "" # needed
RUN_FOLDER = os.path.join(BASE_DIR, "runs")

import os


run_numbers = []
for filename in os.listdir(RUN_FOLDER):
    if filename.endswith('.csv'):
        run_number = filename.replace('run-','').replace('.csv','')
        run_numbers.append(run_number)

# print output
print "-"*80
print "Results"
print "-"*80
for number in run_numbers:
    print number
