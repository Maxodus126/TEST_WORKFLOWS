import pytest
import boto3
import json
from handler import lambda_handler
@pytest.fixture(scope="module")
def setup_dynamodb():
    yield None
def test_get_students_lambda(setup_dynamodb):
    response = lambda_handler({}, {})
    assert response['statusCode'] == 200
