# LT2212 V20 Assignment 3

pt 1.

Updated 15 th July.

The code for a3.1 works to a certain extend. I had issues getting them concatenated into a nice data structure.
Currently, the code is a bunch of Dataframes, one for each author, rather than one neat structure of something else, say CSV or DF.


The other issue I had was getting around the logic of having the code (which worked for me a long time ago) to process more than one 
set of data, save it and reformat it.

I am still upon delivery struggling with the correct names in my DF, why every author will take the last author name of Enron I do apologize about that.
The solution I ended up (uploading) was a simple index +1 logic, but it didnt seem to work how I intended.




In the end, I ended up making a single function out of it, rather than having it all as run-on code, a function that would be called upon by a single line of code which would engage all the authors
and process them individually and then concatenate them in a df. 

Previous to the function I load in the authors/folders as global variables for the convenience of using them both in the function and outside.





The number of dims have been set to 100.

There is not much preprocessing done to the data, but given its Emails, most have been filtered away using isalpha.

The code can be run on terminal using: python3 a3_features.py enron_sample/ ex 100

