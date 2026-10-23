{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoahn Hylton: Roahn Hylton, known as \"First Born\", is a Hip-Hop, R&B, and Pop music producer from Houston, Texas.  He attended Oral Roberts University before becoming a professional music producer.  First Born was a co-producer with Kane Beatz on Nicki Minaj’s first Billboard Top 5 single \"Super Bass\".  In addition to the song being a platinum hit in the U.S., \"Super Bass\" spent several weeks inside the top 20 and is Minaj’s highest charting solo single to date.  First Born has also worked with Flo Rida, Plies, Ne-Yo, Trey Songz, Kaleena, Ludacris, Cassie, The Game, Gucci, and New Boys.  Additional projects Hylton has worked on include Shonlock's LP \"Never Odd or Even\" and Darrell Vanzant's \"Broken: A Musical\".\n\nGeneral Assembly and Church of the First Born: The General Assembly and Church of the First Born (often shortened to just “Church of the First Born”) is a fundamental faith healing sect established in Canada during the 1800s.  This group has no affiliation with the various Mormon fundamentalist groups with similar \"Firstborn\" names.\n\nStarship Highlander: Raumschiff Highlander (translated: Starship Highlander) is a fan-created science fiction film and novel series.  The series was initiated in 1993 by Robert Amper.  Originally, a fan club of science fiction, especially for \"\" (aka \"ST:TOS\" or just \"TOS\"), and the Star Wars movies, whose members met regularly.  Some members having experience in filmmaking, the idea spawned of creating material for a movie.  First episode of the series aired in 1995 on German TV Channel SAT.1.  Inspired by the success of their movie came four additional sequels at the rate of one per year.  The movies are a parody of Star Trek and other classics of the genre.\n\nCinderella (sports): In sports, the terms Cinderella, \"Cinderella story\", and Cinderella team are used to refer to situations in which competitors achieve far greater success than would reasonably have been expected.  Cinderella stories tend to gain much media and fan attention as they move closer to the championship game at the end of the tournament.  The term comes from \"Cinderella\", a well-known European folk tale embodying a myth-element of unjust oppression/triumphant reward.  The title character is a woman living in unfortunate circumstances that are suddenly changed to remarkable fortune.  In a sporting context the term has been used at least since 1939, but came into widespread usage in 1950, when the Disney movie came out that year, and in reference to City College of New York, the unexpected winners of the NCAA Men's Basketball championship also that year.  The term was used by Bill Murray in the 1980 hit movie \"Caddyshack\" where he pretends as the announcer to his own golf fantasy: \"Cinderella story.  Outta nowhere.  A former greenskeeper, now, about to become the Masters champion.\"\n\nRadio tekee murron: Radio tekee murron (\"The Radio Burglary\") (1951) is a Finnish crime comedy directed by Matti Kassila and starring Hannes Häyrinen.  The idea for the movie came from an actual radio program done by sensationalist reporter Usko Santavuori, in which he committed a fake burglary of which local police forces had not been made aware, with the exception of the commander.\n\nFirstborn: A firstborn (also known as an eldest child or sometimes firstling) is the first child born to in the birth order of a couple through childbirth.  Historically, the role of the first born child has been socially significant, particularly for a first born son in patriarchal societies.  In law, many systems have incorporated the concept of primogeniture, wherein the first-born child inherits their parent's property.  The firstborn in Judaism, the \"bechor\", is also accorded a special position.\n\nBorn into Brothels: Born into Brothels: Calcutta's Red Light Kids is a 2004 Indian-American documentary film about the children of prostitutes in Sonagachi, Kolkata's red light district.  The widely acclaimed film, written and directed by Zana Briski and Ross Kauffman, won a string of accolades including the Academy Award for Best Documentary Feature in 2004.\n\nPunk's Not Dead (2007 film): Punk's Not Dead is a 2007 documentary film directed by Susan Dynner, an American hardcore punk fan.  The film claims to infiltrate American clubs, malls, recording studios, etc. where it sets out to claim hardcore punk and pop punk music is \"thriving\" from an American perspective.  Its content features performances largely from 1980s hardcore bands and MTV skate punk and pop punk/rock acts.  It also includes various interviews and behind-the-scenes footage with the bands, labels and fans.\n\nTown Without Pity: Town Without Pity (German: Stadt ohne Mitleid) is a 1961 American, Swiss, and West German international co-production drama film directed by Gottfried Reinhardt.  Produced by The Mirisch Corporation, the film stars Kirk Douglas, Christine Kaufmann, and E. G. Marshall.  Coincidentally, this movie came out the same year that John A. Bennett, to this day the last man executed by the U.S. Army, was hanged for raping an 11-year-old girl.\n\nVedham Pudhithu: Vedham Puthithu (Tamil: வேதம் புதிது English: New vedha ) (1987), starring Sathyaraj and Amala is a Tamil movie, written by K.Kannan, who after this movie came to be Vedham Puthithu Kannan and directed by Bharathiraja.  Charuhasan, Saritha, Raja and 'Nizhalgal' Ravi played supporting roles in the movie.\n\nQuestion: Which movie came out first Born into Brothels or Punk's Not Dead ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_1_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the first movie mentioned in the question.\"\n    },\n    \"movie_1_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the first movie.\"\n    },\n    \"movie_2_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the second movie mentioned in the question.\"\n    },\n    \"movie_2_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the second movie.\"\n    },\n    \"first_released_movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie that was released first.\"\n    },\n    \"first_released_movie_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie that was released first.\"\n    }\n  },\n  \"required\": [\n    \"movie_1_title\",\n    \"movie_1_release_year\",\n    \"movie_2_title\",\n    \"movie_2_release_year\",\n    \"first_released_movie_title\",\n    \"first_released_movie_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_1_title": {
        "type": "string",
        "description": "The title of the first movie mentioned in the question."
      },
      "movie_1_release_year": {
        "type": "integer",
        "description": "The release year of the first movie."
      },
      "movie_2_title": {
        "type": "string",
        "description": "The title of the second movie mentioned in the question."
      },
      "movie_2_release_year": {
        "type": "integer",
        "description": "The release year of the second movie."
      },
      "first_released_movie_title": {
        "type": "string",
        "description": "The title of the movie that was released first."
      },
      "first_released_movie_year": {
        "type": "integer",
        "description": "The release year of the movie that was released first."
      }
    },
    "required": [
      "movie_1_title",
      "movie_1_release_year",
      "movie_2_title",
      "movie_2_release_year",
      "first_released_movie_title",
      "first_released_movie_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
