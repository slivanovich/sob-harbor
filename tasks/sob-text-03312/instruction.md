{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJackson County, Kansas: Jackson County (county code JA) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 13,462.  Its county seat and most populous city is Holton.  The county was named for President Andrew Jackson.  The Prairie Band Potawatomi Indian Reservation, located near the center of the county, comprises about 18.5% of the county's area.\n\nDouglas County, Kansas: Douglas County (county code DG) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 110,826, making it the fifth-most populous county in Kansas.  Its county seat and most populous city is Lawrence.\n\nHarper County, Kansas: Harper County (county code HP) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 6,034.  Its county seat and most populous city is Anthony.  The county was named for Sergeant Marion Harper of the 2nd Kansas Cavalry, who died of wounds suffered near Waldron, Arkansas, in December 1863.\n\nBazaar, Kansas: Bazaar is an unincorporated community in Chase County, Kansas, United States.  The community is part of the Emporia Micropolitan Statistical Area.\n\nJohnson County, Kansas: Johnson County (county code JO) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 544,179, making it the most populous county in Kansas.  Its county seat is Olathe, and its most populous city is Overland Park.\n\nSedgwick County, Kansas: Sedgwick County (county code: SG) is a county located in the U.S. state of Kansas.  As of the 2010 census, the population was 498,365, making it the second-most populous county in Kansas.  The county seat is Wichita, the most populous city in the state.\n\nWyandotte County, Kansas: Wyandotte County ( ; county code WY) is a county located in the U.S. state of Kansas.  As of the 2010 census, the population was 157,505, making it the fourth-most populous county in Kansas.  Its county seat and most populous city is Kansas City, with which it shares a unified government.  Wyandotte County lies immediately west of Kansas City, Missouri.\n\nWonsevu, Kansas: Wonsevu is an unincorporated community in southwest Chase County, Kansas, United States.  It is located at the intersection of Cedar Creek Rd and E Rd, which is 4.5 mi north of the Chase-Butler county line and 3.75 mi east of the Chase-Marion county line in the Flint Hills.\n\nBrown County, Kansas: Brown County (county code BR) is a county located in the northeast portion of the U.S. state of Kansas.  As of the 2010 census, the county population was 9,984.  Its county seat and most populous city is Hiawatha.  Brown County is the location of the Kickapoo Indian Reservation of Kansas, the majority of the Sac and Fox Reservation and the majority of the Iowa Reservation of Kansas and Nebraska.\n\nChase County, Kansas: Chase County (county code CS) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 2,790.  Its county seat and most populous city is Cottonwood Falls.  The center of population of Kansas is located in Chase County, about four miles north of Strong City.\n\nQuestion: Bazaar is an unincorporated community in Chase County (county code CS) is a county located in the U.S. state of Kansas, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"community_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the community.\"\n    },\n    \"community_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of community (e.g., unincorporated community).\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"county_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the county where the community is located.\"\n        },\n        \"county_code\": {\n          \"type\": \"string\",\n          \"description\": \"The county code of the county.\"\n        },\n        \"state_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the state where the community is located.\"\n        },\n        \"country_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the country where the community is located.\"\n        }\n      },\n      \"required\": [\n        \"county_name\",\n        \"county_code\",\n        \"state_name\",\n        \"country_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"community_name\",\n    \"community_type\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "community_name": {
        "type": "string",
        "description": "The name of the community."
      },
      "community_type": {
        "type": "string",
        "description": "The type of community (e.g., unincorporated community)."
      },
      "location": {
        "type": "object",
        "properties": {
          "county_name": {
            "type": "string",
            "description": "The name of the county where the community is located."
          },
          "county_code": {
            "type": "string",
            "description": "The county code of the county."
          },
          "state_name": {
            "type": "string",
            "description": "The name of the state where the community is located."
          },
          "country_name": {
            "type": "string",
            "description": "The name of the country where the community is located."
          }
        },
        "required": [
          "county_name",
          "county_code",
          "state_name",
          "country_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "community_name",
      "community_type",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
