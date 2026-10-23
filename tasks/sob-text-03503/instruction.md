{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShannon Sharpe: Shannon Sharpe (born June 26, 1968) is a former American football tight end who played for the Denver Broncos and Baltimore Ravens of the National Football League (NFL), as well as a former analyst for CBS Sports on its NFL telecasts.  He is currently a TV presenter who co-hosts \"\" with Skip Bayless and Joy Taylor.\n\nNFL Street: NFL Street is an American football video game developed by EA Tiburon and published by Electronic Arts.  It was originally released for the PlayStation 2, GameCube and Xbox on January 13, 2004.  Barry Sanders of the Detroit Lions, Shannon Sharpe of the Denver Broncos, and Ricky Williams of the Miami Dolphins grace the cover.  The game was followed by \"NFL Street 2\" and \"NFL Street 3\".\n\nAlex Gibbs: Alex Gibbs (born February 22, 1941) is a former NFL offensive line coach and former assistant NFL head coach.  He formerly served as an offensive line consultant for the American football team the Denver Broncos.  Gibbs is a well known proponent of the Zone Blocking scheme and popularized its use while he was Offensive line coach of the Denver Broncos.  Denver became famous at that time for its use of smaller and more agile offensive linemen and the success of its running backs, most notably Terrell Davis.  Gibbs was to enter his first season on Pete Carroll's Seattle Seahawks staff as the Assistant Head Coach and Offensive Line coach in 2010, but announced his unexpected retirement a week before the start of the NFL's 2010 regular season.  In May 2013 he returned to the Denver Broncos in a consultant role for one year.\n\n1985 Denver Broncos season: The Denver Broncos season was the team's 26th year in professional football and its 16th with the National Football League (NFL).  Despite finishing with an impressive record of eleven wins and five losses, the Broncos failed to make the playoffs.  The Broncos were coming off a loss to the Steelers in the divisional round, and were picked by many to make the Super Bowl at the end of the 1985 season.  The Broncos would start out well, as they started 6-2 and 8-3.  However, two losses in overtime to arch rival Los Angeles resulted in the Broncos needing to win their final two games of the season to try to sneak into the playoffs.  They did just that, beating Kansas City 14-13 and Seattle 27-24.  However, even though the Broncos finished 11-5, they failed to reach the playoffs by virtue of a tiebreaker with the New England Patriots.  The tiebreaker was based on the teams' common opponents record; and the Patriots beat the Broncos in that category by finishing 4-2 against the Raiders, Seahawks, Dolphins, and Colts, while the Broncos finished just 3-3 against the same four teams.  The 1985 Broncos are one of two teams in NFL history since the 1970 merger to end the season with eleven or more wins and not qualify for the playoffs.  The other is the 2008 Patriots.\n\nHouston Marshals: The Houston Marshals were a professional football team based in Houston, Texas that played in the Spring Football League in 2000.  The Marshals were coached by former Denver Broncos player Ray Woodard.  They played their home games at Robertson Stadium on the University of Houston campus.\n\nDenver Broncos Cheerleaders: The Denver Broncos Cheerleaders are the official cheerleading squad of the Denver Broncos.  In addition to performing on game days, the Denver Broncos Cheerleaders annually commit close to 1,000 hours to various charities and events in Denver and the state of Colorado.\n\nNFL Street 2: NFL Street 2 is American football video game developed by EA Sports BIG and published by Electronic Arts.  It was originally released for the PlayStation 2, GameCube and Xbox on December 22, 2004.  It features then-New York Giants tight end Jeremy Shockey and rapper Xzibit on the cover.  The game is compatible with \"Madden NFL 2006\", as players can import their \"Own The City\" players to it.  The game's compatibility also extends to other EA games like \"\", \"SSX 3\", \"Madden NFL 2005\", \"NCAA Football 2005\", \"NFL Street\", \"\", \"NBA Live 2005\", and \"NBA Street Vol.  2\", where if players have these games on their memory cards, they can earn 25,000 points in the game.\n\nJoe Rizzo: Joe Rizzo (born December 17, 1950 in Glen Cove, New York) is a former linebacker of the Denver Broncos.  He played for the Broncos from 1974 to 1980 and was a starter in Super Bowl XII and member of the Orange Crush Defense.  He had 9 career interceptions.  He was part of one of the most dominant linebacking corps in NFL history.  Known as the Orange Crush, it consisted of, Joe Rizzo, Randy Gradishar, Tom Jackson and Bob Swenson.  The corp was named the 9th best linebacking corps in NFL history by nfl.com.  Joe was also voted by Bronco fans as one of the top 10 linebackers in the 50-year history (1959-2009) of the Denver Broncos.\n\nReggie Rivers: Reggie Rivers (born February 22, 1968 in Dayton, Ohio) is a professional broadcaster and motivational speaker working in Denver, Colorado.  From 1991 to 1996, Rivers was a professional American football player who played running back for the Denver Broncos.  Rivers played in every Broncos game during that span, scoring 8 touchdowns.  In 1993, Rivers was named the Denver Broncos' special teams Player of the Year.  While still a player, Rivers began working for KOA radio; he also wrote a sports column in the \"Rocky Mountain News\".  After retiring from football, Rivers moved to broadcasting full-time, hosting his own talk show on KHOW from 1997-2002.  Rivers' KHOW show focused more on topical issues than sports, as did his \"Rocky Mountain News\" column during the same period (later, Rivers switched to \"The Denver Post\").  Since 2006, Rivers has served as KCNC-TV's weekend sports anchor.\n\nHistory of the Denver Broncos: The history of the Denver Broncos American football club began when the team was chartered a member of the American Football League in 1960.  The Broncos have played in the city of Denver, Colorado throughout their entire history.  The Broncos did not win any titles as members of the AFL.  Since the 1970 AFL–NFL merger, the Broncos have won 15 division titles, and played in eight Super Bowls, following the 1977, 1986, 1987, 1989, 1997, 1998, 2013, and 2015 seasons.  They won Super Bowl XXXII, Super Bowl XXXIII and Super Bowl 50.  Their most famous player is former quarterback John Elway, starting quarterback in five Super Bowls and holder of many NFL records.  The Broncos currently play in the National Football League's AFC West division.  Their current leadership includes owner Pat Bowlen, CEO Joe Ellis, VP John Elway, head coach Vance Joseph, and quarterback, Trevor Siemian.\n\nQuestion: In what month was the Denver Broncos player on the cover of NFL Street born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Denver Broncos player featured on the NFL Street cover.\"\n    },\n    \"birth_month\": {\n      \"type\": \"string\",\n      \"description\": \"The month in which the player was born.\"\n    },\n    \"nfl_street_cover_players\": {\n      \"type\": \"array\",\n      \"description\": \"A list of all players featured on the NFL Street cover.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"player\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the player.\"\n          },\n          \"team\": {\n            \"type\": \"string\",\n            \"description\": \"The team the player represented on the cover.\"\n          }\n        },\n        \"required\": [\n          \"player\",\n          \"team\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"birth_month\",\n    \"nfl_street_cover_players\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the Denver Broncos player featured on the NFL Street cover."
      },
      "birth_month": {
        "type": "string",
        "description": "The month in which the player was born."
      },
      "nfl_street_cover_players": {
        "type": "array",
        "description": "A list of all players featured on the NFL Street cover.",
        "items": {
          "type": "object",
          "properties": {
            "player": {
              "type": "string",
              "description": "The name of the player."
            },
            "team": {
              "type": "string",
              "description": "The team the player represented on the cover."
            }
          },
          "required": [
            "player",
            "team"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "player_name",
      "birth_month",
      "nfl_street_cover_players"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
