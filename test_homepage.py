import pytest

def testfixturedemo(setup):
    print("after fixture we will execute")

@pytest.mark.xfail
def testhomepagefb():
    print("HI We are inside fb home page")

def testfbposts():
    print("We are inside the posts")
@pytest.mark.smoke
def testfbcomments():
    msg="We are viewing comments"
    assert msg=="hi","the test failed because there is an issue with the comments section"