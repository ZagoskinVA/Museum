from SPARQLWrapper import SPARQLWrapper, CSV

class QueryService:
    def query(self, query: str) -> str:
        sparql = SPARQLWrapper('http://localhost:8890/sparql-auth')
        sparql.setHTTPAuth('DIGEST')
        sparql.setCredentials("dba","root")

        sparql.setQuery(query)
        sparql.setReturnFormat(CSV)
        qres = sparql.query().convert().decode('u8')
        return qres