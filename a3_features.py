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
    list_of_authors = glob.glob("{}/*".format(args.inputdir)) #mappe
    # print(inputdir)
    author_files = [glob.glob("{}/*".format(author)) for author in list_of_authors]
    flat_author_list = [a.split('/')[-1] for a in list_of_authors]
    # print(flat_author_list)
    # print(list_of_authors)
    def train_author(author, dims, testsize):
        author_list = list()
        i = 0
        for author in author_files:
       
            local_vocab = list()
            author_list.append(author)
            for file in author:
                vocab = ''
                with open(file, "r") as myfile:
                    content = myfile.readlines()
                    # print(content)
                    # break
                    for line in content:
                        # print(line)   
                        for word in line.split():
                            # print(word)
                            if word.isalpha():
                                word = word.lower()
                                vocab = word
                        local_vocab.append(vocab)
            # print(local_vocab)

                              
               


        # vectorize each file to the global vocab
            # print(author)
            vectorizer = CountVectorizer()
            X = vectorizer.fit_transform(local_vocab)

                    # #reduce dims

            svd = TruncatedSVD(n_components=args.dims)
            reduced_dims=svd.fit_transform(X)

                    # # set length of test / train data

            proportion_lenght = len(reduced_dims)*args.testsize//100
                      
                        

                    # set into DF for fitting size
                    # print(author_list)
                    # flat_author_list = [a.split('/')[1] for au in author_list for a in au]
                    # print(flat_author_list)

                    #working




            test = reduced_dims[:proportion_lenght]
            train = reduced_dims[proportion_lenght:]

            train_labeled = pd.DataFrame(data=train, index = ["train"]*len(train))
            test_labeled = pd.DataFrame(data=test, index = ["test"]*len(test))




            f = pd.concat([train_labeled, test_labeled],axis=0)

            f.insert(0,"author", flat_author_list[i])  ### here's the error about -- the names is from a list, so i can either get the whole list or a index of it ... 
                # print(f)
            i = i + 1

        return f

    # print(flat_author_list[0], flat_author_list[1])
    t = [train_author(author, args.dims, args.testsize) for author in flat_author_list]
    print(t)

    # second test / type script


    # test_data = df.sample(frac=proportion_lenght, replace=True)

    # train_data = df.drop(test_data.index)

    # train_data.insert(0, "Train Data", (len(train_data)*["Train"]))
    # test_data.insert(0, "Test Data", (len(test_data)*["Test"]))

    # df = train_data.append(test_data)
    # df.reset_index(inplace=True, drop=True)


    # print(df)



    # third take 

    # df = pd.DataFrame(data=reduced_dims)
    # print(df)

    # df.insert(0, "Author", [flat_author_list]*len(df))
    # print(list_of_authors)
    # print(df)

    # g = pd.DataFrame(t)
    # print(g)
    # g.to_csv(args.outputfile)

    
    print("Writing to {}...".format(args.outputfile))
    # Write the table out here.

    print("Done!")

    
             