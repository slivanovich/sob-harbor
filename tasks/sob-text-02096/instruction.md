{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoberts Blossom: Roberts Scott Blossom (March 25, 1924July 8, 2011) was an American theatre, film and television character actor, and poet.  He was best known for his roles as Old Man Marley in \"Home Alone\" (1990) and as Ezra Cobb in the horror film \"Deranged\" (1974).  He is also remembered for his supporting roles in films such as \"The Great Gatsby\" (1974), \"Close Encounters of the Third Kind\" (1977), \"Escape from Alcatraz\" (1979), \"Christine\" (1983), and \"The Last Temptation of Christ\" (1988).\n\nThe Great Gatsby (1974 film): The Great Gatsby is a 1974 American romantic drama film based on F. Scott Fitzgerald's 1925 novel of the same name.  It was directed by Jack Clayton and produced by David Merrick from a screenplay by Francis Ford Coppola.  The film stars Robert Redford in the title role of Jay Gatsby, along with Mia Farrow, Sam Waterston, Bruce Dern, Karen Black, Scott Wilson and Lois Chiles, with Howard Da Silva (who previously appeared in the 1949 version), Roberts Blossom and Edward Herrmann.\n\nCarpenter's Station, Kentucky: Carpenter's Station, Kentucky, originally \"Carpenter's Fort\", was established about 2 mi west of present-day Hustonville, Kentucky, by three Carpenter brothers, George Carpenter, John Carpenter, and Adam Carpenter, who came to the site from Rockingham County, Virginia, in the summer of 1779.  The brothers were of Germanic descent, sons of George Zimmerman (which Anglicizes to Carpenter), who was born c. 1720 in Switzerland, emigrated to Pennsylvania colony around 1740, and settled in Rockingham County, Virginia, before the American Revolutionary War.\n\nZophar Carpenter's Fort: Carpenter's Fort on McKenzie's Fork of Paint Lick Creek in Kentucky was established by Zophar Carpenter, a native of New York colony who migrated to western Virginia in the 1750s and to Kentucky about 1788.  The fort is also referred to as Zophar Carpenter's Station, and placed \"near Suck Fork Creek\".  Zophar Carpenter served as a drummer in Captain Dickenson's Company of Virginia Rangers in the French & Indian War.  He appeared on a 1792 tax list in Madison Co.  KY with Edward Carpenter and John Carpenter.  He died on February 6, 1798 at age 65 and is interred in the Carpenter Graveyard near Paint Lick, Garrard County, Kentucky.\n\nReuben, Reuben: Reuben, Reuben is a 1983 comedy-drama film directed by Robert Ellis Miller and starring Tom Conti, Kelly McGillis (in her film debut), Roberts Blossom, Cynthia Harris, and Joel Fabiani.\n\nDoc Hollywood: Doc Hollywood is a 1991 American romantic comedy film directed by Michael Caton-Jones, and written by Jeffrey Price and Peter S. Seaman, based on Neil B. Shulman's book, \"What?  Dead...Again?\" .  The film stars Michael J. Fox, Julie Warner, and Woody Harrelson, with Bridget Fonda, David Ogden Stiers, Frances Sternhagen, Roberts Blossom, and Barnard Hughes appearing in supporting roles.\n\nResurrection (1980 film): Resurrection is a 1980 film which tells the story of a woman who survives the car accident which kills her husband, but discovers that she has the power to heal other people.  She becomes an unwitting celebrity, the hope of those in desperate need of healing, and a lightning rod for religious beliefs and skeptics.  The film stars Ellen Burstyn, Sam Shepard, Richard Farnsworth, Roberts Blossom and Eva Le Gallienne.\n\nIn the Mouth of Madness: In the Mouth of Madness (also known as John Carpenter's In the Mouth of Madness) is a 1994 American psychological Lovecraftian horror film directed and scored by John Carpenter and written by Michael De Luca.  It stars Sam Neill, Julie Carmen, Jürgen Prochnow, David Warner and Charlton Heston.  Informally, the film is the third installment in Carpenter's \"Apocalypse Trilogy\", preceded by \"The Thing\" and \"Prince of Darkness\".\n\nLise Hilboldt: Lise Hilboldt (born January 7, 1954) is an American actress.  She had a leading role in the romantic comedy film \"Sweet Liberty\" (1986), co-starring with writer-director Alan Alda and Michael Caine, and also was featured in \"Noon Wine\" (1985), together with Fred Ward, Stellan Skarsgård, Roberts Blossom and Pat Hingle.\n\nChristine (1983 film): Christine is a 1983 American horror film directed by John Carpenter and starring Keith Gordon, John Stockwell, Alexandra Paul, and Harry Dean Stanton.  The film also features supporting performances from Roberts Blossom and Kelly Preston.  Written by Bill Phillips and based on the novel of the same name by Stephen King, the plot follows a sentient and violent vintage Plymouth Fury named Christine, and its effects on the car's new teenage owner.\n\nQuestion: Which of the movie which Roberts Blossom has a supporting role is directed by John Carpenter? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the movie.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who had a role in the movie.\"\n    },\n    \"role_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of role the actor had in the movie (e.g., 'supporting', 'starring').\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the movie was released.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"director\",\n    \"actor_name\",\n    \"role_type\",\n    \"release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "director": {
        "type": "string",
        "description": "The director of the movie."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who had a role in the movie."
      },
      "role_type": {
        "type": "string",
        "description": "The type of role the actor had in the movie (e.g., 'supporting', 'starring')."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the movie was released."
      }
    },
    "required": [
      "movie_title",
      "director",
      "actor_name",
      "role_type",
      "release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
