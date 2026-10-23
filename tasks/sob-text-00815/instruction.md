{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRosewood, Pennsylvania: Rosewood is the fictional setting for both the \"Pretty Little Liars\" book series and the \"Pretty Little Liars\" television series.  The fictional city is suggested to be loosely based on Rosemont, Pennsylvania.\n\nMary Drake: Mary Drake is a fictional character created by I. Marlene King and portrayed by Andrea Parker in the American television series \"Pretty Little Liars\".  \"Pretty Little Liars\" is a television adaptation of the novel series of the same name written by Sara Shepard, in which the antagonist Alison DiLaurentis has an identical twin sister, Courtney DiLaurentis.  It is believed that Mary is the on-screen counterpart of Courtney, though her recent characterization is more in line with Alison.  The character makes her first official introduction during the sixth-season finale \"Hush, Hush, Sweet Liars\".  The Liars discover that Mary is Jessica DiLaurentis' identical twin sister, a former patient at Radley Sanitarium who is Charlotte's biological mother.  In \"The DArkest Knight\", Drake is also revealed to be Spencer Hastings' biological mother.  During \"Till Death Do Us Part\", the elusive A.D. is revealed to be Alex Drake, Spencer's younger identical twin sister.  Alex believed the Liars knew who was accountable for Charlotte's murder and was also set on physically replacing Spencer due to being jealous of the life that she had.\n\nAeriél Miranda: Aeriél Christine Miranda (born April 3, 1992) is an American actress.  She is best known for her recurring role as Shana Fring on the ABC Family series, \"Pretty Little Liars\" (2013–2014).  She was first introduced as Shana on the \"Pretty Little Liars\" web series, \"Pretty Dirty Secrets\", prior to appearing on \"Pretty Little Liars\".  Miranda also had a recurring role as Lana on the ABC Family series \"The Nine Lives of Chloe King\" (2011).\n\nShay Mitchell: Shannon Ashley \"Shay\" Mitchell (born April 10, 1987) is a Canadian actress, model, entrepreneur and author.  She is best known for her role as Emily Fields in the Freeform series \"Pretty Little Liars\".\n\nCharlotte Drake: Charlotte Drake is a fictional character in \"Pretty Little Liars\", an American mystery drama television series based on the homonymous novel series written by Sara Shepard.  Charlotte is a character that only appears in the television series and is portrayed by Vanessa Ray.  The character is also featured in the \"Pretty Little Liars\" spin-off \"Pretty Dirty Secrets\".\n\nChoose or Lose: \"Choose or Lose\" is the eighteenth episode of the seventh season of \"Pretty Little Liars\", and the show's 158th episode overall, which premiered on the Freeform network in the United States on June 13, 2017.  The episode was directed by Norman Buckley and written by Charlie Craig.  In this episode, the Liars finally discover that Aria (Lucy Hale) has been working with 'A.D.' after Mona (Janel Parrish) investigated on Aria.  Lieutenant Tanner (Roma Maffia) returns to Rosewood to work on the Dunhill's homicide case, quickly targeting the Liars on her radar.  Caleb (Tyler Blackburn) and Hanna (Ashley Benson) secretly marry, while Alison (Sasha Pieterse) and Emily (Shay Mitchell) step forward with their relationship.\n\nRavenswood (TV series): Ravenswood was an American supernatural teen drama, mystery-thriller television series created by I. Marlene King, Oliver Goldstick and Joseph Dougherty.  A first spin-off of \"Pretty Little Liars\", ABC Family green lit the series on March 26, 2013.  It premiered on October 22, 2013, following the \"Pretty Little Liars\" Halloween episode.  The series began filming on August 21, 2013, in New Orleans, Louisiana.\n\nPretty Little Liars: The Perfectionists: Pretty Little Liars: The Perfectionists is a upcoming American teen drama television series developed by I. Marlene King, loosely based on the popular book series \"The Perfectionists\" written by Sara Shepard.  A second spin-off of \"Pretty Little Liars\" after \"Ravenswood\", Freeform greenlit the series on September 25, 2017.\n\nList of Pretty Little Liars episodes: \"Pretty Little Liars\" is a TV series which premiered on ABC Family on June 8, 2010.  Developed by I. Marlene King, the series is based on the \"Pretty Little Liars\" book series by Sara Shepard.  The series follows the lives of four girls, Aria Montgomery, Hanna Marin, Emily Fields, and Spencer Hastings, whose clique falls apart after the disappearance of their leader, Alison DiLaurentis.  One year later, the estranged friends are reunited as they begin receiving messages from a mysterious figure named \"A\" who threatens to expose their deepest secrets, including ones they thought only Alison knew.\n\nPretty Little Liars (novel): Pretty Little Liars is the first book in the \"Pretty Little Liars\" series by Sara Shepard.  It tells the story of four girls - Hanna, Aria, Emily and Spencer - after the disappearance of their clique leader, Alison.  The book was written for the book packaging company Alloy Entertainment, the idea originally developed as a TV series.\n\nQuestion: Who wrote the eighteenth episode of the seventh season of \"Pretty Little Liars\", featuring Shay Mitchell as Emily?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    },\n    \"episode_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"episode_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the specific episode.\"\n        },\n        \"season_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The season number of the episode.\"\n        },\n        \"episode_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The episode number within its season.\"\n        },\n        \"writer\": {\n          \"type\": \"string\",\n          \"description\": \"The writer of the episode.\"\n        }\n      },\n      \"required\": [\n        \"episode_name\",\n        \"season_number\",\n        \"episode_number\",\n        \"writer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor featured in the episode.\"\n        },\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character played by the featured actor.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"character_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"series_title\",\n    \"episode_details\",\n    \"featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_title": {
        "type": "string",
        "description": "The title of the television series."
      },
      "episode_details": {
        "type": "object",
        "properties": {
          "episode_name": {
            "type": "string",
            "description": "The name of the specific episode."
          },
          "season_number": {
            "type": "integer",
            "description": "The season number of the episode."
          },
          "episode_number": {
            "type": "integer",
            "description": "The episode number within its season."
          },
          "writer": {
            "type": "string",
            "description": "The writer of the episode."
          }
        },
        "required": [
          "episode_name",
          "season_number",
          "episode_number",
          "writer"
        ],
        "additionalProperties": false
      },
      "featured_actor": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor featured in the episode."
          },
          "character_name": {
            "type": "string",
            "description": "The name of the character played by the featured actor."
          }
        },
        "required": [
          "actor_name",
          "character_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "series_title",
      "episode_details",
      "featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
