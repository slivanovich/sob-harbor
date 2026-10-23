{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNathaniel Starbuck: Nathaniel Starbuck is a fictional character, Confederate soldier, and the protagonist of British author Bernard Cornwell's (b. 1944), \"\"Starbuck Chronicles\"\" series of novels of historical fiction.  Cornwell is also author of several other series of historical fiction such as the \"Richard Sharpe\" novels of the British campaigns in the Peninsular War in Spain during the Napoleonic Wars of the early 19th Century.\n\nSharpe's Christmas: Sharpe's Christmas, is a short story by historical fiction author Bernard Cornwell.  It features Cornwell's fictional hero Richard Sharpe.  It was originally written for British newspaper \"The Daily Mail\" which serialised it during the Christmas season of 1994.  An extended version was published by The Sharpe Appreciation Society in a short story collection of the same name in 2003 to raise funds for The Bernard and Judy Cornwell Foundation.\n\nSharpe's Peril: Sharpe's Peril is a British TV film from 2008, usually shown in two parts, which is part of an ITV series based on Bernard Cornwell's historical fiction novels about the English soldier Richard Sharpe during the Napoleonic Wars.  Contrary to most parts of the TV series, \"Sharpe's Peril\" isn't based on one of Cornwell's novels.  Both are set in 1817, two years after Sharpe has retired as a farmer in Normandy, so chronologically they come after \"Sharpe's Waterloo\" (1815) and before the final novel \"Sharpe's Devil\" (1820–21).  In \"Sharpe's Challenge\" and \"Sharpe's Peril\", Sharpe and his comrade in arms, Patrick Harper, have been temporarily called out of retirement and asked to go to India.\n\nThe Fort (novel): The Fort is a historical novel written by Bernard Cornwell.  The book relates to the events of the Penobscot Expedition of 1779 during the American Revolutionary War.  While centred on the efforts of a regiment of Scots to establish and hold the fort against superior numbers of American revolutionaries, it contrasts the actions of two military icons: John Moore (later Sir John), a young officer who later laid the foundations of the light infantry doctrine used by the 95th Rifles and others against the French in the Revolutionary and Napoleonic Wars; and Paul Revere, hero of Longfellow's poem written two generations later but, according to Cornwell's research, an insubordinate, unreliable and probably dishonest character who was a major factor in the defeat of the Americans.\n\nSharpe's Ransom: Sharpe's Christmas contains two short stories, \"Sharpe's Christmas\" and \"Sharpe's Ransom\", written by historical fiction author Bernard Cornwell.  They feature Cornwell's fictional hero Richard Sharpe.  Originally, the first short-story, \"Sharpe's Christmas\", was written for British newspaper \"The Daily Mail\" which serialised it during the Christmas season of 1995.  Later, in an effort to raise funds for The Bernard and Judy Cornwell Foundation, an extended version was published by The Sharpe Appreciation Society in 2003 to add \"Sharpe's Ransom\" into a collection of the two short stories simply titled Sharpe's Christmas.\n\nSharpe's Challenge: Sharpe's Challenge is a British TV film from 2006, usually shown in two parts, which is part of an ITV series based on Bernard Cornwell's historical fiction novels about the English soldier Richard Sharpe during the Napoleonic Wars.  Contrary to most parts of the TV series, \"Sharpe's Challenge\", as well as the follow-up \"Sharpe's Peril\", isn't based entirely on one of Cornwell's novels, but it uses and adapts some characters and storylines from \"Sharpe's Tiger\".  Both are set in 1817, two years after Sharpe has retired as a farmer in Normandy, so chronologically they come after \"Sharpe's Waterloo\" (1815) and before the final novel \"Sharpe's Devil\" (1820–21).  Some of the events in the film are, however, inspired by events in the first three novels of the series.  In \"Sharpe's Challenge\" and \"Sharpe's Peril\", Sharpe and his comrade in arms, Patrick Harper, have been temporarily called out of retirement and asked to go to India.\n\nBernard Cornwell: Bernard Cornwell, OBE (born 23 February 1944) is an English author of historical novels and a history of the Waterloo Campaign.  He is best known for his novels about Napoleonic Wars rifleman Richard Sharpe.  Cornwell has written historical novels primarily of English history in five series and one series of contemporary thriller novels.  A feature of his historical novels is an end note on how the novel matches or differs from history, for the re-telling, and what one might see at the modern site of the battles described in the novel.  One series of historical novels is set in the American Civil War.  He wrote a nonfiction book on the battle of Waterloo, in addition to the fictional story of the famous battle in the Sharpe Series.  Two of the historical novel series have been adapted for television; the Sharpe television series by ITV and \"The Last Kingdom\" by BBC.  He lives in the US with his wife.  He alternates between Cape Cod, Massachusetts and Charleston, South Carolina.\n\nList of Sharpe series characters: Sharpe is a series of historical fiction stories by Bernard Cornwell centred on the character of Richard Sharpe.  Cornwell's series (composed of several novels and short stories) charts Sharpe's progress in the British Army during the Napoleonic Wars.\n\nAnne Perry: Anne Perry (born 28 October 1938 as Juliet Marion Hulme) is an English author of historical detective fiction, best known for her Thomas Pitt and William Monk series.  At the age of fifteen she was convicted of participating in the murder of her friend's mother, in 1954.  She changed her name after serving her five-year sentence.\n\nSharpe's Christmas (story collection): Sharpe's Christmas, is a short story collection by historical fiction author Bernard Cornwell which he began conceptualising in 1980s.  It contains two stories featuring Cornwell's fictional hero Richard Sharpe.  It was published by The Sharpe Appreciation Society in 2003 in order to raise funds for The Bernard and Judy Cornwell Foundation.  This novel contains two stories that take place at different times, thus in an interview with the author, the book was left unnumbered in the Sharpe’s series.\n\nQuestion: What profession does Anne Perry and Bernard Cornwell have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession shared by both individuals.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"List of individuals sharing the profession.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"specific_genre\": {\n            \"type\": \"string\",\n            \"description\": \"The specific genre of fiction they write, if mentioned.\"\n          }\n        },\n        \"required\": [\n          \"name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"profession_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of individuals sharing this profession.\"\n    }\n  },\n  \"required\": [\n    \"common_profession\",\n    \"individuals\",\n    \"profession_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_profession": {
        "type": "string",
        "description": "The profession shared by both individuals."
      },
      "individuals": {
        "type": "array",
        "description": "List of individuals sharing the profession.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "specific_genre": {
              "type": "string",
              "description": "The specific genre of fiction they write, if mentioned."
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        }
      },
      "profession_count": {
        "type": "integer",
        "description": "The number of individuals sharing this profession."
      }
    },
    "required": [
      "common_profession",
      "individuals",
      "profession_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
