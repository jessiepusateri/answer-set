import os
import subprocess
import glob

'''
For each file with 'evals_*.txt' format in evals/ folder, creates an output file with 'output_*.txt' format in the output/ folder.
'''

filenames = glob.glob('evals/evals_*.txt')
for filename in filenames:
  filename = filename[12:-4]
  cmd = './dlv -pfilter=class,isa,ins,link classes.inpho.txt evals/evals_{0}.txt program.txt 1> output/output_{0}.txt'.format(filename)
  print 'Creating output/output_{0}.txt'.format(filename)
  subprocess.call(cmd, shell=True)
