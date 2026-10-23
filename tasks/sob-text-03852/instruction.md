{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGrace Metalious: Grace Metalious (September 8, 1924 – February 25, 1964) was an American author known for her controversial novel \"Peyton Place\", one of the best-selling works in publishing history.\n\nMax Jacob: Max Jacob (] ; 12 July 1876 – 5 March 1944) was a French poet, painter, writer, and critic.\n\nReturn to Peyton Place: Return to Peyton Place is a 1959 novel by Grace Metalious, a sequel to her best-selling 1956 novel \"Peyton Place\".\n\nPeyton Place (film): Peyton Place is a 1957 American drama film in color by De Luxe and CinemaScope from 20th Century Fox, produced by Jerry Wald, directed by Mark Robson, that stars Lana Turner and Hope Lange.  In co-starring and supporting roles are Lee Philips, Lloyd Nolan, Diane Varsi, Arthur Kennedy, Russ Tamblyn, and Terry Moore.  The film is based on the bestselling 1956 novel of the same name by Grace Metalious.\n\nPeyton Place (novel): Peyton Place is a 1956 novel by Grace Metalious.  The novel describes how three women are forced to come to terms with their identity, both as women and as sexual beings, in a small, conservative, gossipy New England town, with recurring themes of hypocrisy, social inequities and class privilege in a tale that includes incest, abortion, adultery, lust and murder.  It sold 60 000 copies within the first ten days of its release and remained on the \"New York Times\" best seller list for 59 weeks.\n\nReturn to Peyton Place (film): Return to Peyton Place is a 1961 drama film produced by Jerry Wald and directed by José Ferrer.  The screenplay by Ronald Alexander is based on the 1959 novel \"Return to Peyton Place\" by Grace Metalious.  The film is a sequel to \"Peyton Place\".\n\nGilmanton, New Hampshire: Gilmanton is a town in Belknap County, New Hampshire, United States.  The population was 3,777 at the 2010 census.  Gilmanton includes the villages of Gilmanton Corners and Gilmanton Ironworks.  The town became well known in the 1950s after it was rumored that the popular novel \"Peyton Place\", written by resident Grace Metalious, was based on the town.\n\nConstance MacKenzie: Constance MacKenzie (née Standish) is a fictional character in the 1956 novel \"Peyton Place\" by Grace Metalious.  In the subsequent film adaptation, she was played by Lana Turner; in the sequel \"Return to Peyton Place\", by Eleanor Parker; in the primetime television series, by Dorothy Malone (and briefly by  Lola Albright); and in daytime soap opera \"Return to Peyton Place\", by Bettye Ackerman.\n\nBetty Anderson: Betty Anderson is a fictional character in the novel \"Peyton Place\", written by Grace Metalious, as well as the subsequent films and TV series based on the novel.  In the film, she was played by actress Terry Moore; and in the TV series, she was portrayed by actress Barbara Parkins; in the short-lived daytime soap opera, she was played by actress Julie Parrish and later Lynn Loring.  In a later TV movie, \"Murder in Peyton Place\", Janet Margolin performed the role of Betty.\n\nReturn to Peyton Place (TV series): Return to Peyton Place is an American daytime serial which aired on NBC from April 3, 1972 to January 4, 1974.  The series was a spin-off of the primetime drama series \"Peyton Place\" rather than an adaptation of the 1959 novel of the same name by Grace Metalious.\n\nQuestion: Max Jacob and Grace Metalious, have which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_one\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_two\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mutual_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of occupations shared by both individuals.\"\n    },\n    \"mutual_occupation_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of mutual occupations found.\"\n    }\n  },\n  \"required\": [\n    \"person_one\",\n    \"person_two\",\n    \"mutual_occupations\",\n    \"mutual_occupation_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_one": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "person_two": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "mutual_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of occupations shared by both individuals."
      },
      "mutual_occupation_count": {
        "type": "integer",
        "description": "The number of mutual occupations found."
      }
    },
    "required": [
      "person_one",
      "person_two",
      "mutual_occupations",
      "mutual_occupation_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
