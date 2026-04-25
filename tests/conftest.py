from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    original_activities = deepcopy(activities)

    for activity_name in list(activities.keys()):
        activities.pop(activity_name)
    activities.update(deepcopy(original_activities))

    yield TestClient(app)

    for activity_name in list(activities.keys()):
        activities.pop(activity_name)
    activities.update(original_activities)
