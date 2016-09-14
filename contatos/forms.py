from django import forms

class PessoaForm(forms.Form):
    nome = forms.CharField(label='Novo nome', max_length=80)
    idade = forms.IntegerField(label='Idade')
    site = forms.URLField(label='Site')
    #datacadastro = forms.DateField(label='Data')

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CelForm(forms.Form):
    numero = forms.IntegerField(label="Celular", required=False)

    def __init__(self, *args, **kwargs):
        super(CelForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AddCSV(forms.Form):
    csv = forms.FileField(label="Adicionar CSV")

