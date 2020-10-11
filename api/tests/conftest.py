import pytest
from app import create_app
from flask import Flask
import os
@pytest.fixture(scope="module")
def app():
    """Create and configure a new app instance for each test."""
    os.environ['APP_CFG'] = 'config.DevPyTest'
    app = create_app()
    yield app

@pytest.fixture(scope="module", autouse=True)
def client(app: Flask):
    """A test client for the app."""
    with app.test_client() as tclient:
        return tclient
@pytest.fixture(scope="module")
def runner(app: Flask):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()