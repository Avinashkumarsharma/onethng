import pytest
from app import create_app
from flask import Flask
@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app

@pytest.fixture
def client(app: Flask):
    """A test client for the app."""
    return app.test_client()
@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()