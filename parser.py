import sys
import re
import csv


#filename = "ts_ippcc_mrg_compl_st_g9.txt"

def log_parser(filename):

    with open(filename) as f:
        log = f.read()
        regex = r'Number of tests : \d+'
        number_tests = re.findall(r'\d+', re.findall(regex, log)[0])
        regex = r'Successes.+\d+'
        success_tests = re.findall(r'\d+', re.findall(regex, log)[0])
        result = int(number_tests[0])/int(success_tests[0])
        print ("%.2f" % result)

    
if __name__ == "__main__":
    log_parser(sys.argv[1])