# python_log_parser
"Log parser" script on python to parse logs in the specified folder depending on input key. Results are put to the generated csv report

### Requirements
- Script works on python3

- Script accepts input values:
    - Folder with logs 
        - Internal structure - Platform_name / "test" / Arcitecture / Domain / file\[optimization\].txt
        - txt file must contain lines: 

            `Number of tests : 'value`                                                      
            `Successes       : 'value`
        - for exch txt file the same name .end file must be presented to make calculation

    - Platform (optional) 
        - linux
        - windows
        - macosx

- Output is generated in csv file. 





