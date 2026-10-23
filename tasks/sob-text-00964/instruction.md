{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nElectoral district of Florey: Florey is an electoral district of the House of Assembly in the Australian state of South Australia.  It is named after scientist Howard Florey, who was responsible for the development of penicillin.  It is a 16.1 km² urban electorate in Adelaide's north-east, taking in the suburbs of Modbury, Modbury Heights and Modbury North, as well as parts of Gilles Plains, Hope Valley, Para Hills, Para Vista, Redwood Park, Ridgehaven, Valley View and Wynn Vale.\n\nElectoral district of Newland: Newland is an electoral district of the House of Assembly in the Australian state of South Australia.  It is named after pioneer Simpson Newland, a prominent figure in nineteenth-century South Australia.  It is a 69.3 km² suburban electorate in north-eastern Adelaide, taking in the suburbs of Banksia Park, Fairview Park, Lower Hermitage, Upper Hermitage, Houghton, St Agnes, Surrey Downs, Tea Tree Gully, Vista and Yatala Vale as well as parts of Chain of Ponds, Highbury, Hope Valley, Inglewood, Millbrook, Redwood Park and Ridgehaven.\n\nTea Tree Gully, South Australia: Tea Tree Gully, frequently written \"Teatree Gully\", is a suburb in the greater Adelaide, South Australia area, under the City of Tea Tree Gully.  Tea Tree Gully is in the City of Tea Tree Gully local government area, the South Australian House of Assembly electoral district of Newland and the Australian House of Representatives Division of Makin.\n\nCity of Tea Tree Gully: The City of Tea Tree Gully is a local council in the Australian state of South Australia, in the outer north-eastern suburbs of Adelaide.  The city has an estimated population of 98,861 people and is one of the most populous local government divisions in Adelaide.  The major business district in the city is at Modbury, where Tea Tree Plaza, the Civic Centre and the library are located.\n\nHoughton, South Australia: Houghton is a small town near Adelaide, South Australia.  It is located in the Adelaide Hills, in the City of Tea Tree Gully and the Adelaide Hills Council local government areas between Tea Tree Gully and Inglewood on the North East Road.\n\nModbury, South Australia: Modbury is a suburb of Adelaide, South Australia in the City of Tea Tree Gully.  Modbury is located at the end of the Adelaide O-Bahn and is home to the Tea Tree Plaza shopping complex and a Hospital.\n\nElectoral district of Tea Tree Gully: Tea Tree Gully was an electoral district of the House of Assembly in the Australian state of South Australia from 1970 to 1977.  The suburb of Tea Tree Gully has since been represented by the seat of Newland.\n\nKing's Baptist Grammar School: King's Baptist Grammar School is in Wynn Vale, a north eastern suburb of Adelaide, South Australia, having moved from nearby Tea Tree Gully where it was known as \"Tea Tree Gully Christian School\".  The school is known throughout the region for numerous outstanding accolades.  The school is also recognized for its annual musical production, held at the Shedley Theater in Elizabeth.  In 2013, 950 students were enrolled at the school.\n\nVista, South Australia: Vista is a small north-eastern suburb of Adelaide, South Australia and is within the City of Tea Tree Gully local government area.  It is adjacent to Houghton, Tea Tree Gully, St Agnes and Hope Valley.\n\nMartin Faull: Martin Peter Faull (born 10 May 1968) is a former Australian cricketer, who regularly played for South Australia during the 1990s.  Born in Darwin, Northern Territory, Faull played cricket for South Australia at both under-16 and under-19 level, as well as for the state's Colts and Second XI sides.  Faull made his first-class debut for South Australia in February 1991 during the 1990–91 Sheffield Shield, in a match against New South Wales at the Adelaide Oval.  His first first-class half-century was made the following month, a score of 89 runs in the return match against New South Wales, batting at number three.  Faull played regularly at both Sheffield Shield and domestic one-day level throughout the rest of the decade, at first as a middle-order batsman, but later as an opening batsman, often opening alongside Greg Blewett or David Fitzgerald.  He was more successful at first-class level, with the 1996–97 season his best, where he scored 459 runs from eight matches (including six half-centuries).  Faull's only first-class century came during the 1997–98 season, a score of 103 runs in the second innings of a match against New South Wales, which followed a first innings score of 58 runs.  Overall, he played 30 first-class and nine List A matches over his career, with his final matches at both levels coming in the 1998–99 season.  In the SACA District competition, Faull played for the Tea Tree Gully District Cricket Club.\n\nQuestion: Florey electoral district takes in what suburb in Tea Tree Gully, Adelaide, South Australia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"electoral_district_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the electoral district.\"\n    },\n    \"local_government_area\": {\n      \"type\": \"string\",\n      \"description\": \"The local government area where the suburb is located.\"\n    },\n    \"suburb_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the suburb that is part of both the electoral district and the local government area.\"\n    },\n    \"suburb_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the suburb's location or key features.\"\n        }\n      },\n      \"required\": [\n        \"location_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"electoral_district_name\",\n    \"local_government_area\",\n    \"suburb_name\",\n    \"suburb_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "electoral_district_name": {
        "type": "string",
        "description": "The name of the electoral district."
      },
      "local_government_area": {
        "type": "string",
        "description": "The local government area where the suburb is located."
      },
      "suburb_name": {
        "type": "string",
        "description": "The name of the suburb that is part of both the electoral district and the local government area."
      },
      "suburb_details": {
        "type": "object",
        "properties": {
          "location_description": {
            "type": "string",
            "description": "A description of the suburb's location or key features."
          }
        },
        "required": [
          "location_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "electoral_district_name",
      "local_government_area",
      "suburb_name",
      "suburb_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
