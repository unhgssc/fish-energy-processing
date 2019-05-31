"""
    Binary Table Maker
"""
import itertools, csv, sys

NUM_COLUMNS = 20
OUTPUT_FILE = 'result.csv'
DEBUG_INVALID_ROWS = False
ADD_ROW_NUMBERS = True


# all possible combinations
rows = [i for i in itertools.product([0,1], repeat=NUM_COLUMNS)]

all_columns = [x for x in range(0, NUM_COLUMNS)]
remove_columns = [3, 7, 11, 15, 19]
fishway_columns= set(all_columns) - set(remove_columns)

dam1_columns = range(0,4)
dam2_columns = range(4,8)
dam3_columns = range(8,12)
dam4_columns = range(12,16)
dam5_columns = range(16,20)
dam_dictionary = {
    "1": dam1_columns,
    "2": dam2_columns,
    "3": dam3_columns,
    "4": dam4_columns,
    "5": dam5_columns
}

print("All Columns: {}".format(all_columns))
print("Remove Dam Columns: {}".format(remove_columns))
print("Fishway Columns: {}".format(fishway_columns))

row_index = 0
with open(OUTPUT_FILE, 'wb') as f:
    writer = csv.writer(f)
    try:
        for row in rows:

            invalid = False

            # enforce remove column
            for remove_column in remove_columns:
                if row[remove_column] == 1:

                    # check there is no fishways installed
                    for key in dam_dictionary:
                        #print "check dam: {}".format(key)

                        if remove_column in dam_dictionary[key]:

                            #print "remove column '{}' found '{}'".format(remove_column, dam_dictionary[key])

                            # verify this dams fishways arent installed
                            dam_fishway_columns = set(dam_dictionary[key])- set([remove_column])
                            for dam_fishway_column in dam_fishway_columns:
                                if row[dam_fishway_column] == 1:
                                    invalid = True
                                    break

            if invalid:
                if DEBUG_INVALID_ROWS:
                    print("Invalid Row: {}".format(row))
                continue # dont add this to the output as its an invalid/contradicting run

            row_index += 1

            # add the row
            if ADD_ROW_NUMBERS:
                row = [row_index] + [x for x in row]

            writer.writerow(row)

    except csv.Error as e:
        sys.exit('file {}, line {}, error {}'.format(OUTPUT_FILE, row_index, e))

print("total number of rows added: {}".format(row_index))

