from django.db import models
from django.core.exceptions import ValidationError

class DEPARTAMENTOS(models.Model):
    iddepartamento = models.IntegerField(db_column='idDepartamentos', primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)  
    
    def __str__(self):
        return self.nombre
    
class PUESTOS_TRABAJOS(models.Model):
    departamento = models.ForeignKey(DEPARTAMENTOS, models.DO_NOTHING, db_column='Departamento', to_field='nombre',unique=False)  
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45, primary_key=True) 

    def __str__(self):
        return self.nombre

class TARJETAS(models.Model):
    DISPONIBLE = 'DISPONIBLE'
    ASIGNADA = 'ASIGNADA'
    PERDIDA = 'PERDIDA'
    
    ESTADO_CHOICES = [
        (DISPONIBLE, 'DISPONIBLE'),
        (ASIGNADA, 'ASIGNADA'),
        (PERDIDA, 'PERDIDA'),
    ]
    idtarjeta = models.IntegerField(db_column='idTarjetas', primary_key=True)   
    num_tarjeta = models.CharField(db_column='Num_Tarjeta', unique=True, max_length=45)   
    estado = models.CharField(db_column='Estado', max_length=45, choices=ESTADO_CHOICES)   
    observacion = models.CharField(db_column='Observaciones', max_length=200, blank=True, null=True)   

    def __str__(self):
        return self.num_tarjeta

class EMPLEADOS(models.Model):
    ACTIVO = 'ACTIVO'
    BAJA = 'BAJA'
    DESPEDIDO = 'DESPEDIDO'
    
    ESTADO_CHOICES = [
        (ACTIVO, 'ACTIVO'),
        (BAJA, 'BAJA'),
        (DESPEDIDO, 'DESPEDIDO'),
    ]

    PRESENCIAL = 'PRESENCIAL'
    REMOTO = 'REMOTO'
    HIBRIDO = 'HIBRIDO'
    
    MODALIDAD_CHOICES = [
        (PRESENCIAL, 'Presencial'),
        (REMOTO, 'Remoto'),
        (HIBRIDO, 'Híbrido'),
    ]
    
    L_T_E14 = 'Lenovo ThinkPad E14'
    L_T_E15 = 'Lenovo ThinkPad E15'
    Chromebook = 'Chromebook'
    NONE= 'NONE'
    
    EQUIPO_CHOICES = [
        (L_T_E14, 'Lenovo ThinkPad E14'),
        (L_T_E15, 'Lenovo ThinkPad E15'),
        (Chromebook, 'Chromebook'),
        (NONE, 'NONE')
    ]

    idempleado = models.IntegerField(db_column='idEmpleado', primary_key=True)
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=45)
    dni = models.CharField(db_column='DNI', unique=True, max_length=10)
    nombre = models.CharField(db_column='Nombre', max_length=45)
    apellidos = models.CharField(db_column='Apellidos', max_length=50)
    email = models.CharField(db_column='Email', unique=True, max_length=50)
    fecha_alta = models.DateField(db_column='Fecha_alta')
    fecha_baja = models.DateField(db_column='Fecha_baja')
    departamento = models.ForeignKey(DEPARTAMENTOS, models.DO_NOTHING, db_column='Departamento', to_field='nombre')
    puesto = models.ForeignKey(PUESTOS_TRABAJOS, models.DO_NOTHING, db_column='Puesto', to_field='nombre')
    estado = models.CharField(db_column='Estado', max_length=45, choices=ESTADO_CHOICES)
    modalidad = models.CharField(db_column='Modalidad', max_length=45, choices=MODALIDAD_CHOICES)
    responsable = models.ForeignKey('self', models.DO_NOTHING, db_column='Responsable', to_field='usuario', blank=True, null=True)
    tarjeta = models.ForeignKey(TARJETAS, models.DO_NOTHING, db_column='Tarjeta', to_field='num_tarjeta', blank=True, null=True)
    ordenador1 = models.CharField(db_column='Ordenador1', max_length=90, choices=EQUIPO_CHOICES)
    ordenador2 = models.CharField(db_column='Ordenador2', max_length=90, choices=EQUIPO_CHOICES)
    ordenador3 = models.CharField(db_column='Ordenador3', max_length=90, choices=EQUIPO_CHOICES)
    entrada_cpd = models.IntegerField(db_column='Entrada_CPD')
    llave_acceso = models.IntegerField(db_column='Llave_acceso')
    homy_hub_parking = models.IntegerField(db_column='Homy_Hub_Parking')
    pub_key_pgp = models.CharField(db_column='Pub_Key_PGP', unique=True, max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.usuario
    
    def clean(self):
        super().clean()
        if self.puesto_id is not None:  # Verificar que el puesto no sea None
            departamento_puesto = self.puesto.departamento
            if departamento_puesto != self.departamento:
                raise ValidationError("El puesto no pertenece al departamento seleccionado.")

class ORDENADORES(models.Model):
    L_T_E14 = 'Lenovo ThinkPad E14'
    L_T_E15 = 'Lenovo ThinkPad E15'
    Chromebook = 'Chromebook'
    
    EQUIPO_CHOICES = [
        (L_T_E14, 'Lenovo ThinkPad E14'),
        (L_T_E15, 'Lenovo ThinkPad E15'),
        (Chromebook, 'Chromebook'),
    ]

    DISPONIBLE = 'DISPONIBLE'
    ASIGNADO = 'ASIGNADO'
    DESECHO = 'DESECHO'
    
    ESTADO_CHOICES = [
        (DISPONIBLE, 'DISPONIBLE'),
        (ASIGNADO, 'ASIGNADO'),
        (DESECHO, 'DESECHO'),
    ]

    idordenador = models.IntegerField(db_column='idOrdenador', primary_key=True)   
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)   
    usuario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='usuario', to_field='usuario')
    estado = models.CharField(db_column='Estado', max_length=45,choices=ESTADO_CHOICES)   
    equipo = models.CharField(db_column='Equipo', max_length=90, choices=EQUIPO_CHOICES)   
    numero_serie = models.CharField(db_column='Numero_serie', unique=True, max_length=45)   
    modelo = models.CharField(db_column='Modelo', max_length=45, blank=True, null=True)   
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)   
    cpu = models.CharField(db_column='CPU', max_length=45, blank=True, null=True)   
    memoria = models.CharField(db_column='Memoria', max_length=45, blank=True, null=True)   
    ubicacion = models.CharField(db_column='Ubicacion', max_length=45)   

    def __str__(self):
            return self.nombre

class INCIDENCIAS_TARJETAS(models.Model):
    num_tarjeta = models.ForeignKey(TARJETAS, models.DO_NOTHING, db_column='num_tarjeta', primary_key=True, to_field='num_tarjeta')
    usuario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='usuario', to_field='usuario')   
    incidencia = models.CharField(db_column='Incidencia', max_length=200)

    def __str__(self):
            return self.num_tarjeta.num_tarjeta

class MOVILES(models.Model):

    DISPONIBLE = 'DISPONIBLE'
    ASIGNADO = 'ASIGNADO'
    DESECHO = 'DESECHO'
    
    ESTADO_CHOICES = [
        (DISPONIBLE, 'DISPONIBLE'),
        (ASIGNADO, 'ASIGNADO'),
        (DESECHO, 'DESECHO'),
    ]

    idmovil = models.IntegerField(db_column='idMoviles', primary_key=True)   
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)   
    usuario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='Usuario', to_field='usuario', blank=True, null=True)   
    sim = models.IntegerField(db_column='SIM', blank=True, null=True)   
    numero_telefono = models.IntegerField(db_column='Numero_telefono', blank=True, null=True)   
    estado = models.CharField(db_column='Estado', max_length=45, choices=ESTADO_CHOICES)   
    terminal = models.CharField(db_column='Terminal', max_length=45)   
    modelo = models.CharField(db_column='Modelo', max_length=45, blank=True, null=True)   
    numero_serie = models.CharField(db_column='Numero_Serie', unique=True, max_length=45, blank=True, null=True)         
    tipo = models.CharField(db_column='Tipo', max_length=45)   
    
    def __str__(self):
                return self.nombre
     
class PERIFERICOS(models.Model):
    idperiferico = models.IntegerField(db_column='idPerifericos', primary_key=True)   
    nombre = models.CharField(db_column='Nombre', max_length=45)   
    usuario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='Usuario', to_field='usuario', blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=45)   

    def __str__(self):
        return self.nombre
    
class SERVICIOS(models.Model):
    CLOUD = 'CLOUD'
    FISICO= 'FISICO'
    
    TIPO_CHOICES = [
        (CLOUD, 'CLOUD'),
        (FISICO, 'FISICO'),
    ]

    COMUNICACIONES = 'COMUNICACIONES'
    SEGURIDAD = 'SEGURIDAD'
    NONE = 'NONE'
    BASTIDOR_CHOICES = [
        (COMUNICACIONES, 'COMUNICACIONES'),
        (SEGURIDAD, 'SEGURIDAD'),
        (NONE, 'NONE'),
    ]

    idservicio = models.IntegerField(db_column='idServicios', primary_key=True)   
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50)   
    descripcion = models.CharField(db_column='Descripcion', max_length=200)   
    bastidor = models.CharField(db_column='Bastidor', max_length=45,choices=BASTIDOR_CHOICES)   
    tipo = models.CharField(db_column='Tipo', max_length=45, choices=TIPO_CHOICES)   
    proveedor = models.CharField(db_column='Proveedor', max_length=45, blank=True, null=True)   
    propietario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='Propietario', to_field='usuario',default='jcuellar')   
    responsable = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='Responsable', to_field='usuario', related_name='servicios_responsable_set', default='earmani')   
    observaciones = models.CharField(db_column='Observaciones', max_length=200, blank=True, null=True)   

    def __str__(self):
            return self.nombre

class ELECTRONICA_RED(models.Model):
    idelectronica_red = models.IntegerField(db_column='idElectronica_red', primary_key=True)   
    nombre = models.CharField(db_column='Nombre', max_length=45)   
    modelo = models.CharField(db_column='Modelo', max_length=45)   
    tipo = models.CharField(db_column='Tipo', max_length=45)   
    puertos = models.IntegerField(db_column='Puertos', blank=True, null=True)   
    descripcion = models.CharField(db_column='Descripcion', max_length=200)   

    def __str__(self):
        return self.nombre
    
class DISPOSITIVOS_EXTERNOS(models.Model):
    PUBLICO = 'PUBLICO'
    USO_INTERNO = 'USO INTERNO'
    RESTRINGIDO = 'RESTRINGIDO'
    NO_CLASIFICADO = 'NO CLASIFICADO'

    CRITICIDAD_CHOICES = [
        (PUBLICO, 'PUBLICO'),
        (USO_INTERNO, 'USO INTERNO'),
        (RESTRINGIDO, 'RESTRINGIDO'),
        (NO_CLASIFICADO, 'NO CLASIFICADO')
    ]

    iddispositivo_externo = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)   
    usuario = models.ForeignKey(EMPLEADOS, models.DO_NOTHING, db_column='Usuario', to_field='usuario')   
    departamento = models.ForeignKey(DEPARTAMENTOS, models.DO_NOTHING, db_column='Departamento', to_field='nombre')      
    modelo = models.CharField(db_column='Modelo', max_length=45)   
    numero_serie = models.CharField(db_column='Numero_serie', unique=True, max_length=45)   
    capacidad = models.CharField(db_column='Capacidad', max_length=45, blank=True, null=True)   
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)   
    carcasa = models.CharField(db_column='Carcasa', max_length=45, blank=True, null=True)   
    nivel_criticidad_info = models.CharField(db_column='Nivel_criticidad_info', max_length=45, choices=CRITICIDAD_CHOICES)    
    etiquetado = models.CharField(db_column='Etiquetado', max_length=45, blank=True, null=True)   
    función = models.CharField(db_column='Función', max_length=30, blank=True, null=True)   

    def __str__(self):
            return self.nombre