Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Dennis Byrd (American football, born 1946): Dennis Wayne Byrd (August 31, 1946 – July 22, 2010) was a defensive lineman who played one season in the American Football League for the Boston Patriots.  He attended North Carolina State University, where he was an All-American.  Byrd only played one season in the NFL because of a knee injury he suffered in his senior year at NC State.  After leaving the NFL, Byrd became the high school football coach at West Lincoln High School in Lincolnton, North Carolina, retiring in 2004.

John Avery (gridiron football): John Edward Avery, Jr. (born January 11, 1976) is a former professional Canadian football and American football player.  He last played with the Toronto Argonauts of the Canadian Football League, but also played with the National Football League's (Miami Dolphins, Denver Broncos and Minnesota Vikings) and the XFL (Chicago Enforcers).

Ed Salem: Edward Joseph Salem (August 28, 1928 – December 21, 2001) was an American football quarterback and defensive back.  He was a 1950 College Football All-America Team selection from the University of Alabama Crimson Tide and played one season for the National Football League's Washington Redskins and one season for the Canadian Football League's Montreal Alouettes.

Pete Rose Jr.: Peter Edward "PJ" Rose Jr. (born November 16, 1969) is the manager of the Wichita Wingnuts in the American Association of Independent Professional Baseball and former professional baseball player.  The son of Major League Baseball's all-time hits leader Pete Rose, Rose Jr. played in the minor leagues most of his career except for a brief stint in for the Cincinnati Reds.  He was released September 14, 2009, by the York Revolution of the Atlantic League of Professional Baseball.  In 2011, he joined the White Sox coaching staff and became the manager of their Appalachian League (rookie league) affiliate in Bristol.  In 2012, he moved up to the Pioneer League with the affiliate in Great Falls, Montana.  After one season, he advanced to the lower-A South Atlantic League team in Kannapolis, North Carolina.

Bernie Graham: Bernard W. "Bernie" Graham (February 10, 1863 October 30, 1886) was an American Major League Baseball player who played one season in the Union Association.  The Association lasted just one season, 1884, and Graham played one game for the Chicago Browns and 41 for the Baltimore Monumentals.  He batted .267 for the year, scored 23 runs, and hit 11 doubles.

John Fuller (baseball): John Edward Fuller (born January 29, 1950) is a former Major League Baseball player.  He played one season with the Atlanta Braves from May 9 to May 12, 1974.

John Burton (New Zealand cricketer): John Edward Ledgard Burton (15 February 1925 – 11 May 2010) was a New Zealand cricketer.  He played one first-class match for Wellington in 1946-47 and three for Ceylon on their tour of Pakistan in 1949-50.

John Naylor (cricketer): John Edward Naylor 11 December 1930 – 26 June 1996) was an English first-class cricketer, who played one match for Yorkshire County Cricket Club in 1953, a year when he also appeared for the Second XI.

Gary Keedy: Gary Keedy (born 27 November 1974 in Sandal, West Yorkshire) is a slow-left arm spin bowler for Nottinghamshire.  He played one match for Yorkshire in 1994, having graduated from their cricket academy, before moving to Lancashire.  He played for the club from 1995 to 2012 taking over 500 first-class wickets.  Although he had played youth internationals, he has never represented the senior England team despite having been in the squad a few times.  In 2011 he was part of the Lancashire squad that won the County Championship for the first time since 1950.  He subsequently played one season for Surrey and two for Nottinghamshire, before retiring as a professional cricketer in 2015.  After studying physiotherapy at the University of Salford, Keedy is currently Nottinghamshire's spin bowling coach and assistant physiotherapist.

XFL: The XFL was a professional American football league which played one season in 2001.  It was operated as a joint venture between the World Wrestling Federation (WWF, now known as WWE) and NBC.  The XFL was conceived as an outdoor football league that would take place during the NFL off-season, and promoted as having fewer rules and encouraging rougher play than other major leagues.  The league had eight teams in two divisions, including major markets and those not directly served by the NFL, including Birmingham, Las Vegas, Los Angeles, Memphis, and Orlando.  The XFL operated as a single entity, with all teams centrally owned by the league.

Question: John Edward Avery, Jr. played for what team that only played one season in 2001

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the player."
    },
    "league_name": {
      "type": "string",
      "description": "The name of the league that meets the criteria."
    },
    "league_details": {
      "type": "object",
      "properties": {
        "season_count": {
          "type": "integer",
          "description": "The number of seasons the league played."
        },
        "active_year": {
          "type": "integer",
          "description": "The year the league was active."
        }
      },
      "required": [
        "season_count",
        "active_year"
      ],
      "additionalProperties": false
    },
    "player_teams_in_league": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of teams the player played for within the identified league."
    }
  },
  "required": [
    "player_name",
    "league_name",
    "league_details",
    "player_teams_in_league"
  ],
  "additionalProperties": false
}
