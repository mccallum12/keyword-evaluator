![Python application](https://github.com/mccallum12/keyword-evaluator/workflows/Python%20application/badge.svg)

# Keyword Evaluator

This Python script reports the number of keyword occurrences found in a file being evaluated for keywords.

The execution expects that 2 parameters will be supplied - the name of the keyword file and 
the name of the file to be searched for keywords. Both files are expected to be plain text files and 
must be present in the same directory as the Python script.

### Keyword File
This file should contain keyword entries on separate lines in the plain text file. It can represent general 
keywords you want to ensure are in the file to be evaluated or a reduced set of specific ones. You can 
maintain multiple keyword files i.e. one for any job description you want to evaluate your resume for.
* sample(s) provided in project: _"StandardKeywords.txt"_

### File to be Evaluated 
This file should be a plain text version of any file i.e. your resume that you want to evaluate for keyword
occurrence.
* sample(s) provided in project: _"smaples/TechnicalResumeSample1.txt"_

### Output file
This is the file that the results will be written to in CSV format.

### Execution
I run this script from my PyCharm IDE and it uses Python 3.7. I have also run the script from the commandline.
(see the example below)

#### Example:
* _python keyword_evaluator.py StandardKeywords.txt samples/TechnicalResumeSample1.txt results.txt_

# Keyword Extractor

This Python script extracts the keywords (including phrases) found in a file being evaluated for keywords. The script
uses Rapid Automatic Keyword Extraction (RAKE) algorithm is a well-known keyword extraction method which 
uses a list of stopwords and phrase delimiters to detect the most relevant words or phrases in a piece of text.

The execution expects that 2 parameters will be supplied - the name of the stopword file and 
the name of the file to be searched for keywords. Both files are expected to be plain text files and 
must be present in the same directory as the Python script.

### Stopword file
This is a plain text file which contains the "stop" words to be used by the RAKE library to break the text to be 
processed into keywords and phrases. The file included in the project was downloaded. It can be modified or another 
file which has been created by another source can be used - not sure if there are tailored stopwords for extraction 
of keywords from job description, customer reviews, etc. 
* sample(s) provided in project: _"StandardStopwords.txt"_ 
 
### File to have keywords extracted
This file should be a plain text file with the text of anything you wnat to extract the keywords from i.e. a job
description. Either save an existing file as text format or create a new text file and cust/paste the text you want 
to process for keywords into it.
* sample(s) provided in project: _"samples/JobDescriptionSample1.txt, JobDescriptionSample2.txt"_

### Output file
This is the file that the results will be written. Note this file is plain text and not in CSV format. This file could
could be used as the keyword input file for the Keyword Evaluator but remember it contains all keywords found but not
their ranking/weighting so the evaluator will report how many occurrences of a keyword but not the importance. 

### Execution
I run this script from my PyCharm IDE and it uses Python 3.7. I have also run the script from the commandline.
(see the example below)
_**NOTE:** You will need to install the RAKE module - i.e. python -m pip install python-rake_

#### Example:
* _python keyword_extractor.py StandardStopwords.txt sample/JobDescriptionSample2.txt results.txt_
