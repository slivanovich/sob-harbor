{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRolls-Royce Wraith (2013): The Rolls-Royce Wraith is a British handmade 4 seat luxury grand tourer manufactured by Rolls-Royce Motor Cars and based on the chassis of the Rolls-Royce Ghost.\n\nRolls-Royce Wraith: Rolls-Royce Wraith may refer to a number of different automobiles :\n\nRolls-Royce Phantom Coupé: The Rolls-Royce Phantom Coupé is a British handmade (except chassis) luxury car manufactured by Rolls-Royce Motor Cars that debuted at the 2008 Geneva International Auto Show in Geneva, Switzerland, on 6 March 2008.  The platform is based on the 2003 Rolls-Royce Phantom and has styling heavily derived from the Rolls-Royce 100EX, a concept car unveiled to celebrate the company's centennial in 2004.\n\nBentley 8 Litre: The Bentley 8 Litre was a luxury car based on the largest rolling chassis made by Bentley Motors Limited at Cricklewood, London.  Announced 15 September 1930, it was also the last completely new model by Bentley before the company's financial collapse and forced sale to Rolls-Royce Limited; a 4-Litre engine in a shortened chassis was announced on 15 May 1931.  Intended to provide the basis for a super-luxury car for very wealthy buyers, the 8 Litre chassis was introduced a year into the Great Depression.  Sales of the 8-litre were too slow to turn the company's finances around and, less than nine months after the 8-litre's introduction, Bentley Motors was placed into receivership.\n\nRolls-Royce Silver Dawn: The Rolls-Royce Silver Dawn is a full-size luxury car that was produced by Rolls-Royce at their Crewe works between 1949 and 1955.  It was the first Rolls-Royce car to be offered with a factory built body which it shared, along with its chassis, with the Bentley Mark VI until 1952 and then the Bentley R Type until production finished in 1955.  The car was first introduced as an export only model.  The left hand drive manual transmission models had a column gear change, while right hand drives had a floor change by the door.  Only with the R Type based model was it officially available on the home market, from October 1953.\n\nRolls-Royce Ghost: The Rolls-Royce Ghost is a British luxury car manufactured by Rolls-Royce Motor Cars.  The \"Ghost\" nameplate, named in honour of the Silver Ghost, a car first produced in 1906, was announced in April 2009 at the Auto Shanghai show.  During development, the Ghost was known as the \"RR04\".  Designed as a smaller, \"more measured, more realistic car\" than the Phantom, aiming for a lower price category for Rolls-Royce models, the retail price is around £170,000.  The production model was officially unveiled at the 2009 Frankfurt Motor Show.  The Ghost Extended Wheelbase was introduced in 2011.\n\nMaybach 57 and 62: The Maybach 57 (chassis no.  W240) and 62 (chassis no.  V240) were the first automobile models of the Maybach brand since the brand's revival by DaimlerChrysler AG (now Daimler AG).  They are derived from the Benz Maybach concept car presented at the 1997 Tokyo Motor Show.  The concept car was based on the Mercedes-Benz S-Class sedan, as are the production models.  The Luxury Brand Status Index 2008 voted the Maybach first place, ahead of Rolls-Royce and Bentley.  The models ceased production in 2013, due to continued financial losses for the marque, and sales at one-fifth the level of the profitable Rolls-Royce models.\n\nRolls-Royce Wraith (1938): Full name: Rolls-Royce 25/30 h.p. \"Wraith\".  Not to be confused with the earlier small horsepower (Goshawk) car, the 25/30 h.p. ; as the 'Wraith' was simply a progression of this the name, for the most part, wasn't seen as something to re-think completely.\n\nRolls-Royce Silver Wraith: The Silver Wraith was the first post-war Rolls-Royce.  It was made from 1946 to 1958 as only a chassis at Rolls-Royce's former Merlin engine plant, their Crewe factory, alongside the shorter Bentley Mark VI.  The Bentley too was available as a chassis for coachbuilders but also for the first time could be bought with a Rolls-Royce built standard steel body.\n\nBentley 4 Litre: The Bentley 4 Litre was a motor car built on rolling chassis made by Bentley Motors Limited.  The 4 litre chassis was conceived and built in a failed attempt to restore Bentley to a good financial state.  Announced 15 May 1931, it used a modified four litre Ricardo IOE engine in a shortened 8 litre chassis at two-thirds of the price of the 8 Litre in an attempt to compete with the Rolls-Royce 20/25.  Instead, Bentley went into receivership shortly afterward, from which it was purchased by Rolls-Royce Limited.\n\nQuestion: The Rolls-Royce Wraith is  based on the chassis of what car that was known as RR04 during development?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"query_car_model\": {\n      \"type\": \"string\",\n      \"description\": \"The car model mentioned in the question.\"\n    },\n    \"query_car_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The specific year of the query car model, if provided.\"\n    },\n    \"base_car_model\": {\n      \"type\": \"string\",\n      \"description\": \"The car model whose chassis the query car is based on.\"\n    },\n    \"base_car_development_name\": {\n      \"type\": \"string\",\n      \"description\": \"The development name of the base car model.\"\n    },\n    \"chassis_relationship_confirmed\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the chassis relationship between the two cars is confirmed in the text.\"\n    }\n  },\n  \"required\": [\n    \"query_car_model\",\n    \"query_car_year\",\n    \"base_car_model\",\n    \"base_car_development_name\",\n    \"chassis_relationship_confirmed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "query_car_model": {
        "type": "string",
        "description": "The car model mentioned in the question."
      },
      "query_car_year": {
        "type": "integer",
        "description": "The specific year of the query car model, if provided."
      },
      "base_car_model": {
        "type": "string",
        "description": "The car model whose chassis the query car is based on."
      },
      "base_car_development_name": {
        "type": "string",
        "description": "The development name of the base car model."
      },
      "chassis_relationship_confirmed": {
        "type": "boolean",
        "description": "Indicates if the chassis relationship between the two cars is confirmed in the text."
      }
    },
    "required": [
      "query_car_model",
      "query_car_year",
      "base_car_model",
      "base_car_development_name",
      "chassis_relationship_confirmed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
