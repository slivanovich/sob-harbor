{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSue Ball: Susan Gabrielle \"Sue\" Ball (born March 2, 1967, in Philadelphia, Pennsylvania) is an American actress.  She is best known for her starring role in \"Leo and Liz in Beverly Hills\", which was created by Steve Martin.  She has had many guest starring and recurring roles, most notably \"Rags to Riches\" (TV series), \"Perfect Strangers\" (TV series), \"Valerie\" (TV series), and \"It's a Living\" (1980 TV series).\n\nMicom Film and TV Productions: MICOM Film and TV Productions was established in 1989 by Sreco Mihelcic in a Former Yugoslavian republic Slovenia.  In the early 90' company joined two sons, Matjaz Mihelcic - Program director, Producer and Vasja Mihelcic - technical director and Executive Producer.  MICOM was in 1990s the leading Slovenian creative house, producing TV shows for youth, popular entertainment TV shows and discovered many new TV concepts.  Micom discovered many talents, different creative people and gave them possibility to express themselves.  The most popular TV shows were: Lahkih nog naokrog (educational youth TV series), Cari zacimb (entertaining cooking TV series), Razpoke v casu (fantasy TV series).  They also produced documentary movies.  One of them got in 1996 internationally release - Fight for the river and it's distributed by International Historic Films. .  In the beginning of 2000 company joined Marjana Mihelcic.  It was a family based company with long tradition in show and entertainment business.  Micom produced around 30.000 minutes of program for National TV Slovenia and other media.  In 2002 company stopped producing because of the tragedy in the family.  Both sons went separate way and build their own Film and TV production house.\n\nMacross Ace Frontier: Macross Ace Frontier (マクロス エース フロンティア , makurosu ēsu furontia ) is a shooting game developed by Artdink for the PlayStation Portable.  The game is based on Studio Nue's popular \"Macross\" series, one of which is known in the West as the first generation of \"Robotech\".  It features original elements as well as characters, mechanics, episode plots and BGM borrowed from 1982's \"The Super Dimension Fortress Macross\" original TV series, the 1992 \"Macross Plus\" OVA series, the 1994 \"Macross 7\" TV series and the 2008 \"Macross Frontier\" TV series, as well as incorporating more elements from the 1984 \"\" feature film and the 2002 prequel OVA series \"Macross Zero\".\n\nSuper Islaw: Super Islaw is a fictional Filipino superhero created by J. Erastheo Navoa who appeared in some movies and TV Series.  He was portrayed by Richard Gomez in the movie Super Islaw and The Flying Kids and was later revived by Zanjoe Marudo in ABS-CBN's Super Inggo TV series.\n\nMy Super Ex-Girlfriend: My Super Ex-Girlfriend is a 2006 American superhero comedy film directed by Ivan Reitman and starring Uma Thurman, Luke Wilson, Anna Faris, Eddie Izzard, Rainn Wilson, and Wanda Sykes.\n\nAndy Milder: Andy Milder (born August 16, 1969) is an American actor and voice actor.  He has appeared in such films as \"Apollo 13\", \"Armageddon\", \"Rumor Has It…\", \"Frost/Nixon\", \"Transformers\" and \"Domino\".  He was a series regular on \"Fame L.A.\" and \"Weeds\", and appeared on such shows as \"\", \"\", \"The West Wing\", \"Six Feet Under\", \"Ugly Betty\", \"Boston Legal\", \"Parks and Recreation\", \"Married... with Children\", \"The Wonder Years\", \"Private Practice\" and \"Criminal Minds\".  Milder provided narration for \"Ballroom Bootcamp\", \"101 Most Starlicious Make-Overs\", and \"Wrecks to Riches\".  He provided the voice of Prince Sebastian LaCroix in the 2004 video game \"\" and Lightning Lad in the 2006 animated series \"Legion of Super Heroes\" and the film \"\".  From 2005 to 2009, he was a recurring cast member and later series regular on \"Weeds\" as Dean Hodes.  Starting in 2011, he is a recurring cast member on the Disney Channel sitcom \"Austin & Ally\" as Lester Dawson.  He also had an appearance on the show \"Royal Pains\" on the USA Network.\n\nVijay TV's Super Singer (TV series): Vijay TV's Super Singer is a reality television-music competition series telecast on the Indian Tamil language TV channel, STAR Vijay (also known as Vijay TV).  Originally airing as Airtel Super Singer in April 2006, the TV series has since adapted into various high level music competitions on Vijay TV, including Airtel Super Singer, Airtel Super Singer Junior, Airtel Super Singer T20, and Super Singer Celebrity Season.\n\nSteele Stebbins: Steele Stebbins (born August 19, 2003) is an American child actor.  He is best known for his performance as Kevin Griswold, in the 2015 comedy film \"Vacation\" and as Wyatt, in the 2014 comedy film \"A Haunted House 2\".  In addition, he has appeared in two short films, \"Wish You Were (Here)\" in 2010, and \"Metered\" in 2011, as well as four episodes of the TV series \"Crazy Ex-Girlfriend\".\n\nEddie Izzard: Edward John \"Eddie\" Izzard ( ; born 7 February 1962) is an English stand-up comedian, actor, writer and political activist.  His comedic style takes the form of rambling, whimsical monologue, and self-referential pantomime.  He had a starring role in the television series \"The Riches\" as Wayne Malloy and has appeared in films such as \"Ocean's Twelve\", \"Ocean's Thirteen\", \"Mystery Men\", \"Shadow of the Vampire\", \"The Cat's Meow\", \"Across the Universe\" and \"Valkyrie\".  He has also worked as a voice actor in \"The Wild\", \"Igor\", \"\", \"Cars 2\" and \"The LEGO Batman Movie\".\n\nOded Fehr: Oded Fehr (Hebrew: עודד פהר‎ ‎ ; born on November 23, 1970) is an Israeli film and television actor now based in the United States.  He is known for his appearance as Ardeth Bay in the 1999 remake of \"The Mummy\" and its sequel \"The Mummy Returns\", as well as Carlos Oliveira in \"\", \"\" and \"\", Faris al-Farik in \"Sleeper Cell\", the demon Zankou in the TV series \"Charmed\" and Eli Cohn on the TV series \"V\".  He recently portrayed Eyal Lavin, a Mossad agent, on the TV series \"Covert Affairs\", as well as Beau Bronn on the TV series \"Jane by Design\" and Mossad Deputy Director Ilan Bodnar on \"NCIS\".\n\nQuestion: What actor was in \"My Super Ex-Girlfriend\" and also in the TV series \"the Riches\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"actor_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the actor in 'Day Month Year' format.\"\n    },\n    \"film_appearance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film the actor appeared in.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"tv_series_appearance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the TV series the actor appeared in.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role the actor played in the TV series.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"actor_nationality\",\n    \"film_appearance\",\n    \"tv_series_appearance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "actor_birth_date": {
        "type": "string",
        "description": "The birth date of the actor in 'Day Month Year' format."
      },
      "film_appearance": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film the actor appeared in."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "year"
        ],
        "additionalProperties": false
      },
      "tv_series_appearance": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the TV series the actor appeared in."
          },
          "role": {
            "type": "string",
            "description": "The specific role the actor played in the TV series."
          }
        },
        "required": [
          "title",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "actor_nationality",
      "film_appearance",
      "tv_series_appearance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
