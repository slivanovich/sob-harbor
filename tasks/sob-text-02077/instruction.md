{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1976 ABA All-Star Game: The 1976 ABA All Star Game was the 9th and final American Basketball Association All-Star Game, played at McNichols Arena in Denver, Colorado on January 27, 1976.  This time, the league abandoned the usual East vs. West format it used from the 1967-68 season onward and instead had the league's first place team at the All Star break face off against a team of ABA All Stars.  At the All Star break the Denver Nuggets were in first place, which was convenient as the Nuggets had also been selected to host the game in McNichols Arena.  Kevin Loughery of the New York Nets coached the All-Stars while Larry Brown led the Denver Nuggets.  This was the second year in a row that Loughery and Brown coached against each other in the ABA All-Star Game.  (The Nuggets went on to finish the regular season in first place at 60-24 (.714), but after beating the Kentucky Colonels 4 games to 3 in the ABA Semifinals the Nuggets lost in the 1976 ABA Finals to the New York Nets, 4 games to 2.)\n\nHouston Fancher: Houston Fancher (born February 17, 1966) is an American basketball coach and the current associate head coach of the Charlotte 49ers men's basketball team under head coach Mark Price.  Prior to that, he worked for four years at Tennessee, and the last two as the Director of Basketball Operations.  From 2000-2009, he was the men's head basketball coach of the Mountaineers at Appalachian State University.  His first two seasons saw his team go 11–20, and 10–18 respectively.  The following season, 2002–2003, his team went 19–10, and Fancher was named the Southern Conference Coach of the Year.  In the 2006–2007 season, his squad won a school record 25 games, but failed to make the NCAA Tournament, instead garnering Appalachian's first National Invitation Tournament (NIT) berth instead.  On March 16, 2009 Fancher resigned as head coach following a disappointing 2008–09 season.\n\n2009–10 Denver Nuggets season: The 2009–10 Denver Nuggets season was the 43rd season of the franchise, its 34th in the National Basketball Association (NBA).  After their trip the Conference Finals last season, the Nuggets started the season 35-18 before the All-Star break.  Coach George Karl and Carmelo Anthony were the only Nuggets to represent the Western Conference in the 2010 NBA All-Star Game.  During the break, Anthony sported a new haircut.  However, not long after the break, dark clouds gathered around the team as coach Karl was diagnosed with neck and throat cancer.  Adrian Dantley took over and the team struggled in the second half of the season, finishing with a 53-29 record and earned the number 4 seed in the West.  Denver's season ended in the first round with a defeat to the Jazz in six games.\n\n1983–84 Denver Nuggets season: The 1983-84 Denver Nuggets season was their 17th season, and their eighth in the NBA.  The Nuggets head coach was Doug Moe and his assistant coach was Bill Ficke.\n\n1975–76 Denver Nuggets season: The 1975–76 Denver Nuggets season was Denver's ninth and final season in the American Basketball Association (ABA).  At the conclusion of the season the team would join the National Basketball Association (NBA).  The team was led by an eventual hall of fame coach, Larry Brown.\n\n1982–83 Denver Nuggets season: The 1982-83 Denver Nuggets season was their 16th season, and their seventh in the NBA.  The Nuggets head coach was Doug Moe and his assistant coach was Bill Ficke.\n\n2008–09 Denver Nuggets season: The 2008–09 Denver Nuggets season was the 42nd season of the franchise, 33rd in the National Basketball Association (NBA).  They finished the regular season with 54 wins and 28 loses, the franchise's best record since 1987–88.  The Nuggets ended their streak of five straight first-round exits after Carmelo Anthony was drafted in 2003, advancing to the Conference Finals, where they lost to the eventual champion Los Angeles Lakers in six games, ending the Nuggets season and playoff run.\n\nBernie Bickerstaff: Bernard Tyrone Bickerstaff (born February 11, 1944) is an American basketball coach.  He previously worked as the head coach for the NBA's Seattle SuperSonics, Denver Nuggets, Washington Bullets/Wizards, Charlotte Bobcats, and Los Angeles Lakers.  He has also been an assistant for the Portland Trail Blazers, Chicago Bulls, Los Angeles Lakers, and Cleveland Cavaliers.  He has served in numerous other NBA front office positions, and has been a consultant for the Harlem Globetrotters.\n\nJeff Bzdelik: Jeffrey Joseph Bzdelik (born December 1, 1952) is an American basketball coach who is associate head coach of the Houston Rockets of the National Basketball Association (NBA).  He was head coach of the Denver Nuggets in the NBA for slightly over two seasons, from 2002 until he was fired near the end of 2004.  He also served as a college head coach at Air Force, Colorado and Wake Forest, where he took over programs in need of rebuilding.\n\n1996–97 Denver Nuggets season: The 1996–97 NBA season was the Nuggets' 21st season in the National Basketball Association, and 30th season as a franchise.  In the offseason, the Nuggets acquired Mark Jackson and Ricky Pierce from the Indiana Pacers, and signed free agent Ervin Johnson.  However, after a 4–9 start to the season, Bernie Bickerstaff was forced out as head coach and replaced with Dick Motta, where the Nuggets then lost ten straight games along the way.  Midway through the season, Jackson was traded back to the Indiana Pacers, while Pierce was dealt to the Charlotte Hornets.  Meanwhile, the Nuggets signed free agent Kenny Smith, who won championships with the Houston Rockets.  As the season drew, the Nuggets still struggled losing 26 of their final 30 games, finishing fifth in the Midwest Division with a 21–61 record.  Despite playing just 55 games due to a knee injury and a ruptured achilles tendon, LaPhonso Ellis led the team in scoring with a career high of 21.9 points per game.\n\nQuestion: What American basketball coach, born February 11, 1944 worked as head coach during the 1996–97 Denver Nuggets season?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"coach_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the basketball coach.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The birth date of the coach in YYYY-MM-DD format.\"\n    },\n    \"team_coached\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"team_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team the coach worked for.\"\n        },\n        \"season\": {\n          \"type\": \"string\",\n          \"description\": \"The specific season the coach worked for the team.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the individual within the team for the specified season.\"\n        }\n      },\n      \"required\": [\n        \"team_name\",\n        \"season\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"coach_name\",\n    \"birth_date\",\n    \"team_coached\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "coach_name": {
        "type": "string",
        "description": "The full name of the basketball coach."
      },
      "birth_date": {
        "type": "string",
        "format": "date",
        "description": "The birth date of the coach in YYYY-MM-DD format."
      },
      "team_coached": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The name of the team the coach worked for."
          },
          "season": {
            "type": "string",
            "description": "The specific season the coach worked for the team."
          },
          "role": {
            "type": "string",
            "description": "The role of the individual within the team for the specified season."
          }
        },
        "required": [
          "team_name",
          "season",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "coach_name",
      "birth_date",
      "team_coached"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
