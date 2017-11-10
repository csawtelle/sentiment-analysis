pip3 install nltk

create a simple text file

import nltk

nltk.download() # nltk.download('all') will download everything to the default directory

if you change the default directory you ned to add it to the path

nltk.data.path.append("/build/nlp/nltk_data/")

This will give you an interactive menu where you can change the download directory in the config (c) and choose which files to download (d)


