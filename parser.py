import sys
import re
import csv
import os 

report_header = ['OS', 'Architecture', 'Domain', 'Optimization', 'Pass Rate']
supported_os = ['linux', 'windows', 'macosx']
ext_txt = '.txt'
ext_end = '.end'

def get_pass_rate(filename):

    with open(filename, 'r') as f:
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


def generate_report(path, os_list):

    report = []
    for os_type in os_list:
        tests_path = os.path.join(path, os_type, 'tests')
        for root, dirs, files in os.walk(tests_path):
            for name in files:
                log_file = os.path.splitext(name)
                if ext_txt in log_file[1]:
                    if log_file[0] + ext_end in os.listdir(root):
                        pass_rate = get_pass_rate(os.path.join(root, name))
                    else: 
                        pass_rate = 'n/a'
                    report.append([os_type] + re.findall(r'\w+', root.split(tests_path)[1]) + re.findall(r'..$',log_file[0]) + [pass_rate])
    return report


def generate_csv(report):

    try:
        with open('result.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(report_header)
            writer.writerows(report)
    except: 
        print("CSV file cannot be created")
        exit(1)
    return

    
if __name__ == "__main__":

    if len(sys.argv) >= 2: 
        if not os.path.exists(sys.argv[1]): 
            print("Path is not correct")
            exit(1)
        path = sys.argv[1]
        if len(sys.argv) >= 3:
            if sys.argv[2] not in supported_os:
                print("OS is not correct")
                exit(1)
            elif sys.argv[2] not in os.listdir(path):
                print("OS is not in folder")
                exit(1)
            os_list = [sys.argv[2]]

        else: 
            os_list = os.listdir(path)

        print("Specified path =", path, "selected OS = ", ', '.join(os_list))
        generate_csv(generate_report(path, os_list))
        print("Completed!")