# coding=utf-8
from abc import ABC

import tornado.web
from handlers.base.base_handler import BaseHandler


class MainHandler(BaseHandler, ABC):
    # @tornado.web.authenticated
    def get(self):
        self.write("hello")
        #self.render("main/index.html")
