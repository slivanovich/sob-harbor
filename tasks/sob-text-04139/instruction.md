{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2016 FA Trophy Final: The 2015–16 FA Trophy Final was the 47th final of the Football Association's cup competition for levels 5–8 of the English football league system.  The match was contested by FC Halifax Town and Grimsby Town.  Grimsby Town were beaten finalists in 2013, but it was FC Halifax Town's first final and their first visit to Wembley Stadium.  For the first time the final of the FA Vase was played on the same day at the same venue, contested by Hereford and Morpeth Town.  Both matches were televised in the UK on BT Sport.\n\nList of Trinidad and Tobago FA Trophy winners: The following is a list of Trinidad and Tobago FA Trophy winners, since its inception in 1927.  The FA Trophy, is a knockout cup competition in Trinidad and Tobago football, organised by the Trinidad and Tobago Football Association.  It is the oldest football competition in Trinidad and Tobago.  The tournament is open to all clubs in the top three levels of the football pyramid.  The competition culminates in January with the FA Trophy final, which has traditionally been regarded as the showpiece finale of the Trinidad and Tobago football season.\n\n2014 FA Trophy Final: The 2014 FA Trophy Final was the 45th final of the Football Association's cup competition for levels 5–8 of the English football league system.  The match was contested between Cambridge United of the Conference Premier and Gosport Borough of the Conference South.  Neither team had been in the final before: this was only the third time that Gosport had reached the \"proper\" rounds of the Trophy, and were playing at Wembley Stadium for the first time in their history, while Cambridge were playing there for the first time since 2009, when they lost the Conference play-off final to Torquay United.\n\n2011 FA Trophy Final: The 2011 FA Trophy Final was the 42nd final of the Football Association's cup competition for levels 5–8 of the English football league system.  The match was contested by Mansfield Town and Darlington.  Neither team had ever reached the FA trophy final before, and had only recently become eligible for the FA trophy after Mansfield Town were relegated from League Two in 2008 and Darlington were relegated from League Two in 2010.\n\nDick Hewitt: Richard \"Dick\" Hewitt (born 25 May 1943) is an English former footballer.  He played in the Football League for Barnsley and York City. He won the FA Trophy at Wembley in the 1973 FA Trophy Final, whilst finishing his playing career with Scarborough.  He later became a publican in the town.\n\n1998 Football League Trophy Final: The 1998 Football League Trophy Final (known as the Auto Windscreens Shields Trophy for sponsorship reasons) was the 15th final of the domestic football cup competition for teams from the Second and Third Division of the Football League.  The match was played at Wembley on 19 April 1998, and was contested by Bournemouth and Grimsby Town.  The match was won by Grimsby Town, with Wayne Burnett scoring the winning golden goal in the 2–1 victory during extra-time.  The attendance was the largest for a sporting event in England that weekend.\n\n2017 FA Trophy Final: The 2016–17 FA Trophy Final was the 48th final of the Football Association's cup competition for teams at levels 5–8 of the English football league system.  The match was contested between Macclesfield Town and York City.  The final of the FA Vase was played on the same day at the same venue for the second year running.  Both matches were televised in the UK on BT Sport.  York City won the final 3-2 and became the second club in as many seasons, after Halifax last year, to get relegated from the National League and then win the FA Trophy in the same season.\n\n1984 FA Trophy Final: The 1984 FA Trophy Final was the 15th final of the FA Trophy, the Football Association's cup competition for non-League teams.\n\n2013 FA Trophy Final: The 2013 FA Trophy Final was the 44th final of the Football Association's cup competition for levels 5–8 of the English football league system.  The match was contested between Grimsby Town and Wrexham.  Neither team had been in the final before and it was Wrexham's first visit to Wembley stadium in their 149-year history.\n\n2008 Football League Trophy Final: The 2008 Football League Trophy Final was the 25th final of the domestic football cup competition for teams from Football Leagues One and Two, the Football League Trophy.  The final was played at Wembley Stadium in London on 30 March 2009, the first time that the final had been staged at the stadium since it was rebuilt.  The match was contested by Grimsby Town and Milton Keynes Dons.  MK Dons won the match 2–0 with Keith Andrews and Sean O'Hanlon scoring the goals in the final 20 minutes.\n\nQuestion: What FA Trophy final was the 44th final where Grimsby Town was beaten?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"final_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the FA Trophy final took place.\"\n    },\n    \"final_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The ordinal number of the FA Trophy final.\"\n    },\n    \"competition_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football competition.\"\n    },\n    \"losing_team\": {\n      \"type\": \"string\",\n      \"description\": \"The team that was beaten in the final.\"\n    },\n    \"winning_team\": {\n      \"type\": \"string\",\n      \"description\": \"The team that won the final.\"\n    },\n    \"teams_involved\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of all teams that contested the final.\"\n    }\n  },\n  \"required\": [\n    \"final_year\",\n    \"final_number\",\n    \"competition_name\",\n    \"losing_team\",\n    \"winning_team\",\n    \"teams_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "final_year": {
        "type": "integer",
        "description": "The year the FA Trophy final took place."
      },
      "final_number": {
        "type": "integer",
        "description": "The ordinal number of the FA Trophy final."
      },
      "competition_name": {
        "type": "string",
        "description": "The name of the football competition."
      },
      "losing_team": {
        "type": "string",
        "description": "The team that was beaten in the final."
      },
      "winning_team": {
        "type": "string",
        "description": "The team that won the final."
      },
      "teams_involved": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of all teams that contested the final."
      }
    },
    "required": [
      "final_year",
      "final_number",
      "competition_name",
      "losing_team",
      "winning_team",
      "teams_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
