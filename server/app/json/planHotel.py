# from app import db, models
# from flask_restful import Resource, Api, reqparse, abort
# import flask
#
# # 参数初始化
# parse = reqparse.RequestParser()
# parse.add_argument("wechat")
# parse.add_argument("id")
# parse.add_argument('hotel')
#
# class planHotel(Resource):
#     def get(self):
#
#         print("import")
#         return {"message":"sfsfsfsfsfsffsfs"}
#     # 修改
#     def put(self):
#         print("1")
#         args = parse.parse_args()
#         plan = models.plan.query.filter_by(id=args.id).first()
#         # 判断用户是否存在
#         if plan:
#             if args.wechat==plan.wechat:
#                 plan.hotel = args.hotel if args.hotel else plan.hotel
#                 db.session.commit()
#                 return {"message": True},200
#             else:
#                 return {"message":"Please call the source"},200
#         else:
#             return {
#                 abort(404, message="It doesn't exist")
#             }
#
#         # with open("E://l.txt", "w+") as f:
#         #     f.write("male,160400220,Jon\nfemale,160400101,Marry,")
#         # with open("E://l.txt", "r+") as f:
#         #     h = f.read()
#         # g = list(h)
#         # l = ''
#         # k = []
#         # for i in g:
#         #     if i != ',':
#         #         l += i
#         #     elif i == ',' or i == '\n':
#         #         k.append(l)
#         #         l = ''
#         # for i in k:
#         #     print(k)