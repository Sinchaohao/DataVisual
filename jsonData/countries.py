# @Author:sch
# @Time:2022/07/20
# @File:countries.py
# @software: PyCharm

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

