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
