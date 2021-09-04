from django.core.exceptions import ValidationError
import re


# Проверка на присутствие русских букв в строке
def validateRussianSymbols(val):
    if bool(re.search('[а-яА-Я]', val)):
        raise ValidationError('Присутствуют русские буквы', code='odd', params={'value': val})
