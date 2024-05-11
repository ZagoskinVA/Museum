from visitor import Visitor
from ticket import Ticket
from SPARQLWrapper import SPARQLWrapper, CSV, POST

class Generator:

    def __init__(self) -> None:
        self.query = "Prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n Prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n Prefix ent: <http://www.menthor.net/myontology#>\n PREFIX owl: <http://www.w3.org/2002/07/owl#> \n PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n INSERT DATA { GRAPH <urn:graph:zagoskin> { "

    def generate(self):
        name = input('Введите имя ')
        type = input('Введите тип билета adult или child ')
        birthday = input('Введите дту рождения в формате dd.MM.yyyy ')
        number = int(input('Введите номер билета в числовом формате '))
        price = int(input('Введите стоимость билета '))

        visitor = Visitor(name, type, birthday)
        ticket = Ticket(visitor, number, price)

        triplets = ticket.toTriplets()

        print(triplets)
        print('\n')

        sparql = SPARQLWrapper('http://localhost:8890/sparql-auth')
        sparql.setHTTPAuth('DIGEST')
        sparql.setCredentials("dba","root")

        for s, p, o in triplets:
            self.query += f" {s} {p} {o} ."
        self.query += " } }"
        print(self.query)
        sparql.setQuery(self.query)
        sparql.setMethod(POST)
        sparql.query()
        print('succesful insert')
