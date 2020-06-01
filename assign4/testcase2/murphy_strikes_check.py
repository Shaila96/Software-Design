import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'utilities'))

from utilities.evaluation_result import EvaluationResult

def check(applicant):
  raise Exception("Anything that can go wrong will go wrong—Murphy's Law")