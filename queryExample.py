class QueryExample:
    def getFirstExample(self) -> str:
        query = """
                Prefix owl:	    <http://www.w3.org/2002/07/owl#>
                Prefix rdf:	    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                Prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
                Prefix ent:	    <http://www.menthor.net/myontology#>

                SELECT *
                FROM <urn:graph:zagoskin>
                WHERE {?x rdf:type ?type}
                """
        return query
    
    def getSecondExample(self) -> str:
        query = """
                Prefix owl:	    <http://www.w3.org/2002/07/owl#>
                Prefix rdf:	    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                Prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
                Prefix ent:	    <http://www.menthor.net/myontology#>

                SELECT ?ind ?type
                FROM <urn:graph:zagoskin>
                WHERE {
                    ?ind rdf:type ?type .
                    ?type rdfs:subClassOf ent:Ticket
                }
                """
        return query
    
    def getThirdExample(self) -> str:
        query = """
                Prefix owl:	    <http://www.w3.org/2002/07/owl#>
                Prefix rdf:	    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                Prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
                Prefix ent:	    <http://www.menthor.net/myontology#>

                SELECT *
                FROM <urn:graph:zagoskin>
                WHERE {
                    ?ind rdf:type ?type .
                    ?type rdfs:subClassOf ent:Transport_routes
                }
                """
        return query
    
    def getFourthExample(self) -> str:
        query = """
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX ont: <http://www.menthor.net/myontology#>

                select *
                FROM <urn:graph:zagoskin>
                where
                {
                    ?ind rdf:type ?type .
                    ?type owl:equivalentClass* ont:Exhibition_visitor .
                    ?ind ont:birthday ?bd .
                }
                """
        return query
    
