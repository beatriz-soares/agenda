from django import forms

from contatos.models import TIPO_NUM, SEXO_CHOICES


class PessoaForm(forms.Form):
    nome = forms.CharField(label='Novo nome', max_length=80)
    idade = forms.IntegerField(label='Idade')
    site = forms.URLField(label='Site')
    sexo = forms.ChoiceField(choices=SEXO_CHOICES,
                               widget=forms.Select)
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CelForm(forms.Form):
    numero = forms.CharField(max_length=11, label="Celular", required=False)
    tiponum = forms.ChoiceField(label="Tipo de numero", choices=TIPO_NUM,
                                widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(CelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AddCSV(forms.Form):
    csv = forms.FileField(label="Adicionar CSV")

