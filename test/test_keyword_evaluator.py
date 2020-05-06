import os
import unittest

import keyword_evaluator

MODULE_DIR = os.path.abspath(os.path.dirname(__file__))
EVAL_DIR = os.path.abspath(os.path.dirname(keyword_evaluator.__file__))


class KeywordEvaluatorTest(unittest.TestCase):
    TEST_KEYWORD_FILE_NAME = os.path.join(MODULE_DIR, 'EvaluatorTestKeywords.txt')
    TEST_KEYWORD_EVALUATE_FILE_NAME = os.path.join(EVAL_DIR, 'samples/TechnicalResumeSample1.txt')
    TEST_KEYWORD_EVALUATION_RESULTS_FILE = os.path.join(MODULE_DIR, 'EvaluatorTestOutputFile.txt')
    TEST_KEYWORDS = ['SQL']
    TEST_KEYWORD_RESULTS = [
        ('SQL', 5)
    ]

    def setUp(self):
        self.kw_eval = keyword_evaluator.KeywordEvaluator(self.TEST_KEYWORD_FILE_NAME)

    def tearDown(self):
        self.kw_eval = None

    '''
    Test the loading of the keywords from the keyword file
    '''
    def test_keyword_loading(self):
        for keyword in self.TEST_KEYWORDS:
            self.assertEqual(1, self.kw_eval.keywords_list.count(keyword),
                             'Expected Keyword: {} not found in test file {}'.
                             format(keyword, self.TEST_KEYWORD_FILE_NAME))

    '''
    Test the keyword evaluation of the evaluation file - checking only the high level stats reporting
    function which will report found percentage, number of keywords found (not occurrence) and 
    total number of keywords evaluated 
    '''
    def test_keyword_evaluation_stats(self):
        results_list = self.kw_eval.evaluate_keywords(self.TEST_KEYWORD_EVALUATE_FILE_NAME)
        result_percent, result_kw_found, result_kw_total = self.kw_eval.stats(results_list)
        self.assertEqual(100, result_percent, 'Keywords evaluation result not as expected')
        self.assertEqual(len(self.TEST_KEYWORDS), result_kw_found, 'Keywords found result not as expected')
        self.assertEqual(len(self.TEST_KEYWORDS), result_kw_total, 'Keyword totals not as expected')

    '''
    Test the keyword evaluation of the evaluation file - check the keyword was found and the number of 
    occurrences
    '''
    def test_keyword_evaluation(self):
        results_list = self.kw_eval.evaluate_keywords(self.TEST_KEYWORD_EVALUATE_FILE_NAME)
        self.assertEqual(len(self.TEST_KEYWORD_RESULTS), len(results_list),
                         'Keywords evaluation did not find expected keyword')
        for kw_result in self.TEST_KEYWORD_RESULTS:
            self.assertIn(kw_result, results_list,
                          'Keyword occurrence {}, not found in results'.format(kw_result))

    '''
    Test the writing of the keyword evaluation result to the output file
    '''
    def test_output_file(self):
        results_list = self.kw_eval.evaluate_keywords(self.TEST_KEYWORD_EVALUATE_FILE_NAME)
        self.kw_eval.write_output(results_list, self.TEST_KEYWORD_EVALUATION_RESULTS_FILE)
        with open(self.TEST_KEYWORD_EVALUATION_RESULTS_FILE, 'r') as results_file:
            results_contents_str = results_file.read()
        self.assertIsNotNone(results_contents_str, 'Keyword evaluation results file contents were None')
        for kw_result in self.TEST_KEYWORD_RESULTS:
            self.assertIn("'" + kw_result[0] + "'," + str(kw_result[1]), results_contents_str,
                          'Keyword occurrence {}, not found in results'.format(kw_result))


if __name__ == '__main__':
    unittest.main()
