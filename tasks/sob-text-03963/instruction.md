{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2009–10 Olympique de Marseille season: The 2009–10 season of Olympique de Marseille (OM) had the club being involved in five competitions: the Ligue 1, the Coupe de France, the Coupe de la Ligue, the UEFA Champions League, and the UEFA Europa League.  They won the Ligue 1 for the first time in 18 years.  They also won the Coupe de la Ligue.  In the UEFA Champions League, they were eliminated in the group stage.  They finished third and were given a place in the UEFA Europa League knockout stages.  They were eliminated in the round of 16 by Benfica.\n\n2007 Coupe de France Final: The Coupe de France Final 2007 was a football match held at Stade de France, Saint-Denis on May 12, 2007, that saw FC Sochaux-Montbéliard defeat Olympique de Marseille in a penalty shoot out.  After normal time and extra-time could not separate the two sides, the match was to be decided on penalty kicks.  Toifilou Maoulida and Ronald Zubar' miss for Olympique de Marseille, whereas only FC Sochaux-Montbéliard's captain, Jérémie Bréchet missed for the winning team.\n\n2006 Coupe de France Final: The Coupe de France Final 2006 was a football match held at Stade de France, Saint-Denis on April 29, 2006, that saw Paris SG defeat Olympique de Marseille 2-1 thanks to goals by Bonaventure Kalou and Vikash Dhorasoo.\n\n2008 Coupe de France Final: The 2008 Coupe de France Final was a football match that was held at the Stade de France in Saint-Denis, France on 24 May 2008.  It was the 90th final in the Coupe de France's history.  The final was contested between Paris Saint-Germain FC and Olympique Lyonnais.  This was PSG's 10th appearance in the Coupe de France final, having won the cup in 1982, 1983, 1993, 1995, 1998, 2004, and 2006.  They also lost in the final twice in 1985 and 2003.  With a win in this year's final, PSG would have been granted the rare cup double with their last double coming in 1998.  This was Olympique Lyonnais's 7th appearance in the final having won in 1964, 1967, and 1973.  They lost in the final three times in 1963, 1971, and 1976.\n\n1969 Coupe de France Final: The 1969 Coupe de France Final was a football match held at Stade Olympique Yves-du-Manoir, Colombes on May 18, 1969, that saw Olympique de Marseille defeat FC Girondins de Bordeaux 2–0 thanks to an own goal by Gérard Papin and a goal by Joseph Yegba Maya.\n\n2012 Coupe de la Ligue Final: The 2012 Coupe de la Ligue Final was the 18th final of France's football league cup competition, the Coupe de la Ligue, a football competition for the 42 teams that the Ligue de Football Professionnel (LFP) manages.  The final took place on 14 April 2012 at the Stade de France in Saint-Denis and was contested between Lyon and Marseille.  The latter club entered the match as the two-time defending champions of the competition and sought to become the first club in French football history to win the competition three consecutive years after previously becoming the first club to win the competition in back-to-back seasons.  Lyon made its first finals appearance since the 2008 Coupe de France Final and played at the Stade de France for the first time in nearly three years.  The final was broadcast live on public network broadcaster France Télévisions.\n\n2007–08 Coupe de France: The 2007–2008 Coupe de France was the 91st edition of the prestigious tournament and is open to all clubs in French football, as well as the 4 overseas departments if they qualify.  The defending champions were FC Sochaux-Montbéliard who defeated Olympique Marseille 5-4 on penalties to claim their 2nd Coupe de France trophy.  The final was held on May 24, 2008 at the Stade de France.  The 2008 Coupe de France champions are Olympique Lyonnais, who defeated Paris Saint-Germain 1-0 to claim their 4th Coupe de France trophy.\n\nJean-Pierre Papin: Jean-Pierre Papin (] ; born 5 November 1963 in Boulogne-sur-Mer) is a former French professional football player, who played as a forward, and who was named the European Footballer of the Year in 1991.\n\n1926 Coupe de France Final: The 1926 Coupe de France Final was a football match held at Stade Olympique, Colombes on May 9, 1926, that saw Olympique de Marseille defeat AS Valentigney 4–1 thanks to goals by Jules Dewaquez (2), Douglas De Ruymbecke and Jean Boyer.\n\n1989 Coupe de France Final: The 1989 Coupe de France Final was a football match played at Parc des Princes, Paris, on 10 June 1989 that saw Olympique de Marseille defeat AS Monaco FC 4–3 thanks to three goals by Jean-Pierre Papin and one by Klaus Allofs.\n\nQuestion: During the 1989 Coupe de France Final, which former French professional football player born in 1963 contributed a great deal to the victory of Olympique de Marseille?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football player.\"\n    },\n    \"player_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the player.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the player.\"\n        },\n        \"professional_status\": {\n          \"type\": \"string\",\n          \"description\": \"Indicates if the player was a professional.\"\n        }\n      },\n      \"required\": [\n        \"nationality\",\n        \"birth_year\",\n        \"professional_status\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"match_contribution\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"competition_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the competition.\"\n        },\n        \"final_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the final was held.\"\n        },\n        \"team_played_for\": {\n          \"type\": \"string\",\n          \"description\": \"The team the player played for in the final.\"\n        },\n        \"goals_scored\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of goals scored by the player in the final.\"\n        }\n      },\n      \"required\": [\n        \"competition_name\",\n        \"final_year\",\n        \"team_played_for\",\n        \"goals_scored\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_details\",\n    \"match_contribution\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the football player."
      },
      "player_details": {
        "type": "object",
        "properties": {
          "nationality": {
            "type": "string",
            "description": "The nationality of the player."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the player."
          },
          "professional_status": {
            "type": "string",
            "description": "Indicates if the player was a professional."
          }
        },
        "required": [
          "nationality",
          "birth_year",
          "professional_status"
        ],
        "additionalProperties": false
      },
      "match_contribution": {
        "type": "object",
        "properties": {
          "competition_name": {
            "type": "string",
            "description": "The name of the competition."
          },
          "final_year": {
            "type": "integer",
            "description": "The year the final was held."
          },
          "team_played_for": {
            "type": "string",
            "description": "The team the player played for in the final."
          },
          "goals_scored": {
            "type": "integer",
            "description": "The number of goals scored by the player in the final."
          }
        },
        "required": [
          "competition_name",
          "final_year",
          "team_played_for",
          "goals_scored"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "player_details",
      "match_contribution"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
