import os
import sys
import argparse
import numpy as np
import pandas as pd
# Whatever other imports you need
import glob
import mappe

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
    # parser.add_argument("outputfile", type=str, help="The name of the output file containing the table of instances.")
    parser.add_argument("dims", type=int, help="The output feature dimensions.")
    parser.add_argument("--test", "-T", dest="testsize", type=int, default="20", help="The percentage (integer) of instances to label as test.")

    args = parser.parse_args()
    print("Reading {}...".format(args.inputdir))
    # Do what you need to read the documents here.
    inputdir = glob.glob("{}/*".format(args.inputdir)) #mappe
    list_of_authors = []
    rows_in_array = []
    for directories in inputdir: #baily-s
        list_of_authors.append(directories.split('/')[-1]) #taking the author-name
        files = glob.glob("{}/*".format(directories)) #opening the author-dir
        words = []
        for file in files: #looping through files
            # print(file)

            with open(file, "r") as myfile:
         
                    
                    content = myfile.readlines()

                    
                    for line in content:
                         words += [word.lower() for word in line.split() if (word.isalpha())] #step 1: Create Vocab
        features = defaultdict(int)
        for token in words:
            features[token] += 1
        # print(features)
        

    vectorizer = CountVectorizer()
    array_of_directories = vectorizer.fit_transform(features).toarray()
    print(array_of_directories)

    #print(list_of_authors)
    y = np.array([author for author in list_of_authors])
       
    # print(array_of_authors)
        
    #reduce dim
    #print("Constructing table with {} feature dimensions and {}% test instances...".format(args.dims, args.testsize))
    pca = PCA(n_components = args.dims)
    pca.fit(array_of_directories)
    X = pca.transform(array_of_directories)



    #Classify
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    

    
    #test = args.testsize/100
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test, random_state=30)
    

















                






    
    #print("Writing to {}...".format(args.outputfile))
    # Write the table out here.

   # print("Done!")

    
             