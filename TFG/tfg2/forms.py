from django import forms
from .models import *
from datetime import date

class EmpleadosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmpleadosForm, self).__init__(*args, **kwargs)

        
        ultimo_id = EMPLEADOS.objects.aggregate(models.Max('idempleado'))['idempleado__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idempleado'].widget.attrs['value'] = nuevo_id
        self.fields['fecha_alta'].widget.attrs['value'] = date.today().strftime('%Y-%m-%d')
        self.fields['fecha_baja'].widget.attrs['value'] = '9999-01-01'
        self.fields['entrada_cpd'].widget.attrs['value'] = 0
        self.fields['llave_acceso'].widget.attrs['value'] = 0
        self.fields['estado'].widget.attrs['value'] = 'ACTIVO'
        self.fields['modalidad'].widget.attrs['value'] = 'Presencial'

    class Meta:
        model = EMPLEADOS
        fields = '__all__'

class DepartamentosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartamentosForm, self).__init__(*args, **kwargs)

        
        ultimo_id = DEPARTAMENTOS.objects.aggregate(models.Max('iddepartamento'))['iddepartamento__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['iddepartamento'].widget.attrs['value'] = nuevo_id
        
    class Meta:
        model = DEPARTAMENTOS
        fields = '__all__'

class PuestosTrabajosForm(forms.ModelForm):
    class Meta:
        model = PUESTOS_TRABAJOS
        fields = '__all__'

class TarjetasForm(forms.ModelForm):
    class Meta:
        model = TARJETAS
        fields = '__all__'

class IncidenciasTarjetasForm(forms.ModelForm):
    class Meta:
        model = INCIDENCIAS_TARJETAS
        fields = '__all__'

class MovilesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MovilesForm, self).__init__(*args, **kwargs)

        
        ultimo_id = MOVILES.objects.aggregate(models.Max('idmovil'))['idmovil__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idmovil'].widget.attrs['value'] = nuevo_id
        self.fields['tipo'].widget.attrs['value'] = 'Móvil'

    class Meta:
        model = MOVILES
        fields = '__all__'

class OrdenadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrdenadorForm, self).__init__(*args, **kwargs)

        
        ultimo_id = ORDENADORES.objects.aggregate(models.Max('idordenador'))['idordenador__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idordenador'].widget.attrs['value'] = nuevo_id
        self.fields['tipo'].widget.attrs['value'] = 'Portátil'
        self.fields['ubicacion'].widget.attrs['value'] = 'Oficina PTA'

    class Meta:
        model = ORDENADORES
        fields = '__all__'
 

class PerifericosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PerifericosForm, self).__init__(*args, **kwargs)

        
        ultimo_id = PERIFERICOS.objects.aggregate(models.Max('idperiferico'))['idperiferico__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idperiferico'].widget.attrs['value'] = nuevo_id

    class Meta:
        model = PERIFERICOS
        fields = '__all__'

class ServiciosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiciosForm, self).__init__(*args, **kwargs)

       
        ultimo_id = SERVICIOS.objects.aggregate(models.Max('idservicio'))['idservicio__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idservicio'].widget.attrs['value'] = nuevo_id

    class Meta:
        model = SERVICIOS
        fields = '__all__'

        
class ElectronicaRedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ElectronicaRedForm, self).__init__(*args, **kwargs)

        
        ultimo_id = ELECTRONICA_RED.objects.aggregate(models.Max('idelectronica_red'))['idelectronica_red__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['idelectronica_red'].widget.attrs['value'] = nuevo_id

    class Meta:
        model = ELECTRONICA_RED
        fields = '__all__'

class DispositivosExternosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DispositivosExternosForm, self).__init__(*args, **kwargs)

        
        ultimo_id = DISPOSITIVOS_EXTERNOS.objects.aggregate(models.Max('iddispositivo_externo'))['iddispositivo_externo__max']
        nuevo_id = ultimo_id + 1 if ultimo_id is not None else 1

        
        self.fields['iddispositivo_externo'].widget.attrs['value'] = nuevo_id

    class Meta:
        model = DISPOSITIVOS_EXTERNOS
        fields = '__all__'
