{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEllen Cleghorne: Ellen Cleghorne (born November 29, 1965) is an American actress and comedian, best known as a cast member of \"Saturday Night Live\" from 1991 to 1995.  Cleghorne was the sketch comedy show's second African-American female repertory cast member, succeeding Danitra Vance in its eleventh season, and the first African-American female cast member to stay for more than one season.  She returned for its 40th anniversary special on February 15, 2015.  Cleghorne was ranked the 69th greatest \"Saturday Night Live\" cast member by \"Rolling Stone\" magazine.\n\nMary Katherine Gallagher: Mary Katherine Gallagher is a fictional character invented and portrayed by \"Saturday Night Live\" cast member Molly Shannon from 1995 to 2001.  She was considered the first breakout character from the new 1995 cast, and a significant marker of the increased influence of women writers on the show in the 1990s.  Shannon portrayed the character in a 1999 film, \"Superstar\", and she also reprised the role when she hosted \"Saturday Night Live\" in 2007.\n\nSNL Studios: SNL Studios is a production company, founded in July 1997 as a joint venture between \"Saturday Night Live\" executive producer Lorne Michaels and NBC Studios (now Universal Television, the production arm of NBCUniversal).  While this venture also initially included Paramount Pictures, it was dissolved following NBC's merger with Universal Studios.  On the television side, SNL Studios produces \"Saturday Night Live\" in association with Broadway Video.  Film productions, typically offshoots of Saturday Night Live' sketches, include, among others, \"A Night at the Roxbury\" and \"Superstar\".\n\nCelebrity Jeopardy! (Saturday Night Live): Celebrity Jeopardy! is a series of sketches that aired regularly on the television comedy/variety show \"Saturday Night Live\" between 1996 and 2002, the years when Will Ferrell was a cast member.  It parodies the same-named special event on the television quiz show \"Jeopardy!\" that features competition between notable individuals with all winnings going towards charitable organizations, and significant reductions to the game's level of difficulty.  Fifteen sketches aired between December 1996 and February 2015: two sketches per season from 1996 to 2002, when Ferrell was a regular on the show; and one each in 2005 and 2009, when Ferrell returned to the show as host.  The sketch was revived for the \"Saturday Night Live 40th Anniversary Special\" on February 15, 2015.\n\nJay Pharoah: Jared Antonio Farrow (born 14 October, 1987) better known by his stage name Jay Pharoah, is an American actor, stand-up comedian, impressionist, rapper, and voice actor.  He joined the cast of NBC's \"Saturday Night Live\" in 2010, for its thirty-sixth season.  In 2015, he was ranked the 55th greatest \"Saturday Night Live\" cast member by \"Rolling Stone\" magazine.\n\nBar Hopping: Bar Hopping is a 2000 comedy film directed by Steve Cohen starring Robert Hegyes, Tom Arnold, Linda Favila, Nicole Sullivan, John Henson, Anson Downes, Romy Windsor, Scott Baio and Kevin Nealon.  In the film, a myriad of Generation X couples try to comprehend love in the bar scene.\n\nList of Saturday Night Live guests: \"Saturday Night Live\" (abbreviated as SNL) is a late-night sketch comedy and variety show created by Lorne Michaels.  It premiered on NBC, a terrestrial television network, on October 11, 1975 under the title \"NBC's Saturday Night\".  The show often satirizes contemporary American popular culture and politics.  \"Saturday Night Live\" features a two-tiered cast: the repertory members, also known as the \"Not Ready for Prime-Time Players\", and newer cast members, known as \"Featured Players.\"\n\nA Night at the Roxbury: A Night at the Roxbury is a 1998 American comedy film based on a recurring skit on television's long-running \"Saturday Night Live\" called \"The Roxbury Guys\".  \"Saturday Night Live\" regulars Will Ferrell, Chris Kattan, Molly Shannon, Mark McKinney and Colin Quinn star.  This film expands on the original Saturday Night Live sketches where the Roxbury Guys were joined by that week's host, and bobbed their heads to Haddaway's hit song \"What Is Love\" while being comically rejected by women at various clubs.\n\nList of Saturday Night Live episodes: <section begin=head />\"Saturday Night Live\" (\"SNL\") is a late-night sketch comedy and variety show created by Lorne Michaels.  It premiered on NBC, a terrestrial television network, on October 11, 1975 under the title \"NBC's Saturday Night\".  The show often satirizes contemporary American popular culture and politics.  \"Saturday Night Live\" features a two-tiered cast: the repertory members, also known as the \"Not Ready for Prime-Time Players,\" and newer cast members, known as \"Featured Players.\"  Each week, the show features a host, often a well-known celebrity, who delivers an opening monologue and performs in sketches with the cast.  A musical guest is also invited to perform several sets (usually two, and occasionally more).  Every so often a host or musical guest will fill both roles, such as was the case with Britney Spears in 2000 and 2002, Jennifer Lopez in 2001 and 2010, Justin Timberlake in 2003, 2006 and 2013, Taylor Swift in 2009, Bruno Mars in 2012, Lady Gaga in 2013, Miley Cyrus in 2013 and 2015, Drake in 2014 and 2016, Blake Shelton in 2015, and Ariana Grande in 2016.  With the exception of Season 7 and several other rare cases, the show has begun with a cold open that ends with someone breaking character and proclaiming \"Live from New York, it's Saturday Night! \"\n\nKevin Nealon: Kevin Nealon ( ; born November 18, 1953) is an American actor and comedian, best known as a cast member on \"Saturday Night Live\" from 1986 to 1995, acting in several of the Happy Madison films, for playing Doug Wilson on the Showtime series \"Weeds\", and providing the voice of the title character, Glenn Martin, on \"Glenn Martin, DDS\".\n\nQuestion: Bar Hopping is a film that starred what \"Saturday Night Live\" cast member?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"snl_cast_member\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Saturday Night Live cast member.\"\n        },\n        \"snl_tenure_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the cast member's tenure on Saturday Night Live.\"\n        },\n        \"snl_tenure_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the cast member's tenure on Saturday Night Live.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"snl_tenure_start_year\",\n        \"snl_tenure_end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"role_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the cast member's involvement in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"snl_cast_member\",\n    \"role_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "snl_cast_member": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Saturday Night Live cast member."
          },
          "snl_tenure_start_year": {
            "type": "integer",
            "description": "The start year of the cast member's tenure on Saturday Night Live."
          },
          "snl_tenure_end_year": {
            "type": "integer",
            "description": "The end year of the cast member's tenure on Saturday Night Live."
          }
        },
        "required": [
          "name",
          "snl_tenure_start_year",
          "snl_tenure_end_year"
        ],
        "additionalProperties": false
      },
      "role_description": {
        "type": "string",
        "description": "Description of the cast member's involvement in the film."
      }
    },
    "required": [
      "film_title",
      "snl_cast_member",
      "role_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
