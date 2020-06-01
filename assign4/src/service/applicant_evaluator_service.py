import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from applicant.evaluate_applicant import evaluate_applicant, get_criteria
from applicant.applicant import Applicant

if __name__ == '__main__':
  print('\nPlease select the criteria by yes [y] or no [n]')
  
  selected_criteria = []
  for criterion_name, criterion in get_criteria().items():
    print('\nDo you want to include the criteria "' + criterion_name + '"? [y/n]')
    
    user_input = input()
    while user_input not in ['y', 'n']:
      print('\nPlease provide y or n only!')
      user_input = input()
    
    if user_input == 'y':
      selected_criteria.append(criterion)
  
  evaluation_status, evaluation_details = evaluate_applicant(Applicant(), selected_criteria)
  
  print('\nEvaluation Status: ' + evaluation_status.name.title())
  print('Evaluation Details: ' + evaluation_details + '\n')
