{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLast Bus to Woodstock: Last Bus to Woodstock is a crime novel by Colin Dexter, the first of 13 novels in his Inspector Morse series.\n\nSin Pit: Sin Pit is a crime novel by American journalist Paul S. Meskil (Jul 2, 1923–Oct 11, 2005), published by Lion Books in 1954.  It is one of those rare paperback originals that has achieved cult status through a combination of circumstances, including the fact the author wrote only one work of crime fiction, the initial print run was relatively low for paperbacks at the time, the book had only one print run by the original publisher (Lion Books) and, finally, found an audience years later among collectors of 1950s paperback crime novels.  Sin Pit shares all the above circumstances with another paperback crime novel published a year earlier, in 1953, that similarly achieved cult status — Black Wings Has My Angel by Elliott Chaze, published by Fawcett Gold Medal.  Both authors were respected journalists their entire lives and wrote only a single crime novel that was never republished until years later, only after gaining an audience among aficionados of pulp fiction.\n\nThe Torment of Others: The Torment of Others is a crime novel by Scottish author Val McDermid, and is the fourth entry in her popular Carol Jordan and Dr. Tony Hill series, which has been successfully adapted into the television series \"Wire in the Blood\".  The novel was shortlisted for the Crime Writers' Association Gold Dagger, and won the 2006 Theakston's Old Peculier Crime Novel of the Year Award.  As with her other novels in the Tony Hill series, the title is an extract from a poem by T. S. Eliot.\n\nAlison Joseph: Alison Joseph (born 1958) is an English crime writer based in London where she was born and raised.  She studied French and Philosophy at Leeds University, and started her career as a documentary director, making programmes for Channel 4.  The first in her crime series, featuring detective nun Sister Agnes, was published in 1993.  She has also written for radio, including adaptations of Georges Simenon’s \"Maigret\".  She was Chair of the Crime Writers Association from 2013 to 2015.\n\nPeter May (writer): Peter May (born 20 December 1951) is a Scottish television screenwriter, novelist, and crime writer.  He is the recipient of writing awards in Europe and America.  \"The Blackhouse\" won the U.S. Barry Award for Crime Novel of the Year and the national literature award in France, the CEZAM Prix Litteraire.  \"The Lewis Man\" won the French daily newspaper \"Le Télégramme\"' s 10,000-euro Grand Prix des Lecteurs.  In 2014, \"Entry Island\" won both the Deanston’s Scottish Crime Novel of the Year and the UK’s ITV Crime Thriller Book Club Best Read of the Year Award.  May’s books have sold more than two million copies in the UK and several million internationally.\n\nColin Dexter: Norman Colin Dexter, OBE (29 September 1930 – 21 March 2017) was an English crime writer known for his \"Inspector Morse\" series of novels, which were written between 1975 and 1999 and adapted as an ITV television series, \"Inspector Morse\", from 1987 to 2000.  His characters have spawned a sequel series, \"Lewis\", and a prequel series, \"Endeavour\".\n\nDick Francis: Richard Stanley Francis CBE FRSL (31 October 1920 – 14 February 2010) was a British steeplechase jockey and crime writer, whose novels centre on horse racing in England.\n\nAnthony Gilbert (author): Anthony Gilbert, the pen name of Lucy Beatrice Malleson (15 February 1899 – 9 December 1973), was an English crime writer who was a cousin of actor-screenwriter Miles Malleson.  She also wrote nongenre fiction as Anne Meredith and published one crime novel and an autobiography (\"Three-a-Penny\", 1940) under the Meredith name.\n\nKilling Monica: Killing Monica is a novel written by Candace Bushnell.  It was first released as a hardcover on June 23, 2015.  Bushnell's publisher, the Hachette Book Group describes its central character, Pandy \"PJ\" Wallis, as \"a renowned writer whose novels about a young woman making her way in Manhattan have spawned a series of blockbuster films.\"\n\nDiogenes Small: Diogenes Small (1797–1805) is a fictional character created by the English crime writer Colin Dexter in his Inspector Morse series of novels.  The character, the supposed author of numerous historical and other works, does not appear in the novels although Dexter has used his quotations.\n\nQuestion: Last Bus to Woodstock is a crime novel written by an English crime writer whose novels were adapted as an ITV what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the crime novel.\"\n    },\n    \"author\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the author.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the author.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"adaptation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of adaptation (e.g., television series).\"\n        },\n        \"network\": {\n          \"type\": \"string\",\n          \"description\": \"The network that adapted the novels.\"\n        },\n        \"series_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the adapted series.\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"network\",\n        \"series_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"novel_title\",\n    \"author\",\n    \"adaptation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "novel_title": {
        "type": "string",
        "description": "The title of the crime novel."
      },
      "author": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the author."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "adaptation": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of adaptation (e.g., television series)."
          },
          "network": {
            "type": "string",
            "description": "The network that adapted the novels."
          },
          "series_name": {
            "type": "string",
            "description": "The name of the adapted series."
          }
        },
        "required": [
          "type",
          "network",
          "series_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "novel_title",
      "author",
      "adaptation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
