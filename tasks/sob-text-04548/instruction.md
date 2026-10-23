{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMorphett Vale, South Australia: Morphett Vale is a southern suburb of Adelaide, South Australia in the City of Onkaparinga.  It is the largest suburb in the state, with a population of more than 23,000 and an area of 12.76 km², followed by Paralowie with nearly 10,000 fewer residents.  There are approximately 1,000 businesses in Morphett Vale.\n\nPatpa railway station: Patpa is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.\n\nTaringa railway station, South Australia: Taringa railway station was a ground level stopping place during the passenger transport days of the Willunga railway line which opened in 1915, and a 1965 reference mentioned that it was no longer used at that date.\n\nMcLaren Vale railway station: McLaren Vale is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line and was an unattended crossing station after 1957.  The station yard was noted for its impressive avenue of giant pine trees.\n\nHappy Valley railway station: Happy Valley is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.\n\nYetto railway station: Yetto was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.  It was in what is now the suburb of Morphett Vale\n\nCoorara railway station: Coorara is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.\n\nPimpala railway station: Pimpala is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.\n\nPikkara railway station: Pikkara is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.  It was located just north of McMurtrie Road on the southeastern outskirts of McLaren Vale.\n\nMoana railway station: Moana is a closed railway station in Adelaide, South Australia.  It was a ground level stopping place during the passenger transport days of this line, and a 1965 reference mentioned that it was no longer used at that date.\n\nQuestion: Yetto was a ground level stopping place during the passenger transport days of this line, was in what is now the suburb of Morphett Vale, a southern suburb of Adelaide, South Australia in the City of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"suburb_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the suburb.\"\n    },\n    \"administrative_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city_of_onkaparinga\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the City (local government area) that the suburb is located in.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the suburb is located.\"\n        },\n        \"is_southern_suburb_of_adelaide\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the suburb is a southern suburb of Adelaide.\"\n        }\n      },\n      \"required\": [\n        \"city_of_onkaparinga\",\n        \"state\",\n        \"is_southern_suburb_of_adelaide\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"suburb_demographics\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_largest_suburb_in_state\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the suburb is the largest in its state by population.\"\n        },\n        \"population\": {\n          \"type\": \"integer\",\n          \"description\": \"The population of the suburb.\"\n        },\n        \"area_km2\": {\n          \"type\": \"number\",\n          \"description\": \"The area of the suburb in square kilometers.\"\n        },\n        \"number_of_businesses\": {\n          \"type\": \"integer\",\n          \"description\": \"The approximate number of businesses in the suburb.\"\n        }\n      },\n      \"required\": [\n        \"is_largest_suburb_in_state\",\n        \"population\",\n        \"area_km2\",\n        \"number_of_businesses\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"suburb_name\",\n    \"administrative_location\",\n    \"suburb_demographics\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "suburb_name": {
        "type": "string",
        "description": "The name of the suburb."
      },
      "administrative_location": {
        "type": "object",
        "properties": {
          "city_of_onkaparinga": {
            "type": "string",
            "description": "The name of the City (local government area) that the suburb is located in."
          },
          "state": {
            "type": "string",
            "description": "The state where the suburb is located."
          },
          "is_southern_suburb_of_adelaide": {
            "type": "boolean",
            "description": "Indicates if the suburb is a southern suburb of Adelaide."
          }
        },
        "required": [
          "city_of_onkaparinga",
          "state",
          "is_southern_suburb_of_adelaide"
        ],
        "additionalProperties": false
      },
      "suburb_demographics": {
        "type": "object",
        "properties": {
          "is_largest_suburb_in_state": {
            "type": "boolean",
            "description": "Indicates if the suburb is the largest in its state by population."
          },
          "population": {
            "type": "integer",
            "description": "The population of the suburb."
          },
          "area_km2": {
            "type": "number",
            "description": "The area of the suburb in square kilometers."
          },
          "number_of_businesses": {
            "type": "integer",
            "description": "The approximate number of businesses in the suburb."
          }
        },
        "required": [
          "is_largest_suburb_in_state",
          "population",
          "area_km2",
          "number_of_businesses"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "suburb_name",
      "administrative_location",
      "suburb_demographics"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
