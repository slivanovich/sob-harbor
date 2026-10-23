{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRio (2011 film): Rio is a 2011 American 3D computer-animated adventure film produced by Blue Sky Studios and directed by Carlos Saldanha.  The title refers to the Brazilian city of Rio de Janeiro, where the film is set.  The film features the voices of Jesse Eisenberg, Anne Hathaway, Jemaine Clement, Leslie Mann, George Lopez, and Jamie Foxx.  It tells the story of Blu (Eisenberg), a male Spix's macaw who is taken to Rio de Janeiro to mate with a free-spirited female Spix's macaw, Jewel (Hathaway).  The two eventually fall in love, and together they have to escape from being smuggled by Nigel (Clement), a cockatoo.  The theme song, \"Telling the World\" was performed by Taio Cruz.\n\nGreig Pickhaver: Greig Pickhaver AM (born 1948) is an actor, comedian and writer, who forms one half of the Australian satirical sports comedy duo \"Roy and HG\" as the excitable sports announcer H.G Nelson.  The award-winning duo teamed up in 1986 for the Triple J radio comedy program \"This Sporting Life\", and were broadcast nationwide for 22 years, leading to several successful television spinoffs.\n\nKate Micucci: Kate Micucci (pronounced ; born March 31, 1980) is an American actress, voice actress, comedian, singer, songwriter and artist.  She is one half of the musical comedy duo Garfunkel and Oates.  Her first major television exposure was her role as Stephanie Gooch in \"Scrubs\", and she then portrayed Shelley in \"Raising Hope\".  She currently voices Sadie Miller in \"Steven Universe\", Sara Murphy in \"Milo Murphy's Law\", Daisy in \"Nature Cat\", Velma Dinkley in the Scooby-Doo franchise since 2015 (replacing Mindy Cohn), and Webby Vanderquack in a new series of \"DuckTales\".\n\nRandy Feltface: Randy Feltface, commonly referred to as merely Randy, or on occasion Randy the Purple Puppet, is an Australian puppet comedian voiced and operated by Heath McIvor.  Randy is a permanent fixture on the international stand-up circuit, and makes regular guest appearances on Australian television.  He also performs as one half of the musical comedy duo \"Sammy J and Randy\", who made their television sitcom debut in 2015 with \"Sammy J & Randy in Ricketts Lane\" on ABC in Australia, for which Randy is credited as co-writer and lead actor.\n\nCockatoo Island festival: Cockatoo Island  Festival was a music festival held on Cockatoo Island in Sydney Harbour, over Easter of 2005, organised by Brandon Saul and Julie Howie of Mixed Industry and The Sydney Harbour Federation Trust.  See the section below on 'Progress' for details of more recent events.  The 2005 Cockatoo Island Festival attracted over 20,000 people across the 3 days, with some choosing to camp on the island, others buying a 3-day pass and catching a dedicated ferry service each day and some buying a single day pass.  While some of the island was off limits, many of the old buildings were used as stages, with the Turbine hall used as the main stage for the festival, a natural amphitheatre looking towards the Gladesville Bridge and a spectacular sunset and an old tunnel to host DJs.  In addition to musical acts, there was also on offer a range of other features such as comedy acts, bingo and trivia, conspiracy theory talks and yoga.\n\nNazeem Hussain: Nazeem Hussain (born 21 April 1986) is an Australian comedian, actor, and radio presenter of Sri Lankan descent.  He is best known as creator and star of comedy show \"Legally Brown\", and one half of the comedy duo Fear of a Brown Planet, along with Aamer Rahman.\n\nDaniel Taylor (actor): Daniel Lawrence Taylor is a British actor who has appeared in several sitcoms including Uncle, How Not to Live Your Life and Hunderby.  He starred in ITV2's 2015 comedy Cockroaches and had a small role in The Inbetweeners.  He is one half of the comedy duo Ginger & Black (with Eri Jackson.)\n\nDan Avidan: Leigh Daniel \"Dan\" Avidan (born March 14, 1979), also known by his stage name Danny Sexbang, is an American musician, Internet personality, singer-songwriter, and comedian.  He is one half of the musical comedy duo Ninja Sex Party with Brian Wecht, as well as the co-host of the Let's Play webseries \"Game Grumps\" with Arin Hanson.  He is also part of the video game-based comedy music trio Starbomb, alongside both Wecht and Hanson.\n\nBret McKenzie: Bret Peter Tarrant McKenzie, ONZM (born 29 June 1976) is a New Zealand comedian, actor, musician and producer, best known for being one half of the Grammy Award-winning musical comedy duo Flight of the Conchords along with Jemaine Clement.  The duo's comedy and music became the basis of a BBC radio series and then an oft-lauded American television series, which aired for two seasons on HBO.  McKenzie served as music supervisor for two Muppet films, \"The Muppets \"(2011) and \"Muppets Most Wanted \"(2014), the former of which won him an Academy Award for Best Original Song for the song \"Man or Muppet\".  His latest work has seen him write the lyrics to the 2016 Sainsburys Christmas advert featuring James Corden on vocals.\n\nJemaine Clement: Jemaine Clement (born 10 January 1974) is a New Zealand comedian, actor, voice actor, singer, writer, director, and multi-instrumentalist, best known as one half of the musical comedy duo Flight of the Conchords along with Bret McKenzie.  They have released multiple albums, created a BBC radio series and a HBO American television series that aired for two seasons.\n\nQuestion: What musical comedy duo is one half of the actor who voices Nigel, the cockatoo from Rio?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who voices the character.\"\n    },\n    \"character_voiced\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character voiced by the actor.\"\n    },\n    \"musical_comedy_duo\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musical comedy duo the actor is part of.\"\n    },\n    \"duo_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The names of the members of the musical comedy duo.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_voiced\",\n    \"musical_comedy_duo\",\n    \"duo_members\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who voices the character."
      },
      "character_voiced": {
        "type": "string",
        "description": "The name of the character voiced by the actor."
      },
      "musical_comedy_duo": {
        "type": "string",
        "description": "The name of the musical comedy duo the actor is part of."
      },
      "duo_members": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The names of the members of the musical comedy duo."
      }
    },
    "required": [
      "actor_name",
      "character_voiced",
      "musical_comedy_duo",
      "duo_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
