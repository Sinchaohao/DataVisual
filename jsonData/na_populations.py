# @Author:sch
# @Time:2022/07/20
# @File:na_populations.py
# @software: PyCharm
# description:  在世界地图上呈现数字数据

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')

