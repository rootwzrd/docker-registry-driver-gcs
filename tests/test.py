# -*- coding: utf-8 -*-

import logging

from docker_registry import testing

logger = logging.getLogger(__name__)


class TestQuery(testing.Query):
    def __init__(self):
        self.scheme = 'gcs'


class TestDriver(testing.Driver):
    def __init__(self):
        self.scheme = 'gcs'
        self.path = ''
        self.config = testing.Config({})
