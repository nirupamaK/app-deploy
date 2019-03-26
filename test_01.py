from http.client import HTTPConnection

import pytest
from pytest_docker_tools import fetch, build, container

#myhost = "192.168.1.104"
my_test_backend_app_image = build(
    path='/root/app-deploy',
)

my_test_backend_app  = container(
    image='{my_test_backend_app_image.id}',
    ports={
        '8000/tcp': '9000/tcp',
    }
)

my_test_redis_server_image = fetch(repository='redis:latest')

my_test_redis_server = container(
    image='{my_test_redis_server_image.id}',
)

@pytest.mark.parametrize("i", list(range(100)))
def test_redist(i, my_test_redis_server):
    assert my_test_redis_server.status == "running"


@pytest.mark.parametrize("i", list(range(100)))
def test_app(i, my_test_backend_app):
    assert my_test_backend_app.status == "running"

@pytest.fixture
def apiclient(my_test_backend_app):
    port = my_test_backend_app.ports['8080/tcp']['9000/tcp']
    return HTTPConnection(f'192.168.1.104:{port}')
