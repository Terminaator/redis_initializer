from postgres import Connection

building_codes_sql = """
SELECT (SELECT MAX(EHR_KOOD) FROM DO_EHITIS WHERE EHR_KOOD LIKE '1%') as max, 'HOONE' as type
UNION ALL
SELECT (SELECT MAX(EHR_KOOD) FROM DO_EHITIS WHERE EHR_KOOD LIKE '2%') as max, 'RAJATIS' as type
UNION ALL
SELECT (SELECT MAX(OSA_KOOD) FROM DO_EHITIS_OSA) as max, 'OSA' as type
"""

procedure_code_sql = '''
SELECT MAX(ID) AS MAX FROM ME_MEN
'''

document_codes_sql = '''
SELECT 
    ID AS DOTY, 
    (SELECT 
        MAX(NULLIF(split_part(dok_nr, '/', 2), '')::int)
    FROM DO_DOKU 
    WHERE DO_DOKU.DOTY_ID = R_KL_DOKUMENDI_TYYBID.ID AND DO_DOKU.DOK_NR LIKE TO_CHAR(CURRENT_DATE, 'YY') || R_KL_DOKUMENDI_TYYBID.ID || '/%') AS MAX
FROM R_KL_DOKUMENDI_TYYBID 
WHERE LENGTH(ID::varchar) = 5 AND (CURRENT_DATE <= LOPP_KP OR LOPP_KP IS NULL)
'''

class Postgres:
    def __init__(self):
        self.connection = Connection()

    def get_building_codes(self):
        return self.connection.exec(building_codes_sql)

    def get_procedure_code(self):
        return self.connection.exec(procedure_code_sql)

    def get_document_codes(self):
        return self.connection.exec(document_codes_sql)

    def close(self):
        self.connection.close()
