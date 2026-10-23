{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMy Soul to Keep: My Soul to Keep is a novel by American writer Tananarive Due.  A film version of this book is in production with actor Blair Underwood.  It is the first book in Due's African Immortals Series and it followed by \"The Living Blood\".  The third book in the series, \"Blood Colony\", was published in 2008.\n\nMiguel Lopez-Fitzgerald: Miguel Lopez-Fitzgerald is a fictional character on the NBC/DirecTV soap opera \"Passions\".  The youngest son of the once-missing Martin Fitzgerald and Mexican immigrant Pilar Lopez-Fitzgerald, the character as played by original cast member Jesse Metcalfe (July 5, 1999—July 26, 2004, November 2004-January 2005) was caught in a love triangle with true love Charity Standish and her scheming, manipulative cousin, and his best friend, Kay Bennett.  After being written off-canvas for a year, the character returned on February 8, 2006 played by Adrian Bellani; and engaged in a rivalry with Kay's fiancé, and later husband, Fox Crane.  After a three-month hiatus from September to December 2007, while the character was said to have been kidnapped by the forces of darkness and held prisoner in Hell, Blair Redford replaced Bellani on December 24, 2007 and played the role until August 7, 2008.\n\nBlair Redford: David Blair Redford (born July 27, 1983) is an American actor.  He is known for his television roles such as Scotty Grainger on \"The Young and the Restless\", Miguel Lopez-Fitzgerald on \"Passions\", Ethan Whitehorse on \"The Lying Game\", Tyler \"Ty\" Mendoza on \"Switched at Birth\" and Simon Waverly on \"Satisfaction\".\n\nIf I Was Your Man: \"If I Was Your Man\" is a song by American recording artist Joe.  It was written by Mikkel Storleer Eriksen and Tor Erik Hermansen along with Phillip Lamont Jackson for his sixth studio album \"Ain't Nothin' Like Me\" (2007), with production handled by the former two for Stargate.  The contemporary R&B ballad was selected as the album's second single and released to US radios on July 13, 2007.  It peaked at number 84 on the \"Billboard\" Hot 100 and reached the top forty of the Hot R&B/Hip-Hop Songs chart.  The song's accompanying music video features a cameo appearance by actor Blair Underwood and was inspired by the ending scene of the film \"Casablanca\" as his love interest leaves Joe for the man in the plane.\n\nCane Ashby: Cane Ashby is a fictional character from the American CBS soap opera \"The Young and the Restless\".  He is portrayed by Australian actor Daniel Goddard, who originally auditioned for Brad Snyder on \"As the World Turns\" but was recommended for a role on \"The Young and the Restless\" instead.  The role was to be portrayed as an American, but Goddard's Australian descent influenced the character's background.  Former head writer Lynn Marie Latham introduced him during the episode airing on January 12, 2007 as an Australian bartender in search of his family.  Latham created Cane as the son of Phillip Chancellor II (Donnelly Rhodes) and Jill Abbott (Jess Walton) but the character's background was rewritten by Maria Arena Bell in 2009, re-establishing him as the son of Colin and Genevieve Atkinson (Tristan Rogers and Genie Francis).\n\nChristine Blair: Christine Blair is a fictional character from \"The Young and the Restless\", an American soap opera on the CBS network, portrayed by Lauralee Bell.  The daughter of series creators William J. Bell and Lee Phillip Bell, she was introduced in 1983 as a teen model, later developing into a lawyer and district attorney.  In 2001, Bell asked to be moved to a recurring status from contract after a maternity leave, though she returned to a regular status the following year.  In 2005, she returned to recurring, remaining only for another year until her departure.  In 2007, the character was brought over to \"The Bold and the Beautiful\" by executive producer Bradley Bell, the actress' real-life brother, for a short-term stint.  In 2010, Bell returned to \"The Young and the Restless\", where she continues to make recurring appearances.\n\nPeter Barton (actor): Peter Thomas Barton (born July 19, 1956) is an American actor.  He starred in \"The Powers of Matthew Star\", with Louis Gossett, Jr.; \"Burke's Law\" with Gene Barry; and the soap opera \"Sunset Beach\".  Named one of the 10 sexiest guys in soaps by \"Playgirl\", Barton is probably best known as Dr. Scott Grainger on the daytime drama \"The Young and the Restless\".\n\nDance of the Dead (film): Dance of the Dead is a 2008 American independent zombie comedy, directed by Gregg Bishop and written by Joe Ballarini.  The film featured Jared Kusnitz, Greyson Chadwick, Chandler Darby, Lucas Till, Blair Redford and Carissa Capobianco.  The plot revolves around the mysterious reanimation of the dead and the efforts of several students to save their high school prom from attack.\n\nScotty Grainger: Scott \"Scotty\" Grainger Jr. is a fictional character from the CBS soap opera \"The Young and the Restless\".  He was played by actor Blair Redford from July 2005 until January 2006.  In January 2017, \"Soap Opera Digest\" announced that Daniel Hall had been recast in the role.\n\nMarla Adams: Marla Adams (born August 28, 1938; Ocean City, New Jersey) is an American television actress, best known for her roles as Belle Clemens on \"The Secret Storm\", from 1968 to 1974, and as Dina Abbott Mergeron on \"The Young and the Restless\".  As Belle Clemens, she was the show's reigning villainess for the last years of its run, stopping at almost nothing to destroy the life of the show's leading heroine, Amy Ames.  Like Vicky and Dorian later on \"One Life to Live\", the two rivals were at one time related through marriage.  As Dina Abbott on \"The Young and the Restless\" from 1983 to 1986, in 1991 and again in 1996, she caused major disruptions in the lives of her three children and ex-husband John Abbott and his wife Jill.  She reprised her role as Dina for three episodes on \"The Young and the Restless\" in 2008 when Katharine Chancellor was presumed dead.  In May 2017, Adams returned to \"The Young and the Restless\".\n\nQuestion: American actor Blair Redford was succeeded in the role of Scotty Grainger on \"The Young and the Restless\" by what actor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fictional character.\"\n    },\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television show.\"\n    },\n    \"predecessor_actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who previously played the role.\"\n    },\n    \"successor_actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who succeeded in the role.\"\n    },\n    \"recast_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the role was recast.\"\n    }\n  },\n  \"required\": [\n    \"character_name\",\n    \"show_name\",\n    \"predecessor_actor_name\",\n    \"successor_actor_name\",\n    \"recast_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character_name": {
        "type": "string",
        "description": "The name of the fictional character."
      },
      "show_name": {
        "type": "string",
        "description": "The name of the television show."
      },
      "predecessor_actor_name": {
        "type": "string",
        "description": "The name of the actor who previously played the role."
      },
      "successor_actor_name": {
        "type": "string",
        "description": "The name of the actor who succeeded in the role."
      },
      "recast_year": {
        "type": "integer",
        "description": "The year the role was recast."
      }
    },
    "required": [
      "character_name",
      "show_name",
      "predecessor_actor_name",
      "successor_actor_name",
      "recast_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
