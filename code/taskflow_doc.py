from pprint import pprint
from paddlenlp import Taskflow


schema = ['姓名']
ie = Taskflow("information_extraction", schema=schema, model="uie-x-base")
pprint(ie({"doc": "D:\\ruanjianbeiA8\\resume_parse\\code\\1.pdf"}))
