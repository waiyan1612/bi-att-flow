#!/usr/bin/env bash

# Download GloVe
GLOVE_DIR=glove
mkdir $GLOVE_DIR
wget http://nlp.stanford.edu/data/glove.6B.zip -O $GLOVE_DIR/glove.6B.zip
unzip -o $GLOVE_DIR/glove.6B.zip -d $GLOVE_DIR

# Download NLTK (for tokenizer)
python3 -m nltk.downloader -d $HOME/nltk_data punkt
