{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDie Another Day: Die Another Day (2002) is the twentieth spy film in the \"James Bond\" series, and the fourth and final film to star Pierce Brosnan as the fictional MI6 agent James Bond.  The film follows Bond as he leads a mission to North Korea, during which he is betrayed and, after seemingly killing a rogue North Korean colonel, is captured and imprisoned.  Fourteen months later, Bond is released as part of a prisoner exchange.  Surmising that someone within the British government betrayed him, he attempts to earn redemption by tracking down his betrayer and killing a North Korean agent he believes was involved in his torture.\n\nCasino Royale (2006 film): Casino Royale (2006) is the twenty-first spy film in the Eon Productions \"James Bond\" film series and the first to star Daniel Craig as the fictional MI6 agent James Bond.  Directed by Martin Campbell and written by Neal Purvis & Robert Wade and Paul Haggis, the film marks the third screen adaptation of Ian Fleming's 1953 novel of the same name.  \"Casino Royale\" is a reboot of the film series and as such is set at the beginning of Bond's career as Agent 007, just as he is earning his licence to kill.  After preventing a terrorist attack at Miami International Airport, Bond falls in love with Vesper Lynd, the treasury employee assigned to provide the money he needs to bankrupt a terrorist financier, Le Chiffre, by beating him in a high-stakes poker game.  The story arc continues in the following \"Bond\" film \"Quantum of Solace\" (2008), \"Skyfall\" (2012), and \"Spectre\" (2015) also feature explicit references to characters and events in this film.\n\nThunderball (film): Thunderball (1965) is the fourth spy film in the James Bond series starring Sean Connery as the fictional MI6 agent James Bond.  It is an adaptation of the novel of the same name by Ian Fleming, which in turn was based on an original screenplay by Jack Whittingham.  It was directed by Terence Young, with its screenplay by Richard Maibaum and John Hopkins.\n\nJames Bond 007: From Russia with Love: James Bond 007: From Russia with Love is a third-person shooter video game developed by EA Redwood Shores and published by Electronic Arts featuring Ian Fleming's secret agent, James Bond 007, whose likeness and voice is that of Sean Connery.  The game is based on the 1957 novel and the 1963 film of the same name.  The game follows the storyline of the book and film, albeit adding in new scenes to make the game more action-oriented, as well as changing the affiliation of the main villains.  Additionally, it features many elements of later Bond films to recreate the feel of the era such as the Aston Martin DB5 that debuted in \"Goldfinger\" (1964) and the jet pack from \"Thunderball\" (1965).  \"From Russia with Love\" is also notable in that it is the first video game to use Sean Connery's younger likeness as James Bond and the first to include all new voice work by the actor after twenty-two years away from the role.  \"From Russia with Love\" is the last James Bond video game EA Games marketed before they lost the rights to Activision in 2006.\n\nMr. Wint and Mr. Kidd: W. Winter—known as Wint—and Charles Kidd are fictional characters in the James Bond novel and film, \"Diamonds Are Forever\".  In the novel, Wint and Kidd are members of The Spangled Mob.  In the film, it is assumed that they are henchmen for the villain, Ernst Stavro Blofeld, though the characters share no scenes with and are not seen taking instructions from Blofeld (or anyone else, except for Bert Saxby).  One of their trademarks is trading quips after killing their targets; they also do so after a failed attempt to kill Bond.  In the film, Wint is played by the clean-shaven actor Bruce Glover and Kidd by bespectacled jazz musician Putter Smith in a rare acting role.\n\nGoldfinger (film): Goldfinger (1964) is the third spy film in the James Bond series produced by Eon Productions, and the third to star Sean Connery as the fictional MI6 agent James Bond.  It is based on the novel of the same name by Ian Fleming.  The film also stars Honor Blackman as Bond girl Pussy Galore and Gert Fröbe as the title character Auric Goldfinger, along with Shirley Eaton as the iconic Bond girl Jill Masterson.  \"Goldfinger\" was produced by Albert R. Broccoli and Harry Saltzman and was the first of four Bond films directed by Guy Hamilton.\n\nDiamonds Are Forever (film): Diamonds Are Forever (1971) is the seventh spy film in the \"James Bond\" series by Eon Productions, and the sixth and final Eon film to star Sean Connery as the fictional MI6 agent James Bond.\n\nYou Only Live Twice (film): You Only Live Twice (1967) is the fifth spy film in the \"James Bond\" series, and the fifth to star Sean Connery as the fictional MI6 agent James Bond.  The film's screenplay was written by Roald Dahl, and loosely based on Ian Fleming's 1964 novel of the same name.  It is the first \"James Bond\" film to discard most of Fleming's plot, using only a few characters and locations from the book as the background for an entirely new story.\n\nFrom Russia with Love (film): From Russia with Love (1963) is the second spy film in the \"James Bond\" film series produced by Eon Productions, as well as Sean Connery's second role as MI6 agent James Bond.  It was directed by Terence Young, produced by Albert R. Broccoli and Harry Saltzman, and written by Richard Maibaum and Johanna Harwood, based on Ian Fleming's similarly-named 1957 novel.  In the film, Bond is sent to assist in the defection of Soviet consulate clerk Tatiana Romanova in Turkey, where SPECTRE plans to avenge Bond's killing of Dr. No.\n\nLive and Let Die (film): Live and Let Die (1973) is the eighth spy film in the \"James Bond\" series to be produced by Eon Productions, and the first to star Roger Moore as the fictional MI6 agent James Bond.  Produced by Albert R. Broccoli and Harry Saltzman, it was the third of four Bond films to be directed by Guy Hamilton.  Although the producers had wanted Sean Connery to return after his role in the previous Bond film \"Diamonds Are Forever\", he declined, sparking a search for a new actor to play James Bond.  Moore was signed for the lead role.\n\nQuestion: Which Eon film that stars Sean Connery as the fictional MI6 agent James Bond, features two James Bond villains that are known for trading quips after killing their targets appear?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the James Bond film.\"\n    },\n    \"bond_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The actor who played James Bond in this film.\"\n    },\n    \"film_series_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The numerical order of the film in the James Bond series.\"\n    },\n    \"villains\": {\n      \"type\": \"array\",\n      \"description\": \"A list of villains featured in the film with their notable characteristics.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the villain.\"\n          },\n          \"notable_trait\": {\n            \"type\": \"string\",\n            \"description\": \"A specific characteristic or action associated with the villain.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"notable_trait\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"bond_actor\",\n    \"film_series_number\",\n    \"villains\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the James Bond film."
      },
      "bond_actor": {
        "type": "string",
        "description": "The actor who played James Bond in this film."
      },
      "film_series_number": {
        "type": "integer",
        "description": "The numerical order of the film in the James Bond series."
      },
      "villains": {
        "type": "array",
        "description": "A list of villains featured in the film with their notable characteristics.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the villain."
            },
            "notable_trait": {
              "type": "string",
              "description": "A specific characteristic or action associated with the villain."
            }
          },
          "required": [
            "name",
            "notable_trait"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "film_title",
      "bond_actor",
      "film_series_number",
      "villains"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
