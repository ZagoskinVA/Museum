from visitor import Visitor
class Ticket:
    def __init__(self, visitor: Visitor, number: int, price: int) -> None:
        self.visitor = visitor
        self.number = number
        self.price = price


    def toTriplets(self):
        return [(f'ent:{self.visitor.name}sTicket', 'rdf:type', 'owl:NamedIndividual'),
                (f'ent:{self.visitor.name}sTicket', 'rdf:type', f'ent:{self.visitor.type}_ticket'),
                (f'ent:{self.visitor.name}Visitor', 'rdf:type', 'owl:NamedIndividual'),
                (f'ent:{self.visitor.name}Visitor', 'rdf:type', f'ent:{self.visitor.type}_museum_visitor'),
                (f'ent:{self.visitor.name}Visitor', 'ent:birthday', f'"{self.visitor.birthday}"^^xsd:string'),
                (f'ent:{self.visitor.name}Visitor', 'ent:name2', f'"{self.visitor.name}"^^xsd:string'),
                (f'ent:{self.visitor.name}sTicket', 'ent:number', f'"{self.number}"^^xsd:integer'),
                (f'ent:{self.visitor.name}sTicket', 'ent:price', f'"{self.number}"^^xsd:integer'),
                (f'ent:{self.visitor.name}Visitor', 'ent:privileges_type', f'"{self.visitor.type}"^^xsd:string'),
                (f'ent:{self.visitor.name}', 'ent:ticket', f'ent:{self.visitor.name}sTicket'),
                (f'ent:{self.visitor.name}Visitor', 'ent:type1', f'"{self.visitor.type}"^^xsd:string'),
                (f'ent:{self.visitor.name}sTicket', 'ent:type2', f'"{self.visitor.type}"^^xsd:string')]






#[(dmap:Family_ticket, rdf:type, owl:Class), (dmap:Family_ticket, rdfs:label, Family_ticket), (dmap:Family_ticket, dmap:Name, $(Name)^^xsd:string), (dmap:Family_ticket, dmap:Number, $(Name)^^xsd:integer), (dmap:Family_ticket, dmap:Price, $(Name)^^xsd:integer)]
#
#
#
#
#