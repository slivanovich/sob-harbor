{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Texas Tech Red Raiders in the NFL Draft: The Texas Tech Red Raiders football team, representing Texas Tech University, has had 151 players drafted into the National Football League (NFL) since the league began holding drafts in 1936.  This includes six players taken in the first round and one overall number one pick, Dave Parks in the 1964 NFL Draft.  The Green Bay Packers and Chicago Bears have drafted the most Red Raiders, eleven and nine, respectively.  The Carolina Panthers and Jacksonville Jaguars are the only current franchises to not have drafted a player from Texas Tech.  Three former Red Raiders have been selected to a Pro Bowl, seven former Red Raiders have won a league championship with their respective teams, and three former Red Raiders have been selected to both a Pro Bowl and won a league championship.\n\n2015 Texas Tech Red Raiders football team: The 2015 Texas Tech Red Raiders football team represented Texas Tech University in the 2015 NCAA Division I FBS football season as members of the Big 12 Conference.  Kliff Kingsbury led the Red Raiders in his third season as the program's fifteenth head coach.  The Red Raiders played their home games on the university's campus in Lubbock, Texas at Jones AT&T Stadium.  They finished the season 7-6 and 4-5 in Big 12 play to finish in 7th.  They were invited to the Texas Bowl where they lost to LSU.\n\n2014 Texas Tech Red Raiders football team: The 2014 Texas Tech Red Raiders football team represented Texas Tech University in the 2014 NCAA Division I FBS football season as members of the Big 12 Conference.  Kliff Kingsbury lead the Red Raiders in his second season as the program's fifteenth head coach.  The Red Raiders played home games on the university's campus in Lubbock, Texas at Jones AT&T Stadium.  They finished the season 4–8, 2–7 in Big 12 play to finish in eighth place.\n\n2012 Texas Tech Red Raiders football team: The 2012 Texas Tech Red Raiders football team represented Texas Tech University in the 2012 NCAA Division I FBS football season as members of the Big 12 Conference.  Tommy Tuberville lead the Red Raiders in his third season as the program's fourteenth head coach.  The Red Raiders played home games on the university's campus in Lubbock, Texas at Jones AT&T Stadium.  They finished the season 8–5, 4–5 in Big 12 play to finish in a four way tie for fifth place.  They were invited to the Meineke Car Care Bowl of Texas where they defeated Minnesota.\n\n2009 Texas Tech Red Raiders football team: The 2009 Texas Tech Red Raiders football team represented Texas Tech University in the 2009 NCAA Division I FBS football season.  The team was coached by Mike Leach during the regular season, and was coached by interim head coach Ruffin McNeill during the 2010 Valero Alamo Bowl.  The Red Raiders played their home games at Jones AT&T Stadium in Lubbock, Texas.  The football team competed in the Division I NCAA Division I Football Bowl Subdivision.  The Red Raiders finished the season 9–4, 5–3 in Big 12 play and won the Valero Alamo Bowl 41–31 against Michigan State.\n\n2011 Texas Tech Red Raiders football team: The 2011 Texas Tech Red Raiders football team represented Texas Tech University in the 2011 NCAA Division I FBS football season.  The Red Raiders were led for the second year by head coach Tommy Tuberville, and played their home games at Jones AT&T Stadium.  They are a member of the Big 12 Conference.  The 2011 Red Raiders Season finished with a 5–7 overall record, 2–7 in Big 12 play.  It was the first losing season for Texas Tech football since the 1992 season.  As a result, the Red Raiders failed to qualify for a bowl game for the first time since 1999.\n\nMike Leach (American football coach): Michael Charles Leach (born March 9, 1961) is an American college football coach.  He is the head coach of the Washington State Cougars football team.  Previously, he was head coach of the Texas Tech Red Raiders football team, leading the Red Raiders to winning seasons in every year of his tenure.\n\nTexas Tech Red Raiders football: The Texas Tech Red Raiders football program is a college football team that represents Texas Tech University (variously \"Texas Tech\" or \"TTU\").  The team competes, as a member of the Big 12 Conference, which is a Division I Football Bowl Subdivision (formerly Division I-A) of the National Collegiate Athletic Association (NCAA).  The program began in 1925 and has an overall winning record, including a total of 11 conference titles and one division title.  On December 12, 2012, former Red Raiders quarterback Kliff Kingsbury became the team's 15th head coach, following the resignation of Tommy Tuberville.  Home games are played at Jones AT&T Stadium in Lubbock, Texas.\n\nGrady Higginbotham: Grailey Hewett \"Grady\" \"Big Hig\" Higginbotham (December 31, 1892 – February 10, 1989) was an American football and baseball player, coach of football, basketball, and baseball, and college athletics administrator.  He was the first head coach of the Texas Tech Red Raiders men's basketball team, leading it to a 14–18 record from 1925 to 1927.  Higginbotham coached the Red Raiders baseball team to a 10–17 record from 1928 to 1929.  He was also the head coach of the Texas Tech Red Raiders football team in 1929, tallying a mark of 1–7–2.  He was the athletic director at Texas Tech from 1927 to 1929.  Higginbotham played college football and college baseball at Texas A&M University.  After graduating, he played in minor league baseball or several years.  He was the older brother of Roswell G. Higginbotham, who also played at Texas A&M and became a college baseball coach.\n\n2013 Texas Tech Red Raiders football team: The 2013 Texas Tech Red Raiders football team represented Texas Tech University in the 2013 NCAA Division I FBS football season as members of the Big 12 Conference.  Kliff Kingsbury led the Red Raiders in his first season as the program's fifteenth head coach.  The Red Raiders played home games on the university's campus in Lubbock, Texas at Jones AT&T Stadium.\n\nQuestion: The head coach of the 2009 Texas Tech Red Raiders football is currently the head coach of what college team?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"coach_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the head coach for the specified Texas Tech season.\"\n    },\n    \"coached_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the coach led the Texas Tech team.\"\n    },\n    \"texas_tech_coach_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the coach for Texas Tech in that year.\"\n    },\n    \"current_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the college team the coach currently leads.\"\n    },\n    \"current_coach_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the coach for the current team.\"\n    }\n  },\n  \"required\": [\n    \"coach_name\",\n    \"coached_year\",\n    \"texas_tech_coach_role\",\n    \"current_team_name\",\n    \"current_coach_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "coach_name": {
        "type": "string",
        "description": "The name of the head coach for the specified Texas Tech season."
      },
      "coached_year": {
        "type": "integer",
        "description": "The year the coach led the Texas Tech team."
      },
      "texas_tech_coach_role": {
        "type": "string",
        "description": "The role of the coach for Texas Tech in that year."
      },
      "current_team_name": {
        "type": "string",
        "description": "The name of the college team the coach currently leads."
      },
      "current_coach_role": {
        "type": "string",
        "description": "The role of the coach for the current team."
      }
    },
    "required": [
      "coach_name",
      "coached_year",
      "texas_tech_coach_role",
      "current_team_name",
      "current_coach_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
