import model_mult as mult
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    mult.init(value_a, value_b) #инициализаци значений
    result = mult.do_it()
    view.view_data(result, 'mult')