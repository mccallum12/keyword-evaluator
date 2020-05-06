import sys

import RAKE


class KeywordExtractor:
    TXT_FILE_LINE_SEPARATOR = '\n'

    def __init__(self, keyword_stopword_filename):
        '''
        Initialize the Keyword Extractor and RAKE engine with the RAKE stopword file provided.
        :param keyword_extraction_filename:
        '''
        try:
            self.rake = RAKE.Rake(keyword_stopword_filename)
        except Exception as err:
            print('Caught Exception initializing extractor', err)
            raise

    def extract_keywords(self, keyword_extraction_filename):
        '''
        Performs an extraction of the keywords from the provided file based on RAKE algorithm.
        :param keyword_extraction_filename:
        :return keyword_list: a list of tuples which has the kyword or phrase and ranking/weighting
        '''
        # Open the provided keyword extraction filename to retrieve content before passing to RAKE for
        # keyword extraction
        try:
            print('Opening file: {} for keywords extraction...'.format(keyword_extraction_filename))
            with open(keyword_extraction_filename, 'r') as extraction_file:
                extraction_contents_str = extraction_file.read()
            # We strip out all new line characters and replace with space to make results easier to read
            extraction_contents_str = extraction_contents_str.replace('\n', ' ')
            # Now hand over content to RAKE for keyword extraction
            keyword_list = self.rake.run(extraction_contents_str)
            return keyword_list
        except Exception as err:
            print('Caught Exception opening / processing file for keywords extraction', err)
            raise

    def write_keywords(self, keyword_list, output_file_str):
        '''
        Writes the extracted keywords provided to a text file. The provided keywords (list) were the result of the
        Keyword Extractors extract_keywords function and are expected as tuples (keyword(phrase), weighting).
        Only the keyword or phrase is written to the keyword output file as it is expected to be used with the
        Keyword Evaluator
        :param keyword_list:
        :param output_file_str
        '''
        try:
            with open(output_file_str, 'w') as output_file:
                # output_file.write("Keyword, Result" + self.TXT_FILE_LINE_SEPARATOR)
                for keyword in keyword_list:
                    # We separate the tuple for the CSV format and then add the line ending
                    output_file.write(keyword[0] + self.TXT_FILE_LINE_SEPARATOR)
            print('Successfully wrote output file: {} for keywords'.format(output_file_str))
        except Exception as err:
            print('Caught Exception opening / writing keyword results to file: {}'.format(output_file_str))
            raise


def main():
    '''
    Creates an instance of the KeywordExtractor and completes an extraction of the keywords from a file - will
    output the results to the console and additionally to a file if requested.
    All input parameters are passed via commandline arguments

    Commandline ex:
    Python keyword_extractor.py keyword_stopword_filename text_filename_for_keyword_extraction [results_output_file]
    :return:
    '''
    # Make a list of command line arguments, omitting the [0] element which is the script itself.
    args = sys.argv[1:]

    if not args and len(args) < 2:
        print('usage: keyword_stopword_text_filename text_filename_for_keyword_extraction [--o output file]')
        sys.exit(1)

    try:
        kw_extrctr = KeywordExtractor(args[0])
        results_list = kw_extrctr.extract_keywords(args[1])
        print('Specific Results were {}'.format(results_list))
        if len(args) == 3:
            kw_extrctr.write_keywords(results_list, args[2])
    except Exception as err:
        print('Caught Exception opening / processing file for keywords extraction: {}'.format(err))

if __name__ == "__main__":
    main()