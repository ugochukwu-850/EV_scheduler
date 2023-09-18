# This file would run insite API test and THIRD party SDk  and API TEST
import dotenv
import os

loaded = dotenv.load_dotenv()

def test_running():
    assert(loaded == True)