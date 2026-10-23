{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1999 in film: The year 1999 in film included Stanley Kubrick's final film \"Eyes Wide Shut\", Pedro Almodóvar's first Oscar-winning film \"All About My Mother\", the science-fiction hit \"The Matrix\", the Deep Canvas-pioneering Disney animated feature \"Tarzan\" and Best Picture-winner \"American Beauty\" and the well-received \"The Green Mile\", as well as the animated works \"The Iron Giant\", \"Toy Story 2\", \"Stuart Little\" and \"\".  Other noteworthy releases included Spike Jonze's and Charlie Kaufman's breakout film \"Being John Malkovich\" and M. Night Shyamalan's breakout film \"The Sixth Sense\", the controversial \"Fight Club\" and Paul Thomas Anderson's \"Magnolia\".  The year also featured George Lucas' top-grossing \"\".\n\nEternal Sunshine of the Spotless Mind: Eternal Sunshine of the Spotless Mind is a 2004 American romantic science fiction comedy-drama film written by Charlie Kaufman and directed by Michel Gondry.  It follows an estranged couple who have erased each other from their memories, then, started dating again.  Pierre Bismuth created the story with Kaufman and Gondry.  The ensemble cast includes Jim Carrey, Kate Winslet, Kirsten Dunst, Mark Ruffalo, Elijah Wood and Tom Wilkinson.  The title of the film is a quotation from \"Eloisa to Abelard\" by Alexander Pope.\n\nSynecdoche, New York: Synecdoche, New York is a 2008 American postmodern drama film written and directed by Charlie Kaufman, and starring Philip Seymour Hoffman.  It is Kaufman's directorial debut.\n\nPierre Bismuth: Pierre Bismuth (6 June 1963) is a French artist and filmmaker based in Brussels.  His practice can be placed in the tradition of conceptual art and appropriation art.  His work uses a variety of media and materials, including painting, sculpture, collage, video, architecture, performance, music, and film.  He is best known for being among the authors of the story for \"Eternal Sunshine of the Spotless Mind\" (2004), for which he won an Academy Award for Best Original Screenplay in 2005 alongside Michel Gondry and Charlie Kaufman.  Bismuth made his directorial debut with the 2016 feature film \"Where is Rocky II?\" .\n\nAnomalisa: Anomalisa is a 2015 American adult stop-motion animated comedy-drama film directed and produced by Charlie Kaufman and Duke Johnson, based on Kaufman's 2005 play \"Anomalisa\".  It was released on 30 December 2015, by Paramount Pictures.  The film follows a lonely customer service expert (voiced by David Thewlis) who perceives everyone (Tom Noonan) as identical until he meets a unique woman (Jennifer Jason Leigh) in a Cincinnati hotel.\n\nConfessions of a Dangerous Mind: Confessions of a Dangerous Mind is a 2002 biographical spy comedy film depicting the life of popular game show host and producer Chuck Barris, who claimed to have also been an assassin for the CIA.  The film was George Clooney's directorial debut, was written by Charlie Kaufman, and starred Sam Rockwell, Julia Roberts, Drew Barrymore, and Clooney.\n\nBeing John Malkovich: Being John Malkovich is a 1999 American fantasy-comedy film directed by Spike Jonze and written by Charlie Kaufman, both making their feature film debut.  The film stars John Cusack, Cameron Diaz, and Catherine Keener, with John Malkovich and Charlie Sheen as themselves.  The film follows a puppeteer who finds a portal that leads into Malkovich's mind.\n\nMythgardia: Mythgardia is a fantasy boardgame designed by Bob Harris.  It is a follow-up to his best selling and widely acclaimed fantasy adventure game, Talisman.\n\nAdaptation (film): Adaptation (stylized as Adaptation.)  is a 2002 American comedy-drama metafilm directed by Spike Jonze and written by Charlie Kaufman.  The film is based on Susan Orlean's non-fiction book \"The Orchid Thief\", with numerous self-referential events added.  The film stars Nicolas Cage as Charlie and Donald Kaufman, and Meryl Streep as Susan Orlean, Chris Cooper as John Laroche, with Cara Seymour, Brian Cox, Tilda Swinton, Ron Livingston, and Maggie Gyllenhaal in supporting roles.\n\nCharlie Kaufman: Charles Stuart Kaufman (born November 19, 1958) is an American screenwriter, producer, director, and lyricist.  He wrote the films \"Being John Malkovich\" (1999), \"Adaptation\" (2002), and \"Eternal Sunshine of the Spotless Mind\" (2004).  He made his directorial debut with \"Synecdoche, New York\" (2008), which was also well-received; film critic Roger Ebert named it \"the best movie of the decade\" in 2009.  It was followed by \"Anomalisa\" (2015).\n\nQuestion: Charlie Kaufman wrote which acclaimed fantasy film in 1999 journeying into an actor's mind?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the film.\"\n    },\n    \"writer\": {\n      \"type\": \"string\",\n      \"description\": \"The main writer of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"plot_summary_key_element\": {\n      \"type\": \"string\",\n      \"description\": \"A key element of the plot related to the question, specifically the journey into an actor's mind.\"\n    },\n    \"acclaim_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the film's acclaim or significance.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"writer\",\n    \"director\",\n    \"plot_summary_key_element\",\n    \"acclaim_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "genre": {
        "type": "string",
        "description": "The primary genre of the film."
      },
      "writer": {
        "type": "string",
        "description": "The main writer of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "plot_summary_key_element": {
        "type": "string",
        "description": "A key element of the plot related to the question, specifically the journey into an actor's mind."
      },
      "acclaim_description": {
        "type": "string",
        "description": "Description of the film's acclaim or significance."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "writer",
      "director",
      "plot_summary_key_element",
      "acclaim_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
