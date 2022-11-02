
# модуль 1: data_provider (сбор информации с датчиков)
# модуль 2: logger (логирование)
# модуль 3: user_interface (UI)
# модуль 4: html_creator (HTML-генератор)
# модуль 5: main (главный модуль)

import html_creator as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

xg.new_create(dp.data_collection())