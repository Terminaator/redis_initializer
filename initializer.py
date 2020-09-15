from postgres_interface import Postgres
from oracle_interface import Oracle

postgres = Postgres()
oracle = Oracle()

bul_codes_postgres = postgres.get_building_codes()
bul_codes_oracle = oracle.get_building_codes()

#todo võrdlemine
#todo commandi tegemine

pro_code_postgres = postgres.get_procedure_code()
pro_code_oracle = oracle.get_procedure_code()

#todo võrdlemine
#todo commandi tegemine

doc_codes_postgres = postgres.get_document_codes()
doc_codes_oracle = oracle.get_document_codes()

#todo võrdlemine
#todo commandi tegemine

postgres.close()
oracle.close()