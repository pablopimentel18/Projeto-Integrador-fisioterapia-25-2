from django import template

register = template.Library()

@register.filter(name='desunder')
def desunder(value):
    """Substitui underscores ('_') por espaços em branco (' ')."""
    if isinstance(value, str):
        return value.replace('_', ' ')
    return value

@register.filter(name='mask_cpf')
def mask_cpf(value):
    """Aplica a máscara '000.000.000-00' a um CPF."""
    value = str(value)
    if not value or not value.isdigit() or len(value) != 11:
        return value
    
    return f"{value[0:3]}.{value[3:6]}.{value[6:9]}-{value[9:11]}"

@register.filter(name='mask_phone')
def mask_phone(value):
    """Aplica a máscara '(00) 00000-0000' ou '(00) 0000-0000'."""
    value = str(value)
    if not value or not value.isdigit():
        return value 

    if len(value) == 11:
        return f"({value[0:2]}) {value[2:7]}-{value[7:11]}"
    elif len(value) == 10:
        return f"({value[0:2]}) {value[2:6]}-{value[6:10]}"
    else:
        return value