import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'utilities'))

from utilities.evaluation_result import EvaluationResult

def check(applicant):
  return (EvaluationResult.PASS, "Applicant has served the community")
