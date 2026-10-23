{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBaton Rouge–Pierre Part combined statistical area: The Baton Rouge–Pierre Part Combined Statistical Area is a former Combined Statistical Area made up of ten parishes in southeastern Louisiana.  The statistical area consisted of the Baton Rouge Metropolitan Statistical Area (MSA) and the Pierre Part Micropolitan Statistical Area (μSA).  As of the 2000 census, the CSA had a population of 729,361 (though a July 1, 2009 estimate placed the population at 809,821).  The Combined Statistical Area ceased to exist when the Pierre Part Micropolitan Statistical Area was eliminated by the Census Bureau.\n\nCheyenne metropolitan area: The Cheyenne Metropolitan Statistical Area is a United States Census Bureau defined Metropolitan Statistical Area (MSA) located in the Cheyenne region of the State of Wyoming.  The Cheyenne Metropolitan Statistical Area is defined as Laramie County, Wyoming.  Many consider the Cheyenne Metro Area to be the economic hub of eastern Wyoming .  The Census Bureau estimates that the population was 86,353 in 2007, ranking as the 340th most populous metropolitan area in the United States.\n\nFort Hood: Fort Hood is a U.S. military post located in Killeen, Texas.  The post is named after Confederate General John Bell Hood.  It is\n\nLongview–Marshall combined statistical area: The Longview–Marshall Combined Statistical Area covers four counties in Northeast Texas.  The statistical area consists of the Longview Metropolitan Statistical Area and the Marshall Micropolitan Statistical Area.  Prior to 2003, the area was known as the Longview-Marshall Metropolitan Statistical Area, which consisted of Gregg, Harrison, Rusk, and Upshur counties.  As of the 2000 census, the CSA had a population of 256,152 (though a July 1, 2009 estimate placed the population at 271,669).\n\nSouth Mountain, Texas: South Mountain is a town in Coryell County, Texas, United States.  The population was 384 at the 2010 census.  It is part of the Killeen–Temple–Fort Hood Metropolitan Statistical Area.\n\nTyler–Jacksonville combined statistical area: The Tyler–Jacksonville combined statistical area is made up of two counties in East Texas.  The statistical area consists of the Tyler metropolitan statistical area and the Jacksonville metropolitan statistical area.  As of the 2000 census, the CSA had a population of 221,365 (though a July 1, 2009 estimate placed the population at 253,138).\n\nKilleen, Texas: Killeen is a city in Bell County, Texas, United States.  According to the recent populations estimates, its population was 140,806, making it the 21st most populous city in Texas.  It is the principal city of the Killeen–Temple–Fort Hood Metropolitan Statistical Area.\n\nWest Point, New York: West Point is the oldest continuously occupied military post in the United States.  West Point was established in 1775 by George Washington who considered it the most important strategic position in America.  Until January 1778, West Point was not occupied by the military.  On January 27, 1778, Brigadier General Samuel Holden Parsons and his brigade crossed the ice on the Hudson River and climbed to the plain on West Point and from that day to the present, West Point has been occupied by the United States Army.  It comprises approximately 16000 acre including the campus of the United States Military Academy at West Point, which is also frequently called \"West Point\".  It is a Census Designated Place (CDP) located in the Town of Highlands in Orange County, New York, located on the western bank of the Hudson River.  The population was 6,763 at the 2010 census.  It is part of the New York–Newark–Jersey City, NY–NJ–PA Metropolitan Statistical Area as well as the larger New York–Newark, NY–NJ–CT–PA Combined Statistical Area.\n\nGrand Junction Metropolitan Statistical Area: The Grand Junction Metropolitan Statistical Area is a United States Census Bureau defined Metropolitan Statistical Area (MSA) located in the Grand Junction region of the State of Colorado.  The Grand Junction Metropolitan Statistical Area is defined as Mesa County, Colorado.  The Census Bureau estimates that the population was 147,083 in 2011, ranking as the 269th most populous metropolitan area in the United States.\n\nHarker Heights, Texas: Harker Heights is a city in Bell County, Texas, United States.  As of the 2010 census there were 26,700 people, 9,488 households, and 7,139 families residing in the city, up from a population of 17,308 in 2000.  This makes Harker Heights the third largest city in Bell County, after Killeen and Temple.  Incorporated in 1960, the city derives its name from one of the two original landowners and founder, Harley Kern.  Harker Heights is part of the Killeen–Temple–Fort Hood Metropolitan Statistical Area.  People usually refer to the town as just \"Heights\".\n\nQuestion: What military post located in Killeen, Texas that is part of the Kileen-Temple Metropolitan Statistical Area?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"military_post_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the military post.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the military post is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the military post is located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"metropolitan_statistical_area\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Metropolitan Statistical Area the post is part of.\"\n    },\n    \"named_after\": {\n      \"type\": \"string\",\n      \"description\": \"The person or entity the military post is named after.\"\n    }\n  },\n  \"required\": [\n    \"military_post_name\",\n    \"location\",\n    \"metropolitan_statistical_area\",\n    \"named_after\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "military_post_name": {
        "type": "string",
        "description": "The name of the military post."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the military post is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the military post is located."
          }
        },
        "required": [
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "metropolitan_statistical_area": {
        "type": "string",
        "description": "The name of the Metropolitan Statistical Area the post is part of."
      },
      "named_after": {
        "type": "string",
        "description": "The person or entity the military post is named after."
      }
    },
    "required": [
      "military_post_name",
      "location",
      "metropolitan_statistical_area",
      "named_after"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
