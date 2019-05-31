"""
    process results

    generates one output file generalizing all results

    iterate over a run results file to create one row of processed output
"""

import os, csv

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_FILENAME = "simplified_results.csv"
OUTPUT_FILE = os.path.join(BASE_DIR, OUTPUT_FILENAME)
RUN_FOLDER = os.path.join(BASE_DIR, "successful_result_csv/results_csv")

DATA_DERIVE_METHODS = {
    'Time': None,
    'alewife spawner output': {'Time':54750},
    'shad spawner output': {'Time':54750},
    'salmon spawner output': {'Time':54750},
    'lamprey spawner output': {'Time':54750},
    'total dam removal cost': {'Time':54750},
    'total fishway installation cost': {'Time':54750},
    'total energy generation': {'Sum and Divide':15},
    'total energy revenue': {'Sum and Divide':15},
}

with open(OUTPUT_FILE, 'wb+') as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    num_variables = None # first input file is opened to scan for how many variables it contains
    variables = []
    variable_indexes = []

    for count, filename in enumerate(sorted(os.listdir(RUN_FOLDER))):
        if filename.endswith('.csv'):
            # output row
            row = []

            # run number
            run_number = int(filename.replace('fish-energy-run-', '').replace('.csv', ''))
            row.append(run_number)
            #print("Row with row number!: {}".format(row))

            # count number of variables in input file
            # NOTE: these csvs have headers in column 0 instead of row 0
            # NOTE: only ran once to query number of variables, make sure all files have same variables
            if num_variables == None:
                with open(os.path.join(RUN_FOLDER, filename), 'rb') as infile:
                    num_variables = 0

                    for line in infile:
                        variable_name = line.split(',')[0]
                        variables.append(variable_name)
                        variable_indexes.append(variable_name)
                        num_variables += 1

                    # remove time from variables
                    actual_variables = variables
                    del actual_variables[0]
                    writer.writerow(["Run#"] + variables)

                    #print("Number of Variables: {} Variables: {}".format(num_variables, variables))

            #
            with open(os.path.join(RUN_FOLDER, filename), 'rb') as infile:
                # make sure file is at start position
                infile.seek(0)

                line_index = 0
                for line in infile:
                    variable = variable_indexes[line_index]
                    method = DATA_DERIVE_METHODS[variable]
                    cells = line.split(',')
                    assert variable == cells[0]

                    del cells[0] # remove the variable name from the row

                    if method:
                        if 'Time' in method:
                            #print("length of data for variable: {} len: {}".format(variable, len(cells)))
                            # NOTE: since we pop the first cell we have to adjust our array access
                            value = float(cells[(method['Time'] - 1)])
                            row.append(
                                    value
                            )
                            if (variable == 'total dam removal cost'):
                                if (value != 0.0):
                                    print("variable: {} value: {}".format(variable, value))

                        elif 'Sum and Divide' in method:
                            total = sum(float(cell) for cell in cells)
                            divide = total/method['Sum and Divide']
                            #print("Sum and divide total: {}".format(divide))
                            row.append(divide)
                        else:
                            print "UNKNOWN DATA DERIVATION METHOD"

                    line_index += 1
                #print("Row Done!: {}".format(row))

            writer.writerow(row)
