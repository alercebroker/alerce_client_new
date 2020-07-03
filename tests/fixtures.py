import sys
sys.path.append("..")
from alerce.core import AlerceAPI
import pytest


## TODO 
## Create some responses to use as return_value of mocks
## 
@pytest.fixture
def alerce():
    alerce = AlerceAPI()
    return alerce