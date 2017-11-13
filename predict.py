import subprocess
import basic.cli
import shutil

print("Beginning Prediction ... This might take a few minutes ...")
basic.cli.predict()
shutil.copy2('out/basic/00/answer/predict-020000.csv', './test.csv')

