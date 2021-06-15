from django import template
 
register = template.Library()
censor_list = ['TEST', 'sit']

def censor(value):
    for censor in censor_list:
        value = value.replace(censor, '***')
    return value

register.filter(name='censor', filter_func=censor)