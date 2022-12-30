import os
import re
import sys
import json
import argparse
import gensim
import sklearn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Grab root directory for project (FIXME)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TODO: Turn into Class
'''
- topic models will train and inference on threads
- topic models and outputs will be saved and stored in database
- 
'''

def find_relevant_topics(model, topics, nums):
    """
    Pick the relevant topics to the problem
    :param: topics
    :param: nums
    :return:
    """
    new_topics = []
    for n in nums:
        new_topics.append(str(topics[n]))

    return new_topics


def display_generate_topics(model, output):
    """
    Write topics to a file
    :param model: LDA model
    :param output: Output file name
    :return:
    """
    topics = {}
    write_output = open(ROOT + '/topic_model/performance/' + output, 'w+')
    for topic, words in model.print_topics(-1):
        write_output.write("\nTopic: {}".format(topic))
        words = re.sub(r'[\+\*]', '', words)
        print(words)
        write_output.write("\nWords: {}\n".format(words))
        match = re.findall(r'\"([A-Za-z])*\"', words)
        print(match)
        sys.exit(0)
        word_distribution = model.show_topics(topic)
        # print(word_distribution)
        keywords = ', '.join([word for word, prop in word_distribution])
        topics[topic] = keywords
    
    with open(ROOT + '/topic_model/performance/topics.json', 'w+') as file:
        json.dump(topics, file)
    
    return topics


def fit_model(corpus, vocab, docs):
    """
    Fits a Latent Dirichlett Allocation model
    :param corpus: BoW corpus
    :param vocab: vocabulary mappings for corpus
    :param docs: documents
    return:
    """
    model = gensim.models.LdaModel(corpus=corpus, 
                                   num_topics=10, 
                                   alpha=0.4, 
                                   eta=0.05,
                                   passes=3,
                                   id2word=vocab, 
                                   per_word_topics=True)
    return model

    
def create_bow_corpus(docs):
    """
    Using Sklearn's CountVectorizer, we create a Bag-of-words representation of the corpus
    :param corpus: Collection of documents
    :return: A vectorized corpus and vocabulary
    """
    vectorizer = CountVectorizer()
    corpus = vectorizer.fit_transform(docs)
    vocab = vectorizer.get_feature_names()
    vocab = dict([(i, s) for i, s in enumerate(vocab)])
    corpus = gensim.matutils.Sparse2Corpus(corpus.T)

    return corpus, vocab


def clean_document(text):
    """
    Executes the final round of data cleaning
    :param text: A single tweet
    :return: A processed tweet ready for vectorization 
    """
    processed_docs = []
    text = re.sub(r'\d+', '', str(text))
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            processed_docs.append(gensim.parsing.preprocessing.stem(token))
    
    return ' '.join(processed_docs)


def data_processing(dataset, nouns=False):
    """
    Executes the functions to prepare our data to fit the model
    :param dataset: The dataset of Tweets
    :param nouns:  A boolean value indicating usage of only nouns
    :return: we'll see :)
    """
    # TODO: Parallelize?
    docs = list()
    for tweet in dataset['clean_text']:
        docs.append(clean_document(tweet))

    if nouns:
        print("- Filtering nouns -")
        # TODO: Fill out conditional
    
    corpus, vocab = create_bow_corpus(docs)

    return corpus, vocab, docs
    

def parse_cli():
    """
    Reads from command-line arguments
    :return: args
    """
    parser = argparse.ArgumentParser(description='Topic model settings')
    parser.add_argument('--i', type=str, help='Input file')
    parser.add_argument('--o', type=str, help='Output file')
    parser.add_argument('--n', type=str, default='', help='Option to use only nouns')

    return parser.parse_args()


def main(args):
    """
    Run streamer
    """
    if args.i is None:
        print("- Need input file -")
        sys.exit(0)

    if args.o is None:
        print("- Need output file -")
        sys.exit(0)
    
    nouns = None
    if args.n is None:
        nouns = False
    
    output = args.o

    cols = ['created_at', 'tweet_id', 'text', 'clean_text', 'hashtags', 'user_id']
    dataset = pd.read_csv(ROOT + '/data/' + args.i, names=cols)

    # Send our data to another round of processing
    corpus, vocab, docs = data_processing(dataset, nouns)

    # Fit the LDA model to the data
    model = fit_model(corpus, vocab, docs)

    # Display topics
    display_generate_topics(model, output)

    # topics_num = 
    find_relevant_topics(model, topics)


if __name__ == '__main__':
    main(parse_cli())
