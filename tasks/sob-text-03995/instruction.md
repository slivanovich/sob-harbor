{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrank Eck Stadium: Frank Eck Stadium is a baseball stadium in Notre Dame, Indiana.  It hosts the University of Notre Dame Fighting Irish college baseball team.  The stadium holds 2,500 people and was built in 1994.  The stadium was named after Frank Eck, an alumnus, benefactor and advisor to the university.\n\nNotre Dame Fighting Irish baseball: The Notre Dame Fighting Irish baseball team represents the University of Notre Dame in National Collegiate Athletic Association (NCAA) Division I college baseball.  Notre Dame competes as a member of the Atlantic Coast Conference and plays its home games at Frank Eck Stadium.\n\n1989 Wichita State Shockers baseball team: The 1989 Wichita State Shockers baseball team represented Wichita State University in the 1989 NCAA Division I baseball season.  The Shockers played their home games at Eck Stadium.  The team was coached by Gene Stephenson in his 12th season at Wichita State.\n\nRhoads Stadium: The John and Ann Rhoads Softball Stadium (frequently shortened to Rhoads Stadium) is a college softball stadium located on the campus of the University of Alabama in Tuscaloosa, Alabama.  It serves as the home field of the Alabama Crimson Tide softball team and is located on the corner of 5th Avenue and Campus Drive on the northeast corner of campus.  The Crimson Tide's all-time record at Rhoads Stadium is 316–50 ( ), and the official capacity of the stadium is 3,940.  After they played their first season at Sokol Park and at Bowers Park for both the 1998 and 1999 seasons, the Crimson Tide opened Rhoads Stadium on February 23, 2000, with a 7–1 victory over the UAB Blazers.\n\nKarnataka State Cricket Association: Karnataka State Cricket Association (KSCA) is the governing body of Cricket in the Indian state of Karnataka.  The association is affiliated to the Board of Control for Cricket in India and governs the Karnataka cricket team.  The association was founded in 1933 and has been affiliated to the BCCI ever since.  The KSCA operates the M. Chinnaswamy Stadium in Bangalore, which hosts International level Test, ODI and T20 cricket matches.  It also operates a newly built stadium in Hubli and Belgaum.\n\nVasai-Virar City Municipal Corporation: The Vasai-Virar City Municipal Corporation, (VVCMC) is the civic body that governs areas and villages in Vasai-Virar tehsil in Maharashtra state, western India comprising the most populated part of Palghar district.  It is an extended suburb of Mumbai.  According to the 2011 census, it is the fifth largest city in Maharashtra with a population of more than 1.3 million.  The city is located 50 km north of Mumbai, on the north bank of Vasai Creek, part of the estuary of the Ulhas River.  It was formed on 3 July 2009 by combining four municipal councils and 53 \"gram panchayats\".\n\nEck Stadium: Eck Stadium is a baseball stadium in Wichita, Kansas, United States.  It is located on the south side of 21st Street between Hillside and Oliver on the campus of Wichita State University in northeast Wichita.\n\nWichita State University: Wichita State University (WSU) is a public research university in Wichita, Kansas, United States.  It is the third-largest university governed by the Kansas Board of Regents.\n\nKollam Municipal Corporation: Kollam Municipal Corporation (KMC) is the civic body that governs the City of Kollam in the Indian state of Kerala.  It is the fourth largest city corporation in the state by population and fifth largest by area.  Constituted in 1903 and officially recognized as city corporation in 2000, the body governs an area of 73.03 km2 centered on Kollam with about 55 wards and a population of 397,419.\n\n2015 Notre Dame Fighting Irish baseball team: The 2015 Notre Dame Fighting Irish baseball team will represent the University of Notre Dame during the 2015 NCAA Division I baseball season.  The Fighting Irish will play their home games at Frank Eck Stadium as a member of the Atlantic Coast Conference.  They were led by head coach Mik Aoki, in his 5th season at Notre Dame.\n\nQuestion: What body governs the campus where Eck Stadium is located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"stadium_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the stadium.\"\n    },\n    \"university\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the university.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the university is located.\"\n            },\n            \"state\": {\n              \"type\": \"string\",\n              \"description\": \"The state where the university is located.\"\n            }\n          },\n          \"required\": [\n            \"city\",\n            \"state\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"governing_body\": {\n      \"type\": \"string\",\n      \"description\": \"The body that governs the university.\"\n    }\n  },\n  \"required\": [\n    \"stadium_name\",\n    \"university\",\n    \"governing_body\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "stadium_name": {
        "type": "string",
        "description": "The name of the stadium."
      },
      "university": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the university."
          },
          "location": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "The city where the university is located."
              },
              "state": {
                "type": "string",
                "description": "The state where the university is located."
              }
            },
            "required": [
              "city",
              "state"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "location"
        ],
        "additionalProperties": false
      },
      "governing_body": {
        "type": "string",
        "description": "The body that governs the university."
      }
    },
    "required": [
      "stadium_name",
      "university",
      "governing_body"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
