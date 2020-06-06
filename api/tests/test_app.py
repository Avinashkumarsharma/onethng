import os
import tempfile

import pytest
from flask import current_app as app

def test_hello(client):
    response = client.get("/ping")
    assert response.data == b"pong"