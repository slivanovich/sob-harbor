{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichigan's 6th House of Representatives district: Michigan's 6th House of Representatives district (also referred to as Michigan's 6th House district) is a legislative district within the Michigan House of Representatives located in the eastern portion of Wayne County, Michigan, including much of Southwest Detroit and the Cities of Ecorse and River Rouge.  The district was created in 1965, when the Michigan House of Representatives district naming scheme changed from a county-based system to a numerical one.\n\nMichigan's 3rd House of Representatives district: Michigan's 3rd House of Representatives district (also referred to as Michigan's 3rd House district) is a legislative district within the Michigan House of Representatives located in the northeastern portion of Wayne County, Michigan, including much of Detroit's East Side.  The district was created in 1965, when the Michigan House of Representatives district naming scheme changed from a county-based system to a numerical one.\n\nTimothy Leonard (Colorado politician): Timothy Leonard is a state representative from Evergreen, Colorado.  A Republican, Leonard represents Colorado House of Representatives District 25, which encompasses much of western Jefferson County, including the communities of Aspen Park, Dakota Ridge, Evergreen, Fairmount, Genesee, Idledale, Indian Hills, Kittredge, and Morrison.\n\nKenneth Fredette: Kenneth Wade Fredette (born March 3, 1964) is a member of the Maine House of Representatives for District 25.  Fredette's district represents part of Penobscot County, Maine including the towns of Corinna, Maine; Exeter, Maine; Newport, Maine; Plymouth, Maine; and part of Corinth, Maine.\n\nMichigan's 4th House of Representatives district: Michigan's 4th House of Representatives district (also referred to as Michigan's 4th House district) is a legislative district within the Michigan House of Representatives located in the eastern portion of Wayne County, Michigan, including much of Detroit's Midtown and New Center neighborhoods, and all of the city of Hamtramck.  The district was created in 1965, when the Michigan House of Representatives district naming scheme changed from a county-based system to a numerical one.\n\nRay Scott (Colorado politician): Ray Scott (born in Youngstown, Ohio) is an American politician and a Republican member of the Colorado State Senate representing District 7 since January 7, 2015.  Scott served consecutively from January 12, 2011 until January 9, 2013 in the Colorado House of Representatives District 54 seat, and from January 9, 2013 to January 7, 2015 in the Colorado House of Representatives District 55 seat.\n\nMichigan's 2nd House of Representatives district: Michigan's 2nd House of Representatives district (also referred to as Michigan's 2nd House district) is a legislative district within the Michigan House of Representatives located in the northeastern portion of Wayne County, Michigan, including much of Detroit's East Side and the Cities of Grosse Pointe Farms, Grosse Pointe, and Grosse Pointe Park.  The district was created in 1965, when the Michigan House of Representatives district naming scheme changed from a county-based system to a numerical one.\n\nNewport, Maine: Newport is a town in Penobscot County, Maine, United States.  The population was 3,275 at the 2010 census.  Newport is situated on Sebasticook Lake.\n\nTim Rave: Timothy Allan Rave (born July 24, 1967) is an American politician and a Republican member of the South Dakota Senate representing District 25 since January 11, 2011.  Rave served consecutively in the South Dakota Legislature from January 2003 until January 11, 2011 in the South Dakota House of Representatives District 25 seat.\n\nMichigan's 5th House of Representatives district: Michigan's 5th House of Representatives district (also referred to as Michigan's 5th House district) is a legislative district within the Michigan House of Representatives located in the eastern portion of Wayne County, Michigan, including much of Southwest Detroit.  The district was created in 1965, when the Michigan House of Representatives district naming scheme changed from a county-based system to a numerical one.\n\nQuestion: Which Lake, home to Newport, Maine, is located in Maine's House of Representatives District 25?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"lake_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the lake.\"\n    },\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town located on the lake.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the town and district are located.\"\n    },\n    \"house_district_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The numerical identifier of the House of Representatives district.\"\n    },\n    \"house_district_representative\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the representative for the specified House district.\"\n    }\n  },\n  \"required\": [\n    \"lake_name\",\n    \"town_name\",\n    \"state\",\n    \"house_district_number\",\n    \"house_district_representative\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "lake_name": {
        "type": "string",
        "description": "The name of the lake."
      },
      "town_name": {
        "type": "string",
        "description": "The name of the town located on the lake."
      },
      "state": {
        "type": "string",
        "description": "The state where the town and district are located."
      },
      "house_district_number": {
        "type": "integer",
        "description": "The numerical identifier of the House of Representatives district."
      },
      "house_district_representative": {
        "type": "string",
        "description": "The name of the representative for the specified House district."
      }
    },
    "required": [
      "lake_name",
      "town_name",
      "state",
      "house_district_number",
      "house_district_representative"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
