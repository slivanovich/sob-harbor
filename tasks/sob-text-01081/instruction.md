{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBurton L. King: Burton L. King (August 25, 1877 – May 4, 1944) was an American film actor and director.  One of his best-known productions was \"The Lost Battalion\" (1919).\n\nSunchaser: Sunchaser (titled on-screen as The Sunchaser) is a 1996 film directed by Michael Cimino and starring Woody Harrelson, Jon Seda and Anne Bancroft.  It was director Cimino's last feature-length film.\n\nHansel and Gretel (1982 film): Hansel and Gretel is a TV special that was made in 1983 for Disney directed by Tim Burton.  It only aired once on October 31, 1983 at 10:30pm.  The only other times it was shown was as part of the Tim Burton retrospective at the Museum of Modern Art in New York City, and the Tim Burton L'Exposition at the Cinémathèque Française in Paris as part of a traveling exhibit.\n\nJoseph Cotten: Joseph Cheshire Cotten, Jr. (May 15, 1905 – February 6, 1994) was an American film, stage, radio and television actor.  Cotten achieved prominence on Broadway, starring in the original stage productions of \"The Philadelphia Story\" and \"Sabrina Fair\".  He first gained worldwide fame in three Orson Welles films: \"Citizen Kane\" (1941), \"The Magnificent Ambersons\" (1942), and \"Journey into Fear\" (1943), for which Cotten was also credited with the screenplay.  He went on to become one of the leading Hollywood actors of the 1940s, appearing in films such as \"Shadow of a Doubt\" (1943), \"Love Letters\" (1945), \"Duel in the Sun\" (1946), \"Portrait of Jennie\" (1948), \"The Third Man\" (1949) and \"Niagara\" (1953).  One of his final films was Michael Cimino's \"Heaven's Gate\" (1980).\n\nMichael Cimino: Michael Cimino ( ; February 3, 1939 – July 2, 2016) was an American film director, screenwriter, producer and author.\n\nConquering Horse: Conquering Horse is Frederick Manfred's first novel in a five-volume series he called \"The Buckskin Man Tales\".  It tells a mythic story about Indian life on the Great Plains before the arrival of white people to the region.  Academy Award winning film director Michael Cimino and producer Michael Gruskoff attempted to adapt Manfred's novel to film, but the project scrapped when his 1980 United Artists western film \"Heaven's Gate\" had become a critical and financial failure.\n\nSteven Paul: Steven Paul (born May 16, 1959) is an American film producer and manager for Jon Voight, Gene Wilder, Michael Cimino, and Bob Clark (before Clark's death in 2007).  He is also an occasional writer, director, actor, and visual effects producer.\n\nYear of the Dragon (film): Year of the Dragon is a 1985 American neo-noir action film directed by Michael Cimino, starring Mickey Rourke, Ariane Koizumi and John Lone.  The screenplay was written by Cimino and Oliver Stone and adapted from the novel by Robert Daley.\n\nPeter Bogdanovich: Peter Bogdanovich (Serbian: Петар Богдановић, \"Petar Bogdanović\", born July 30, 1939) is an American director, writer, actor, producer, critic and film historian.  He is part of the wave of \"New Hollywood\" directors, which included William Friedkin, Brian De Palma, George Lucas, Martin Scorsese, Michael Cimino and Francis Ford Coppola.  His most critically acclaimed and well-known film is the drama \"The Last Picture Show\" (1971).\n\nHeaven's Gate (film): Heaven's Gate is a 1980 American epic Western film written and directed by Michael Cimino.  Loosely based on the Johnson County War, it portrays a fictional dispute between land barons and European immigrants in Wyoming in the 1890s.  The film features an ensemble cast, including Kris Kristofferson, Christopher Walken, Isabelle Huppert, Jeff Bridges, John Hurt, Sam Waterston, Brad Dourif, Joseph Cotten, Geoffrey Lewis, David Mansfield, Richard Masur, Terry O'Quinn, Mickey Rourke, Willem Dafoe and Nicholas Woodeson, the last two in their first film roles.  It is generally considered one of the biggest box office bombs of all time, and was initially described as one of the worst films ever made.\n\nQuestion: Who was born first, Burton L. King or Michael Cimino?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person being compared.\"\n    },\n    \"person_1_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person being compared.\"\n    },\n    \"person_2_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the second person.\"\n    },\n    \"earliest_born_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born first.\"\n    },\n    \"earliest_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person who was born first.\"\n    },\n    \"comparison_result\": {\n      \"type\": \"string\",\n      \"description\": \"A statement indicating who was born first and their birth year.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_1_birth_year\",\n    \"person_2_name\",\n    \"person_2_birth_year\",\n    \"earliest_born_person_name\",\n    \"earliest_birth_year\",\n    \"comparison_result\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person being compared."
      },
      "person_1_birth_year": {
        "type": "integer",
        "description": "The birth year of the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person being compared."
      },
      "person_2_birth_year": {
        "type": "integer",
        "description": "The birth year of the second person."
      },
      "earliest_born_person_name": {
        "type": "string",
        "description": "The name of the person who was born first."
      },
      "earliest_birth_year": {
        "type": "integer",
        "description": "The birth year of the person who was born first."
      },
      "comparison_result": {
        "type": "string",
        "description": "A statement indicating who was born first and their birth year."
      }
    },
    "required": [
      "person_1_name",
      "person_1_birth_year",
      "person_2_name",
      "person_2_birth_year",
      "earliest_born_person_name",
      "earliest_birth_year",
      "comparison_result"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
