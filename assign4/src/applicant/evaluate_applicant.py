import sys, os, pkgutil
import importlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'utilities'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'evaluate'))

from utilities.evaluation_result import EvaluationResult

def get_criteria():
  criteria_methods = [file_name for _, file_name, _ in pkgutil.iter_modules(
    [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'evaluate')])]
  
  return {criterion.replace('_', " ").title():
    importlib.import_module("evaluate.%s" % criterion) for criterion in criteria_methods}

def evaluate_applicant(applicant, selected_criteria):
  if not selected_criteria:
    return (EvaluationResult.FAIL, 'No criteria was provided')
  
  try:
    evaluation_statuses, evaluation_details = zip(*list(map(
      lambda criterion: criterion.check(applicant), selected_criteria)))
    
    return (max(evaluation_statuses), ', '.join(evaluation_details))
  
  except:
    return (EvaluationResult.FAIL, 'Invalid record found at least for one criteria')
