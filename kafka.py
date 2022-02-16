from pytest import mark
from src import scraper
from src import markov

input = {
     "Prozess": "https://www.gutenberg.org/cache/epub/22367/pg22367.txt",
     "Urteil": "https://www.gutenberg.org/files/21593/21593-0.txt",
}

if __name__ == "__main__":
     inputText = scraper.runScrape(input.values())

     wordChain = markov.unifyText(inputText)
     model = markov.model(wordChain)
     for i in range(1,10):
          print(markov.predict_words(model, "Ich", 8)) # print 10 predicted phrases with 8 words
