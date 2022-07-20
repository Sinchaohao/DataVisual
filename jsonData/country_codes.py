# @Author:sch
# @Time:2022/07/20
# @File:country_codes.py
# @software: PyCharm

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定国家，返回Pygal_maps_world使用的两字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定国家返回None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))