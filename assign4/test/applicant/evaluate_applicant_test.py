import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))

from applicant.applicant import Applicant
from applicant.evaluate_applicant import evaluate_applicant, get_criteria
from utilities.evaluation_result import EvaluationResult
from evaluate import credit_check, employment_check, criminal_record_check, visa_status_check, formal_education_check

class EvaluateCriteriaApplicantTest(unittest.TestCase):
  def setUp(self):
    self.applicant = Applicant()
  
  def test_get_all_criteria(self):
    self.assertEqual({
      'Credit Check': credit_check,
      'Employment Check': employment_check,
      'Criminal Record Check': criminal_record_check,
      'Formal Education Check': formal_education_check,
      'Visa Status Check': visa_status_check},
      get_criteria())
  
  def test_applicant_empty_criteria(self):
    self.assertEqual((EvaluationResult.FAIL, 'No criteria was provided'),
      evaluate_applicant(self.applicant, []))
  
  def test_pass_applicant_one_passing_criteria(self):
    self.assertEqual((EvaluationResult.PASS, 'Applicant has no criminal record'),
      evaluate_applicant(self.applicant, [criminal_record_check]))
  
  def test_fail_applicant_one_failing_criteria(self):
    self.assertEqual((EvaluationResult.FAIL, 'Applicant has suspicious credit history'),
      evaluate_applicant(self.applicant, [credit_check]))
  
  def test_pass_applicant_two_passing_criteria(self):
    self.assertEqual(
      (EvaluationResult.PASS, 'Applicant has no criminal record, Applicant has previous employment'),
      evaluate_applicant(self.applicant, [criminal_record_check, employment_check]))
  
  def test_fail_applicant_two_failing_criteria(self):
    self.assertEqual(
      (EvaluationResult.FAIL, 'Applicant has suspicious credit history, Applicant do not have valid working visa'),
      evaluate_applicant(self.applicant, [credit_check, visa_status_check]))
  
  def test_fail_applicant_two_passing_one_failing_criteria(self):
    self.assertEqual((EvaluationResult.FAIL,
    'Applicant has no criminal record, Applicant has previous employment, Applicant do not have valid working visa'),
      evaluate_applicant(self.applicant, [criminal_record_check, employment_check, visa_status_check]))
  
  def test_fail_applicant_invalid_criteria(self):
    self.assertEqual((EvaluationResult.FAIL, 'Invalid record found at least for one criteria'),
      evaluate_applicant(self.applicant, [formal_education_check]))
