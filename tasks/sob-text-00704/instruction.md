{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDaniel Negreanu: Daniel Negreanu ( ; born July 26, 1974) is a Canadian professional poker player who has won six World Series of Poker (WSOP) bracelets and two World Poker Tour (WPT) championship titles.  The independent poker ranking service Global Poker Index (GPI) recognised Negreanu as the best poker player of the decade in 2014.\n\nMimi Rogers: Miriam \"Mimi\" Rogers (née Spickler; born January 27, 1956) is an American film and television actress, producer and competitive poker player.  Her notable film roles include \"Gung Ho\" (1986), \"Someone to Watch Over Me\" (1987), and \"Desperate Hours\" (1990).  She garnered the greatest acclaim of her career for her role in the religious drama, \"The Rapture\" (1991), with critic Robin Wood declaring that she \"gave one of the greatest performances in the history of the Hollywood cinema.\"  Rogers has since appeared in \"Reflections on a Crime\" (1994), \"The Mirror Has Two Faces\" (1996), \"\" (1997), \"Lost in Space\" (1998), \"Ginger Snaps\" (2000), \"The Door in the Floor\" (2004), and \"For a Good Time, Call... \" (2012).  Her extensive work in television includes \"Paper Dolls\" (1984), \"Weapons of Mass Distraction\" (1997), \"The Loop\" (2006–2007), and recurring roles on \"The X-Files\" (1998–1999), \"Two and a Half Men\" (2011–2015), \"Wilfred\" (2014) and \"Mad Men\" (2015).\n\nAndy Frankenberger: Andy Frankenberger is a professional poker player and former equity derivatives trader from New York City.  In his first year as a professional poker player, Frankenberger was named World Poker Tour (WPT) Season IX Player of the Year.  Card Player Magazine described this as one of poker's best rookie years in a September 2011 cover story.  Frankenberger followed this up by winning back to back bracelets at the World Series of Poker in 2011 and 2012.  He has been prominently featured in financial media including The Wall Street Journal, Fox Business Network, and Bloomberg Television.\n\nHoward Lederer: Howard Henry Lederer (born October 30, 1963) is an American professional poker player.  He has won two World Series of Poker bracelets and holds two World Poker Tour titles.  Lederer has also contributed to several books on poker strategy and has provided commentary for poker programming.  He is known by poker fans and players as \"The Professor\" and is the older brother of professional poker player Annie Duke.\n\nDag Palovic: Dag Palovič (* 4 January 1975, Bratislava) is a Slovak professional poker player, businessman and a former TV host.  Since 1 January 2011, he is a member of PokerStars Team Pro, first and as of October 2011 only sponsored poker player from Slovakia.  He is best known for making two European Poker Tour (EPT) final tables as well as being the only player from Slovakia who has cashed in the World Series of Poker (WSOP) Main Event, finishing 120th in 2009 and 37th in 2010.  As of March 2013, he is second leading Slovak all time money list with career earnings of $909,405 and is also an author of first Slovak poker book on poker titled \"Ako sa stať poker pro\" (How to become a poker pro), co-authored by 1983 World Series Of Poker champion Tom McEvoy.  From 2000 until 2004 he was CEO and Chairman Of The Board of Directors of \"ad pepper media Slovakia, a.s.\", the daughter company of one of the world´s leading e-Adverising german-dutch agency \"ad pepper media International N.V.\" for Slovak and Czech Republic.\n\nBarry Shulman: Barry Shulman (born May 8, 1946) is an American poker player who has enjoyed success in competitive poker tournaments over the past 15 years, and is the CEO of CardPlayer Magazine.\n\nCyborg (truck): Cyborg is a monster truck currently racing in the USHRA Monster Jam series.  It is owned and driven by Jack Koberna.  It is notable in that it is the only two-wheeled drive vehicle on the circuit, and features an independent front suspension, as the front wheels are the two which are not powered.  Although this provides recognition, the two-wheel drive presents a serious competitive disadvantage, as the truck cannot climb over obstacles as easily as other trucks.  However, the front suspension has received large amounts of attention from other teams.  Although Jack runs Cyborg most of the time, he does have a four-wheeled drive monster truck that is called Tuff-E-Nuff that runs on occasion.\n\nKevin Pollak: Kevin Elliot Pollak (born October 30, 1957) is an American actor, impressionist, and comedian.  He started performing stand-up comedy at the age of 10 and touring professionally at the age of 20.  In 1988, he landed a role in \"Willow\", his first major role in a film.  Pollak is an avid poker player, hosting weekly home games with some of Hollywood's A-list celebrities.  He finished 134th out of 6,598 entrants in the 2012 World Series of Poker, his winnings totaling to $52,718.\n\nDavid Catapano: David Catapano is an American celebrity chef, professional poker player, and reality television personality.  He is known for his mastery in Italian Cuisine and his self-developed \"Twisted Mediterranean\" style.  However, he is most notable for having appeared on a wide variety of cooking TV shows, including the long-running FoodyTV show \"Italian Style with Chef Catman\" and \"Food Network\" shows such as iron chef and chopped.  Over the years he pioneered several catchphrases, including \"My Kitchen, My rules!\" , \"Bada Bing!\"  and \"Why, No?\"  Catapano is an avid poker player and has played professionally and for large charity events.  Sometimes billed a Celebrity Poker Player because of his chef profile.\n\nAvalon (soundtrack): Avalon is the original soundtrack of the 1990 film \"Avalon\" starring Armin Mueller-Stahl, Elizabeth Perkins, Kevin Pollak and Elijah Wood.  The original score was composed by Randy Newman.\n\nQuestion: Which actor who starred in \"Avalon\" was a serious competitive poker player?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"is_professional_poker_player\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the actor is a professional or serious competitive poker player.\"\n    },\n    \"movie_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie the actor starred in, as per the question.\"\n    },\n    \"poker_career_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"poker_player_description\": {\n          \"type\": \"string\",\n          \"description\": \"How the actor's poker involvement is described in the context.\"\n        },\n        \"wsop_participation\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"year\": {\n              \"type\": \"integer\",\n              \"description\": \"The year of World Series of Poker participation.\"\n            },\n            \"finish_position\": {\n              \"type\": \"integer\",\n              \"description\": \"The actor's finish position in the WSOP event.\"\n            },\n            \"total_entrants\": {\n              \"type\": \"integer\",\n              \"description\": \"The total number of entrants in the WSOP event.\"\n            },\n            \"winnings_usd\": {\n              \"type\": \"number\",\n              \"description\": \"The amount of winnings from the WSOP event in USD.\"\n            }\n          },\n          \"required\": [\n            \"year\",\n            \"finish_position\",\n            \"total_entrants\",\n            \"winnings_usd\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"poker_player_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"is_professional_poker_player\",\n    \"movie_starred_in\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "is_professional_poker_player": {
        "type": "boolean",
        "description": "Indicates if the actor is a professional or serious competitive poker player."
      },
      "movie_starred_in": {
        "type": "string",
        "description": "The title of the movie the actor starred in, as per the question."
      },
      "poker_career_details": {
        "type": "object",
        "properties": {
          "poker_player_description": {
            "type": "string",
            "description": "How the actor's poker involvement is described in the context."
          },
          "wsop_participation": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer",
                "description": "The year of World Series of Poker participation."
              },
              "finish_position": {
                "type": "integer",
                "description": "The actor's finish position in the WSOP event."
              },
              "total_entrants": {
                "type": "integer",
                "description": "The total number of entrants in the WSOP event."
              },
              "winnings_usd": {
                "type": "number",
                "description": "The amount of winnings from the WSOP event in USD."
              }
            },
            "required": [
              "year",
              "finish_position",
              "total_entrants",
              "winnings_usd"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "poker_player_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "is_professional_poker_player",
      "movie_starred_in"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
