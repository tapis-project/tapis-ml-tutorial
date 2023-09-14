import argparse, csv
from transformers import pipeline
import os.path
import os

parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--text', required=True)

# Parse the argument
args = str(parser.parse_args())
os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache'
print("after os.env")
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer(args)


# Print output to screen and write to file
tapis_app_id = os.environ.get('_tapisAppId')
print('_tapisAppId: %s\n' % tapis_app_id)
if tapis_app_id is None:
    outputPath = '/tmp/output.txt'
else:
    outputPath = os.path.expandvars('${_tapisSysRootDir}/${_tapisExecSystemOutputDir}/output.txt')
print('Using output path: %s\n' % outputPath)
f = open(outputPath, "a")
print(str(result))
f.write(str(result))
f.close()