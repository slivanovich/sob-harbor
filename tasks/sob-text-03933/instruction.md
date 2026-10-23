{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2009 NECBL All-Star Game: The 2009 NECBL All-Star Game was the 16th exhibition game between all-stars from the NECBL's East and West Divisions.  The game was held at Mackenzie Stadium in Holyoke, Massachusetts, the home field of the West Division's Holyoke Blue Sox.  The West Division won the game by a final score of 6-5 in front of a record All-Star Game attendance of 4,906.  This mark broke the previous record mark of 4,210 set at the 2007 All-Star Game hosted by the North Adams SteepleCats.  Holyoke's Jake Rosenbeck was named All-Star Game Most Valuable Player.  The contest was broadcast with live audio and video online provided by Teamline.  The game was announced online by Keene's Shawn Medeiros (West Division) and Newport's Nicholas Lima (East Division) on the NECBL Broadcast Network.\n\nList of MCLA teams: This is a list of colleges and universities in the United States (and one school in Canada) which sponsored a men's lacrosse team that belonged to the Men's Collegiate Lacrosse Association in 2015.  Per MCLA rules, a University or College with fielding an NCAA Division I FBS football team must play at the Division I level.  Any other school plays at the MCLA Division II level, but may petition to \"play up\" at the Division I level.  Likewise, teams designated as Division I may petition to \"play down\" at the Division II level, if they are deemed a \"developing\" team, and are ineligible for post season play.\n\nIndiana State Sycamores football: The Indiana State Sycamores football team is the NCAA Division I men's football program of Indiana State University in Terre Haute, Indiana.  They currently compete in the Missouri Valley Football Conference.  The team last played in the NCAA Playoffs in the 2014 NCAA Division I Football Championship.  Their first season was 1896.  The Sycamores boast of 8 Conference Player(s) of the Year; 19 First Team All-Americans, and 90+ First Team All-Conference players.  The Sycamore's greatest season was 1983, when coach Dennis Raetz led them to the 2nd round of the 1983 NCAA Division I Football Championship versus the Southern Illinois Salukis and ended the season with a record of 9–4.  The Sycamores also appeared in 1984 NCAA Division I Football Championship playoffs.  Past coaches include Dennis Raetz; Jerry Huntsman, George Ashworth and Wally Marks.  The Indiana State Sycamores play their home games at Memorial Stadium, which seats 12,764.  There have been recent discussions on replacing venerable Memorial Stadium; according to the new ISU Master Plan, a new football-only stadium in downtown Terre Haute, could be realized if funding becomes available.\n\nCalifornia Golden Bears football: The California Golden Bears football team is the college football team of the University of California, Berkeley.  The team plays its home games at California Memorial Stadium.  Memorial Stadium was built to honor Berkeley alumni, students, and other Californians who died in World War I and modeled after the Colosseum in Rome.  Memorial Stadium was named one of the 40 best college football stadiums by the \"Sporting News\".  The team also has produced two of the oddest and most memorable plays in college football: Roy \"Wrong Way\" Riegels' fumble recovery and run toward the California goal line in the 1929 Rose Bowl, and The Play in the 1982 Big Game with the last play five lateral winning kickoff return.\n\nNew England Collegiate Conference: The New England Collegiate Conference (NECC) is an NCAA Division III college athletic conference based in the Northeastern United States.\n\nToronto Lynx: Toronto Lynx is a Canadian soccer team based in Toronto, Ontario, Canada.  Founded in 1997, the team plays in the USL Premier Development League (PDL), the fourth tier of the American Soccer Pyramid, in the Great Lakes Division of the Central Conference.  The team plays its home games at Centennial Park Stadium, where they have played since 2003.  The team's colours are white, gold and black.  The team has a sister organization, the Toronto Lady Lynx, who play in the women's USL W-League, and also fields a team in the USL's Super-20 League, a league for players 17 to 20 years of age run under the United Soccer Leagues umbrella.\n\n2014 NECBL All-Star Game: The 2014 NECBL All-Star Game will be the 21st exhibition game between all-stars from the New England Collegiate Baseball League's North and South Divisions.  The game will be held at Mackenzie Stadium in Holyoke, Massachusetts, the home field of the North Division's Holyoke Blue Sox, on July 20, 2014.\n\nMackenzie Stadium: Mackenzie Stadium is a baseball venue located in Holyoke, Massachusetts.  It was home to the Holyoke Millers and today is used by both the Valley Blue Sox of the New England Collegiate Baseball League (since 2008) and the Elms College Blazers of the New England Collegiate Conference (since 2005).  It was built in 1933 and has a capacity of 4,100 people.\n\nHolyoke Millers: The Holyoke Millers were a minor league baseball team located in Holyoke, Massachusetts.  The team played in the Eastern League.  Their home stadium was Mackenzie Stadium.  The Millers played from 1977 to 1982 and was a farm team of the Milwaukee Brewers the first four years and the California Angels the last two years.  In 1980, the team won the Eastern League championship.\n\nValley Blue Sox: The Valley Blue Sox are a collegiate summer baseball team based in Holyoke, Massachusetts.  The team, a member of the New England Collegiate Baseball League, plays its home games at Mackenzie Stadium.  The Blue Sox were founded in 2001 as the Concord Quarry Dogs but moved following the 2007 season to Holyoke to fill the void left by the departure of the Holyoke Giants to Lynn, Massachusetts.\n\nQuestion: What Division does the team that plays at Mackenzie Stadium play in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the team that plays at the stadium.\"\n    },\n    \"stadium_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the stadium where the team plays.\"\n    },\n    \"conference_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the athletic conference the team belongs to.\"\n    },\n    \"ncaa_division\": {\n      \"type\": \"string\",\n      \"description\": \"The NCAA division of the team's conference.\"\n    },\n    \"sport\": {\n      \"type\": \"string\",\n      \"description\": \"The sport the team plays.\"\n    }\n  },\n  \"required\": [\n    \"team_name\",\n    \"stadium_name\",\n    \"conference_name\",\n    \"ncaa_division\",\n    \"sport\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "team_name": {
        "type": "string",
        "description": "The name of the team that plays at the stadium."
      },
      "stadium_name": {
        "type": "string",
        "description": "The name of the stadium where the team plays."
      },
      "conference_name": {
        "type": "string",
        "description": "The name of the athletic conference the team belongs to."
      },
      "ncaa_division": {
        "type": "string",
        "description": "The NCAA division of the team's conference."
      },
      "sport": {
        "type": "string",
        "description": "The sport the team plays."
      }
    },
    "required": [
      "team_name",
      "stadium_name",
      "conference_name",
      "ncaa_division",
      "sport"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
