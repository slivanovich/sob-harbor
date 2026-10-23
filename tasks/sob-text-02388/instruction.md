{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nP. King Duckling: P. King Duckling is a Chinese/American animated children's television series created by Josh Selig.  The series debuted on Disney Junior in the United States on November 7, 2016.\n\nWacky Races (2017 TV series): Wacky Races is an American animated children's television series created by Rebecca Himot and Tramm Wigzell.  It is a remake of the 1968 Hanna-Barbera animated series \"Wacky Races\" and is the first television series to be directly produced by Hanna-Barbera since \"I Am Weasel\".  The show debuted on Boomerang's SVOD service in the United States, and will premiere internationally in 2017.\n\nLittle Airplane Productions: Little Airplane Productions is an American television production company, most well-known for producing preschool television programs.  Founded by Josh Selig in 1998, the company created and produced \"Wonder Pets! \" and \"Oobi\" for Nickelodeon, \"Go, Baby! \" for Playhouse Disney, and \"3rd & Bird\" for the BBC's children's channel CBeebies.\n\nMeet the Small Potatoes: Meet the Small Potatoes is a 2013 family film written and directed by Josh Selig and starring Malcolm McDowell.  It is a follow-up to Selig's television series Small Potatoes.  The film serves as both a prequel to and spinoff of the show.  The special premiered on Disney Jr. on February 15, 2013, using the voices and likenesses of real fans for the film's man on the street interviews.\n\nWonder Pets: Wonder Pets!  is an American animated children's television series.  It debuted March 3, 2006, on the Nick Jr. block of the Nickelodeon cable television network and Noggin (now Nick Jr.) on August 31, 2006.  It briefly aired on CBS as part of its Nick Jr. on CBS block until September 9, 2006.  It won an Emmy Award in 2008–2010 and 2012 for Outstanding Music Direction and Composition in the United States.\n\nSmall Potatoes (2011 TV series): Small Potatoes is a British animated series of shorts aimed at pre-school children.  It features a group of four potatoes who sing songs.  The series is written and directed by Josh Selig, creator of \"Oobi\", \"Wonder Pets\" and \"3rd & Bird\".  The \"Small Potatoes\" series is currently airing on CBeebies in the UK, ABC 4 Kids in Australia and on the Disney Junior channel in the United States.  The series was followed by a motion picture in 2013, Meet the Small Potatoes.\n\nOobi (TV series): Oobi is an American children's television series created by Josh Selig of Little Airplane Productions.  It began as a series of shorts commissioned by the Noggin network during a three-year period in which all of the channel's programming was co-produced by Nickelodeon and Sesame Workshop.  Full-length episodes of the show began airing on April 7, 2003, and the series ended its run on February 11, 2005.\n\nList of Oobi episodes: \"Oobi\" is an American children's television series created by Josh Selig.  It premiered on Nickelodeon's Noggin network during a three-year period in which the channel's programming was controlled by Viacom, Sesame Workshop, and the Jim Henson Company.  The series centers on a group of four characters represented by bare hand puppets with eyes and accessories.  The program was highly influenced by \"Sesame Street\", which Selig had worked on since its first season.  The cast of \"Oobi\" consists exclusively of Muppet performers.\n\nWe're Lalaloopsy: We're Lalaloopsy is an American animated children's television series produced by MGA Entertainment, Splash Entertainment, and Netflix.  The series is based on the \"Lalaloopsy\" dolls from MGA Entertainment, and is a spin-off of the American animated television series \"Lalaloopsy\".  It debuted on Netflix on January 10, 2017.\n\nThe Adventures of Napkin Man!: The Adventures of Napkin Man!  is a Canadian children's television series created by Tone Thyne and Josh Selig.  It premiered in 2013 on CBC Television, as part of the \"Kids' CBC\" block.It also aired on Tiny Pop in the UK.Mixing live action with animation, the series stars Yannick Bisson as Mr. Anthony, a preschool teacher who writes and illustrates stories featuring Napkin Man, a superhero figure, to teach his students how to handle difficult emotions.\n\nQuestion: Which American animated children's television series that debuted in 2006 was created by Josh Selig?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"creator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the creator of the series.\"\n    },\n    \"debut_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the series debuted.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the series originated.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the series, e.g., animated children's television series.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"creator_name\",\n    \"debut_year\",\n    \"country_of_origin\",\n    \"genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "creator_name": {
        "type": "string",
        "description": "The name of the creator of the series."
      },
      "debut_year": {
        "type": "integer",
        "description": "The year the series debuted."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the series originated."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the series, e.g., animated children's television series."
      }
    },
    "required": [
      "series_name",
      "creator_name",
      "debut_year",
      "country_of_origin",
      "genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
