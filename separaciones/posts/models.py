from django.db import models

class solicitud_separaciones(models.Model):
    numeroSolicitud = models.IntegerField()
    hojaTrabajo = models.IntegerField()
    cdrp = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    nombreSistema = models.CharField(max_length=100)
    nombreCorrecto = models.CharField(max_length=100)
    ramo = models.CharField(max_length=50)
    Campo = models.DateField()
    dependencia = models.CharField(max_length=50)
    fechaRo = models.DateField()
    fechaAnalisis = models.DateField()
    cotizacionesMacot = models.DecimalField(max_digits=10, decimal_places=2)
    rebajas = models.DecimalField(max_digits=10, decimal_places=2)
    montoBeneficios = models.DecimalField(max_digits=10, decimal_places=2)
    montoResumen = models.DecimalField(max_digits=10, decimal_places=2)
    diferencia = models.DecimalField(max_digits=10, decimal_places=2)
    montoRo = models.DecimalField(max_digits=10, decimal_places=2)
    interesAlRo = models.DecimalField(max_digits=10, decimal_places=2)
    cotDespuesRoAl12052014 = models.DecimalField(max_digits=10, decimal_places=2)
    intDespuesRoAl12052014 = models.DecimalField(max_digits=10, decimal_places=2)
    cot13052014Delante = models.DecimalField(max_digits=10, decimal_places=2)
    interesRebajas = models.DecimalField(max_digits=10, decimal_places=2)
    tasaMes = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False 
        db_table = 'solicitud_separaciones'
