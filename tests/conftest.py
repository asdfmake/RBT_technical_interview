import pytest
from mixer.backend.sqlalchemy import Mixer

@pytest.fixture
def mixer():
    return Mixer()