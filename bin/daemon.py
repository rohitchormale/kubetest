#!/usr/bin/python3

import json
from twisted.logger import Logger
from twisted.application import service, internet
from twisted.logger import ILogObserver, textFileLogObserver, FilteringLogObserver, LogLevelFilterPredicate, LogLevel
from twisted.python.logfile import LogFile
from twisted.internet import defer
from twisted.web import resource, server


class Liveness(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        data = {"msg": "Liveness checking"}
        request.setResponseCode(500)
        return json.dumps(data)


class Readiness(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        data = {"msg": "Readiness checking"}
        request.setResponseCode(200)
        return json.dumps(data)


def getAppService(port, interface):
    root = resource.Resource()
    root.putChild("liveness", Liveness())
    root.putChild("readiness", Readiness())
    site = server.Site(root)
    return internet.TCPServer(port, site, interface=interface)


application = service.Application('app')
log_file = LogFile('daemon.log', './', rotateLength=1024*1024*1024, maxRotatedFiles=2)
log_observer = FilteringLogObserver(textFileLogObserver(log_file), predicates=[LogLevelFilterPredicate(LogLevel.debug),])
application.setComponent(ILogObserver, log_observer)
app_service = getAppService(5000, '0.0.0.0')
app_service.setServiceParent(application)

