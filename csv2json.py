import json
import pandas as pd
from elasticseach import Elasticsearch

def indexit(path):
    es = Elasticsearch()
    df = pd.DataFrame().from_csv(path)
    j_entries = json.loads(df.to_json(orient='records'))
    for j in j_entries:
        es.index(index='ufos', doc_type='ufosighting', body=j)


if '__name__' == '__main__':
    indexit('scrubbed.csv')
