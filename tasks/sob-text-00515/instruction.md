{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhantom of the Mall: Eric's Revenge: Phantom of the Mall: Eric's Revenge is a 1989 horror film about a young man who apparently dies in a suspicious house fire after saving his girlfriend, Melody; a year later, at the new mall built over the site of the burned-out house, thefts and murders begin to occur as a mysterious figure secretly prowls around the shopping center and takes a keen interest in watching over and protecting Melody.  The film was directed by Richard Friedman, and stars Derek Rydall, Jonathan Goldsmith, Rob Estes, Pauly Shore, Kari Whitman, Ken Foree and Morgan Fairchild.\n\nRisk Everything: Risk Everything is an advertisement campaign created for American sports apparel company Nike by the American advertising agency Wieden+Kennedy.  The advertisement campaign, spanning radio, television, out-of-home, online advertising and print media, was specially made for the 2014 FIFA World Cup and starring well-known football players from national teams and clubs.  This campaign emphasizes the mantra of \"risk everything\" – taking every dangerous life-or-death chance to succeed and outshine your rivals.\n\nPaul Goldsmith (politician): Paul Jonathan Goldsmith (born 1971) is a New Zealand politician and, since the 2011 election , a list member of the New Zealand House of Representatives.  He is a member of the National Party.\n\nThe Most Interesting Man in the World: The Most Interesting Man in the World is an advertising campaign for the Dos Equis brand of beer.  The ads feature \"the world's most interesting man,\" a bearded, debonair gentleman, with voiceovers that are intended to be both humorous and outrageous.  The advertisements first began appearing in the United States in 2006 and have since then become a popular Internet meme.\n\nHal Goldsmith: Harold Eugene \"Hal\" Goldsmith (August 18, 1898 – October 20, 1985) was a pitcher in Major League Baseball.  He played for the Boston Braves from 1926 through 1928 and the St. Louis Cardinals in 1929.  He had a career 4.04 earned run average as a professional.  Goldsmith played collegiately at St. Lawrence University.\n\nNo issue, lelo tissue: No issue, lelo tissue (Urdu: ‎ ) was a Pakistani television advertisement campaign started by Jazz Pakistan, following the victory of Pakistan's cricket team in the 2017 ICC Champions Trophy Final.  It was directed by Hassan Dawar.  The advertisement has been dubbed as Pakistan's response to India's famous \"Mauka Mauka\" commercials.\n\nSkin (Rihanna song): \"Skin\" is a song by Barbadian recording artist Rihanna from her fifth studio album, \"Loud\" (2010).  The song was written by Kenneth Coby and Ursula Yancy, with production helmed by Soundz.  Musically, \"Skin\" is a R&B song that contains influences from pop, dance-pop and dubstep genres, whilst lyrically, the song is about being in a relationship with someone and only wanting to feel their skin close to the protagonists.  \"Skin\" received generally positive reviews from critics, as part of their overall review of \"Loud\", praising \"Skins compositions as well as Rihanna's sensual vocal performance.  The song was included on the set list of the Loud Tour (2011), where Rihanna retrieves a man or woman from the audience near the end of the song, and performs a lap-dance whilst on an elevated platform.  \"Skin\" was also used in Rihanna's advertisement campaign for Armani Jeans.\n\nDavid Goldsmith (actor): David Goldsmith (born July 19, 1969 in New Brunswick, New Jersey) is an American actor.  He is the son of \"Gunsmoke\" regular Jonathan Goldsmith.\n\nAugustin Legrand: Augustin Legrand is a French actor.  He replaced Jonathan Goldsmith as Dos Equis' Most Interesting Man in the World in 2016.\n\nJonathan Goldsmith: Jonathan Goldsmith (born September 26, 1938) is an American actor.  He began his career on the New York stage, then started a career in film and television.  He appeared in several TV shows from the 1960s to the 1990s.  He is best known for appearing in television commercials for Dos Equis beer, from 2006 to 2016, as the character The Most Interesting Man in the World.\n\nQuestion: Jonathan Goldsmith played \"the most interesting man in the world\" and represented what advertisement campaign?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The specific character or role the actor played in the campaign.\"\n    },\n    \"advertisement_campaign\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"campaign_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the advertisement campaign.\"\n        },\n        \"brand_advertised\": {\n          \"type\": \"string\",\n          \"description\": \"The brand or product that was advertised.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the campaign began.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the actor's involvement in the campaign ended.\"\n        }\n      },\n      \"required\": [\n        \"campaign_name\",\n        \"brand_advertised\",\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_played\",\n    \"advertisement_campaign\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_played": {
        "type": "string",
        "description": "The specific character or role the actor played in the campaign."
      },
      "advertisement_campaign": {
        "type": "object",
        "properties": {
          "campaign_name": {
            "type": "string",
            "description": "The name of the advertisement campaign."
          },
          "brand_advertised": {
            "type": "string",
            "description": "The brand or product that was advertised."
          },
          "start_year": {
            "type": "integer",
            "description": "The year the campaign began."
          },
          "end_year": {
            "type": "integer",
            "description": "The year the actor's involvement in the campaign ended."
          }
        },
        "required": [
          "campaign_name",
          "brand_advertised",
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "role_played",
      "advertisement_campaign"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
