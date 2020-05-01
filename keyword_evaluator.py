import sys


class KeywordEvaluator:
    '''
    A simple class to evaluate files for occurrences of defined keywords - originally designed to review your
    resume against a defined set of keywords. You can create multiple keyword definition files and evaluate your file
    against any set. You could use a file for general keywords and another file for keywords you have detected
    on a specific job description.
    '''
    TXT_FILE_LINE_SEPARATOR = '\n'

    def __init__(self, kw_filename):
        '''
        The KeywordEvaluator initialization requires a keyword file name which is read to initialize the keyword list
        that will be searched for in an evaluation of a file.
        :param kw_filename:
        '''
        self.keywords_list = []
        kw_file = None
        try:
            # Read keyword file to seed keyword list
            print('Reading keyword file: {}...'.format(kw_filename))
            with open(kw_filename, 'r') as kw_file:
                for line in kw_file:
                    # We are adding each keyword to our keyword list - also need to strip off the line ending so
                    # we split at the line ending and append the keyword portion only
                    self.keywords_list.append(line.split(self.TXT_FILE_LINE_SEPARATOR)[0])
            print('Keyword file: {} read successfully'.format(kw_filename))
        except Exception as err:
            print('Caught Exception opening / reading keyword file: {}', err)
            raise
        # I don't think this is needed with since we used 'with open()'
        finally:
            if kw_file:
                kw_file.close()

    def evaluate_keywords(self, file_to_evaluate_str):
        '''
        Searches the file to be evaluated for occurrences of the keyword that were read at
        instanciation of the evaluator.
        :param file_to_evaluate_str:
        :return: sorted list of result tuples (keyword, detected occurences)
        '''
        evaluation_file = None
        try:
            # Will read the entire file to avoid missing keywords spanning lines (possible?)
            # Only needs to be read once as we will search same copy as we iterate through the keywords
            print('Opening file: {} for keywords evaluation...'.format(file_to_evaluate_str))
            with open(file_to_evaluate_str, 'r') as evaluation_file:
                evaluation_contents_str = evaluation_file.read()
            # For each keyword we will search the file contents and record the instances
            kw_results_list = []
            for keyword in self.keywords_list:
                keyword_count_int = evaluation_contents_str.count(keyword)
                kw_results_list.append((keyword, keyword_count_int))
            print('Successfully evaluated file: {} for keywords'.format(file_to_evaluate_str))
            # Now sort before returning using reverse sort to see highest hits
            # key is set to sort using second element of sublist lambda has been used
            return sorted(kw_results_list, key=lambda x: x[1], reverse=True)
        except Exception as err:
            print('Caught Exception opening / evaluating file for keywords file', err)
            raise
        # I don't think this is needed with since we used 'with open()'
        finally:
            if evaluation_file:
                evaluation_file.close()

    def stats(self, keyword_results_list):
        # Calculate stats on keyword results - the percentage of keywords that have at
        # least 1 occurrence in the file being evaluated
        found_keywords_count = 0
        for result in keyword_results_list:
            if result[1] > 0:
                found_keywords_count += 1
        return round(found_keywords_count/len(keyword_results_list)*100,2), \
                     found_keywords_count, len(keyword_results_list)

    def write_output(self, keyword_results_list, output_file_str):
        '''
        Writes the keyword evaluation results (tuples of keyword and occurrences in the evaluation file) to
        the requested output file.
        :param keyword_results_list:
        :param output_file_str:
        :return:
        '''
        try:
            with open(output_file_str, 'w') as output_file:
                output_file.write("Keyword, Result" + self.TXT_FILE_LINE_SEPARATOR)
                for result in keyword_results_list:
                    # We separate the tuple for the CSV format and then add the line ending
                    output_file.write("'" + result[0] + "'," + str(result[1]) + self.TXT_FILE_LINE_SEPARATOR)
            print('Successfully wrote output file: {} for keywords results'.format(output_file_str))
        except Exception as err:
            print('Caught Exception opening / writing keyword results to file: {}'.format(output_file_str))
            raise
        # I don't think this is needed with since we used 'with open()'
        finally:
            if output_file:
                output_file.close()


def main():
    '''
    Creates an instance of the KeywordEvaluator and completes an evaluation of a file for occurrences of the
    defined keywords - will output the results to the console and additionally to a file if requested.
    All input parameters are passed via commandline arguments

    Commandline ex: Python keyword_evaluator.py keyword_text_file text_file_to_be_evaluated [results_output_file]
    :return:
    '''
    # Make a list of command line arguments, omitting the [0] element which is the script itself.
    args = sys.argv[1:]

    if not args and len(args) < 2:
        print('usage: keyword_file_name file_for_evaluation [--o output file]')
        sys.exit(1)

    try:
        kw_eval = KeywordEvaluator(args[0])
        results_list = kw_eval.evaluate_keywords(args[1])
        keywords_found_float, keywords_found_int, total_keywords_int = kw_eval.stats(results_list)
        print('Summary Results: Found {}% of keywords ({} / {})'.format(
              keywords_found_float, keywords_found_int, total_keywords_int))
        print('Specific Results were {}'.format(results_list))
        if len(args) == 3:
            kw_eval.write_output(results_list, args[2])
    except Exception as err:
        print('Caught Exception opening / evaluating file for keywords file: {}'.format(err))


if __name__ == "__main__":
    main()