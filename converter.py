#usage: python3 converter.py -i <inputfile> -o <outputfile>
import csv
import sys
from optparse import OptionParser

#TODO - Genericize the classes so that it can take in any CSV format.

# There are three multi-value dimensions that are important.
loc_name = 'Location: '
qua_name = 'Qualitative: '
size_name = 'Size: '
maj_name = 'Majors: '
type_name = 'Type: '
sel_name = 'Selectivity: '
pay_name = 'Paying: '
cre_name = 'Credit: '
oth_name = 'Other: '
dim1_name = 'Qualitative, Majors: '
dim2_name = 'Size, Type, Selectivity: '
dim3_name = 'Location, Size, Majors: '
tot_name = 'Total: '

class SomeCollection:
    location = 0
    qualitative = 0
    size = 0
    majors = 0
    type = 0
    selectivity = 0
    paying = 0
    credit = 0
    other = 0
    qualitative_majors = 0
    size_type_selectivity = 0
    location_size_majors = 0
    total = 0
    data = []

    def all(self, f):
        if self.location  > 0:
            f.write(loc_name + str(self.location)
                                + '/'
                                + str(int(self.location
                                * (100/self.total)))
                                + '%\n')
        if self.qualitative  > 0:
            f.write(qua_name + str(self.qualitative)
                                + '/'
                                + str(int(self.qualitative
                                * (100/self.total)))
                                + '%\n')
        if self.size  > 0:
            f.write(size_name + str(self.size)
                                + '/'
                                + str(int(self.size
                                * (100/self.total)))
                                + '%\n')
        if self.majors  > 0:
            f.write(maj_name + str(self.majors)
                                + '/'
                                + str(int(self.majors
                                * (100/self.total)))
                                + '%\n')
        if self.type  > 0:
            f.write(type_name + str(self.type)
                                + '/'
                                + str(int(self.type
                                * (100/self.total)))
                                + '%\n')
        if self.selectivity  > 0:
            f.write(sel_name + str(self.selectivity)
                                + '/'
                                + str(int(self.selectivity
                                * (100/self.total)))
                                + '%\n')
        if self.paying  > 0:
            f.write(pay_name + str(self.paying)
                                + '/'
                                + str(int(self.paying
                                * (100/self.total)))
                                + '%\n')
        if self.credit  > 0:
            f.write(cre_name + str(self.credit)
                                + '/'
                                + str(int(self.credit
                                * (100/self.total)))
                                + '%\n')
        if self.other  > 0:
            f.write(oth_name + str(self.other)
                                + '/'
                                + str(int(self.other
                                * (100/self.total)))
                                + '%\n')
        if self.qualitative_majors  > 0:
            f.write(dim1_name + str(self.qualitative_majors)
                                + '/'
                                + str(int(self.qualitative_majors
                                * (100/self.total)))
                                + '%\n')
        if self.size_type_selectivity  > 0:
            f.write(dim2_name + str(self.size_type_selectivity)
                                + '/'
                                + str(int(self.size_type_selectivity
                                * (100/self.total)))
                                + '%\n')
        if self.location_size_majors  > 0:
            f.write(dim3_name + str(self.location_size_majors)
                                + '/'
                                + str(int(self.location_size_majors
                                * (100/self.total)))
                                + '%\n')
        if self.total  > 0:
            f.write(tot_name + str(self.total)
                                + '/'
                                + str(int(self.total
                                * (100/self.total)))
                                + '%\n')

    def addSomeData(self, rowData):

        self.data.append(rowData)

        if rowData.location:
            self.location += 1
            self.total += 1

        if rowData.qualitative:
            self.qualitative += 1
            self.total += 1

        if rowData.size:
            self.size += 1
            self.total += 1

        if rowData.majors:
            self.majors += 1
            self.total += 1

        if rowData.type:
            self.type += 1
            self.total += 1

        if rowData.selectivity:
            self.selectivity += 1
            self.total += 1

        if rowData.paying:
            self.paying += 1
            self.total += 1

        if rowData.credit:
            self.credit += 1
            self.total += 1

        if rowData.other:
            self.other += 1
            self.total += 1

        if rowData.qualitative and rowData.majors:
            self.qualitative_majors += 1
            self.total += 1

        if rowData.size and rowData.type and rowData.selectivity:
            self.size_type_selectivity += 1
            self.total += 1

        if rowData.qualitative and rowData.majors:
            self.location_size_majors += 1
            self.total += 1

class SomeData:
    rowname = ''
    location = 0
    qualitative = 0
    size = 0
    majors = 0
    type = 0
    selectivity = 0
    paying = 0
    credit = 0
    other = 0
    qualitative_majors = 0
    size_type_selectivity = 0
    location_size_majors = 0
    total = 0

    def __init__(self, row):
        self.rowname = row["\ufeffName"]

        if str.isalpha(row["Location"]):
            self.location += 1
            self.total += 1

        if str.isalpha(row["Qualitative"]):
            self.qualitative += 1
            self.total += 1

        if str.isalpha(row["Size"]):
            self.size += 1
            self.total += 1

        if str.isalpha(row["Majors"]):
            self.majors += 1
            self.total += 1

        if str.isalpha(row["Type"]):
            self.type += 1
            self.total += 1

        if str.isalpha(row["Selectivity"]):
            self.selectivity += 1
            self.total += 1

        if str.isalpha(row["Paying"]):
            self.paying += 1
            self.total += 1

        if str.isalpha(row["Credit"]):
            self.credit += 1
            self.total += 1

        if str.isalpha(row["Other"]):
            self.other += 1
            self.total += 1

        if self.qualitative > 0 and self.majors > 0:
            self.qualitative_majors += 1
            self.total += 1

        if self.size > 0 and self.type > 0 and self.selectivity > 0:
            self.size_type_selectivity += 1
            self.total += 1

        if self.qualitative > 0 and self.majors > 0:
            self.location_size_majors += 1
            self.total += 1

    def all(self):

        if self.location  > 0:
            f.write(loc_name + str(self.location)
                                + '/'
                                + str(int(self.location
                                * (100/self.total)))
                                + '%\n')

        if self.qualitative  > 0:
            f.write(qua_name + str(self.qualitative)
                                + '/'
                                + str(int(self.qualitative
                                * (100/self.total)))
                                + '%\n')
        if self.size  > 0:
            f.write(size_name + str(self.size)
                                + '/'
                                + str(int(self.size
                                * (100/self.total)))
                                + '%\n')
        if self.majors  > 0:
            f.write(maj_name + str(self.majors)
                                + '/'
                                + str(int(self.majors
                                * (100/self.total)))
                                + '%\n')

        if self.type  > 0:
            f.write(type_name + str(self.type)
                                + '/'
                                + str(int(self.type
                                * (100/self.total)))
                                + '%\n')
        if self.selectivity  > 0:
            f.write(sel_name + str(self.selectivity)
                                + '/'
                                + str(int(self.selectivity
                                * (100/self.total)))
                                + '%\n')

        if self.paying  > 0:
            f.write(pay_name + str(self.paying)
                                + '/'
                                + str(int(self.paying
                                * (100/self.total)))
                                + '%\n')

        if self.credit  > 0:
            f.write(cre_name + str(self.credit)
                                + '/'
                                + str(int(self.credit
                                * (100/self.total)))
                                + '%\n')

        if self.other  > 0:
            f.write(oth_name + str(self.other)
                                + '/'
                                + str(int(self.other
                                * (100/self.total)))
                                + '%\n')

        if self.qualitative_majors  > 0:
            f.write(dim1_name + str(self.qualitative_majors)
                                + '/'
                                + str(int((self.qualitative_majors
                                * (100/self.total))))
                                + '%\n')


        if self.size_type_selectivity  > 0:
            f.write(dim2_name + str(self.size_type_selectivity)
                                + '/'
                                + str(int(self.size_type_selectivity
                                * (100/self.total)))
                                + '%\n')

        if self.location_size_majors  > 0:
            f.write(dim3_name + str(self.location_size_majors)
                                + '/'
                                + str(int(self.location_size_majors
                                * (100/self.total)))
                                + '%\n')

        if self.total  > 0:
            f.write(tot_name + str(self.total)
                                + '/'
                                + str(int(self.total
                                * (100/self.total)))
                                + '%\n')

# The presence of a value or a multi-value dimension scores a point.
# The points are added together to produce a total.
# Each value or a multi-value dimension gets a percentage contribution to the total score.

# Command line arguments for filenames
parser = OptionParser()

# Name of the CSV input file to parse
parser.add_option("-i",
                    "--input",
                    action="store",
                    type="string",
                    dest="inputfile",
                    help="get csv data from FILE",
                    metavar="INPUT")

## Name of the TXT file you want to output
parser.add_option("-o",
                    "--output",
                    action="store",
                    type="string",
                    dest="outputfile",
                    help="write information to FILE",
                    metavar="OUTPUT")
try:
    (options, args) = parser.parse_args()
    # print ('Input file is ', options.inputfile)
    # print ('Output file is ', options.outputfile)
except:
    print(f'Unexpected error:', sys.exc_info()[0])

# keep track of the counts for the whole file
collection = SomeCollection()

# Read the file into a dictionary
# TODO Handle FileNotFoundError
#try:
with open(options.inputfile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    # print(f'csv_reader: ', str(csv_reader))

    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1

        rowData = SomeData(row)
        collection.addSomeData(rowData)
        line_count += 1
        # print(f'Processed {line_count} lines.')

with open(options.outputfile, mode='w') as f:

    #Write collection information
    f.write('All\n')
    collection.all(f)
    f.write('\n')

    #Write row by row information
    for rowData in collection.data:
        f.write(rowData.rowname + '\n')
        if rowData.total > 0:
            rowData.all()
        f.write('\n')

#except:
#    print(f'EXCEPTION')
