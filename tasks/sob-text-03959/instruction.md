{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPFA Players' Player of the Year: The Professional Footballers' Association Players' Player of the Year (often called the PFA Players' Player of the Year, the Players' Player of the Year, or simply the Player of the Year) is an annual award given to the player who is adjudged to have been the best of the year in English football.  The award has been presented since the 1973–74 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The current holder is N'Golo Kanté, who won the award on 23 April 2017 for his displays throughout the 2016–17 season, representing Chelsea.\n\nPFA Young Player of the Year: The Professional Footballers' Association Young Player of the Year (often called the PFA Young Player of the Year, or simply the Young Player of the Year) is an annual award given to the player aged 23 or under at the start of the season who is adjudged to have been the best of the season in English football.  The award has been presented since the 1973–74 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The first winner of the award was Ipswich Town defender Kevin Beattie.  The current holder is Dele Alli, who won the award for his performances throughout the 2016–17 campaign for Tottenham Hotspur.\n\nDele Alli: Bamidele Jermaine Alli (born 11 April 1996) is an English professional footballer who plays as a midfielder for Premier League club Tottenham Hotspur and the England national team.\n\nPFA Women's Players' Player of the Year: The Professional Footballers' Association Women's Players' Player of the Year is an annual award given to the player who is voted to have been the best of the year in English women's football.  The award has been presented since the 2012–13 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The current holder is Lucy Bronze, who won the award on 23 April 2017.  The first winner of the award was Arsenal midfielder Kim Little in 2013.\n\nPFA Women's Young Player of the Year: The Professional Footballers' Association Women's Young Player of the Year (commonly referred to as PFA Young Player of the Year) is an annual award given to the player who is voted to have been the best of the year in English women's football.  The award has been presented since the 2013–14 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).\n\nLigue 1 Young player of the year: The Ligue 1 Young Player of the Year is an award given to the player aged 23 years or under at the start of the season whose performances are considered to be the best, playing in Ligue 1.  The award has been presented since the 1993–94 season and the first winner of the award was Bordeaux midfielder Zinedine Zidane.  The current holder is Ousmane Dembélé, who won the award for his performances throughout the 2015–16 campaign for Rennes scoring 12 goals and assisting 5.  Eden Hazard is the only player to have won this award twice\n\nA-League Young Footballer of the Year: The A-League Young Footballer of the Year is an annual soccer award given to the player aged 23 or under at the start of the season who is adjudged to have been the best of the season in the A-League.  It is currently called the NAB Young Footballer of the Year for sponsorship purposes.  The award has been presented since the 2005–06 season and the winner is chosen by a panel of experts and media representatives.  In 2014, the age for eligibility was lifted from 21 to 23.  The first winner of the award was Perth Glory midfielder Nick Ward.  The current holder is Jamie Maclaren, who won the award for his performances throughout the 2015–16 campaign for Brisbane Roar.\n\nEric Dier: Eric Jeremy Edgar Dier (born 15 January 1994) is an English professional footballer who plays for Premier League club Tottenham Hotspur and the England national team.  A versatile defensive player, Dier has been deployed as a defensive midfielder, a centre-back and a right-back.\n\nPFA Scotland Players' Player of the Year: The Professional Footballers' Association Scotland Players' Player of the Year (often called the PFA Scotland Players' Player of the Year, the Players' Player of the Year, or simply the Scottish Player of the Year) is an annual award given to the player who is adjudged to have been the best of the season in Scottish football.  The award has been presented since the 1977–78 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association Scotland (PFA Scotland).  The award was formerly known as the Scottish Professional Footballers' Association Players' Player of the Year, but was renamed after the SPFA merged with the (English) Professional Footballers' Association to become PFA Scotland.\n\nPFA Scotland Team of the Year: The Professional Footballers' Association Scotland Team of the Year (often called the PFA Scotland Team of the Year, or simply the Team of the Year) is an annual award given to a set of 44 footballers in the four national tiers of the Scottish football league system, who are seen to be deserving of being named in a \"Team of the Year\".  The award is compiled by the members of the players' trade union, Professional Footballers' Association Scotland (PFA Scotland), with the winners then being voted for by the other players in their respective divisions.  Unlike the (English) Professional Footballers' Association, which first announced its teams of the year in the 1970s, the award has only been instituted since the 2006–07 season.  In that first season, the award was voted for by the managers in each division.\n\nQuestion: The Professional Footballers' Association Young Player of the Year, is an annual award given to the player aged 23 or under at the start of the season who is adjudged to have been the best of the season in English football, the current holder is which English professional footballer who plays as a midfielder for Premier League club Tottenham Hotspur and the England national team, known commonly as?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the award.\"\n    },\n    \"current_holder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"player_common_name\": {\n          \"type\": \"string\",\n          \"description\": \"The commonly known name of the current award holder.\"\n        },\n        \"player_full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the current award holder.\"\n        },\n        \"club\": {\n          \"type\": \"string\",\n          \"description\": \"The Premier League club the player plays for.\"\n        },\n        \"position\": {\n          \"type\": \"string\",\n          \"description\": \"The primary playing position of the player.\"\n        },\n        \"national_team\": {\n          \"type\": \"string\",\n          \"description\": \"The national team the player represents.\"\n        },\n        \"season_awarded_for\": {\n          \"type\": \"string\",\n          \"description\": \"The season for which the award was won.\"\n        }\n      },\n      \"required\": [\n        \"player_common_name\",\n        \"player_full_name\",\n        \"club\",\n        \"position\",\n        \"national_team\",\n        \"season_awarded_for\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"award_criteria\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"age_limit_at_start_of_season\": {\n          \"type\": \"integer\",\n          \"description\": \"The maximum age a player can be at the start of the season to be eligible for the award.\"\n        },\n        \"football_region\": {\n          \"type\": \"string\",\n          \"description\": \"The geographical region of football for which the award is given.\"\n        }\n      },\n      \"required\": [\n        \"age_limit_at_start_of_season\",\n        \"football_region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"award_name\",\n    \"current_holder_details\",\n    \"award_criteria\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_name": {
        "type": "string",
        "description": "The full name of the award."
      },
      "current_holder_details": {
        "type": "object",
        "properties": {
          "player_common_name": {
            "type": "string",
            "description": "The commonly known name of the current award holder."
          },
          "player_full_name": {
            "type": "string",
            "description": "The full name of the current award holder."
          },
          "club": {
            "type": "string",
            "description": "The Premier League club the player plays for."
          },
          "position": {
            "type": "string",
            "description": "The primary playing position of the player."
          },
          "national_team": {
            "type": "string",
            "description": "The national team the player represents."
          },
          "season_awarded_for": {
            "type": "string",
            "description": "The season for which the award was won."
          }
        },
        "required": [
          "player_common_name",
          "player_full_name",
          "club",
          "position",
          "national_team",
          "season_awarded_for"
        ],
        "additionalProperties": false
      },
      "award_criteria": {
        "type": "object",
        "properties": {
          "age_limit_at_start_of_season": {
            "type": "integer",
            "description": "The maximum age a player can be at the start of the season to be eligible for the award."
          },
          "football_region": {
            "type": "string",
            "description": "The geographical region of football for which the award is given."
          }
        },
        "required": [
          "age_limit_at_start_of_season",
          "football_region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "award_name",
      "current_holder_details",
      "award_criteria"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
