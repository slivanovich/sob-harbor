{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1986–87 Indiana Hoosiers men's basketball team: The 1986–87 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 16th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.  The team is noted for having achieved much success without much NBA talent.\n\n1991–92 Indiana Hoosiers men's basketball team: The 1991–92 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 21st year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\n1978–79 Indiana Hoosiers men's basketball team: The 1978–79 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 8th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\n1980–81 Indiana Hoosiers men's basketball team: The 1980–81 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 10th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\n1996–97 Indiana Hoosiers men's basketball team: The 1996–97 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 26th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.  The Hoosiers finished the regular season with an overall record of 22–11 and a conference record of 9–9, finishing in a tie for sixth in the Big Ten.  The Hoosiers received an at-large bid to the NCAA Tournament as a No. 8 seed.  However, IU made a quick exit with a loss in the First Round to Colorado.\n\n1971–72 Indiana Hoosiers men's basketball team: The 1971–72 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 1st year.  The team played its home games in the newly constructed Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\nBob Knight: Robert Montgomery Knight (born October 25, 1940) is a retired American basketball coach.  Nicknamed \"The General\", Knight won 902 NCAA Division I men's college basketball games, the most all-time at the time of his retirement and currently second all-time, behind his former player and assistant coach Mike Krzyzewski of Duke University.  Knight is best known as the head coach of the Indiana Hoosiers from 1971 to 2000.  He also coached at Texas Tech (2001–2008) and at Army (1965–1971).\n\n2000–01 Indiana Hoosiers men's basketball team: The 2000–01 Indiana Hoosiers men's basketball team represented Indiana University.  At beginning of the season, the head coach was Bobby Knight; however, Knight was fired early September 2000, and Mike Davis was named interim head coach.  The team played its home games in the Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\n1999–2000 Indiana Hoosiers men's basketball team: The 1999–2000 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who (unbeknownst to Knight) was coaching his last full season.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\n1992–93 Indiana Hoosiers men's basketball team: The 1992–93 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 22nd year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.\n\nQuestion: The 1991–92 Indiana Hoosiers men's basketball team represented Indiana University, their head coach was Bobby Knight, Robert Montgomery Knight, a retired American basketball coach, who was in his which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"team_season\": {\n      \"type\": \"string\",\n      \"description\": \"The season of the Indiana Hoosiers men's basketball team.\"\n    },\n    \"coach\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the head coach.\"\n        },\n        \"year_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The numerical year of the coach's tenure for that season.\"\n        },\n        \"year_ordinal\": {\n          \"type\": \"string\",\n          \"description\": \"The ordinal representation of the coach's tenure year (e.g., '1st', '21st').\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"year_number\",\n        \"year_ordinal\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"university\": {\n      \"type\": \"string\",\n      \"description\": \"The university the team represented.\"\n    }\n  },\n  \"required\": [\n    \"team_season\",\n    \"coach\",\n    \"university\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "team_season": {
        "type": "string",
        "description": "The season of the Indiana Hoosiers men's basketball team."
      },
      "coach": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the head coach."
          },
          "year_number": {
            "type": "integer",
            "description": "The numerical year of the coach's tenure for that season."
          },
          "year_ordinal": {
            "type": "string",
            "description": "The ordinal representation of the coach's tenure year (e.g., '1st', '21st')."
          }
        },
        "required": [
          "name",
          "year_number",
          "year_ordinal"
        ],
        "additionalProperties": false
      },
      "university": {
        "type": "string",
        "description": "The university the team represented."
      }
    },
    "required": [
      "team_season",
      "coach",
      "university"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
