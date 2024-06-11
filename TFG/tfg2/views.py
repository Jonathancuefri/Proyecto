from django.apps import apps
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from datetime import datetime

def index(request):
    return render(request, 'index.html', {})
    
def update_registro(request, tabla, nombre):
    if tabla=='empleados':
        objeto = get_object_or_404(EMPLEADOS, usuario=nombre)
        form = EmpleadosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/empleados/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
    
    elif tabla=='departamentos':
        objeto = get_object_or_404(DEPARTAMENTOS, nombre=nombre)
        form = DepartamentosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/departamentos/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='puestos_trabajos':
        tabla='puestos'
        objeto = get_object_or_404(PUESTOS_TRABAJOS, nombre=nombre)
        form = PuestosTrabajosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/puestos/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='incidencias_tarjetas':
        tabla='incidencias'
        objeto = get_object_or_404(INCIDENCIAS_TARJETAS, num_tarjeta=nombre)
        form = IncidenciasTarjetasForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/incidencias/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='moviles':
        objeto = get_object_or_404(MOVILES, nombre=nombre)
        form = MovilesForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/moviles/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='ordenadores':
        objeto = get_object_or_404(ORDENADORES, nombre=nombre)
        form = OrdenadorForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/ordenadores/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='perifericos':
        objeto = get_object_or_404(PERIFERICOS, nombre=nombre)
        form = PerifericosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/perifericos/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='servicios':
        objeto = get_object_or_404(SERVICIOS, nombre=nombre)
        form = ServiciosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/servicios/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='electronica_red':
        tabla='electronica_red'
        objeto = get_object_or_404(ELECTRONICA_RED, nombre=nombre)
        form = ElectronicaRedForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/electronica/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='dispositivos_externos':
        tabla='dispositivos'
        objeto = get_object_or_404(DISPOSITIVOS_EXTERNOS, nombre=nombre)
        form = DispositivosExternosForm(request.POST or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('/read/dispositivos/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
        
    elif tabla=='tarjetas':
        objeto = get_object_or_404(TARJETAS, num_tarjeta=nombre)
        form = TarjetasForm(request.POST or None, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('/read/tarjetas/')
        else:
            return render(request, 'formulario.html', {'form': form, 'tabla' : tabla})
    

def formulario(request, tipo):
    if tipo=='empleados':
        form = EmpleadosForm(request.POST)
    elif tipo=='departamentos':
        form = DepartamentosForm(request.POST)
    elif tipo=='puestos_trabajos':
        tipo='puestos'
        form = PuestosTrabajosForm(request.POST)
    elif tipo=='incidencias_tarjetas':
        tipo='incidencias'
        form = IncidenciasTarjetasForm(request.POST)
    elif tipo=='moviles':
        form = MovilesForm(request.POST)
    elif tipo=='ordenadores':
        form = OrdenadorForm(request.POST)
    elif tipo=='perifericos':
        form = PerifericosForm(request.POST)
    elif tipo=='servicios':
        form = ServiciosForm(request.POST)
    elif tipo=='electronica_red':
        tipo='electronica'
        form = ElectronicaRedForm(request.POST)
    elif tipo=='dispositivos_externos':
        tipo='dispositivos'
        form = DispositivosExternosForm(request.POST)
    elif tipo=='tarjetas':
        form = TarjetasForm(request.POST)
    
    if form.is_valid():
        form.save()
        return render(request, 'formulario.html', {'form': form, 'exito':True, 'tabla' : tipo})
    else:
        return render(request, 'formulario.html', {'form': form, 'tabla' : tipo})

def lectura_general(request, tabla):
    if tabla=='empleados':
        try:
            tabla = 'EMPLEADOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = EMPLEADOS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation and (field.many_to_many or field.one_to_one or field.one_to_many))]
            campo_seleccionado='usuario'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='departamentos':
        try:
            tabla = 'DEPARTAMENTOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = DEPARTAMENTOS.objects.order_by('iddepartamento')
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='puestos':
        try:
            tabla = 'PUESTOS_TRABAJOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = PUESTOS_TRABAJOS.objects.order_by('departamento')
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='incidencias':
        try:
            tabla = 'INCIDENCIAS_TARJETAS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = INCIDENCIAS_TARJETAS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='num_tarjeta'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='moviles':
        try:
            tabla = 'MOVILES'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = MOVILES.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='ordenadores':
        try:
            tabla = 'ORDENADORES'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = ORDENADORES.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='perifericos':
        try:
            tabla = 'PERIFERICOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = PERIFERICOS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='servicios':
        try:
            tabla = 'SERVICIOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = SERVICIOS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='electronica':
        try:
            tabla = 'ELECTRONICA_RED'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = ELECTRONICA_RED.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='dispositivos':
        try:
            tabla = 'DISPOSITIVOS_EXTERNOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = DISPOSITIVOS_EXTERNOS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='tarjetas':
        try:
            tabla = 'TARJETAS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = TARJETAS.objects.all()
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='num_tarjeta'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_general.html', {'empleados': registros, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    
def lectura_personal(request, tabla, nombre):
    if tabla=='empleados':
        try:
            tabla = 'EMPLEADOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = EMPLEADOS.objects.all()
            empleado_queryset = EMPLEADOS.objects.filter(usuario=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation and (field.many_to_many or field.one_to_one or field.one_to_many))]
            campo_seleccionado='usuario'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='departamentos':
        try:
            tabla = 'DEPARTAMENTOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = DEPARTAMENTOS.objects.all()
            empleado_queryset = DEPARTAMENTOS.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='puestos_trabajos':
        try:
            tabla = 'PUESTOS_TRABAJOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = PUESTOS_TRABAJOS.objects.all()
            empleado_queryset = PUESTOS_TRABAJOS.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='incidencias':
        try:
            tabla = 'INCIDENCIAS_TARJETAS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = INCIDENCIAS_TARJETAS.objects.all()
            empleado_queryset = INCIDENCIAS_TARJETAS.objects.filter(usuario=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='num_tarjeta'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='moviles':
        try:
            tabla = 'MOVILES'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = MOVILES.objects.all()
            empleado_queryset = MOVILES.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='ordenadores':
        try:
            tabla = 'ORDENADORES'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = ORDENADORES.objects.all()
            empleado_queryset = ORDENADORES.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='perifericos':
        try:
            tabla = 'PERIFERICOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = PERIFERICOS.objects.all()
            empleado_queryset = PERIFERICOS.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='servicios':
        try:
            tabla = 'SERVICIOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = SERVICIOS.objects.all()
            empleado_queryset = SERVICIOS.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='electronica_red':
        try:
            tabla = 'ELECTRONICA_RED'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = ELECTRONICA_RED.objects.all()
            empleado_queryset = ELECTRONICA_RED.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='dispositivos_externos':
        try:
            tabla = 'DISPOSITIVOS_EXTERNOS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = DISPOSITIVOS_EXTERNOS.objects.all()
            empleado_queryset = DISPOSITIVOS_EXTERNOS.objects.filter(nombre=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not (field.is_relation  and (field.many_to_many or field.one_to_many))]
            campo_seleccionado='nombre'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    elif tabla=='tarjetas':
        try:
            tabla = 'TARJETAS'
            model_class = apps.get_model(app_label='tfg2', model_name=tabla)
            registros = TARJETAS.objects.all()
            empleado_queryset = TARJETAS.objects.filter(num_tarjeta=nombre)
            fields = model_class._meta.get_fields()
            fields_directos = [field for field in fields if not field.is_relation]
            campo_seleccionado='num_tarjeta'
        except model_class.DoesNotExist:
            raise Http404("El objeto no existe")
        return render(request, 'lectura_personal.html', {'empleados': empleado_queryset, 'objects': registros, 'fields': fields_directos, 'tabla':tabla, 'campo_seleccionado': campo_seleccionado})
    
def delete_registro(request, tabla, nombre):
    if tabla=='empleados':
        objeto = EMPLEADOS.objects.get(usuario=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/empleados/')
    elif tabla=='departamentos':
        objeto = DEPARTAMENTOS.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/departamentos/')
    elif tabla=='puestos_trabajos':
        tabla='puestos'
        objeto = PUESTOS_TRABAJOS.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/puestos/')
    elif tabla=='incidencias_tarjetas':
        tabla='incidencias'
        objeto = INCIDENCIAS_TARJETAS.objects.get(num_tarjeta=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/incidencias/')
    elif tabla=='moviles':
        objeto = MOVILES.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/moviles/')
    elif tabla=='ordenadores':
        objeto = ORDENADORES.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/ordenadores/')
    elif tabla=='perifericos':
        objeto = PERIFERICOS.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/perifericos/')
    elif tabla=='servicios':
        objeto = SERVICIOS.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/servicios/')
    elif tabla=='electronica_red':
        tabla='electronica'
        objeto = ELECTRONICA_RED.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/electronica/')
    elif tabla=='dispositivos_externos':
        tabla='dispositivos'
        objeto = DISPOSITIVOS_EXTERNOS.objects.get(nombre=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/dispositivos/')
    elif tabla=='tarjetas':
        objeto = TARJETAS.objects.get(num_tarjeta=nombre)
        if request.method == 'POST':
            # Confirmación de eliminación
            objeto.delete()
            return redirect('/read/tarjetas/')
    
    return render(request, 'delete_registro.html', {'objeto': objeto, 'tabla' : tabla})

def hoja_devolucion(request, nombre):
    try:
        # Obtener el empleado correspondiente al nombre de usuario proporcionado en la URL
        empleado = EMPLEADOS.objects.get(usuario=nombre)
    except EMPLEADOS.DoesNotExist:
        # Manejar el caso donde no se encuentra ningún empleado con el nombre de usuario dado
        # Por ejemplo, puedes devolver una respuesta de error o redirigir a otra página
        return HttpResponseNotFound("El empleado no fue encontrado.")
    
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Mapear los nombres de los meses en inglés a los equivalentes en español
    meses_espanol = {
        'January': 'enero',
        'February': 'febrero',
        'March': 'marzo',
        'April': 'abril',
        'May': 'mayo',
        'June': 'junio',
        'July': 'julio',
        'August': 'agosto',
        'September': 'septiembre',
        'October': 'octubre',
        'November': 'noviembre',
        'December': 'diciembre'
    }
    
    # Obtener el nombre del mes actual en español
    mes_actual = meses_espanol[fecha_actual.strftime('%B')]
    
    # Renderizar la plantilla con el empleado, día, año y el nombre del mes en español
    return render(request, 'hoja_devolucion.html', {'empleado': empleado, 'dia_actual': fecha_actual.day, 'ano_actual': fecha_actual.year, 'mes_actual': mes_actual})