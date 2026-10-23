{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Conspiracy of Friends: A Conspiracy of Friends is the third online novel by Alexander McCall Smith, author of the The No. 1 Ladies' Detective Agency series.  In the first series, the author wrote a chapter a day, starting from 15 September 2008, and the series ran for 20 weeks, totalling 100 episodes.  The daily chapters, read by Andrew Sachs, were also available as an audio download.\n\nThe Dog Who Came in from the Cold: The Dog Who Came in from the Cold is the second online novel by Alexander McCall Smith, author of the The No. 1 Ladies' Detective Agency series.  In the first series, the author wrote a chapter a day, starting on 15 Sep 2008, the series running for 20 weeks and totalling 100 episodes.  The daily chapters, read by Andrew Sachs were also available as an audio download.\n\nMr. Brownlow: Mr. Brownlow is a character from the novel \"Oliver Twist\" by Charles Dickens.  A bookish and kindly middle-aged bachelor, he helps Oliver to escape the clutches of Fagin.  He later adopts Oliver Twist by the end of the novel.\n\nHenry Stephenson: Henry Stephenson (16 April 1871 – 24 April 1956) was a British stage and film actor.  He portrayed friendly and wise gentlemen in many films of the 1930s and 1940s.  Among his roles were Sir Joseph Banks in \"Mutiny on the Bounty\" (1935) and Mr. Brownlow in \"Oliver Twist\" (1948).\n\nCorduroy Mansions: Corduroy Mansions is the first online novel by Alexander McCall Smith, author of the The No. 1 Ladies' Detective Agency series.  In the first series, the author wrote a chapter a day, starting on 15 Sep 2008, the series running for 20 weeks and totalling 100 episodes.  The daily chapters, read by Andrew Sachs were also available as an audio download.\n\nOliver Twist: Oliver Twist, or The Parish Boy's Progress, is the second novel by English author Charles Dickens and was first published as a serial 1837–39.  The story is of the orphan Oliver Twist, who is born in a workhouse and is then sold into apprenticeship with an undertaker.  He escapes from there and travels to London, where he meets the Artful Dodger, a member of a gang of juvenile pickpockets led by the elderly criminal, Fagin.\n\nSin Pit: Sin Pit is a crime novel by American journalist Paul S. Meskil (Jul 2, 1923–Oct 11, 2005), published by Lion Books in 1954.  It is one of those rare paperback originals that has achieved cult status through a combination of circumstances, including the fact the author wrote only one work of crime fiction, the initial print run was relatively low for paperbacks at the time, the book had only one print run by the original publisher (Lion Books) and, finally, found an audience years later among collectors of 1950s paperback crime novels.  Sin Pit shares all the above circumstances with another paperback crime novel published a year earlier, in 1953, that similarly achieved cult status — Black Wings Has My Angel by Elliott Chaze, published by Fawcett Gold Medal.  Both authors were respected journalists their entire lives and wrote only a single crime novel that was never republished until years later, only after gaining an audience among aficionados of pulp fiction.\n\nMyōjin Yahiko: Myōjin Yahiko (明神 弥彦 ) , known as Yahiko Myojin in the Media Blasters English-language dub and Yoshi Myojin in the English Sony \"Samurai X\" dub, is a fictional character from the \"Rurouni Kenshin\" manga and anime series authored by Nobuhiro Watsuki.  The character of Yahiko is based on the author's childhood experiences practicing kendo; since Watsuki's experienced frustration during kendo classes, the author wrote Yahiko as experiencing frustration with his kendo skills.  Watsuki liked Yahiko, and while writing the manga, he began to develop the character so that readers would enjoy him.\n\nThe New Centurions (novel): The New Centurions, written by Joseph Wambaugh, is a 1971 novel depicting the stresses of police work in Los Angeles, California in the early 1960s.  The author wrote the novel, his first, while a working member of the Los Angeles Police Department.  The novel became a film starring George C. Scott and Stacy Keach.\n\nBottom's Dream: Bottom's Dream (German: \"Zettels Traum\" or \"ZETTEL’S TRAUM\" as the author wrote the title) is a novel published in 1970 by West German author Arno Schmidt.  Schmidt began writing the novel in December 1963 while he and Hans Wollschläger began to translate the works of Edgar Allan Poe into German.  The novel was inspired by James Joyce's novel \"Finnegans Wake\", particularly Schmidt's use of columns (his \"SpaltenTechnik\"), which Schmidt claimed was borrowed from the \"Wake\".\n\nQuestion: Which author wrote the novel which Mr. Brownlow is a character in \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character.\"\n    },\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel the character appears in.\"\n    },\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author who wrote the novel.\"\n    },\n    \"character_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the character's role or traits.\"\n    }\n  },\n  \"required\": [\n    \"character_name\",\n    \"novel_title\",\n    \"author_name\",\n    \"character_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character_name": {
        "type": "string",
        "description": "The name of the character."
      },
      "novel_title": {
        "type": "string",
        "description": "The title of the novel the character appears in."
      },
      "author_name": {
        "type": "string",
        "description": "The name of the author who wrote the novel."
      },
      "character_description": {
        "type": "string",
        "description": "A brief description of the character's role or traits."
      }
    },
    "required": [
      "character_name",
      "novel_title",
      "author_name",
      "character_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
