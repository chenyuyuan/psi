#-*- coding: UTF-8 -*-
from app import api

from app.url.login import login
api.add_resource(login, '/login')

from app.url.login import logout
api.add_resource(logout, '/logout')

from app.url.login import test_login
api.add_resource(test_login, '/test_login')

from app.url.login import who
api.add_resource(who,'/who')

from app.url.login import art
api.add_resource(art,'/art')