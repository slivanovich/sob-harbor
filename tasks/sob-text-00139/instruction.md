{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHot Lead and Cold Feet: Hot Lead and Cold Feet (originally titled Welcome to Bloodshy) is a 1978 American comedy-western film produced by Walt Disney Productions and starring Jim Dale, Karen Valentine, Don Knotts, Jack Elam and Darren McGavin.\n\nSnowball Express: Snowball Express is a 1972 American screwball comedy film made by Walt Disney Productions about a man who leaves his middle class job to run a hotel left to him by his uncle.\n\nThe Perfect Match (1995 film): The Perfect Match is a British comedy-drama television film written by Mike Bullen and directed by Nick Hurran.  It stars Saskia Reeves and Con O'Neill as Bridget and Phil, a couple whose marriage proposal is broadcast to football fans.  It was first broadcast on the ITV network on 6 September 1995.  The programme was not well received by critics but it was enough of a success for producers Granada Television to ask Bullen for further ideas, leading to the commissioning of the long-running television series \"Cold Feet\".\n\nBackpackers (web series): Backpackers is a Canadian comedy web series, which aired in 2013 on CTV.ca and CW Seed.  The CW picked up the series for television broadcast, for which material from the web series was edited into four half-hour episodes, and six new episodes were produced.  \"Backpackers\" made its television premiere on July 14, 2014.  The series stars Dillon Casey and Noah Reid as Brandon and Ryan, two friends on a backpacking trip across Europe after Ryan and his girlfriend Beth (Meghan Heffern) experience cold feet over their pending engagement.  Ryan's stolen journal is posted on the Internet and goes viral, sending Ryan, Brandon, and Brandon's brother Andrew (Giacomo Gianniotti) on another journey, to recover the journal and fulfill Ryan's dream of becoming a published author.\n\nTom Leetch: Tom Leetch is an American film producer, writer and director.  His career included working on films for Walt Disney Productions, under the leadership of Walt Disney's son-in-law, Ron Miller.  At Disney, Leetch first began as an assistant director on films such as \"Mary Poppins\", \"The Ugly Dachshund\" and \"Monkeys, Go Home\".  He then served in several positions as producer, associate producer, and director on films such as \"Snowball Express\", \"Napoleon and Samantha\", \"Freaky Friday\", \"The North Avenue Irregulars\", and \"The Watcher in the Woods\", a project in which he pitched to Ron Miller stating, \"This could be our \"Exorcist\".\"\n\nCel Spellman: Ceallach \"Cel\" Spellman ( ; born 31 August 1995) is an English actor and presenter known for playing Malky McConnell in the BBC Two mockumentary \"The Cup\", Harry Fisher in the BBC One drama \"Waterloo Road\" from 2010–11 and hosting \"Friday Download\" and the \"CBBC Official Chart Show\".  Since July 2015 he has presented his own show on BBC Radio 1 which airs Sunday afternoons between 16:00 and 19:00.  He also stars as Matthew Williams in \"Cold Feet\", and contributes to \"The Voice UK\".\n\nHot Lead: Hot Lead is a 1951 Western film.  It stars Tim Holt and Joan Dixon and is directed by Stuart Gilmore.\n\nCold Feet (1989 film): Cold Feet is a 1989 film directed by Robert Dornhelm.  It stars Keith Carradine and Sally Kirkland.\n\nPilot (Cold Feet): Cold Feet is a British television pilot directed by Declan Lowney.  It stars James Nesbitt and Helen Baxendale as Adam and Rachel, a couple who meet and fall in love, only for the relationship to break down when he gets cold feet.  John Thomson, Fay Ripley, Hermione Norris and Robert Bathurst appear in supporting roles.  The programme was written by Mike Bullen, a BBC radio producer with little screenwriting experience, who was tasked with creating a one-off television production that would appeal to middle-class television audiences, who the executive producer Andy Harries believed were underepresented on British television.\n\nKaren Valentine: Karen Lynne Valentine (born May 25, 1947) is an American actress.  She is best known for her role as the idealistic schoolteacher Alice Johnson in the ABC comedy drama series \"Room 222\" from 1969 to 1974, for which she won Primetime Emmy Award for Outstanding Supporting Actress in a Comedy Series in 1970, and received a Golden Globe Award nomination in 1971.  She later went to star in own short-lived sitcom \"Karen\" (1975), and played female leading roles in films \"Hot Lead and Cold Feet\" (1978) and \"The North Avenue Irregulars\" (1979).\n\nQuestion: Which Disney film stars Don Knotts, Snowball Express or Hot Lead and Cold Feet?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that stars the actor in question.\"\n    },\n    \"is_disney_production\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film was produced by Walt Disney Productions.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the main actors starring in the film.\"\n    },\n    \"actor_in_question\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor whose presence in the film was queried.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"is_disney_production\",\n    \"release_year\",\n    \"starring_actors\",\n    \"actor_in_question\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that stars the actor in question."
      },
      "is_disney_production": {
        "type": "boolean",
        "description": "Indicates if the film was produced by Walt Disney Productions."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the main actors starring in the film."
      },
      "actor_in_question": {
        "type": "string",
        "description": "The name of the actor whose presence in the film was queried."
      }
    },
    "required": [
      "film_title",
      "is_disney_production",
      "release_year",
      "starring_actors",
      "actor_in_question"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
