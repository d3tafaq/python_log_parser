import sys
import re
import csv
import os 
import glob


str_txt = '*.txt'
str_end = '*.end'

def get_log_files(path):
    file_list = []
    path = path + '/**/' + str_txt #ToDo: cange to another mathod
    for file in (glob.glob(path, recursive=True)):
        new_path = file[:-4] + str_end
        if glob.glob(new_path): 
            file_list.append(file)
    return file_list

def generate_report(files):
    report = []
    for file in files:
        path_parsed = re.findall(r'\w+', file)
        parameters = [item for item in path_parsed[-6:-2] if item != 'tests']
        parameters.append(re.findall(r'..$', path_parsed[-2])[0])
        parameters.append(get_pass_rate(file))
        print(parameters)
        report.append(parameters)

    return report

def generate_csv(report):

    return

def get_pass_rate(filename):

    with open(filename) as f:
        log = f.read()
        number_tests = 0
        success_tests = 0
        if (re.search(r'Number of tests', log)):
            number_tests = re.findall(r'\d+', re.findall(r'Number of tests.*\d+', log)[0])
            if (re.search(r'Successes', log)):
                success_tests = re.findall(r'\d+', re.findall(r'Successes.*\d+', log)[0])
                result = int(success_tests[0])/int(number_tests[0]) * 100
                return ("%.2f" % result)
        else:
            return 'Aborted'

    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please, provide path to folder")
        exit(1)
    
    os_type = "all"
    path = sys.argv[1]
    try:
        os_type = sys.argv[2]
        print("OS type is", os_type)
    except:
        print("OS type is not specified")

    print("Specified path is", path, "selected OS is", os_type)


    generate_csv (generate_report (get_log_files(path)))


