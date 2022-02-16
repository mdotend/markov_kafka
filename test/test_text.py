import unittest
from ..src import markov

class textTest(unittest.TestCase):
    def test_removePunctuation(self):
        self.assertEqual(markov.remove_punctuations(".a."),"a")
    
    def test_replaceNewLines(self):
        self.assertEqual(markov.remove_newlines("a\r\nb"),"a b")


    def test_model(self):
        self.assertEqual(markov.model("a b"), {'a': ['b']})

    def test_prediction(self):
        self.assertEqual(markov.predict_words({'a': ['b']}, "a", 1), "A.")

if __name__ == "__main__":     
     unittest.main()