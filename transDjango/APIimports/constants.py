API_META = {
    'Capital Improv. Project - Points': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/93ed0b190bc6441fad1e48871b4c58d2_43.geojson',
        'sourceName': 'Capital Improv. Projects',
        'startDateField': 'Est_Construction_Start_Date',
        'endDateField': 'Est_Construction_Comp_Date',
        'status': 'Status',
        'forConflict': True,
    },
    'Capital Improv. Project - Lines': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/698e0309785e4062b301190244e5a5e7_44.geojson',
        'sourceName': 'Capital Improv. Projects',
        'startDateField': 'Est_Construction_Start_Date',
        'endDateField': 'Est_Construction_Comp_Date',
        'status': 'Status',
        'forConflict': True,
    },
    'Capital Improv. Project - Polygons': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/b8ce5b03674841e4834de1617b7f84ef_45.geojson',
        'sourceName': 'Capital Improv. Projects',
        'startDateField': 'Est_Construction_Start_Date',
        'endDateField': 'Est_Construction_Comp_Date',
        'status': 'Status',
        'forConflict': False,
    },
    'Street Permit Jobs - Points': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/027156c0ed574d79a2b7a7a2f4c941f1_56.geojson',
        'sourceName': 'Street Permit Jobs',
        'startDateField': 'COCDate',
        'endDateField': 'COCDate',
        'status': 'Status',
        'forConflict': True,
    },
    'Street Permit Jobs - Lines': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/3c3d35ff54964d3fa7c27ed846774695_65.geojson',
        'sourceName': 'Street Permit Jobs',
        'startDateField': 'COCDate',
        'endDateField': 'COCDate',
        'status': 'Status',
        'forConflict': True,
    },
    'Street Permit Jobs - Polygons': {
        'uri': 'http://gis.pdx.opendata.arcgis.com/datasets/ed82f763d4604f669680525912d51b1f_66.geojson',
        'sourceName': 'Street Permit Jobs',
        'startDateField': 'COCDate',
        'endDateField': 'COCDate',
        'status': 'Status',
        'forConflict': False,
    },
}

CSV_META = {

    'Grind and Pave': {
        'uri': '../management/commands/datafiles/grind_pave.csv',
        'sourceName': 'Grind and Pave',
        'startDateField': 'start',
        'endDateField': 'finish',
        'forConflict': True,
    },
    'Pavement Moratorium': {
        'uri': '../management/commands/datafiles/pavement_moratorium.csv',
        'sourceName': 'Pavement Moratorium',
        'startDateField': 'start',
        'endDateField': 'finish',
        'forConflict': True,
    },
}

GEOJSON_META = {

    'ROW Closures': {
        'uri': '../management/commands/datafiles/ROWClosures_02012017.geojson',
        'sourceName': 'ROW Closures',
        'startDateField': 'ClosureS_1',
        'endDateField': 'ClosureEnd',
        'status': 'ClosureSta',
        'forConflict': True,
    },
}