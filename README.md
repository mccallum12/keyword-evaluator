# Keyword Evaluator

This Python script reports the number of keyword occurrences found in a file being evaluated for keywords.

The execution expects that 2 parameters will be supplied - the name of the keyword file and 
the name of the file to be searched for keywords. Both files are expected to be plain text files and 
must be present in the same directory as the Python script.

### Keyword File
This file should contain keyword entries on separate lines in the plain text file. It can represent general 
keywords you want to ensure are in the file to be evaluated or a reduced set of specific ones. You can 
maintain multiple keyword files i.e. one for any job description you want to evaluate your resume for.

### File to be Evaluated 
This file should be a plain text version of any file i.e. your resume that you want to evaluate for keyword
occurrence.

### Output file
This is the file that the results will be written to in CSV format

### Execution
I run this script from my PyCharm IDE and it uses Python 3.7. I have also run the script from the commandline.
(see the example below)

#### Example:
* _python keywordevaluator.py keywords.txt "Technical Resume Template 2018 V5.txt" results.txt_
