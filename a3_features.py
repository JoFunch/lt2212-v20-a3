import os
import sys
import argparse
import numpy as np
import pandas as pd
# Whatever other imports you need
import glob
import mappe
import enron_sample

from sklearn.base import is_classifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.base import is_classifier
from sklearn.decomposition import TruncatedSVD

from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn.preprocessing import LabelEncoder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert directories into table.")
    parser.add_argument("inputdir", type=str, help="The root of the author directories.")
    parser.add_argument("outputfile", type=str, help="The name of the output file containing the table of instances.")
    parser.add_argument("dims", type=int, help="The output feature dimensions.")
    parser.add_argument("--test", "-T", dest="testsize", type=int, default="20", help="The percentage (integer) of instances to label as test.")

    args = parser.parse_args()
    print("Reading {}...".format(args.inputdir))
    # Do what you need to read the documents here.
    list_of_authors = glob.glob("{}/*".format(args.inputdir)) 
    author_files = [glob.glob("{}/*".format(author)) for author in list_of_authors]
    flat_author_list = [a.split('/')[-1] for a in list_of_authors]



    def train_author(author, dims, testsize):
        author_list = list()
        i = 0
        for author in author_files:
                    #Grab files and content
            local_vocab = list()
            author_list.append(author)
            for file in author:
                vocab = ''
                with open(file, "r") as myfile:
                    content = myfile.readlines()
                    #Tokenize and filter words for non-words, lowercasing
                    for line in content:

                        for word in line.split():

                            if word.isalpha():
                                word = word.lower()
                                vocab = word
                    #Collect items into vocabulary
                        local_vocab.append(vocab) 


                              
               


                    # vectorize each file to the global vocab

            # print(author)
            vectorizer = CountVectorizer()
            X = vectorizer.fit_transform(local_vocab)

                    # #reduce dims

            svd = TruncatedSVD(n_components=args.dims)
            reduced_dims=svd.fit_transform(X)

                    # # set length of test / train data

            proportion_lenght = len(reduced_dims)*args.testsize//100
                      
                        

                    

            # print(author_list)
            # flat_author_list = [a.split('/')[1] for au in author_list for a in au]
            # print(flat_author_list)

            #working

                     # set into DF for fitting size


            test_length = reduced_dims[:proportion_lenght]
            train_length = reduced_dims[proportion_lenght:]

            train_data = pd.DataFrame(data=train_length, index = ["train"]*len(train_length))
            test_data = pd.DataFrame(data=test_length, index = ["test"]*len(test_length))




            df = pd.concat([train_data, test_data],axis=0)

            df.insert(0,"author", flat_author_list[i])  ### here's the error about -- the names is from a list, so i can either get the whole list or a index of it ... 
                # print(f)
            i = i + 1

        return df




    t = [train_author(author, args.dims, args.testsize) for author in flat_author_list]
    print(t)

    
    g = pd.DataFrame(t)
    print(g)
    g.to_csv(args.outputfile)

    
    print("Writing to {}...".format(args.outputfile))
    # Write the table out here.

    print("Done!")

    
             