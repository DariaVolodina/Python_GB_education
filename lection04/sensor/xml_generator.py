from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n' 
    xml += '   <temperature units = "f>{}</temperature>\n'\
        .format(t)
    xml += '   <pressure units = "mmHg>{}</pressure>\n'\
        .format(p)
    xml += '   <wind_speed_view units = "m/s>{}</wind_speed_view>\n'\
        .format(w)
    xml += '   <body>\n</html>'

    with open('index.xml', 'w') as page:
        page.write(xml)
    
    return data


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n' 
    xml += '   <temperature units = "f>{}</temperature>\n'\
        .format(t)
    xml += '   <pressure units = "mmHg>{}</pressure>\n'\
        .format(p)
    xml += '   <wind_speed_view units = "m/s>{}</wind_speed_view>\n'\
        .format(w)
    xml += '   <body>\n</html>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)
    
    return data