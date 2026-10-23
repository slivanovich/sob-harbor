{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlexis Lykiard: Alexis Lykiard (born 1940) is a British writer of Greek heritage, who began his prolific career as novelist and poet in the 1960s.  His poems about jazz have received particular acclaim, including from Maya Angelou, Hugo Williams, Roy Fisher, Kevin Bailey and others.  He is also known as translator of Isidore Ducasse, Comte de Lautréamont, Alfred Jarry, Antonin Artaud and many notable French literary figures.  In addition, Lykiard has written two highly praised intimate memoirs of Jean Rhys: \"Jean Rhys Revisited\" (2000) and \"Jean Rhys: Afterwords\" (2006).\n\nAn Open Swimmer: An Open Swimmer was the first novel by multi-award-winning Australian author, Tim Winton.  Winton wrote this novel while attending a creative writing course at Curtin University.  In 1981 it won The Australian/Vogel Literary Award, and thereby kick-started Tim Winton's successful writing career.\n\nThe Boy Behind the Curtain: The Boy Behind the Curtain (2016) is an autobiographical work by multi award-winning Australian author Tim Winton.  Through a series of short stories he chronicles important events which helped to shape his life and his writing.\n\nDown to Earth: Australian Landscapes: Down to Earth: Australian Landscapes is a non-fiction book by photographer Richard Woldendorp with an essay by multi-award winning Australian author Tim Winton originally published in 1999.  The book is a collection of photographs of the Australian landscape, with an accompanying essay by Winton that examines his personal responses to the land.\n\nThe Collected Shorter Novels of Tim Winton: The Collected Shorter Novels of Tim Winton is a collection of early short novels by award-winning Australian author Tim Winton.  Published in 1995, it includes \"An Open Swimmer\", \"That Eye, The Sky\" and \"In the Winter Dark\".\n\nGood Morning, Midnight (Rhys novel): Good Morning, Midnight is a 1939 modernist novel by the author Jean Rhys.  Often considered a continuation of Rhys' three other early novels, \"Quartet\" (1928), \"After Leaving Mr Mackenzie\" (1930) and \"Voyage in the Dark\" (1934), it is experimental in design and deals with a woman's feelings of vulnerability, depression, loneliness and desperation during the years between the two World Wars.  The book initially sold poorly—critics thought it well written, but too depressing—and after its publication Rhys spent a decade living in obscurity.  It was not until it was adapted into a theatrical production in 1949, and again into a radio play 1957 by the BBC, that Rhys was once again put into the spotlight.\n\nTigers Are Better-Looking: Tigers are Better-Looking is a collection of short stories written by famed Dominican author Jean Rhys, published in 1968 by André Deutsch and reissued by Penguin ten years later.  This collection combines eight stories written by Rhys during the 1950s (her period of obscurity) with another nine from her previous efforts in 1927's \"The Left Bank and Other Stories\".  In 1979, the title story from Rhys's collection was adapted into a UK-produced short film, directed by Hussein Shariffe.\n\nTim Winton: Tim (Timothy John) Winton (born 4 August 1960) is a multi-award-winning Australian writer of novels, children's books, non-fiction books and short stories.\n\nJean Rhys: Jean Rhys, CBE ( ; 24 August 1890 – 14 May 1979), born Ella Gwendolyn Rees Williams, was a mid-20th-century novelist who was born and grew up in the Caribbean island of Dominica, though she was mainly resident in England from the age of 16.  She is best known for her novel \"Wide Sargasso Sea\" (1966), written as a prequel to Charlotte Brontë's \"Jane Eyre\".\n\nThe Turning (short story collection): The Turning is a collection of short stories by multi-award winning Australian author Tim Winton published in April 2005.\n\nQuestion: Tim Winton and Jean Rhys, have very similar occupations?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"are_occupations_similar\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the occupations of the two authors are similar.\"\n    },\n    \"author_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first author.\"\n        },\n        \"occupation_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the first author's occupation as found in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupation_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"author_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second author.\"\n        },\n        \"occupation_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the second author's occupation as found in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupation_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for the similarity or dissimilarity of their occupations based on the provided context.\"\n    }\n  },\n  \"required\": [\n    \"are_occupations_similar\",\n    \"author_1\",\n    \"author_2\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "are_occupations_similar": {
        "type": "boolean",
        "description": "Indicates whether the occupations of the two authors are similar."
      },
      "author_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first author."
          },
          "occupation_description": {
            "type": "string",
            "description": "A description of the first author's occupation as found in the context."
          }
        },
        "required": [
          "name",
          "occupation_description"
        ],
        "additionalProperties": false
      },
      "author_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second author."
          },
          "occupation_description": {
            "type": "string",
            "description": "A description of the second author's occupation as found in the context."
          }
        },
        "required": [
          "name",
          "occupation_description"
        ],
        "additionalProperties": false
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for the similarity or dissimilarity of their occupations based on the provided context."
      }
    },
    "required": [
      "are_occupations_similar",
      "author_1",
      "author_2",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
