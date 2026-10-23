{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAda High School (Ohio): Ada High School is a public high school located in Ada, Ohio.  It is the only high school in the Ada Exempted Village School District.\n\nAda, Serbia: Ada (; Hungarian: \"Ada\" ) is a town and municipality located in the North Banat District of the autonomous province of Vojvodina, Serbia.  It is situated near the river Tisa in the geographical region of Bačka.  The town has a population of 9,564, while Ada municipality has 16,991 inhabitants (2011 census).\n\nAda Kasseh: Kasseh is a town in the Ada East district, a district in the Greater Accra Region of Ghana.  It is a major town located between Sege and Sogakope on the Accra-Aflao road.  Kasseh has the biggest market in four districts(Ada West, Ada East, South Tongu and North Tongu) in its area.  Kasseh is connected to almost all the towns and villages in the Ada East district by road or path.  It is the most easily accessible town in the district.  It is connected by road to the district capital town of Ada Foah and the Town called Big Ada.\n\nAda (Ghana parliament constituency): Ada is one of the constituencies represented in the Parliament of Ghana.  It elects one Member of Parliament (MP) by the first past the post system of election.  The Ada constituency is located in the Dangme East District of the Greater Accra Region of Ghana.\n\nAda Ciganlija: Ada Ciganlija (Serbian Cyrillic: Ада Циганлија, ] ), colloquially shortened to Ada, is a river island that has artificially been turned into a peninsula, located in the Sava River's course through central Belgrade, the capital of Serbia.  The name can also refer to the adjoining artificial Lake Sava and its beach.  To take advantage of its central location, over the past few decades, it was turned into an immensely popular recreational zone, most notable for its beaches and sports facilities, which, during summer seasons, can have over 100,000 visitors daily and up to 300,000 visitors over the weekend.  Owing to this popularity, Ada Ciganlija has been commonly nicknamed \"More Beograda\" (\"Belgrade's Sea\"), which was officially accepted as an advertising slogan in 2008, stylised as \"More BeogrADA\".\n\nAda Municipal Airport: Ada Municipal Airport (IATA: ADT, ICAO: KADH, FAA LID: ADH) is a public airport located two miles (3 km) north of the central business district of Ada, a city in Pontotoc County, Oklahoma, United States.  It is owned by the City of Ada, which is located in southeast Oklahoma, 88 mi southeast of Oklahoma City.\n\nDangme East District: The Dangme East District is one of the ten (10) districts in the Greater Accra Region of Ghana, and covers a surface of 909 km².  Major Towns in the district are Big Ada and Ada Kasseh.  Ada Foah, which is the district capital, is located at the beach and river estuary.  Most of the inhabitants (85.9%) belong to the cultural group of the Dangme.  It has a population of 71,671.\n\nBig Ada: Big Ada is a town in the Dangme East district, a district in the Greater Accra Region of Ghana.  The settlement lies along the road from Ada Kasseh to the district capital Ada Foah, just off the Accra-Aflao motorway.\n\nAda Međica: Ada Međica () is an island and an urban neighborhood of Belgrade, the capital of Serbia.  It is located in Belgrade's municipality of Novi Beograd.  Ada Međica is an ovally shaped river island in the Sava river, a 1.5 km long and 200 m wide.  It is located just north of the central part of the much larger Ada Ciganlija.\n\nCentennial High School (Idaho): Centennial High School is a four-year public secondary school in Boise, Idaho.  Although located in Boise, it is part of the West Ada School District; at the time of its construction, CHS was in unincorporated Ada County.  The West Ada district's second of five traditional high schools, Centennial opened in 1987 and serves neighborhoods in northwestern Boise and northeastern Meridian.  The centennial of Idaho statehood was observed in 1990.\n\nQuestion: What is the capital of the district where Ada is located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"district_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the district where an 'Ada' entity is located.\"\n    },\n    \"district_capital\": {\n      \"type\": \"string\",\n      \"description\": \"The capital city of the identified district.\"\n    },\n    \"ada_locations_in_district\": {\n      \"type\": \"array\",\n      \"description\": \"A list of 'Ada' related locations found within this district.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the 'Ada' related location.\"\n          },\n          \"location_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of the 'Ada' related location (e.g., town, constituency).\"\n          }\n        },\n        \"required\": [\n          \"location_name\",\n          \"location_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"district_name\",\n    \"district_capital\",\n    \"ada_locations_in_district\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "district_name": {
        "type": "string",
        "description": "The name of the district where an 'Ada' entity is located."
      },
      "district_capital": {
        "type": "string",
        "description": "The capital city of the identified district."
      },
      "ada_locations_in_district": {
        "type": "array",
        "description": "A list of 'Ada' related locations found within this district.",
        "items": {
          "type": "object",
          "properties": {
            "location_name": {
              "type": "string",
              "description": "The name of the 'Ada' related location."
            },
            "location_type": {
              "type": "string",
              "description": "The type of the 'Ada' related location (e.g., town, constituency)."
            }
          },
          "required": [
            "location_name",
            "location_type"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "district_name",
      "district_capital",
      "ada_locations_in_district"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
