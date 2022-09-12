# test_loadbalancer.py

import pytest
import requests
import datetime
import concurrent.futures
from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_mylb(client):
    result = client.get('/', headers={'Host': 'www.mylb.com'})
    #assert b'Web Server' in result.data
    print ('Received: ', result.status_code)

start_time = datetime.datetime.now()
print ('Starting:', start_time)


import time
time.sleep(0)
end_time = datetime.datetime.now()
print ('Finished start time:', start_time, 'duration: ', end_time-start_time)
