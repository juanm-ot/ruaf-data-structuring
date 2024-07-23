# This file contains data structures used by the pipelines for organizing, renaming, and structuring data

## field_code:The column names in the 'field' column of the DataFrame produced by int_pipeline are very long
## This data dictionary provides shorter names for easier manipulation in table operations
field_code = {
    'informacion_basica':'info',
    'vinculacion_a_programas_de__asistencia_social':'social',
    'pensionados':'pens',
    'afiliacion_a_cesantias':'cesantias',
    'afiliacion_a_riesgos_laborales':'riesgos',
    'afiliacion_a_salud':'salud',
    'afiliacion_a_pensiones':'pensiones',
    'afiliacion_a_compensacion_familiar':'compensacion'
    }

## base_columns: Defines the columns that are kept as indices for the pivot function.
## These columns serve as references for structuring the record.
base_columns = ['f_consulta', 'key_fep', 'tipo_id_num', 'tipo_id_str', 'num_id']

## set_up_columns: Dictionary that reorders and renames columns according to the reference XLSX file 
## The renaming is also based on the validated sections and related fields proposed in the project
set_up_columns = {
       'info/numero_de_identificacion':'nume_id',
       'info/primer_nombre':'primer_nombre',
       'info/segundo_nombre':'segundo_nombre',
       'info/primer_apellido':'primer_apellido',
       'info/segundo_apellido': 'segundo_apellido',
       'info/sexo':'sexo',
       'salud/administradora':'admon_salud',
       'salud/regimen':'regimen_salud',
       'salud/fecha_afiliacion':'f_afiliacion_salud',
       'salud/fecha_de_afiliacion':'f_de_afiliacion_salud',
       'salud/estado_de_afiliacion':'est_afiliacion_salud',
       'salud/tipo_de_afiliado':'tipo_afiliado_salud',   
       'salud/departamento_->_municipio':'dep_municipio',
       'pensiones/regimen': 'regimen_pension',
       'pensiones/administradora':'admon_pension', 
       'pensiones/fecha_de_afiliacion':'f_afiliacion_pension',
       'pensiones/estado_de_afiliacion':'est_afiliacion_pension',
       'riesgos/administradora':'admon_rl',
       'riesgos/fecha_de_afiliacion':'f_afiliacion_rl',
       'riesgos/estado_de_afiliacion':'est_afiliacion_rl',
       'riesgos/actividad_economica':'act_economica_rl',
       'riesgos/municipio_labora':'municipio_laborl_rl',
       'compensacion/administradora_cf':'admon_cf',
       'compensacion/fecha_de_afiliacion':'f_afiliacion_cf',
       'compensacion/estado_de_afiliacion': 'est_afiliacion_cf',
       'compensacion/tipo_de_miembro_de_la_poblacion_cubierta':'tipo_miembro_pobl_cf',
       'compensacion/tipo_de_afiliado': 'tipo_afiliado_cf',
       #'compensacion/municipio_labora':'municipio_laboral_cf',
       'cesantias/administradora':'admon_cesantias',
       'cesantias/fecha_de_afiliacion':'f_afiliacion_cesantias',
       'cesantias/estado_de_afiliacion':'est_afiliacion_cesantias', 
       'cesantias/regimen':'regimen_cesantias',
       'cesantias/municipio_labora':'municipio_laboral_cesantias',
       'pens/entidad_que_reconoce_la_pension':'entidad_pension',
       'pens/fecha_resolucion':'f_resolucion_pension',
       'pens/estado':'est_pension',
       'pens/modalidad':'modalidad_pension',
       'pens/numero_resolucion_pension_pg':'num_resolucion_pension',
       'pens/tipo_de_pension':'tipo_pension', 
       'pens/tipo_de_pensionado':'tipo_pensionado',
       'social/administradora':'admon_vpas',
       'social/fecha_de_vinculacion':'f_vinculacion_vpas',
       'social/estado_de_la_vinculacion':'est_vinculacion_vpas',
       'social/estado_del_beneficio':'est_beneficio_vpas',
       'social/fecha_ultimo_beneficio':'f_ult_beneficio_vpas',
       'social/programa':'programa_vpas', 
       'social/ubicacion_de_entrega_del_beneficio':'ubicacion_entrega_vpas',
       '/request':'evaluacion_marca'
}
