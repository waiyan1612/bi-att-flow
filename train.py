import subprocess
import squad.prepro
import basic.cli

print("Beginning downloading glove vectors and nltk ...")
subprocess.call(['./download.sh'])

print("Beginning processing of word vectors ...")
squad.prepro.main()

print("Beginning Training ... This might take a few hours ...")
basic.cli.train()



