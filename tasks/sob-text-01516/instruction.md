{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAirAsia X: AirAsia X Berhad () (previously known as \"FlyAsianXpress Sdn.  Bhd.\"), operating as AirAsia X, is a long-haul budget airline based in Malaysia, and a sister company of AirAsia.  It commenced operations on 2 November 2007 with its first service flown from Kuala Lumpur International Airport, Malaysia, to Gold Coast Airport in Australia.  AirAsia X flies to destinations within Asia and Australia.  The airline operates a fleet of 31 aircraft and has placed orders for 76 more.\n\nAir Freight NZ: Air Freight NZ was a cargo airline based in Auckland, New Zealand.  It operated scheduled overnight cargo services on behalf of owner Freightways, and is supported by sister company Fieldair holdings.  Domestic charter services are also operated.  Its main base is Auckland Airport, with hubs at Christchurch International Airport and Palmerston North International Airport.\n\nAustral Líneas Aéreas: Cielos del Sur S.A., operating as Austral Líneas Aéreas, more commonly known by its shortened name Austral, is a domestic airline of Argentina, the sister company of Aerolíneas Argentinas.  It is the second largest domestic scheduled airline in the country, after Aerolíneas Argentinas itself.  As a subsidiary of Aerolíneas Argentinas, the company shares its headquarters with that airline, which is located in the Aeroparque Jorge Newbery of Buenos Aires, the main base of operations of the company.\n\nSauce Viejo, Argentina: Sauce Viejo is a city in the province of Santa Fe, Argentina.  It is located about 22 km from the province's capital city, Santa Fe, and has a population of 6,825 inhabitants (2001 census ) which represents a growth of 87.96% compared to the 3,631 inhabitants (2001 census ) of the previous census.\n\nSAS Commuter: SAS Commuter, also branded as Scandinavian Commuter, was a regional airline which operated in Denmark, Norway and Sweden.  A sister company of Scandinavian Airlines (SAS), it operated various regional services on behalf of the Scandinavian flag carrier.  The airline was headquartered at Copenhagen Airport, which also served as its main base.  It later also operated bases at Tromsø Airport; Stockholm Arlanda Airport; Trondheim Airport, Værnes and Bergen Airport, Flesland.\n\nThames &amp; Hudson: Thames & Hudson (also Thames and Hudson and sometimes T&H for brevity) is a publisher of illustrated books on art, architecture, design, and visual culture.  With its headquarters in London, England, it has a sister company in New York and subsidiaries in Melbourne, Singapore and Hong Kong.  In Paris, it has a further subsidiary company, Interart, which is engaged in the distribution of English-language books and a sister company, Éditions Thames & Hudson.  It has been an independent, family-owned company since its founding in 1949.\n\nNortheast Express Regional Airlines: Northeast Express Regional Airlines was a regional airline based in Manchester, New Hampshire.  The airline was originally known as Valley Airlines started by Maine businessman Roland Martin it capitalized on the US government essential air service by flying intrastate Maine to small communities that otherwise would not have access to airline services.  Then the airline was brought by Allen Caruso of Bar Harbor Airlines fame.  They rebranded and became Northeast Express Regional Airlines and became a Northwest Airlines codeshare affiliate dba Northwest Airlink.  The airline declared bankruptcy and was liquidated, along with its sister company Precision Airlines, in 1995.\n\nBraathens Helikopter: Braathens Helikopter A/S was a Norwegian helicopter airline based at Stavanger Airport, Sola, and Bergen Airport, Flesland.  It used a fleet of seven Aérospatiale Super Pumas to serve offshore oil platforms in the North Sea.  The customers were Phillips Petroleum, Norsk Hydro, Statoil, Amoco and British Petroleum, serving their oil fields Ekofisk, Oseberg, Gullfaks, Veslefrikk, Valhall, Ula and Gyda.  Braathens Helikopter operated from 1989 to 1993, after which it was sold to and merged with the main competitor, Helikopter Service.  Braathens Helikopter was owned by Ludvig G. Braathens Rederi and was a sister company of the airline Braathens SAFE.\n\nPAL Express: PAL Express, formerly Air Philippines and Airphil Express, is an airline operating under the business name of Air Philippines Corporation.  It operates domestic and international scheduled services from Manila, Cebu, Davao and Zamboanga.  The airline has been re-branded a number of times, first as Air Philippines, then Airphil Express, and is now known as PAL Express.  After a series of financial losses, Air Philippines ceased operations until it was acquired by investors from Philippine Airlines.  After the acquisition, the airline was re-launched as PAL Express, operating some routes and slot assignments of its sister company Philippine Airlines until management decided to re-brand the carrier as a budget airline known as Airphil Express.  However, in March 2013, the company's CEO announced that the name would be reverted to PAL Express.  As a codeshare partner of Philippine Airlines, PAL Express operates as a full service carrier within a low-cost model.\n\nSauce Viejo Airport: Sauce Viejo Airport (Spanish: \"Aeropuerto de Santa Fe – Sauce Viejo\" ) (IATA: SFN, ICAO: SAAV) is an airport in Santa Fe Province, Argentina serving the city of Santa Fe.  It is served by Austral Líneas Aéreas.\n\nQuestion: What is the sister company of the airline which serves Sauce Viejo Airport?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airport_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the airport.\"\n        },\n        \"iata_code\": {\n          \"type\": \"string\",\n          \"description\": \"The IATA code of the airport.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"iata_code\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"airline_serving_airport\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the airline that serves the airport.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of airline (e.g., domestic, cargo, long-haul budget).\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the airline is based.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sister_company\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the sister company.\"\n        },\n        \"relationship_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of relationship to the serving airline.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"relationship_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"airport_info\",\n    \"airline_serving_airport\",\n    \"sister_company\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airport_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the airport."
          },
          "iata_code": {
            "type": "string",
            "description": "The IATA code of the airport."
          }
        },
        "required": [
          "name",
          "iata_code"
        ],
        "additionalProperties": false
      },
      "airline_serving_airport": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the airline that serves the airport."
          },
          "type": {
            "type": "string",
            "description": "The type of airline (e.g., domestic, cargo, long-haul budget)."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the airline is based."
          }
        },
        "required": [
          "name",
          "type",
          "country_of_origin"
        ],
        "additionalProperties": false
      },
      "sister_company": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the sister company."
          },
          "relationship_type": {
            "type": "string",
            "description": "The type of relationship to the serving airline."
          }
        },
        "required": [
          "name",
          "relationship_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "airport_info",
      "airline_serving_airport",
      "sister_company"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
