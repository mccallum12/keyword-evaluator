import os
import unittest

import keyword_extractor

MODULE_DIR = os.path.abspath(os.path.dirname(__file__))
EXTRACT_DIR = os.path.abspath(os.path.dirname(keyword_extractor.__file__))


class KeywordExtractorTest(unittest.TestCase):
    TEST_KEYWORD_EXTRACT_STOPWORD_FILE_NAME = os.path.join(EXTRACT_DIR,'StandardStopwords.txt')
    TEST_KEYWORD_EVALUATE_FILE_NAME = os.path.join(MODULE_DIR, 'ExtractorTestText.txt')
    TEST_KEYWORD_EXTRACTION_RESULTS_FILE = os.path.join(MODULE_DIR, 'ExtractorTestOutputFile.txt')
    TEST_KEYWORD_EXTRACTION_RESULTS = [
        ('mobile version works', 8.5),
        ('web version', 4.5),
        ('create pages', 4.0),
        ('simple controls', 4.0),
        ('love', 1.0),
        ('app', 1.0),
        ('amazing', 1.0),
        ('control', 1.0),
        ('content', 1.0),
        ('displayed', 1.0),
        ('easily', 1.0),
        ('intuitive', 1.0)
    ]

    def setUp(self):
        self.kw_extrctr = keyword_extractor.KeywordExtractor(self.TEST_KEYWORD_EXTRACT_STOPWORD_FILE_NAME)

    def tearDown(self):
        self.kw_extrctr = None

    '''
    Test the keyword extraction from the evaluation file - check the keywords were found and the 
    ranking / weighting as expected
    '''
    def test_keyword_extraction(self):
        results_list = self.kw_extrctr.extract_keywords(self.TEST_KEYWORD_EVALUATE_FILE_NAME)
        self.assertEqual(len(self.TEST_KEYWORD_EXTRACTION_RESULTS), len(results_list),
                         'Keywords extraction did not find expected keyword')
        for kw_result in self.TEST_KEYWORD_EXTRACTION_RESULTS:
            self.assertIn(kw_result, results_list,
                          'Keyword occurrence {}, not found in results'.format(kw_result))

    '''
    Test the writing of the keyword evaluation result to the output file
    '''
    def test_output_file(self):
        results_list = self.kw_extrctr.extract_keywords(self.TEST_KEYWORD_EVALUATE_FILE_NAME)
        self.kw_extrctr.write_keywords(results_list, self.TEST_KEYWORD_EXTRACTION_RESULTS_FILE)
        with open(self.TEST_KEYWORD_EXTRACTION_RESULTS_FILE, 'r') as results_file:
            results_contents_str = results_file.read()
        self.assertIsNotNone(results_contents_str, 'Keyword evaluation results file contents were None')
        for kw_result in self.TEST_KEYWORD_EXTRACTION_RESULTS:
            self.assertIn(kw_result[0], results_contents_str,
                          'Keyword occurrence {}, not found in results'.format(kw_result))


if __name__ == '__main__':
    unittest.main()
