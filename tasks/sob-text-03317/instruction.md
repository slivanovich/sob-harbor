{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUEFA Euro 2004 Group A: Group A of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 12 June and was completed on 20 June.  The group consisted of hosts Portugal, Spain, Russia and Greece.\n\nUEFA Euro 2004 Group B: Group B of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 13 June and was completed on 21 June.  The group consisted of defending champions France, England, Croatia and Switzerland.\n\nUEFA Euro 1984 Group 2: Group 2 of UEFA Euro 1984 was one of only two groups in the final tournament's initial group stage.  It began on 14 June and was completed on 20 June.  The group consisted of West Germany, Spain, Portugal, and Romania.\n\nUEFA Euro 1996 Group B: Group B of UEFA Euro 1996 was one of four groups in the final tournament's initial group stage.  It began on 9 June and was completed on 18 June.  The group consisted of France, Spain, Bulgaria and Romania.\n\nFrance national football team: The France national football team (French: \"Équipe de France de football\" ) represents France in international football.  The team's colours are blue, white and red, and the \"coq gaulois\" its symbol.  France are colloquially known as \"Les Bleus\" (The Blues).\n\nUEFA Euro 1996 Group A: Group A of UEFA Euro 1996 was one of four groups in the final tournament's initial group stage.  It began on 8 June and was completed on 18 June.  The group consisted of hosts England, Switzerland, the Netherlands and Scotland.\n\nUEFA Euro 1992 Group 1: Group 1 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage.  It began on 10 June and was completed on 17 June.  The group consisted of hosts Sweden, fellow Scandinavians Denmark, France and England.\n\nUEFA Euro 2004 Group C: Group C of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 14 June and was completed on 22 June.  The group consisted of Italy, Denmark, Sweden and Bulgaria.\n\nUEFA Euro 1984 Group 1: Group 1 of UEFA Euro 1984 was one of only two groups in the final tournament's initial group stage.  It began on 12 June and was completed on 19 June.  The group consisted of hosts France, Belgium, Denmark, and Yugoslavia.\n\nUEFA Euro 1992 Group 2: Group 2 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage.  It began on 12 June and was completed on 18 June.  The group consisted of the Netherlands, Scotland, Germany and the CIS, a team composed of players from 12 of the 15 former Soviet Union members.\n\nQuestion: Group 1 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage, it consisted of hosts Sweden, fellow Scandinavians Denmark, France and England, the France national football team, represents which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The official name of the national football team.\"\n    },\n    \"represented_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country that the national football team represents.\"\n    },\n    \"team_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"colloquial_name\": {\n          \"type\": \"string\",\n          \"description\": \"The common or informal name for the team.\"\n        },\n        \"symbol\": {\n          \"type\": \"string\",\n          \"description\": \"The symbol associated with the team.\"\n        },\n        \"colors\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The primary colors of the team's kit.\"\n        }\n      },\n      \"required\": [\n        \"colloquial_name\",\n        \"symbol\",\n        \"colors\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"team_name\",\n    \"represented_country\",\n    \"team_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "team_name": {
        "type": "string",
        "description": "The official name of the national football team."
      },
      "represented_country": {
        "type": "string",
        "description": "The country that the national football team represents."
      },
      "team_attributes": {
        "type": "object",
        "properties": {
          "colloquial_name": {
            "type": "string",
            "description": "The common or informal name for the team."
          },
          "symbol": {
            "type": "string",
            "description": "The symbol associated with the team."
          },
          "colors": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The primary colors of the team's kit."
          }
        },
        "required": [
          "colloquial_name",
          "symbol",
          "colors"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "team_name",
      "represented_country",
      "team_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
