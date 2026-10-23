{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSome Like It Hot (album): Some Like It Hot (subtitled Modern Jazz Performances of Songs featured in the Motion Picture starring Marilyn Monroe, Tony Curtis & Jack Lemmon Produced and Directed by Billy Wilder) is an album by guitarist Barney Kessel performing adaptations music from Billy Wilder's 1959 film \"Some Like It Hot\", recorded in 1959 and released on the Contemporary label.\n\nAvanti!: Avanti!  is a 1972 American/Italian comedy film produced and directed by Billy Wilder.  The film stars Jack Lemmon and Juliet Mills.  The screenplay by Wilder and I.A.L. Diamond is based on the play of the same title by Samuel Taylor, which had a short run on Broadway in 1968.\n\nThe Front Page (1974 film): The Front Page is a 1974 American black comedy-drama film directed by Billy Wilder and starring Jack Lemmon and Walter Matthau.  The screenplay by Wilder and I.A.L. Diamond is based on Ben Hecht and Charles MacArthur's play of the same name (1928), which inspired several other films.\n\nThe Fortune Cookie: The Fortune Cookie (alternative UK title: Meet Whiplash Willie) is a 1966 black comedy film starring Jack Lemmon and Walter Matthau in their first on-screen collaboration.  It was produced and directed by Billy Wilder from a script by Wilder and I.A.L. Diamond.\n\nBilly Wilder: Samuel \"Billy\" Wilder ( ; ] ; June 22, 1906March 27, 2002) was an Austrian-American filmmaker, screenwriter, producer, artist, and journalist whose career spanned more than five decades.  He is regarded as one of the most brilliant and versatile filmmakers of Hollywood's golden age.  With \"The Apartment\", Wilder became the first person to win Academy Awards as producer, director, and screenwriter for the same film.\n\nGrumpy Old Men (film): Grumpy Old Men is a 1993 American romantic comedy-drama film starring Jack Lemmon, Walter Matthau and Ann-Margret, with Burgess Meredith, Daryl Hannah, Kevin Pollak, Ossie Davis and Buck Henry.  Directed by Donald Petrie, the screenplay was written by Mark Steven Johnson, who also wrote the sequel, \"Grumpier Old Men\" (1995).  The original music score was composed by Alan Silvestri.  This was the sixth film starring both Jack Lemmon and Walter Matthau and their first on-screen pairing since 1981's \"Buddy Buddy\" and was released on December 25, 1993.\n\nBuddy Buddy: Buddy Buddy is a 1981 American comedy film directed by Billy Wilder that stars Jack Lemmon and Walter Matthau.  The screenplay by Wilder and I.A.L. Diamond is based on the 1973 French language film \"L'emmerdeur\", which screenwriter Francis Veber had adapted from his play \"Le contrat\".\n\nJack Lemmon - A Twist of Lemmon: In the setting of his office, Jack Lemmon shares some memories of his childhood and his relationship with his father that led him to develop a certain sense of humour and, ultimately, to become a professional entertainer.  Lemmon expresses his personal mantra about film acting (“Simple is good”), and discusses some of his most important parts in Some Like it Hot and The Days of Wine and Roses.  The film also contains original interviews with Walter Matthau and Billy Wilder, and film clips from The Odd Couple (1968), Kotch (1971), Lemmon’s first directorial effort, The Front Page (1974) and the 1976 TV adaptation of The Entertainer (play).\n\nSome Like It Hot: Some Like It Hot is a 1959 American romantic comedy film set in 1929, directed and produced by Billy Wilder, starring Marilyn Monroe, Tony Curtis, and Jack Lemmon.  The supporting cast includes George Raft, Pat O'Brien, Joe E. Brown, Joan Shawlee, and Nehemiah Persoff.  The screenplay by Billy Wilder and I.A.L. Diamond is based on a screenplay by Billy Wilder and Michael Logan from the French film \"Fanfare of Love\".  The film is about two musicians who dress in drag in order to escape from mafia gangsters whom they witnessed commit a crime inspired by the Saint Valentine's Day Massacre.  The film was produced in black and white, even though color films were increasing in popularity.\n\nWalter Matthau: Walter Matthau ( ; born Walter John Matthow; October 1, 1920 – July 1, 2000) was an American actor and comedian, best known for his role as Oscar Madison in \"The Odd Couple\" and its sequel 30 years later, \"The Odd Couple II\", and his frequent collaborations with \"Odd Couple\" co-star Jack Lemmon, particularly in the '90s with \"Grumpy Old Men\" and its sequel \"Grumpier Old Men\".  He won the Academy Award for Best Supporting Actor for his performance in the 1966 Billy Wilder film \"The Fortune Cookie.\"  Besides the Oscar, he was the winner of BAFTA, Golden Globe and Tony awards.\n\nQuestion: The Fortune Cookie (alternative UK title: Meet Whiplash Willie) is a 1966 black comedy film starring Jack Lemmon and Walter Matthau in their first on-screen collaboration, It was produced and directed by Billy Wilder, Samuel \"Billy\" Wilder was an Austrian-American filmmaker, screenwriter, producer, artist, and journalist whose career spanned more than how many decades?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person being described.\"\n    },\n    \"main_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The primary profession of the person.\"\n    },\n    \"career_span_decades\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of decades the person's career spanned.\"\n    },\n    \"career_span_qualifier\": {\n      \"type\": \"string\",\n      \"description\": \"A qualifier for the career span, e.g., 'more than'.\"\n    },\n    \"notable_achievement\": {\n      \"type\": \"string\",\n      \"description\": \"A significant achievement of the person mentioned in the context.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"main_profession\",\n    \"career_span_decades\",\n    \"career_span_qualifier\",\n    \"notable_achievement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person being described."
      },
      "main_profession": {
        "type": "string",
        "description": "The primary profession of the person."
      },
      "career_span_decades": {
        "type": "integer",
        "description": "The number of decades the person's career spanned."
      },
      "career_span_qualifier": {
        "type": "string",
        "description": "A qualifier for the career span, e.g., 'more than'."
      },
      "notable_achievement": {
        "type": "string",
        "description": "A significant achievement of the person mentioned in the context."
      }
    },
    "required": [
      "person_name",
      "main_profession",
      "career_span_decades",
      "career_span_qualifier",
      "notable_achievement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
