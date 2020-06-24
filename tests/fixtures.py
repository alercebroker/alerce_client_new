import sys
sys.path.append("..")
from client.core import ALeRCE
import pytest


## TODO 
## Create some responses to use as return_value of mocks
## 
@pytest.fixture
def alerce():
    alerce = ALeRCE()
    return alerce