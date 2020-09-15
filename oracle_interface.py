from oracle import Connection

building_codes_sql = """
SELECT GREATEST((
SELECT MAX(EHR_KOOD) fROM EHR.DO_EHITIS WHERE EHR_KOOD LIKE '1%'),
(SELECT MAX(EHR_KOOD) fROM EHR.EH_EHITIS WHERE EHR_KOOD LIKE '1%')
) as max, 'HOONE' as type FROM DUAL
UNION ALL
SELECT GREATEST(
(SELECT MAX(EHR_KOOD) fROM EHR.DO_EHITIS WHERE EHR_KOOD LIKE '2%'),
(SELECT MAX(EHR_KOOD) fROM EHR.EH_EHITIS WHERE EHR_KOOD LIKE '2%')
) as max, 'RAJATIS' as type FROM DUAL
UNION ALL
SELECT GREATEST(
(SELECT MAX(OSA_KOOD) fROM EHR.DO_EHITIS_OSA),
(SELECT MAX(OSA_KOOD) fROM EHR.EH_EHITIS_OSA)
) as max, 'OSA' as type FROM DUAL
"""

procedure_code_sql = """SELECT MAX(ID) AS MAX FROM EHR.ME_MEN"""

document_codes_sql = """
SELECT 
    ID AS DOTY, 
    (SELECT 
        MAX(TO_NUMBER(REGEXP_SUBSTR(EHR.DO_DOKU.DOK_NR,'[^/]+',2,2)))
    FROM EHR.DO_DOKU 
    WHERE DO_DOKU.DOTY_ID = KL_DOKUMENDI_TYYBID.ID AND DO_DOKU.DOK_NR LIKE TO_CHAR(CURRENT_DATE, 'YY') || KL_DOKUMENDI_TYYBID.ID || '/%') AS MAX
FROM EHR.KL_DOKUMENDI_TYYBID 
WHERE LENGTH(ID) = 5 AND (CURRENT_DATE <= LOPP_KP OR LOPP_KP IS NULL)
"""

class Oracle:
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