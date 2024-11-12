import logging

import pytest

from pytestfacebook.Baseclass import Baseclass1
from pytestfacebook.conftest import dataload
from pytestfacebook import Baseclass


class test_fixdemo(Baseclass1):
    def test_usedata(self, dataload):
        log = self.getlogger()
        log.Info(dataload)

        #print(dataload)
        #print("this is a method to fixture return")
        def testcrossbrsr(crossBrowser):
            log = self.getlogger()
            log.Info("Runnig info log")
            print("running in the browser")
