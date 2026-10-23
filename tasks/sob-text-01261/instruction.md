{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSophie Kinsella: Madeleine Sophie Wickham (née Townley; born 12 December 1969), also known under the pen name Sophie Kinsella, is an English author of chick lit.  The first two novels in her best-selling Shopaholic series, \"The Secret Dreamworld of a Shopaholic\" and \"Shopaholic Abroad\", were adapted into the film \"Confessions of a Shopaholic\" (2009).  Her books have been translated into over 30 languages.\n\nTaking Tiger Mountain by Strategy: Taking Tiger Mountain by Strategy (Chinese: 智取威虎山; pinyin: zhì qǔ wēi hǔshān) is a Peking opera, and one of the eight model plays allowed during the Chinese Cultural Revolution.  The story is based on the novel \"Lin hai xue yuan\" (林海雪原) by Qu Bo, which in turn, is based on the real-life story of an incident in 1946 during the Chinese Civil War, involving a communist reconnaissance team soldier Yang Zirong (杨子荣) who disguised himself as a bandit to infiltrate a local gang of bandits, eventually helping the main communist force to destroy the bandits.  Unlike other characters depicted in the opera and novel, most of the names of both the protagonists and the bandits are real.\n\nLiu Qingtang: Liu Qingtang (1932 - May 2, 2010)(; pinyin: Líu Qìngtáng) is a Chinese ballet dancer born in Gai County, Liaoning Province, who made a fame through his role as Hong Changqing in the ballet Red Detachment of Women of the National Ballet of China, one of the eight model plays during the Cultural Revolution.  Xue Jinghua was cast as Wu Qinghua in the same ballet.\n\nConfessions of a Shopaholic (film): Confessions of a Shopaholic is a 2009 American romantic comedy film based on the first two entries in the \"Shopaholic\" series of novels by Sophie Kinsella.  Directed by P. J. Hogan, the film stars Isla Fisher as the shopaholic journalist and Hugh Dancy as her boss.\n\nOn the Docks: On the Docks (Chinese: 海港; pinyin: hǎi gǎng) is a Chinese revolutionary opera and one of the eight model plays available during the Cultural Revolution.  Also known as The Harbor, it was the first revolutionary opera with a story about working peasants eagerly accepting the responsibility of militant struggle.  The creation of the drama was inspired by Mao Zedong's publication Talks at the Yan'an Forum on Literature and Art, whose agenda was the development of social entertainment for workers, peasants, and soldiers.  His wife Jiang Qing played a significant role in devising both the words and the music, which at times led to a power struggle with Liu Shaoqi over the opera's ideological message.  The director Xie Jin staged the original production in the early 1960s and also filmed the story in 1972.\n\nErin Wyatt: Erin Wyatt is an Ohio-born American model and actress who appeared in movies such as \"Ghosts of Girlfriends Past\", \"Confessions of a Shopaholic\", and \"\" and television shows such as \"Ugly Betty\" and \"Smash\".  In 2009, she appeared with Alec Baldwin in a commercial that aired during the Super Bowl.  Wyatt is primarily a print ad, catalog, and magazine cover model.\n\nTaking Tiger Mountain by Strategy (film): Taking Tiger Mountain by Strategy () is a Chinese film from 1970, during the height of the Cultural Revolution.  The film was directed by Xie Tieli and was based on a contemporary Beijing opera, one of the eight model plays allowed during the Cultural Revolution.  The story is based on the novel \"Lin hai xue yuan\" (林海雪原), and tells the story of an incident in 1946, during the Chinese Civil War.\n\nHugh Dancy: Hugh Michael Horace Dancy is an English actor and model.  He was born in Stoke-on-Trent, Staffordshire, England, to Sarah Ann (Birley), who works in academic publishing, and Jonathan Peter Dancy, a Philosophy professor and writer, on 19th June 1975.  He has a brother, Jack (b. 1977), and a sister, Kate (b. 1980).  He was raised in Newcastle-under-Lyme.\n\nThe Legend of the Red Lantern: The Legend of the Red Lantern () is one of the Eight model plays, the only operas and ballets permitted during the Cultural Revolution in China.  The official version was that of a Beijing Opera.  It was additionally adapted to a piano-accompanied cantata by pianist Yin Chengzong, formed by a cycle of arias extracted from the opera itself.\n\nKrysten Ritter: Krysten Alyce Ritter (born December 16, 1981) is an American actress and former model.  Ritter is known for her roles as lead superheroine Jessica Jones on the Marvel Cinematic Universe series \"Jessica Jones\" and \"The Defenders\", Jane Margolis on the AMC drama series \"Breaking Bad\", and Chloe on the ABC comedy series \"Don't Trust the B---- in Apartment 23\".  She has appeared in films such as \"What Happens in Vegas\" (2008), \"27 Dresses\" (2008), \"Confessions of a Shopaholic\" (2009), \"She's Out of My League\" (2010), \"Veronica Mars\" (2014), and \"Big Eyes\" (2014).  She has also appeared in roles \"Gravity\", \"'Til Death\", \"Veronica Mars\", and \"The Blacklist\".\n\nQuestion: Which English actor and model plays a role in Confessions of a Shopaholic?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"actor_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actor appeared in.\"\n    },\n    \"role_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The role played by the actor in the specified film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"actor_nationality\",\n    \"actor_professions\",\n    \"film_title\",\n    \"role_in_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "actor_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the actor."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actor appeared in."
      },
      "role_in_film": {
        "type": "string",
        "description": "The role played by the actor in the specified film."
      }
    },
    "required": [
      "actor_name",
      "actor_nationality",
      "actor_professions",
      "film_title",
      "role_in_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
