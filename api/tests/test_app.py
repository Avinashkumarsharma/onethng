import os
import tempfile
import pytest

def test_ping(client):
    response = client.get("/ping")
    assert response.data == b"pong"