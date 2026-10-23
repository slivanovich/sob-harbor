{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStrathfield, New South Wales: Strathfield is a suburb in the Inner West of Sydney, Australia.  It is located 12 kilometres west of the Sydney central business district and is the administrative centre of the Strathfield Local Government Area.  A small section of the suburb north of the railway line sits in the local government area of the City of Canada Bay, while the area east of The Boulevard sits within the Burwood Council.  North Strathfield and Strathfield South are separate suburbs, to the north and south respectively.\n\nPalais Theatre: The Palais Theatre is a concert venue and theatre located in the Melbourne inner suburb of St Kilda.  With a capacity of 2,896 people, it is the largest seated theatre in Australia.\n\nAlbert Park, Victoria: Albert Park is an inner suburb of Melbourne, Australia, 3 km south of Melbourne's central business district.  Its local government area is the City of Port Phillip.  At the 2011 census , Albert Park had a population of 5,955.\n\nMiddle Park, Victoria: Middle Park is an inner suburb of Melbourne, Victoria, Australia, 4 km south of Melbourne's Central Business District.  Its local government area is the City of Port Phillip.  At the 2011 Census, Middle Park had a population of 4,058.\n\nBalaclava, Victoria: Balaclava is an inner suburb of Melbourne, Victoria, Australia, 7 km south from Melbourne's Central Business District.  Its local government area is the City of Port Phillip.  At the 2011 Census, Balaclava had a population of 5,383.\n\nSt Kilda, Victoria: St Kilda is an inner suburb (neighbourhood) of the metropolitan area of Melbourne, Victoria, Australia, 6 km south-east of Melbourne's Central Business District.  Its local government area is the City of Port Phillip.  At the 2011 Census, St Kilda had a population of 17,795.\n\nElwood, Victoria: Elwood is an inner suburb of Melbourne, Victoria, Australia, 8 km south of Melbourne's Central Business District.  Its local government area is the City of Port Phillip.  At the 2011 Census, Elwood had a population of 14,638.\n\nPort Melbourne, Victoria: Port Melbourne is an inner suburb of Melbourne, Australia, 5 km south-west from Melbourne's Central Business District.  It is split between the local government areas of Melbourne and Port Phillip.  The area to the north of the West Gate Freeway is in the City of Melbourne.  The area to the south is in the City of Port Phillip.  At the 2011 Census, Port Melbourne had a population of 14,521.\n\nSouth Melbourne, Victoria: South Melbourne is an inner suburb of Melbourne, Australia, 2 km south of Melbourne's Central Business District (CBD).  It is in the local government area of the City of Port Phillip.  At the 2011 Census, South Melbourne had a population of 9,317.\n\nRipponlea, Victoria: Ripponlea is an inner suburb of Melbourne, Victoria, Australia, named after the adjoining Rippon Lea Estate.  It is 7 km south east of Melbourne's Central Business District.  Its local government area is the City of Port Phillip.  At the 2011 Census, Ripponlea had a population of 1,478.\n\nQuestion: The Palais Theater is located in what inner suburb, whose local government area is the City of Port Philip?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"theatre_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the theatre.\"\n    },\n    \"suburb_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the inner suburb where the theatre is located.\"\n    },\n    \"city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the suburb is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the suburb is located.\"\n    },\n    \"local_government_area\": {\n      \"type\": \"string\",\n      \"description\": \"The local government area of the suburb.\"\n    }\n  },\n  \"required\": [\n    \"theatre_name\",\n    \"suburb_name\",\n    \"city\",\n    \"state\",\n    \"local_government_area\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "theatre_name": {
        "type": "string",
        "description": "The name of the theatre."
      },
      "suburb_name": {
        "type": "string",
        "description": "The name of the inner suburb where the theatre is located."
      },
      "city": {
        "type": "string",
        "description": "The city where the suburb is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the suburb is located."
      },
      "local_government_area": {
        "type": "string",
        "description": "The local government area of the suburb."
      }
    },
    "required": [
      "theatre_name",
      "suburb_name",
      "city",
      "state",
      "local_government_area"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
