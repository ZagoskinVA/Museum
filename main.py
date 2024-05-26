"""
from SPARQLWrapper import SPARQLWrapper, CSV, POST
import time
start_time = time.time()
sparql = SPARQLWrapper('http://localhost:8890/sparql-auth')
sparql.setHTTPAuth('DIGEST')
sparql.setCredentials("dba","root")
print("------------------------------------------------")


triples = [('ent:vladVisitor', 'ent:name2', '"vlad"^^xsd:string')]
query = "Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n Prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n Prefix ent: <http://www.menthor.net/myontology#>\n PREFIX owl: <http://www.w3.org/2002/07/owl#> \n PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n INSERT DATA { GRAPH <urn:graph:zagoskin> { "
for s, p, o in triples:
    query += f" {s} {p} {o} ."
query += " } }"
print(query)

sparql.setQuery(query)
sparql.setMethod(POST)
sparql.query()
"""

from generator import Generator
from queryService import QueryService


#generator = Generator()

#generator.generate()

queryService = QueryService()
#example = QueryExample()

#query = example.getFirstExample()

#result = queryService.query(query)

#print(result)
#from queryExample import QueryExample
#from SPARQLWrapper import SPARQLWrapper, CSV, POST
#federated_query = """
#PREFIX dmap: <http://www.menthor.net/myontology#>
#PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#PREFIX owl: <http://www.w3.org/2002/07/owl#>
#PREFIX dbo: <http://dbpedia.org/ontology/>
#PREFIX dbpedia-res: <http://dbpedia.org/resource/>
#INSERT {
#GRAPH <urn:graph:evtodienko> {
#dmap:Family_ticket rdfs:label ?abstract .
#}
#}
#WHERE {
#SERVICE <http://dbpedia.org/sparql> {
#dbpedia-res:Family dbo:abstract ?abstract .
#FILTER (LANG(?abstract) = "en")
#}
#}
#"""
#sparql = SPARQLWrapper('http://localhost:8890/sparql-auth')
#sparql.setHTTPAuth('DIGEST')
#sparql.setCredentials("dba","root")
#sparql.setMethod(POST)
#sparql.setQuery(federated_query)
#result = sparql.query()
#print(result)
#result = queryService.query("""
#SELECT ?subject ?predicate ?object
#FROM <urn:graph:zagoskin>
#WHERE {
#  ?subject ?predicate ?object
#}
#                   """)

#print(result)



#from pydbpedia import PyDBpedia, namespace

#dbpedia_uris = ["http://dbpedia.org/resource/Albert_Einstein"]

#dbpedia_wrapper = PyDBpedia(endpoint="http://dbpedia.org/sparql")
#objects = dbpedia_wrapper.get_objects(subjects=dbpedia_uris, predicates=[namespace.RDF_TYPE])

#print(objects)

import morph_kgc
from SPARQLWrapper import SPARQLWrapper, CSV, POST
config_file = "data/config"

g = morph_kgc.materialize(config_file)

   # Сохранение RDF графа в файл
print(g)
s = g.serialize(format='nt')

print(s)


sparql = SPARQLWrapper('http://localhost:8890/sparql-auth')
sparql.setHTTPAuth('DIGEST')
sparql.setCredentials("dba","root")

query = 'INSERT DATA { GRAPH <urn:graph:zagoskin> { '

query = query + s + ' } }'

print(query)

sparql.setQuery(query)
sparql.setMethod(POST)
sparql.query()
