#-*- coding: UTF-8 -*-
from app import api

# 方案宾馆接口--PUT
from app.json.login import planHotel
api.add_resource(planHotel, '/login1')
