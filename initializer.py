from postgres_interface import Postgres
from oracle_interface import Oracle

postgres = Postgres()
oracle = Oracle()

print(postgres.get_building_codes())
print(oracle.get_building_codes())

#todo võrdlemine
#todo commandi tegemine

print(postgres.get_procedure_code())
print(oracle.get_procedure_code())

#todo võrdlemine
#todo commandi tegemine

#print(postgres.get_document_codes())
#print(oracle.get_document_codes())

#todo võrdlemine
#todo commandi tegemine

postgres.close()
oracle.close()