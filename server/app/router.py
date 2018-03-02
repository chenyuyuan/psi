#-*- coding: UTF-8 -*-
from app import api

from app.json.planHotel import planHotel
api.add_resource(planHotel,'/plan')
