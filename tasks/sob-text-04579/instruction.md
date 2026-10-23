{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of The Fairly OddParents episodes: \"The Fairly OddParents\" is an animated American television series that airs on Nicktoons, and previously Nickelodeon.  The series is based on a series of \"Oh Yeah!  Cartoons\", beginning with the short \"The Fairly OddParents!\" .\n\nThe Fairly OddParents: Breakin' da Rules: The Fairly OddParents: Breakin' Da Rules is a video game released for the Game Boy Advance, Nintendo GameCube, PlayStation 2, Xbox, and the PC in North America in 2003.  It is based on the Nickelodeon cartoon \"The Fairly OddParents\".  It was developed by Blitz Games and published by THQ.  Its sequel, \"\" was released on the GameCube, Game Boy Advance and PlayStation 2.  The console versions of this game feature a different plot than the PC version.  It is the only video game based on \"The Fairly OddParents\" to be released for Xbox.\n\nThe Fairly OddParents (film series): The Fairly OddParents is a series of live action spinoff telefilms produced through Nickelodeon, loosely based on Butch Hartman's animated series \"The Fairly OddParents\".  The series currently comprises three films: \"\" (2011), \"A Fairly Odd Christmas\" (2012), and \"A Fairly Odd Summer\" (2014).  The three films take place in a separate universe from the animated series.\n\nThe Fairly OddParents (season 3): The Fairly OddParents' third season began on January 20, 2003. \" The Fairly OddParents\" first movie, \"Abra-Catastrophe!\"  aired in the summer of 2003.\n\nDrake &amp; Josh: Drake & Josh is an American television sitcom created by Dan Schneider for Nickelodeon.  The series follows the lives of two teenage boys with opposite personalities, Drake Parker (Drake Bell) and Josh Nichols (Josh Peck), who become stepbrothers.  Both actors previously appeared in \"The Amanda Show\" along with Nancy Sullivan, who plays Drake and Megan's mother in the series.  Miranda Cosgrove plays Megan, Drake's mischievous younger sister, and Jonathan Goldstein plays Walter, Josh's father.  The series' opening theme song, \"Found a Way\", is written by Drake Bell and Backhouse Mike and performed by Bell.  The series ran from January 11, 2004, to September 16, 2007, totaling 57 episodes in 4 seasons.  It also had two TV films: \"Drake & Josh Go Hollywood\" and \"Merry Christmas, Drake & Josh\".\n\nThe Fairly OddParents (season 5): The 5th season of \"The Fairly OddParents\" started on  14, 2005 (2005--) .  In this season, the show aired its seventh TV movie, \"Fairy Idol\", and three \"The Jimmy Timmy Power Hour\" movies.  After \"The Jerkinators\", \"The Fairly OddParents\" and \"\" seem to end, but later in 2006, they aired episodes that chronologically come before the season finale.  After November 25, 2006, \"Jimmy Neutron\" ended its run, and \"The Fairly OddParents\" was sent on hiatus for 15 months, between December 2006 and December 2007.\n\nA Fairly Odd Summer: A Fairly Odd Summer (also known as A Fairly Odd Movie 3 or A Fairly Odd Paradise) is a 2014 television film and is the third live action film based on the animated series \"The Fairly OddParents\" as well as the third installment in the live action film series.  It is a sequel to \"\" and \"A Fairly Odd Christmas\", and was released on August 2, 2014.\n\nA Fairly Odd Christmas: A Fairly Odd Christmas (also known as A Fairly Odd Movie 2) is a 2012 television film that is the sequel to the 2011 live-action TV film \"\" and the second live-action adaptation of the Nickelodeon animated television series \"The Fairly OddParents\".  This was Drake Bell's second appearance in a Christmas-themed Nickelodeon film, the first being \"Merry Christmas, Drake & Josh\".\n\nDrake Bell: Jared Drake Bell (born June 27, 1986) is an American actor, voice actor, and musician.  Born in Newport Beach, California, he began his career as an actor in the early 1990s at the age of five with his first televised appearance on \"Home Improvement\".  Bell also appeared in several commercials, such as one for \"Pokémon Red\" and \"Blue\", but is best known for his starring roles on Nickelodeon's \"The Amanda Show\" and \"Drake & Josh\".  Bell starred in a trilogy of \"The Fairly OddParents\" movies on Nickelodeon.  Bell was the voice of Peter Parker / Spider-Man in the animated series \"Ultimate Spider-Man\" on Disney XD.  He appeared on ABC's reality TV series \"Splash\".\n\nThe Fairly OddParents: Shadow Showdown: The Fairly OddParents: Shadow Showdown is a platforming video game released in 2004 for Microsoft Windows, GameCube, PlayStation 2, and Game Boy Advance by THQ.  ImaginEngine developed the PC version while Blitz Games developed the GameCube and PlayStation 2 versions.  The game is based on the animated series \"The Fairly OddParents\" and is the sequel to \"\".\n\nQuestion: What is a sequel to a movie with Drake Bell based on \"The Fairly OddParents\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sequel_movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the sequel movie.\"\n    },\n    \"original_movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie to which the answer is a sequel.\"\n    },\n    \"original_movie_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the original movie.\"\n    },\n    \"sequel_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the sequel movie.\"\n    },\n    \"is_live_action\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the movie is a live-action adaptation.\"\n    },\n    \"starring_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor starring in the original movie.\"\n    },\n    \"based_on_series\": {\n      \"type\": \"string\",\n      \"description\": \"The animated series the movie is based on.\"\n    }\n  },\n  \"required\": [\n    \"sequel_movie_title\",\n    \"original_movie_title\",\n    \"original_movie_release_year\",\n    \"sequel_release_year\",\n    \"is_live_action\",\n    \"starring_actor\",\n    \"based_on_series\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sequel_movie_title": {
        "type": "string",
        "description": "The title of the sequel movie."
      },
      "original_movie_title": {
        "type": "string",
        "description": "The title of the movie to which the answer is a sequel."
      },
      "original_movie_release_year": {
        "type": "integer",
        "description": "The release year of the original movie."
      },
      "sequel_release_year": {
        "type": "integer",
        "description": "The release year of the sequel movie."
      },
      "is_live_action": {
        "type": "boolean",
        "description": "Indicates if the movie is a live-action adaptation."
      },
      "starring_actor": {
        "type": "string",
        "description": "The name of the actor starring in the original movie."
      },
      "based_on_series": {
        "type": "string",
        "description": "The animated series the movie is based on."
      }
    },
    "required": [
      "sequel_movie_title",
      "original_movie_title",
      "original_movie_release_year",
      "sequel_release_year",
      "is_live_action",
      "starring_actor",
      "based_on_series"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
