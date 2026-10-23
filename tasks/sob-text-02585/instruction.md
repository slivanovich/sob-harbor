{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nErik Jacobsen: Erik Jacobsen (born May 19, 1940) is an American record producer, song publisher and artist manager.  He is best known for his work in the 1960s with Tim Hardin, The Lovin' Spoonful, The Charlatans, Sopwith Camel, and later with Norman Greenbaum and Chris Isaak.  Though semi-retired, Jacobsen continues to manage many of his published songs and masters for various uses.\n\nAnjani: Anjani Thomas (born July 10, 1959) is an American singer-songwriter and pianist, best known for her work with singer-songwriter Leonard Cohen, as well as Carl Anderson, Frank Gambale, and Stanley Clarke.  She became a solo artist in 2000.\n\nAnnie Jacobsen: Annie Jacobsen is an American investigative journalist, author and 2016 Pulitzer Prize finalist in history.  She was a contributing editor to the \"Los Angeles Times Magazine\" from 2009 until 2012.  Jacobsen writes about war, weapons, security and secrets.  Jacobsen is best known as the author of the 2011 nonfiction book \"\", which \"The New York Times\" called \"cauldron-stirring.\"\n\nWayne Jacobsen: Wayne Jacobsen is an American author, best known for \"He Loves Me!\" , a nonfiction book about the Love of God.  He also collaborated on the writing of \"The Shack\" and helped create Windblown Media, the publishing company behind the phenomenon.  He was a pastor for 20 years and a Contributing Editor to \"Leadership Journal\" and has authored numerous articles on spiritual formation, relational community and engagement of culture.  As President of BridgeBuilders, he is also a nationally recognized specialist and mediator in resolving cultural and religious conflicts.  Jacobsen has become known for his expertise in the pros and cons of organized religion.\n\nEric Jacobsen: Eric N. Jacobsen (born February 22, 1960.  in New York City, New York) is the Sheldon Emery Professor of Chemistry and Chair of the Department of Chemistry and Chemical Biology at Harvard University.  He is a prominent figure in the field of organic chemistry and is best known for the development of the Jacobsen epoxidation and other work in selective catalysis.\n\nHolger Jacobsen: Holger Jacobsen (30 October 1876 – 27 March 1960) was a Danish architect.  His best known work is Stærekassen, an extension to the Royal Danish Theatre on Kongens Nytorv in Copenhagen.\n\nDanny Weis: Guitarist Danny Weis (born 28 September 1948 in Huntington Park, California) is best known as a founding member of both Iron Butterfly and Rhinoceros, as well as co-writer of Rhinoceros's only charting single, \"Apricot Brandy\".  Though he left Iron Butterfly after only one album due to internal tensions, his work was an influence in the band for most of their history, since his replacement Erik Brann made a conscious effort to imitate his playing.  Weis later recounted \"Erik Braunn replaced me in Iron Butterfly, and if I remember correctly, he bought a lot of my equipment, some of my clothes, they tried to clone me basically...\"\n\nNorman Greenbaum: Norman Joel Greenbaum (born November 20, 1942) is an American singer-songwriter.  He is best known for writing and performing the 1969 song \"Spirit in the Sky\".\n\nChuck Carrington: Chuck Carrington (born 1968 in Lynchburg, Virginia) is an American actor best known for playing Petty Officer Jason Tiner on \"JAG\", and also starred as Renny Jacobsen in the independent feature thriller \"The List\", alongside Malcolm McDowell and Hilarie Burton.\n\nMaria McKee: Maria Luisa McKee (born August 17, 1964) is an American singer-songwriter.  She is best known for her work with Lone Justice, her 1990 UK solo chart-topping hit, \"Show Me Heaven\", and her song \"If Love Is a Red Dress (Hang Me in Rags)\" from the film \"Pulp Fiction\".  She is the half-sister of Bryan MacLean, who was best known as a guitarist and vocalist in the band Love.\n\nQuestion: what is the American singer-songwriter who Erik Jacobsen work with best known for \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the producer mentioned in the context.\"\n    },\n    \"collaborating_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American singer-songwriter who collaborated with the producer.\"\n    },\n    \"artist_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The primary occupation of the collaborating artist.\"\n    },\n    \"artist_best_known_for\": {\n      \"type\": \"string\",\n      \"description\": \"The specific work or achievement the collaborating artist is best known for.\"\n    },\n    \"collaboration_type\": {\n      \"type\": \"string\",\n      \"description\": \"The nature of the collaboration between the producer and the artist.\"\n    }\n  },\n  \"required\": [\n    \"producer_name\",\n    \"collaborating_artist_name\",\n    \"artist_occupation\",\n    \"artist_best_known_for\",\n    \"collaboration_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "producer_name": {
        "type": "string",
        "description": "The name of the producer mentioned in the context."
      },
      "collaborating_artist_name": {
        "type": "string",
        "description": "The name of the American singer-songwriter who collaborated with the producer."
      },
      "artist_occupation": {
        "type": "string",
        "description": "The primary occupation of the collaborating artist."
      },
      "artist_best_known_for": {
        "type": "string",
        "description": "The specific work or achievement the collaborating artist is best known for."
      },
      "collaboration_type": {
        "type": "string",
        "description": "The nature of the collaboration between the producer and the artist."
      }
    },
    "required": [
      "producer_name",
      "collaborating_artist_name",
      "artist_occupation",
      "artist_best_known_for",
      "collaboration_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
