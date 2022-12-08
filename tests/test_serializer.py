from unittest import TestCase
from asosiyapp.serializers import *
from asosiyapp.models import *
from userapp.models import *


# class TestMijozSer(TestCase):
#     def setUP(self) -> None:
#         self.data = {
#             "id":5, "ism":"ALi", "nom":"tuxum", "manzil":"fargona", "tel":"+12312312",
#             "qarz":213, "sotuvchi":Sotuvchi.objects.get(id=1)}
#
#     def test_mijoz_ser(self):
#         mijoz = {
#             "id": 5, "ism": "Ali", "nom": "tuxum", "manzil": "fargona", "tel": "+12312312",
#             "qarz": 213, "sotuvchi": Sotuvchi.objects.get(id=1)}
#         ser = MijozSerializer(mijoz)
#         assert ser.data["id"] == 5
#         assert ser.data["ism"] == "Ali"
#         assert ser.data["nom"] == "tuxum"
#         assert ser.data["sotuvchi"] == 1
#
#     def test_mijoz_valid(self):
#         mijoz = {"id": 5, "ism": "Ali", "nom": "tuxum", "manzil": "fargona", "tel": "+12312312",
#             "qarz": 213, "sotuvchi": 1}
#         ser = MijozSerializer(data=mijoz)
#         assert ser.is_valid() == True
#
#     def test_mijoz_invalid(self):
#         mijoz = {"id": 5, "ism": "Ali", "nom": "tuxum", "manzil": "fargona", "tel": "+12312312",
#             "qarz": 7000000, "sotuvchi": 1}
#         ser = MijozSerializer(data=mijoz)
#         assert ser.is_valid() == False
#         print(ser.errors['qarz'][0])