from education_data_economy import func_econonomy
import json


d = func_econonomy()

print(json.dumps(d, indent = 4, ensure_ascii=False))