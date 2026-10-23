{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nClear and Present Danger (film): Clear and Present Danger is a 1994 American spy thriller film directed by Phillip Noyce and based on Tom Clancy's novel of the same name.  It was preceded by the 1990 film \"The Hunt for Red October\" and the 1992 film \"Patriot Games\", all three featuring Clancy's character Jack Ryan.  It is the last film version of Clancy's novels to feature Harrison Ford as Ryan and James Earl Jones as Vice Admiral James Greer, as well as the final installment directed by Noyce.\n\nNewsfront: Newsfront is a 1978 Australian drama film starring Bill Hunter, Wendy Hughes, Chris Haywood and Bryan Brown, directed by Phillip Noyce.  The screenplay is written by David Elfick, Bob Ellis, Philippe Mora, and Phillip Noyce.  The original music score is composed by William Motzing.  This film was shot on location in Sydney, New South Wales, Australia.  Incorporating much actual newsreel footage, the film is shot in both black and white and colour.\n\nDead Calm (film): Dead Calm is a 1989 Australian psychological thriller film starring Sam Neill, Nicole Kidman and Billy Zane.  It was based on the 1963 novel of the same name by Charles Williams.  The film was directed by Australian filmmaker Phillip Noyce and filmed around the Great Barrier Reef.  Cinematography by Dean Semler and score composed by Graeme Revell.\n\nCatch a Fire (film): Catch a Fire is a 2006 biographical thriller film about activists against apartheid in South Africa.  The film was directed by Phillip Noyce, from a screenplay written by Shawn Slovo.  Slovo's father, Joe Slovo, and mother Ruth First, leaders of the South African Communist Party and activists in the Anti-Apartheid Movement, appear as characters in the film, while her sister, Robyn Slovo, is one of the film's producers and also plays their mother Ruth First.  \"Catch a Fire\" was shot on location in South Africa, Swaziland and Mozambique.\n\nSliver (film): Sliver is a 1993 erotic thriller film based on the Ira Levin novel of the same name about the mysterious occurrences in a privately owned New York high-rise apartment building.  Phillip Noyce directed the film, from a screenplay by Joe Eszterhas.  Because of a major battle with the MPAA (which originally gave the film an NC-17 rating), the filmmakers were forced to make extensive reshoots before release.  These reshoots actually necessitated changing the killer's identity.  The film stars Sharon Stone, William Baldwin and Tom Berenger.\n\nRobert Rehme: Robert Rehme (born 5 May 1935 in Cincinnati, Ohio) is an American film producer whose credits include the films \"Patriot Games\", \"Clear and Present Danger\" and \"The General's Daughter\".  His first major job involving motion pictures was president of Avco Embassy Pictures in 1978, a post he held until 1981.  In 1983, he became co-chairman and chief executive officer of New World Entertainment, Inc until 1989, when he and producer Mace Neufeld co-founded the motion picture production company Neufeld/Rehme Productions.  It was during this time that he created the pictures for which he is most known, such as \"Patriot Games\" and \"Flight of the Intruder\".  Rehme served as President of the Academy of Motion Picture Arts and Sciences twice, between 1992–1993 and 1997–2001.\n\nThe Bone Collector: The Bone Collector is a 1999 psychological thriller film starring Denzel Washington and Angelina Jolie, directed by Phillip Noyce and produced by Martin Bregman.\n\nSalt (2010 film): Salt is a 2010 American action thriller film directed by Phillip Noyce, written by Kurt Wimmer, and starring Angelina Jolie, Liev Schreiber, Daniel Olbrychski, August Diehl, and Chiwetel Ejiofor.  Jolie plays Evelyn Salt, who is accused of being a Russian sleeper agent and goes on the run to try to clear her name.\n\nPatriot Games (film): Patriot Games is a 1992 American spy thriller film directed by Phillip Noyce and based on Tom Clancy's novel of the same name.  It is a sequel to the 1990 film \"The Hunt for Red October\", but with different actors in the leading roles, Harrison Ford starring as Jack Ryan and Anne Archer as his wife.  James Earl Jones is the lone holdover, reprising his role as Admiral James Greer.  The cast also includes Sean Bean, Patrick Bergin, Thora Birch, Samuel L. Jackson, James Fox, and Richard Harris.\n\nBackroads (film): Backroads is a 1977 Australian film directed by Phillip Noyce.  Two strangers – one white (Jack), one black (Gary) – steal a car in western New South Wales and drive around the coast.  The original characters came from a story by Adelaide writer John Emery, with whom Noyce had worked on a short film.  Australian reviews of the film were mixed, and it opened commercially in only one cinema.\n\nQuestion: Which 1992 American spy thriller film directed by Phillip Noyce did Robert Rehme produce?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"producer\": {\n      \"type\": \"string\",\n      \"description\": \"The producer of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"producer\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "producer": {
        "type": "string",
        "description": "The producer of the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "producer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
