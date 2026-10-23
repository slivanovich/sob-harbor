{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Minnesota Vikings head coaches: The Minnesota Vikings are a professional American football team based in Minneapolis.  The Vikings are members of the North Division of the National Football Conference in the National Football League (NFL).  The club was founded by Minneapolis businessmen Bill Boyer, H. P. Skoglund and Max Winter in 1959 as a member of the American Football League.  However, they forfeited their membership in January 1960 and became the National Football League's 14th franchise in 1961.\n\nList of Minnesota Vikings seasons: The Minnesota Vikings are an American football team playing in the National Football League (NFL).  The Vikings compete in the NFL as a member club of the league's National Football Conference (NFC) North division.  The team was established in 1959, when three Minneapolis businessmen – Bill Boyer, H. P. Skoglund and Max Winter – were awarded a franchise in the new American Football League (AFL).  In January 1960, the ownership group, along with Bernie Ridder, forfeited its AFL membership and was awarded the NFL's 14th franchise, with play to begin in 1961.\n\nGerry Huth: Gerald Bernard Huth (July 23, 1933 – February 11, 2011) was an American football guard in the National Football League for the New York Giants, the Philadelphia Eagles, and the Minnesota Vikings.  He played college football at Wake Forest University and was drafted in the twenty fourth round of the 1956 NFL Draft.  Postmortem research diagnosed Huth with chronic traumatic encephalopathy.\n\nMinnesota Vikings: The Minnesota Vikings are an American football team based in Minneapolis, Minnesota.  The Vikings joined the National Football League (NFL) as an expansion team in 1960, and first took the field for the 1961 season.  The team competes in the National Football Conference (NFC) North division; before that, the Vikings were in the NFC Central, and before that they were in the NFL's Western Conference Central Division.  The team has played in four Super Bowl games, but have not won one.  They were the NFL champions in 1969.  The team plays its home games at U.S. Bank Stadium in the Downtown East section of Minneapolis.\n\nPete Perreault: Pete Perreault (March 1, 1939 – December 8, 2001) was an American football guard who played nine seasons of professional football.  He played for the American Football League's New York Jets from 1963 through 1967, for the AFL's Cincinnati Bengals in 1968, then returned to the Jets in 1969.  He also played for the National Football League's Jets in 1970 and the Minnesota Vikings in 1971.\n\nFoolish Club: The Foolish Club was the self-imposed name taken by the owners of the eight original franchises of the American Football League (AFL).  When Texas oil magnates Lamar Hunt and Bud Adams, Jr. were refused entry to the established NFL in 1959, they contacted other businessmen to form an eight-team professional football league, and called it the American Football League.  Though Max Winter had originally committed to fielding a Minneapolis team, he reneged when lured away by the NFL; Winter's group instead joined the NFL as the Minnesota Vikings in 1961 (the Minneapolis AFL franchise only went as far as participating in the 1960 American Football League Draft and never actually fielded a team).  Hunt owned the Dallas Texans (now the Kansas City Chiefs), while the Houston Oilers (now the Tennessee Titans) were Adams' franchise.  The other six members of the \"\"Original Eight\"\" were Harry Wismer (New York Titans, now the New York Jets), Bob Howsam (Denver Broncos), Barron Hilton (Los Angeles Chargers), Ralph C. Wilson, Jr. (Buffalo Bills), Billy Sullivan (Boston Patriots, now the New England Patriots), and a group of eight investors led primarily by F. Wayne Valley and, briefly, Chet Soda (Oakland Raiders, who replaced the Vikings).  They called themselves the \"Foolish Club\" because of their seemingly foolhardy venture in taking on the established NFL.\n\nTodd Steussie: Todd Edward Steussie ( ; born December 1, 1970) is a former American football guard and tackle for Minnesota Vikings, Carolina Panthers, Tampa Bay Buccaneers, and St. Louis Rams of the National Football League.  He was originally drafted by the Minnesota Vikings 19th overall in the 1994 NFL Draft.  He attended the University of California, Berkeley and played college football for the California Golden Bears.\n\nBrian Daniels: Brian Daniels (born October 31, 1984) is a former American football guard who last played for the Minnesota Vikings of the National Football League.  He was signed by the Vikings as an undrafted free agent in 2007.  He played college football at Colorado.\n\nList of Minnesota Vikings starting quarterbacks: The Minnesota Vikings are a professional American football team based in Minneapolis.  They are members of the North Division of the National Football Conference (NFC) in the National Football League (NFL).  A franchise was granted to Minneapolis businessmen Bill Boyer, H. P. Skoglund and Max Winter in 1959 as a member of the American Football League (AFL).  The ownership forfeited their AFL membership in January 1960 and received the National Football League's 14th franchise on January 28, 1960 that started play in 1961.\n\nDanny Isidora: Danny Isidora (born June 5, 1994) is an American football guard for the Minnesota Vikings of the National Football League (NFL).  He played college football for the Miami Hurricanes.  Isidora was drafted by the Vikings in the fifth round of the 2017 NFL Draft.\n\nQuestion: Gerald Bernard Huth, was an American football guard in which sports organization, for three teams, including the Minnesota Vikings, an American football team based in Minneapolis, Minnesota?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the player.\"\n    },\n    \"player_position\": {\n      \"type\": \"string\",\n      \"description\": \"The position the player played.\"\n    },\n    \"sports_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The primary sports organization the player was part of.\"\n    },\n    \"teams_played_for\": {\n      \"type\": \"array\",\n      \"description\": \"A list of teams the player played for within the specified organization.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"team_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the team.\"\n          },\n          \"team_city\": {\n            \"type\": \"string\",\n            \"description\": \"The base city of the team, if available.\"\n          }\n        },\n        \"required\": [\n          \"team_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_position\",\n    \"sports_organization\",\n    \"teams_played_for\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the player."
      },
      "player_position": {
        "type": "string",
        "description": "The position the player played."
      },
      "sports_organization": {
        "type": "string",
        "description": "The primary sports organization the player was part of."
      },
      "teams_played_for": {
        "type": "array",
        "description": "A list of teams the player played for within the specified organization.",
        "items": {
          "type": "object",
          "properties": {
            "team_name": {
              "type": "string",
              "description": "The name of the team."
            },
            "team_city": {
              "type": "string",
              "description": "The base city of the team, if available."
            }
          },
          "required": [
            "team_name"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "player_name",
      "player_position",
      "sports_organization",
      "teams_played_for"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
