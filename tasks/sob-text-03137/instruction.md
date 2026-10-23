{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2015 Independence Bowl: The 2015 Independence Bowl was a college football bowl game that was played on Saturday, December 26, 2015 at Independence Stadium in Shreveport, Louisiana in the United States.  The 40th annual Independence Bowl featured the Virginia Tech Hokies of the Atlantic Coast Conference against the Tulsa Golden Hurricane of the American Athletic Conference.  Sponsored by Camping World, the game was officially known as the Camping World Independence Bowl.  The first half of the game, in which 76 points were scored, was the highest scoring half in college football bowl history.\n\n1993 Independence Bowl: The 1993 Independence Bowl was a post-season American college football bowl game between the Virginia Tech Hokies and the Indiana Hoosiers at Independence Stadium in Shreveport, Louisiana on December 31, 1993.  The 18th edition of the Independence Bowl was the final contest of the 1993 NCAA Division I-A football season for both teams, and ended in a 45–20 victory for Virginia Tech.  The game was the first bowl victory for Virginia Tech head coach Frank Beamer and began a record streak of 23 consecutive bowl appearances for Virginia Tech.\n\nThe Pride of the South: The Pride of the South is the name of the marching band at The University of Mississippi in Oxford, Mississippi.  The full band plays at all Ole Miss home football games, and a smaller pep band is sent to most away games.  The full band also travels to Ole Miss bowl games and Starkville, Mississippi when Mississippi State University hosts the Egg Bowl. The University of Mississippi Band has been giving outstanding performances in concert and in support of Ole Miss athletic events since it was organized in 1928.  In addition to performing at all home football games and many away games, the marching band has attended numerous bowl games including the Sugar Bowl, the Gator Bowl, the Liberty Bowl, the Independence Bowl, the Peach Bowl, the Cotton Bowl, and more recently the Motor City Bowl in 1997, the Music City Bowl in 2000, the Independence Bowl in 1998, 1999 and 2002, the Cotton Bowl in 2004, 2009 and 2010, the Chick-fil-a Classic in 2014, the Peach Bowl in 2014, and the Sugar Bowl in 2016.\n\n2012 Independence Bowl: The 2012 AdvoCare V100 Independence Bowl was a post-season American college football bowl game held on December 28, 2012 at Independence Stadium in Shreveport, Louisiana in the United States.  The 37th edition of the Independence Bowl began at 1:00 p.m. CST and aired on ESPN.  It featured the Ohio Bobcats from the Mid-American Conference against the Louisiana–Monroe Warhawks from the Sun Belt Conference and was the final game of the 2012 NCAA Division I FBS football season for both teams.  Both the Bobcats and the Warhawks accepted their invitation after finishing at 8–4 during the regular season.\n\n2004 Independence Bowl: The 2004 Independence Bowl was a post-season college football bowl game between the Iowa State Cyclones and the Miami RedHawks on December 28, 2004, at Independence Stadium in Shreveport, Louisiana.  It was the twenty-ninth time the Independence Bowl had been played and the final game of the 2004 NCAA Division I FBS football season for both teams.  Iowa State defeated Miami 17-13.\n\n2014 Independence Bowl: The 2014 Independence Bowl was a college football bowl game played on December 27, 2014 at Independence Stadium in Shreveport, Louisiana in the United States.  The 39th annual Independence Bowl, it pitted the Miami Hurricanes of the Atlantic Coast Conference against the South Carolina Gamecocks of the Southeastern Conference.  The game will start at 3:30 p.m. CST and air on ABC.  It was one of the 2014–15 bowl games that conclude the 2014 FBS football season.  Sponsored by duck call manufacturer Duck Commander, the game was officially known as the Duck Commander Independence Bowl.\n\n2009 Georgia Bulldogs football team: The 2009 Georgia Bulldogs football team represented the University of Georgia in the 2009 NCAA Division I FBS football season.  The Bulldogs competed in the East Division of the Southeastern Conference (SEC).  This was the Georgia Bulldogs' ninth season under head coach Mark Richt.  The Bulldogs finished the season 8–5, 4–4 in SEC play and won the Independence Bowl, 44–20, against Texas A&M.\n\n2009 Texas A&amp;M Aggies football team: The 2009 Texas A&M Aggies football team (often referred to as \"A&M\" or the \"Aggies\") represented Texas A&M University in the 2009 NCAA Division I FBS football season.  The team was led by second-year head coach Mike Sherman and played their home games at Kyle Field in College Station, Texas.  The Aggies finished the season 6–7, 3–5 in Big 12 play and lost in the Independence Bowl 44–20 against Georgia.\n\n2016 Independence Bowl: The 2016 Independence Bowl was a college football bowl game played on December 26, 2016 at Independence Stadium in Shreveport, Louisiana.  The 41st annual Independence Bowl featured the NC State Wolfpack of the ACC against the Vanderbilt Commodores of the SEC.  Sponsored by Camping World, the game was officially known as the Camping World Independence Bowl.\n\nList of Independence Bowl broadcasters: This is a list of Independence Bowl broadcasters.  The Independence Bowl is a post-season NCAA-sanctioned Division I college football bowl game that is played annually at Independence Stadium in Shreveport, Louisiana.\n\nQuestion: The Auggies lost the Independence Bowl by a span of what points?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"losing_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the team that lost the game.\"\n    },\n    \"winning_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the team that won the game.\"\n    },\n    \"bowl_game_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the bowl game played.\"\n    },\n    \"game_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the bowl game was played.\"\n    },\n    \"winning_score\": {\n      \"type\": \"integer\",\n      \"description\": \"The points scored by the winning team.\"\n    },\n    \"losing_score\": {\n      \"type\": \"integer\",\n      \"description\": \"The points scored by the losing team.\"\n    },\n    \"point_difference\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in points between the winning and losing team.\"\n    }\n  },\n  \"required\": [\n    \"losing_team_name\",\n    \"winning_team_name\",\n    \"bowl_game_name\",\n    \"game_year\",\n    \"winning_score\",\n    \"losing_score\",\n    \"point_difference\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "losing_team_name": {
        "type": "string",
        "description": "The name of the team that lost the game."
      },
      "winning_team_name": {
        "type": "string",
        "description": "The name of the team that won the game."
      },
      "bowl_game_name": {
        "type": "string",
        "description": "The name of the bowl game played."
      },
      "game_year": {
        "type": "integer",
        "description": "The year the bowl game was played."
      },
      "winning_score": {
        "type": "integer",
        "description": "The points scored by the winning team."
      },
      "losing_score": {
        "type": "integer",
        "description": "The points scored by the losing team."
      },
      "point_difference": {
        "type": "integer",
        "description": "The difference in points between the winning and losing team."
      }
    },
    "required": [
      "losing_team_name",
      "winning_team_name",
      "bowl_game_name",
      "game_year",
      "winning_score",
      "losing_score",
      "point_difference"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
