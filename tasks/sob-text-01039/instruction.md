{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Optimists of Nine Elms: The Optimists of Nine Elms, also known as The Optimists, is a 1973 British drama film starring Peter Sellers and directed by Anthony Simmons, who also wrote the 1964 novel upon which the film is based.  The film is about an old street musician (played by Sellers) who strikes up a friendship with two children - Liz, played by Donna Mullane, and her young brother Mark, played by John Chaffey.  Neither of the child actors were featured in future films.  A young Keith Chegwin also played a small role in the film.\n\nCurse of the Pink Panther: Curse of the Pink Panther is a 1983 British comedy film and a continuation of \"The Pink Panther\" series of films started by Blake Edwards in the early 1960s.  The film was one of two produced concurrently following the death of the series' star Peter Sellers.  Whereas the previous film \"Trail of the Pink Panther\" made use of unused footage of Sellers as Inspector Clouseau, \"Curse\" attempted to relaunch the series with a new lead, Ted Wass, as bumbling American detective Clifton Sleigh, assigned to find the missing Inspector Clouseau.\n\nTrail of the Pink Panther: Trail of the Pink Panther is a 1982 British comedy film starring Peter Sellers for the sixth and final time.  It was the seventh film in \"The Pink Panther\" series, the first film in the series following Sellers' death and also the last in which he appeared as Inspector Clouseau.  Sellers died before production began.  His performance consists only of deleted scenes from previous films.\n\nNever Let Go: Never Let Go is a 1960 British thriller film starring Richard Todd, Peter Sellers, and Elizabeth Sellars.  It concerns a man's attempt to recover his stolen Ford Anglia car.  Sellers played a London villain, in one of his rare straight roles.\n\nThe Life and Death of Peter Sellers: The Life and Death of Peter Sellers is a 2004 British-American television film about the life of English comedian Peter Sellers, based on Roger Lewis's book of the same name.  It was directed by Stephen Hopkins and stars Geoffrey Rush as Sellers, Miriam Margolyes as his mother Peg Sellers, Emily Watson as his first wife Anne Howe, Charlize Theron as his second wife Britt Ekland, John Lithgow as Blake Edwards, Stephen Fry as Maurice Woodruff and Stanley Tucci as Stanley Kubrick.\n\nThe Fiendish Plot of Dr. Fu Manchu: The Fiendish Plot of Dr. Fu Manchu is a 1980 comedy film, primarily notable as the final film of Peter Sellers, David Tomlinson and John Le Mesurier.  Pre-production began with Richard Quine as director.  By the time the film entered production, Piers Haggard had replaced him.  Peter Sellers handled the re-shoots himself.  Based on characters created by Sax Rohmer, the film stars Sellers in the dual role of Fu Manchu, a stereotypical Chinese evil genius, and English country gentleman detective Nayland Smith.  Released only two weeks after Sellers death, the film was a commercial and critical failure.  It was also the final screen appearance for Tomlinson, who retired from acting shortly before its release.\n\nPeter Sellers: Peter Sellers, CBE (born Richard Henry Sellers; 8 September 1925 – 24 July 1980) was an English film actor, comedian and singer.  He performed in the BBC Radio comedy series \"The Goon Show\", featured on a number of hit comic songs and became known to a worldwide audience through his many film characterisations, among them Chief Inspector Clouseau in \"The Pink Panther\" series of films.\n\nGhost in the Noonday Sun: Ghost in the Noonday Sun is a 1973 British comedy film directed by Peter Medak starring Peter Sellers, Anthony Franciosa and Spike Milligan.  The film suffered a notoriously difficult production due to Sellers's erratic behavior and was never released in cinemas.  Medak described the film as \"the biggest disaster of my life”.\n\nCharlize Theron filmography: Charlize Theron is a South African-born American actress who made her film debut in an uncredited role as a follower of a cult in the 1995 horror film \"\".  Theron followed this with appearances as a hitwoman in \"2 Days in the Valley\", a waitress in the romantic comedy \"Trial and Error\" (1997), and a woman suffering with schizophrenia in the mystery thriller \"The Devil's Advocate\" (1997) with Keanu Reeves and Al Pacino.  She appeared in the science fiction thriller \"The Astronaut's Wife\" with Johnny Depp, and Lasse Hallström's \"The Cider House Rules\" (both in 1999).  For her portrayal of serial killer Aileen Wuornos in the crime drama \"Monster\" (2003), Theron received the Academy Award for Best Actress, the Golden Globe Award for Best Actress in a Motion Picture – Drama, and the Screen Actors Guild Award for Outstanding Performance by a Female Actor in a Leading Role.  The following year, she played Swedish entertainer Britt Ekland in the biographical film \"The Life and Death of Peter Sellers\".\n\nMiriam Margolyes: Miriam Margolyes, {'1': \", '2': \", '3': \", '4': \"} ( ; born 18 May 1941) is an English character actress and voice artist.  Her earliest roles were in theatre and after several supporting roles in film and television she won a BAFTA Award for her role in \"The Age of Innocence\" (1993) and went on to take the role of Professor Sprout in the \"Harry Potter\" film series.\n\nQuestion: The actress who played peg in  The Life and Death of Peter Sellers was born in which year ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who played the character.\"\n    },\n    \"actress_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actress.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"character_name\",\n    \"actress_name\",\n    \"actress_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actress."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who played the character."
      },
      "actress_birth_year": {
        "type": "integer",
        "description": "The birth year of the actress."
      }
    },
    "required": [
      "film_title",
      "character_name",
      "actress_name",
      "actress_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
