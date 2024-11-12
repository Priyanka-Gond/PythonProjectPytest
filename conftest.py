import pytest


@pytest.fixture()
#used to setup prerequisites
def setup():
    print("first it will be runed as it is setup method")
    #yield runs post prereuisites like to close browser an ddeleting cookies
    yield
    print("will be executed after the test fixtures")


@pytest.fixture()
def dataload():
    print("we are getting the data from the fixture returned method")
    return ["piryank@", "password", "priya@gmail.com"]


@pytest.fixture(params=["chromre", "firefox", "IE"])
def crossBrowser(request):
    return request.param
