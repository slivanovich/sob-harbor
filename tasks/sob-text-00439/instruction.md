{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHuston–Tillotson University: Huston–Tillotson University (abbreviated as HTU) is a private historically black university in Austin, Texas, United States.  The school is affiliated with the United Methodist Church, the United Church of Christ, and the United Negro College Fund.  Huston–Tillotson University awards four-year degrees in business, education, the humanities, natural sciences, social sciences, science and technology.  The University also offers alternative teacher certification and academic programs for undergraduates interested in pursuing post-graduate degrees in Law and Medicine.  Established in 1875, Huston-Tillotson University is the first institution of higher learning in Austin, Texas.\n\nSpelman College: Spelman College is a four-year liberal arts women's college located in Atlanta, Georgia, United States.  The college is part of the Atlanta University Center academic consortium in Atlanta.  Founded in 1881 as the Atlanta Baptist Female Seminary, Spelman was the fourth historically black female institution of higher education to receive its collegiate charter in 1924.  (Two schools were strictly seminaries and one was originally coeducational.)  Therefore, Spelman College holds the distinction of being America's first, and thereby oldest, private, liberal arts historically black colleges for women.\n\nMamie Locke: Mamie Evelyn Locke (born March 19, 1954) is an African-American politician and educator.  A Democrat, she was a member of the Hampton, Virginia city council 1996–2004, and mayor 2000–2004.  Since 2004, she has been a member of the Senate of Virginia from the 2nd district.  She currently represents parts of the cities of Hampton, Newport News and Portsmouth, plus part of York County.  She is also Professor of Political Science and Dean of the School of Liberal Arts at Hampton University.\n\nNorfolk State University: Norfolk State University (NSU) is a public four-year, coed, liberal arts, historically black university located in Norfolk, Virginia.  The university is a member-school of Thurgood Marshall College Fund and the Virginia High-Tech Partnership.\n\nPhilander Smith College: Philander Smith College is a private historically black college, four-year undergraduate liberal arts institution, located in Little Rock, Arkansas .  Philander Smith College is affiliated with the United Methodist Church and a founding member of the United Negro College Fund (UNCF).  Philander Smith College is accredited by the North Central Association of Colleges and Schools.  The Mission of Philander Smith College is, \"\"To graduate academically accomplished students who are grounded as advocates for social justice, determined to change the world for the better.\"\"\n\nTalladega College: Talladega College, located in Talladega, Alabama, is a private, liberal arts college.  It is Alabama's oldest private historically black college.  As of 2009, it received full SACS accreditation.\n\nFlorida A&amp;M University: Florida Agricultural and Mechanical University, commonly known as FAMU, is a public, historically black university in Tallahassee, Florida, United States.  Florida A&M University was founded on the highest of seven hills in Tallahassee, Florida on October 3, 1887.  It is one of the largest historically black universities in the United States by enrollment and the only public historically black university in Florida.  It is a member institution of the State University System of Florida, as well as one of the state's land grant universities, and is accredited to award baccalaureate, master's and doctoral degrees by the Commission on Colleges of the Southern Association of Colleges and Schools.  The university is a member-school of the Thurgood Marshall College Fund.\n\nHampton University: Hampton University (also HU, or Home by the Sea) is a private historically black university located in Hampton, Virginia, United States.  It was founded in 1868 by black and white leaders of the American Missionary Association after the American Civil War to provide education to freedmen.  In 1878, it established a program for teaching Native Americans, which lasted until 1923.\n\nFisk University: Fisk University is a private historically black university founded in 1866 in Nashville, Tennessee, United States.  The 40 acre campus is a historic district listed on the National Register of Historic Places.\n\nSavannah State University: Savannah State University is a four-year, state-supported, historically black university (HBCU) located in Savannah, Georgia, United States.  It is the oldest public historically black university in the state.  Savannah State University's mission statement is \"to graduate students who are prepared to perform at higher levels of economic productivity, social responsibility, and excellence in their chosen career fields of endeavor in a changing global community.\"  The University is a member-school of the Thurgood Marshall College Fund.\n\nQuestion: Mamie Evelyn Locke, is an African-American politician and educator, she is Dean of the School of Liberal Arts at which private historically black university located in Hampton, Virginia, United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"university_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the university (e.g., 'private', 'public').\"\n        },\n        \"is_historically_black_university\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the university is a historically black university.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the university is located.\"\n            },\n            \"state\": {\n              \"type\": \"string\",\n              \"description\": \"The state where the university is located.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the university is located.\"\n            }\n          },\n          \"required\": [\n            \"city\",\n            \"state\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"is_historically_black_university\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"dean_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"person_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who is the dean.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role of the person at the university.\"\n        }\n      },\n      \"required\": [\n        \"person_name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"university_details\",\n    \"dean_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "university_details": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of the university (e.g., 'private', 'public')."
          },
          "is_historically_black_university": {
            "type": "boolean",
            "description": "Indicates if the university is a historically black university."
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
              },
              "country": {
                "type": "string",
                "description": "The country where the university is located."
              }
            },
            "required": [
              "city",
              "state",
              "country"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "type",
          "is_historically_black_university",
          "location"
        ],
        "additionalProperties": false
      },
      "dean_information": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the person who is the dean."
          },
          "role": {
            "type": "string",
            "description": "The specific role of the person at the university."
          }
        },
        "required": [
          "person_name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "university_name",
      "university_details",
      "dean_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
