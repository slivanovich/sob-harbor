{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHeath Streak: Heath Hilton Streak (born 16 March 1974, in Bulawayo) is a former Zimbabwean cricketer, and a former Test and ODI captain.  By his statistical record, he is the best bowler to have played for Zimbabwe.  He is the only Zimbabwean bowler to have taken over 100 Test wickets and one of only 4 Zimbabwean bowlers to have taken over 100 ODI wickets (the others being Grant Flower, Prosper Utseya & Ray Price).  He is currently the head coach of Zimbabwe national cricket team.\n\nEthan Dube: Langalibalele Ethan Dube (born 7 September 1970) is a former Zimbabwean cricketer who represented Matabeleland in Zimbabwean domestic cricket.  He played as a right-arm fast bowler, but had his career cut short by knee and back injuries.  After his retirement, Dube moved into sports administration, serving as chairman of the Matabeleland Cricket Association, as a selector for the Zimbabwean national team, and as a member of the government's Sports and Recreation Commission.\n\nGlen Barrett: Glen Frederick Barrett (born 31 March 1979) is a former Zimbabwean cricketer who represented several teams in Zimbabwean domestic cricket.  He played predominantly as a middle-order batsman.\n\nKyle Jarvis: Kyle Malcolm Jarvis (born 16 February 1989) is a Zimbabwean cricketer who represents Zimbabwe and played for Lancashire.  The son of another former Zimbabwean international cricketer Malcolm Jarvis, he was educated at St Johns College, Harare, where he excelled at rugby and cricket.  Kyle was a key bowler for Zimbabwe in the 2008 Under-19 World Cup and he also played for the Zimbabwe U-19 Rugby Team.\n\nLance Malloch-Brown: Lance Stephen Malloch-Brown (born 29 June 1979) is a former Zimbabwean cricketer who represented several teams in Zimbabwean domestic cricket.  He played as a right-handed opening batsman.\n\nGraeme Ferreira: Graeme David Ferreira (born 10 April 1977) is a former Zimbabwean cricketer who represented Matabeleland and Midlands in Zimbabwean domestic cricket.  He played as an all-rounder, batting right-handed and bowling right-arm off-spin.\n\nGrant Flower: Grant William Flower (born 20 December 1970) is a former Zimbabwean cricketer and a former ODI captain, who played Tests and ODIs.  He is rated among the best Zimbabwean cricketers in history for his handy left arm spin and fine batting skills.  He was a fitness fanatic who spends hours in the gym, and was also regarded as a brilliant fielder who was usually seen in the gully.  \"Flower Power\", the combination of Grant and his brother Andy Flower, was the mainstay of Zimbabwean batting for a decade.  He was his team's most successful opening batsman who played the role of anchorman, with strokeplayers coming in down the order.\n\nHarare: Harare ( ; officially called Salisbury until 1982) is the capital and most populous city of Zimbabwe.  Situated in the north-east of the country in the heart of historic Mashonaland, the city has an estimated population of 1,606,000 (2009), with 2,800,000 in its metropolitan area (2006).  Administratively, Harare is a metropolitan province, which also incorporates Chitungwiza town and Epworth.  It is situated at an elevation of 1,483 m above sea level and its climate falls into the subtropical highland category.\n\nGavin Briant: Gavin Aubrey Briant (born 11 April 1969 in Salisbury - now Harare) is a former Zimbabwean cricketer.\n\nKudzai Taibu: Kudzai James Taibu (born 20 November 1984) is a former Zimbabwean cricketer who represented Mashonaland and Manicaland in Zimbabwean domestic cricket.  He played as a right-handed top-order batsman and occasional wicket-keeper.\n\nQuestion: The former Zimbabwean cricketer was born in the capital city with the population of how many?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cricketer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former Zimbabwean cricketer.\"\n    },\n    \"birth_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the cricketer was born.\"\n    },\n    \"is_capital_city\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the birth city is the capital city of Zimbabwe.\"\n    },\n    \"city_population\": {\n      \"type\": \"integer\",\n      \"description\": \"The estimated population of the birth city.\"\n    },\n    \"population_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year for which the city population was estimated.\"\n    }\n  },\n  \"required\": [\n    \"cricketer_name\",\n    \"birth_city\",\n    \"is_capital_city\",\n    \"city_population\",\n    \"population_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cricketer_name": {
        "type": "string",
        "description": "The name of the former Zimbabwean cricketer."
      },
      "birth_city": {
        "type": "string",
        "description": "The city where the cricketer was born."
      },
      "is_capital_city": {
        "type": "boolean",
        "description": "Indicates if the birth city is the capital city of Zimbabwe."
      },
      "city_population": {
        "type": "integer",
        "description": "The estimated population of the birth city."
      },
      "population_year": {
        "type": "integer",
        "description": "The year for which the city population was estimated."
      }
    },
    "required": [
      "cricketer_name",
      "birth_city",
      "is_capital_city",
      "city_population",
      "population_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
