#-*- coding: UTF-8 -*-
from app import api

from app.url.login import login,logout,test_login,who,art,bootstrap
api.add_resource(login, '/login')

api.add_resource(logout, '/logout')

api.add_resource(test_login, '/test_login')

api.add_resource(who,'/who')

api.add_resource(art,'/art')

api.add_resource(bootstrap,'/main')

from app.json.planHotel import planHotel
api.add_resource(planHotel,'/plan')
