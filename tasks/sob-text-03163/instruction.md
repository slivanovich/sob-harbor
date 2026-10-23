{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLeandro Estebecorena: Leandro Estebecorena is a Special Effects Technical Director for the company Industrial Light & Magic.  Born in Buenos Aires, Argentina, Estebecorena has been working in the film industry of the USA since 1996.  He has participated in the special effects of the films \"Transformers\", \"\", \"Mission Impossible III\" and \"Chicken Little\".  He is the principal Technical Director for the special effects of the 2008 film \"The Spiderwick Chronicles\".\n\nMore Mission: Impossible: More Mission Impossible is an album featuring music composed and conducted by Lalo Schifrin recorded in 1968 and released on the Paramount label.  As with \"\" (1967) the music on this album is rerecorded and extended scores that were originally commissioned for the TV series .\n\nMission: Impossible III (soundtrack): Mission: Impossible III – Music from the Original Motion Picture Soundtrack is a soundtrack album for the 2006 film \"\", composed by Michael Giacchino.  Unlike the previous two films in the series, there was no album released containing the film's contemporary music.\n\nJonathan Dixon (American actor): Jonathan Dixon (born October 25, 1965) is an American male television actor, best known for playing in a long series of J.J. Abrams productions such as \"Lost, Alias, Felicity, Mission Impossible III\" and \"Star Trek\" in small roles since 2003.  He is related to the English retired footballer, Lee Dixon who played for Arsenal and the English national team.\n\nStillking Films: Stillking Films is a production company based in the Czech Republic.  Its films include \"Mission Impossible Ghost Protocol\", \"Child 44\", \"Snowpiercer\" and others.  It is owned by Matthew Stillman.\n\nStephen C. Apostolof: Stephen C. Apostolof (February 25, 1928 in Burgas, Bulgaria – August 14, 2005 in Mesa, Arizona), sometimes credited under aliases A.C. Stephen(s) or Robert Lee, was a Bulgarian-American filmmaker specializing in low-budget exploitation and erotic films, who gained a cult following for a wide variety of films that range from erotic horror (\"Orgy of the Dead\") and suburban exposé (\"Suburbia Confidential\") to western-themed costume pictures (\"Lady Godiva Rides\") and \"Mission Impossible\"-type capers such as (\"Hot Ice\").  Apostolof had gained a reputation for creating high-quality mass entertainment with minimal budgets.  He was also one of the few directors to work steadily with the infamous Ed Wood and such sexploitation icons as Marsha Jordan and Rene Bond in the 1960s and 1970s.\n\nMission: Impossible III: Mission: Impossible III (stylized as M:i:III) is a 2006 American action spy film co-written and directed by J.J. Abrams in his directorial debut and starring Tom Cruise, who also served as a producer, in the role of IMF agent Ethan Hunt.  It is the third installment in the .  In the film, Ethan Hunt (Cruise) has retired from field work for the Impossible Missions Force (IMF) and trains new recruits.  However, he is sent back into action to track down the elusive arms dealer Owen Davian (Philip Seymour Hoffman).\n\nMichael Giacchino: Michael Giacchino ( ; ] ; born October 10, 1967) is an American composer of music for films, television and video games.  He composed the scores to the television series \"Lost\", \"Alias\" and \"Fringe\", the video game series \"Medal of Honor\" and \"Call of Duty\" and many films such as \"The Incredibles\", \"\", \"Ratatouille\", \"Star Trek\", \"Up\", \"Super 8\", \"\", \"Star Trek Into Darkness\", \"Dawn of the Planet of the Apes\", \"Jurassic World\", \"Inside Out\", \"Zootopia\", \"Star Trek Beyond\", \"Doctor Strange\", \"Rogue One\", \"\", \"War for the Planet of the Apes\" and \"Coco\".\n\nNick Benedict: Nick Benedict (born July 14, 1947 in Los Angeles) is an American actor.  He played the role of Curtis Reed in \"Days of Our Lives\" between 1993 and 2001.  He is the older half-brother of Samuel Benedict and the son of actor Richard Benedict.  He made his debut in 1955 in the series \"Wiretapper\" as a child.  His first performance as an adult was in \"Mike and the Mermaid\" at the age of 17.  In 1969 he appeared in the \"Mission Impossible\" TV series episode, \"The Vault\".  He appeared on The Dukes Of Hazzard, as Frank James, in the seventh-season episode Go West, Young Dukes.  In 1990 he starred alongside Nancy Allen in the TV film \"Memories of a Murder\".  In the 1990s he mainly appeared in films aside from his ongoing role in \"Days of our Lives\".  His last screen appearance was minor role in George Santo Pietro's \"Kept\" in 2001.\n\nMusic from Mission: Impossible: Music from Mission Impossible is an album featuring music composed and conducted by Lalo Schifrin recorded in 1967 and released on the Dot label.  The music on this album is rerecorded and extended scores that were originally commissioned for the TV series \"\".\n\nQuestion: Who is the American composer of music for films who composed Mission Impossible III?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the composer.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the composer.\"\n    },\n    \"profession\": {\n      \"type\": \"string\",\n      \"description\": \"The primary profession of the composer.\"\n    },\n    \"film_composed_for\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film for which the music was composed.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"composer_name\",\n    \"nationality\",\n    \"profession\",\n    \"film_composed_for\",\n    \"film_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_name": {
        "type": "string",
        "description": "The name of the composer."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the composer."
      },
      "profession": {
        "type": "string",
        "description": "The primary profession of the composer."
      },
      "film_composed_for": {
        "type": "string",
        "description": "The title of the film for which the music was composed."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "composer_name",
      "nationality",
      "profession",
      "film_composed_for",
      "film_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
