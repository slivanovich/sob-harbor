{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDenmark–Sweden football rivalry: The Denmark–Sweden football rivalry is a highly competitive sports rivalry that exists between the national men's football teams of Denmark and Sweden.  The clashes between the two neighbouring countries has since the very first match in 1913 attracted large crowds that have witnessed several spectacular games and controversial incidents, despite the fact that the two teams very seldom have met in any of the larger international football tournaments.  Sweden leads the series 45–18–40.\n\nArgentina v England (1986 FIFA World Cup): Argentina v England, played on 22 June 1986, was a football match between Argentina and England in the quarter-finals of the 1986 FIFA World Cup at the Estadio Azteca in Mexico City.  The game was held four years after the Falklands War between Argentina and the United Kingdom, and was a key part in the already intense Argentina–England football rivalry.  It was also a match which included two of the most famous goals in football history, both scored by Diego Maradona.\n\nCzech Republic–Slovakia ice hockey rivalry: The Czech Republic–Slovakia ice hockey rivalry is a highly competitive sports rivalry that exists between the national ice hockey teams of the two countries, as well as their respective sets of fans.  Games between the two teams, even those that are only friendly matches, are often marked by notable and sometimes controversial incidents.  These matches are also called \"Federal derby.\"\n\nArgentina–Brazil football rivalry: The Argentina–Brazil rivalry is a highly competitive sports rivalry that exists between the national football teams of the two countries, as well as their respective sets of fans.  Games between the two teams, even those that are only friendly matches, are often marked by notable and sometimes controversial incidents.  This rivalry is also called the \"Battle of the South Americans.\"  FIFA have described it as the \"essence of football rivalry\", while \"ESPN FC\" ranked it top of their list of rivalries between national sides.\n\nAustralia–Japan football rivalry: The Australia–Japan football rivalry is a sports rivalry that exists between the national association football teams of each country, regarded as one of Asia's biggest football rivalries.  The rivalry is a relatively recent one, born from a number of highly competitive matches between the two teams since Australia joined the Asian Football Confederation in 2006.  The two teams have played each other in several significant matches, including a World Cup group stage match and the 2011 Asian Cup Final.\n\nAustria–Hungary football rivalry: The Austria–Hungary rivalry is a highly competitive sports rivalry that exists between the national football teams of the two countries, as well as their respective sets of fans.  The match-up between Austria and Hungary is the second most-played international in football (only Argentina and Uruguay have met each other in more matches).\n\nMexico–Puerto Rico boxing rivalry: The Mexico–Puerto Rico boxing rivalry is a highly competitive sports rivalry that exists between boxers from the country of Mexico and the Commonwealth of Puerto Rico, as well as their respective sets of fans.\n\nHungary–Romania football rivalry: The Hungary–Romania football rivalry is a competitive sports rivalry that exists between the national football teams of the two countries, as well as their respective sets of fans.\n\nCzech Republic–Slovakia football rivalry: The Czech Republic–Slovakia football rivalry is a highly competitive sports rivalry exists between the national football teams of the two countries, as well as their respective sets of fans.  Games between the two teams, even those that are only friendly matches, are often marked by notable and sometimes controversial incidents.  These matches are also called \"Federal derby.\"\n\nArgentina–England football rivalry: The Argentina–England football rivalry is a highly competitive sports rivalry that exists between the national football teams of the two countries, as well as their respective sets of fans.  Games between the two teams, even those that are only friendly matches, are often marked by notable and sometimes controversial incidents.\n\nQuestion: What is a highly competitive sports rivalry that exists between the national football teams of the two countries that played on 22 June 1986 in the quarter-finals of the 1986 FIFA World Cup?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"rivalry_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the highly competitive sports rivalry.\"\n    },\n    \"sport\": {\n      \"type\": \"string\",\n      \"description\": \"The sport in which the rivalry takes place.\"\n    },\n    \"countries_involved\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The two countries whose national teams are involved in the rivalry.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the specific event where the teams played.\"\n        },\n        \"event_stage\": {\n          \"type\": \"string\",\n          \"description\": \"The stage of the event (e.g., quarter-finals).\"\n        },\n        \"event_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date when the match was played.\"\n        }\n      },\n      \"required\": [\n        \"event_name\",\n        \"event_stage\",\n        \"event_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"rivalry_name\",\n    \"sport\",\n    \"countries_involved\",\n    \"event_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "rivalry_name": {
        "type": "string",
        "description": "The name of the highly competitive sports rivalry."
      },
      "sport": {
        "type": "string",
        "description": "The sport in which the rivalry takes place."
      },
      "countries_involved": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The two countries whose national teams are involved in the rivalry."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_name": {
            "type": "string",
            "description": "The name of the specific event where the teams played."
          },
          "event_stage": {
            "type": "string",
            "description": "The stage of the event (e.g., quarter-finals)."
          },
          "event_date": {
            "type": "string",
            "format": "date",
            "description": "The date when the match was played."
          }
        },
        "required": [
          "event_name",
          "event_stage",
          "event_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "rivalry_name",
      "sport",
      "countries_involved",
      "event_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
