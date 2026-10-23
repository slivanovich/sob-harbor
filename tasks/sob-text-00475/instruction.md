{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNLM CityHopper: NLM CityHopper full name Nederlandse Luchtvaart Maatschappij (Dutch Aviation Company), was a Dutch commuter airline, founded in 1966.  Its head office was in Building 70 in Schiphol Airport East in Haarlemmermeer, Netherlands.\n\nGroninger Luchtvaart Maatschappij: The Groninger Luchtvaart Maatschappij (GLM) was a Dutch start-up airline which aimed to start operations in 2013 from Groningen Airport Eelde with a twice daily service to London Southend Airport.  Plans include flights to Copenhagen, Brussel and Paris.  The airline is yet to acquire any aircraft and has yet to advertise any routes for sale.  GLM has joined the Join!  Regional Airlines start up initiative to help get the airline started with leased aircraft.\n\nAruba Airlines: Arubaanse Luchtvaart Maatschappij N.V., operating as Aruba Airlines, is an airline headquartered in Oranjestad, Aruba.  Established in 2006, it has a fleet of four aircraft and 300 employees as of July 2016.\n\nALM Antillean Airlines: ALM Antillean Airlines (Dutch: \"Antilliaanse Luchtvaart Maatschappij\" ) was the main airline of the Netherlands Antilles between its foundation in 1964 and its shut-down in 2001, operating out of Aruba, Bonaire, and Curaçao.\n\nKNILM: Koninklijke Nederlandsch-Indische Luchtvaart Maatschappij (in English: Royal Dutch Indies Airways) was the airline of the former Dutch East Indies.  Headquartered in Amsterdam, KNILM was \"not\" a subsidiary of the better-known KLM (Royal Dutch Airlines), despite the similar name.  The airline had its headquarters in Amsterdam and an office in Batavia (current Jakarta).\n\nHipódromo Camarero: Hipódromo Camarero, formerly known as El Nuevo Comandante, is a horse racing building located in Canóvanas, Puerto Rico, to the east of San Juan and Carolina.  It is about a fifteen-minute drive from Carolina's Luis Muñoz Marín International Airport, and 25 minutes east from the Isla Verde hotel area.  The new administration of Camarero Race Track Corporation start operations on January 5, 2007.\n\nDuqm Jaaluni Airport: Duqm Jaaluni Airport (IATA: JNJ) is an airport in the vicinity of Duqm in the Al Wusta Region of Oman.  Oman Air was due to start operations on July 23, 2014.  The airport was officially opened on 24 July 2014, with Oman Air announcing that there will be four scheduled flights a week (Sunday, Monday, Wednesday, Thursday).\n\nGroningen Airport Eelde: Groningen Airport Eelde (IATA: GRQ, ICAO: EHGG) is a civilian international airport near Eelde in the province of Drenthe in the northeastern Netherlands.  It is 4.8 NM south of the city of Groningen.\n\nSurinam Airways: Surinam Airways (Dutch: \"Surinaamse Luchtvaart Maatschappij\" ), also known by its initials \"SLM\", is the flag carrier of Suriname, based in Paramaribo.  It operates regional and long-haul scheduled passenger services.  Its hub is at Johan Adolf Pengel International Airport.\n\nKLM: KLM Royal Dutch Airlines, legally \"Koninklijke Luchtvaart Maatschappij N.V.\", is the flag carrier airline of the Netherlands.  KLM is headquartered in Amstelveen, with its hub at nearby Amsterdam Airport Schiphol.  It is part of the Air France–KLM group, and is a member of the SkyTeam airline alliance.  KLM was founded in 1919; it is the oldest airline in the world still operating under its original name and had 32,505 employees as of 2013 .  KLM operates scheduled passenger and cargo services to 145 destinations.\n\nQuestion: What province is the airport at which Groninger Luchtvaart Maatschappij aimed to start operations located in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airline_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airline.\"\n    },\n    \"airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport where the airline aimed to operate.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"province\": {\n          \"type\": \"string\",\n          \"description\": \"The province where the airport is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the airport is located.\"\n        }\n      },\n      \"required\": [\n        \"province\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"airline_name\",\n    \"airport_name\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airline_name": {
        "type": "string",
        "description": "The name of the airline."
      },
      "airport_name": {
        "type": "string",
        "description": "The name of the airport where the airline aimed to operate."
      },
      "location": {
        "type": "object",
        "properties": {
          "province": {
            "type": "string",
            "description": "The province where the airport is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the airport is located."
          }
        },
        "required": [
          "province",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "airline_name",
      "airport_name",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
