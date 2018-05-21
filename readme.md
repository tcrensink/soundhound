# Project organization
- **readme.md**: (this file) contains installation, task description, and brief description of solution
- **driver**: the (python) executable, called as `./driver ./text_samples/text.txt`
- **setup.sh**: a bash setup file to create a conda environment and install dependencies 
- **environment.yml**: environment file to construct conda environment 
- **utils**: scripts to produce text_samples, and english_corpus unigram and bigram text files 
- **text_samples**: includes the complete '20 newsgroups' corpus of test documents, generated from sklearn

# Requirements to run driver (specificss in environment.yml):
- pandas
- scikit-learn
- python 3.6

# Run ./driver
**If requirements are satisfied:**: navigate to folder containing driver and run `./driver text_samples/article_18795`
**If requirements are not satisfied:** run `setup.sh` to create a conda env with dependencies from environment.yml.  Instructions will be printed to terminal to activate the environment and run `./driver text_samples/article_18795`

# Problem description (skip to next section)
You can select any input document/article for the same, and your submission should include the input file, code, and a readme file which can describe your process.

1. Create a driver that will read in an input file, specified on the command line, and construct a mapping between each unique word in the document and the frequency with which it occurs.

2. Write a method, called performTermExtraction that takes in the constructed map and returns a set of terms that has between three (3) and seven (7) terms that are somewhat representative of what the content of the document is. The procedure for eliminating the terms from the frequency map is as follows:
    a. Eliminate the most frequent term
    b. Eliminate the two least frequent terms
    c. Repeat steps (a) and (b) until the number of words in your frequency map is between three (3) and seven (7)

3. The result of the program should be the following two pieces of data printed out to the command line:
     a. The original frequency map
     b. The extracted terms

4. If you feel you understand what is taking place in step two (2), you are welcome to adjust the elimination ratios and experiment empirically to find a “better” means of terms elimination. This way you should be able to find the gist of the article or text.

5. (optional). Can you extend the functionality to allow terms to be either 1 or 2 words (instead of assuming every term is 1 word)? You should avoid including in your output any ‘overlapping’ terms (e.g. don’t include “Donald Trump”, “Donald”, and “Trump”).

You can make assumptions (make sure to mention them), and generate a sample input file by yourself to work on the same.

(clarifications)
- Since it is an open ended question, we would focus more on creativity, approach to the problem, coding style (but wouldn't encourage to spend too much time on that), and most importantly what conclusions you arrive for any sample dataset you chose.
- Just handle any one type, a text (.txt) file which could be any news article. 
- Feel free to use any library, nltk or sci-kit, or any frameworks.
- That means, your submission would comprise of the sample article (\*.txt file or files) you chose as the input to your program. List any assumptions you made or your approach in a readme.txt file which would illustrate high level steps you did to solve this problem)

# General comments on solutions
The solution uses sklearn and pandas (NLTK could also have been used), using essentially uses a (simplified) 'bag of words' model.  Sklearn.feature_extraction.text.CountVectorizer tokenizes the text file and creates a frequency table using the default regex pattern `(?u)\b\w\w+\b`; this excludes single character strings and treats punctuation as separators.  Several "solutions" are included.  The code has been tested on short documents and has not been performance optimized for very long documents.

# Basic solution to problem description parts 1, 2 ,3:
- Terms are sorted by frequency, and subsorted alphabetically.  This is a niave and undesirable for "flat" distributions (short documents have long tails with words of equal count, e.g. n=1).  This is improved in subsequent solutions.  Other bits:
- No stop words are removed to adhere closely to challenge guidelines
- Keywords are selected according to the rule: "remove the most frequent term, remove least two frequent terms; repeat until seven or fewer terms remain."  The algorithm is implemented with divmod for efficiency.

# Solution 2:
This solution includes the following modifications to the basic solution:
- a default set of [stop words](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/stop_words.py) is excluded
- terms with equal frequency in the document are subsorted by their 'global' frequency across a [corpus](http://norvig.com/ngrams/) of words 333,332 words.  This is *highly* preferable to alphabetical subsorting, esp. for short documents.

# Solution 3:
In addition to the previous solution:

- a score similar to [tf-idf](https://en.wikipedia.org/wiki/Tf–idf) is used as an improved measure of word value.  Here, the score is weighted by its occurence in the document (to some power) and inversely weighted by its general frequency of appearance. If the corpus reflects typical usage frequency of a term, this score will normalize by that frequency, and augment words that are both common in the document and relatively rare otherwise.  There are more sophisticated versions similar to this score.

# Solution 4 (not fully implemented):
- The same as solution 3 but implemented with bigrams. The standard method for calculating bigrams is via the conditional probability of the second word given the first.  Unigram/bigram entries could be filtered by taking whichever maxed a score like in soln 3.  This was not implemented; the bigram solution in the code does not filter out repeated bigram/unigram terms.

# More advanced solutions (not implemented):
- A supervised model could be trained on wikipedia data.  Wikipedia includes body text and titles; a parameterized score like that in soln 3 could be fit to find a score that maximizes the score of the corpus/documnt frequency data to match that of title words.

- It would be interesting to try clustering of the words in some embedding model like word2vec; one could measure the size and density of a cluster using something like k-means and then scoring a cluster based on their density (average inverse distance of all points) and number N/k in cluster.

