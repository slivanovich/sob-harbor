{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2015 Diamond Head Classic: The 2015 Diamond Head Classic was a mid-season eight-team college basketball tournament that was played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the seventh annual Diamond Head Classic tournament and was part of the 2015–16 NCAA Division I men's basketball season.  No. 3-ranked Oklahoma defeated Harvard to win the tournament championship.  Buddy Hield was named the tournament's MVP.\n\n2014 Diamond Head Classic: The 2014 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the sixth annual Diamond Head Classic tournament and was part of the 2014–15 NCAA Division I men's basketball season.  George Washington defeated No. 11-ranked Wichita State to with the tournament championship.  Kevin Larsen was named the tournament's MVP.\n\n2012 Diamond Head Classic: The 2012 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the fourth annual Diamond Head Classic tournament and was part of the 2012–13 NCAA Division I men's basketball season.  No. 3-ranked Arizona defeated No. 17-ranked San Diego State to win the tournament championship.  Solomon Hill was named the tournament's MVP.\n\n2013 Diamond Head Classic: The 2013 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the fifth annual Diamond Head Classic tournament and was part of the 2013–14 NCAA Division I men's basketball season.  No. 14-ranked Iowa State defeated Boise State 70–66 to win the tournament championship.  DeAndre Kane was named the tournament's MVP.\n\n2009 Diamond Head Classic: The 2009 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22 , 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the first annual Diamond Head Classic tournament and was part of the 2009–10 NCAA Division I men's basketball season.  USC defeated No. 20-ranked UNLV to win the tournament championship.  Mike Gerrity was named the tournament's MVP.\n\n2016 Diamond Head Classic: The 2016 Diamond Head Classic was a mid-season eight-team college basketball tournament that was played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the eighth annual Diamond Head Classic tournament and was part of the 2016-17 NCAA Division I men's basketball season.  San Diego State defeated San Francisco to win the tournament championship.  Zylan Cheatham was named the tournament's MVP.\n\nBuddy Hield: Chavano Rainier \"Buddy\" Hield (born December 17, 1993) is a Bahamian professional basketball player for the Sacramento Kings of the National Basketball Association (NBA).  He was named the Big 12 Conference Men's Basketball Player of the Year in 2015 and 2016, and in 2016, he received four major national player of the year awards—the John R. Wooden Award, the Naismith Award, \"Sporting News\" Player of the Year, and the Oscar Robertson Trophy.  Hield was selected with the sixth overall pick in the 2016 NBA draft by the New Orleans Pelicans.\n\n2010 Diamond Head Classic: The 2010 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the second annual Diamond Head Classic tournament and was part of the 2010–11 NCAA Division I men's basketball season.  Butler defeated Washington State to win the tournament championship.  Matt Howard was named the tournament's MVP.\n\n2011 Diamond Head Classic: The 2011 Diamond Head Classic was a mid-season eight-team college basketball tournament played on December 22, 23, and 25 at the Stan Sheriff Center in Honolulu, Hawaii.  It was the third annual Diamond Head Classic tournament and was part of the 2011–12 NCAA Division I men's basketball season.  Kansas State defeated Long Beach State to win the tournament championship.  Rodney McGruder was named the tournament's MVP.\n\nMalcolm Brogdon: Malcolm Moses Adams Brogdon (born December 11, 1992) is an American professional basketball player for the Milwaukee Bucks of the National Basketball Association (NBA).  He played college basketball for the Virginia Cavaliers under Tony Bennett.  As a senior in 2015–16, he was named the ACC Player of the Year and ACC Defensive Player of the Year, becoming the first player in conference history to earn both honors in the same season.  He was selected in the second round of the 2016 NBA draft by the Bucks with the 36th overall pick.  He went on to win the NBA Rookie of the Year Award, becoming the first second-round pick in the NBA draft lottery era to do so.\n\nQuestion: The MVP of the 2015 Diamond Head Classic was Bahamian professional basketball player that was with the sixth overall pick in the 2016 NBA draft by who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tournament_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the Diamond Head Classic tournament.\"\n    },\n    \"mvp_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Most Valuable Player for the specified tournament.\"\n    },\n    \"player_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the MVP.\"\n    },\n    \"nba_draft_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"draft_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the player was drafted into the NBA.\"\n        },\n        \"overall_pick\": {\n          \"type\": \"integer\",\n          \"description\": \"The overall pick number in the NBA draft.\"\n        },\n        \"drafting_team\": {\n          \"type\": \"string\",\n          \"description\": \"The NBA team that drafted the player.\"\n        }\n      },\n      \"required\": [\n        \"draft_year\",\n        \"overall_pick\",\n        \"drafting_team\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"tournament_year\",\n    \"mvp_name\",\n    \"player_nationality\",\n    \"nba_draft_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tournament_year": {
        "type": "integer",
        "description": "The year of the Diamond Head Classic tournament."
      },
      "mvp_name": {
        "type": "string",
        "description": "The name of the Most Valuable Player for the specified tournament."
      },
      "player_nationality": {
        "type": "string",
        "description": "The nationality of the MVP."
      },
      "nba_draft_details": {
        "type": "object",
        "properties": {
          "draft_year": {
            "type": "integer",
            "description": "The year the player was drafted into the NBA."
          },
          "overall_pick": {
            "type": "integer",
            "description": "The overall pick number in the NBA draft."
          },
          "drafting_team": {
            "type": "string",
            "description": "The NBA team that drafted the player."
          }
        },
        "required": [
          "draft_year",
          "overall_pick",
          "drafting_team"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "tournament_year",
      "mvp_name",
      "player_nationality",
      "nba_draft_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
