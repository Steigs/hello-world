# page 220
import pytest
from ch11_survey import AnonymousSurvey

pytest.fixture
def language_survey():
    '''A survey that will be available to all test functions'''
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response():
    '''Test that a single response is stored properly'''
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    '''Test that three individual responses are stores properly.'''
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses