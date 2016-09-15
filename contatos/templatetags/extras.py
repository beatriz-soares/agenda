from django import template

register = template.Library()

@register.filter(name='formatar')
def formata_cel(value):
    tamanho = len(value)

    if tamanho >= 11:
        value = "(" + value[:2] + ") " + value[2:7] + '-' + value[7:12]
    else:
        zeros = 11 - tamanho
        for i in range(zeros):
            value = "0" + value

        value = "(" + value[:2] + ") " + value[2:7] + '-' + value[7:]

    return value