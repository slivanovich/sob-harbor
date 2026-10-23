{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBetter Than Life: Better Than Life is a science fiction comedy novel by Grant Naylor, the collective name for Rob Grant and Doug Naylor, co-creators and writers of the \"Red Dwarf\" television series, on which the novel is based.  The main plotline was developed and expanded from the \"Red Dwarf\" episode of the same name, as well as the Series 3 and 4 episodes: \"White Hole, Marooned, Polymorph,\" and \"Backwards\".\n\nDiary of a Wimpy Kid: Rodrick Rules: Diary of a Wimpy Kid: Rodrick Rules is a satirical realistic fiction novel by American author and cartoonist Jeff Kinney, based on the FunBrain.com version.  It is the sequel to \"Diary of a Wimpy Kid\", followed by \"The Last Straw\".  The hardcover was released on February 1, 2008.  \"Rodrick Rules\" was named \"New York Times\" bestseller among awards and praise.  A was released on March 25, 2011.\n\nLast Human: Last Human is the title of a 1995 science fiction comedy novel written by Doug Naylor.  It is part of the \"Red Dwarf\" series of novels, based on the popular television show created by Naylor and his partner Rob Grant.  Like the other novels, it does not take place within the television series continuity, but instead adapts situations presented on the series to occur within an alternative universe.\n\nDiary of a Wimpy Kid: Diary of a Wimpy Kid is a satirical realistic fiction comedy novel for children and teenagers written and illustrated by Jeff Kinney.  It is the first book in the \"Diary of a Wimpy Kid\" series.  The book is about a boy named Greg Heffley and his struggles to fit in as he begins middle school.\n\nPoptropica: Poptropica is an online role-playing game, developed in 2007 by Pearson Education's Family Education Network, and targeted towards children aged 6 to 15.  \"Poptropica\" was primarily the creation of Jeff Kinney, the author of the \"Diary of a Wimpy Kid\" series.  As of 2015, he remains at the company as Creative Director.\n\nRed Dwarf: Infinity Welcomes Careful Drivers: Red Dwarf: Infinity Welcomes Careful Drivers is a best-selling science fiction comedy novel by Grant Naylor, the collective name for Rob Grant and Doug Naylor, co-creators and writers of the \"Red Dwarf\" television series, on which the novel is based.  First published in 1989, the novel presents the plotline of the TV series as a cohesive linear narrative, providing expanded backstory of the Red Dwarf world and more fully developing each of the characters, particularly Lister and Rimmer.  The book incorporates elements and scenes from the first and second-season episodes \"The End\", \"Future Echoes\", \"Kryten\", \"Me²\" and \"Better Than Life\".  In 1990 the book was followed by a sequel, \"Better Than Life\".\n\nThe Private Blog of Joe Cowley: The Private Blog of Joe Cowley is a teen realistic fiction novel series by British author Ben Davis, and also the title of the first book in the series.\n\nHomeroom Diaries: Homeroom Diaries is a realistic fiction novel by James Patterson aimed at teenagers.  Published in the United States by Little, Brown and Company on July 22, 2014, the book follows high-schooler Margaret Clarke, who goes by the nickname Cuckoo.  When the book begins, Cuckoo is living with a foster mother after her own mother abandoned her, an incident that caused Cuckoo to have a brief stay at a mental institution.\n\nBig Nate: Strikes Again: Big Nate Strikes Again is a realistic fiction novel by American cartoonist Lincoln Peirce.  It is based on the comic strip and the second book in the \"Big Nate\" novel series.  The book was released on October 19, 2010.  It is aimed at children aged 8 to 12.  It was published by HarperCollins Publishers.  The book has a 13,928 sale rank.\n\nHit and Run (novel): Hit and Run is a realistic fiction novel by Lurlene McDaniel, published in 2007.  It focuses on four teenagers whose lives intersect following a hit-and-run car crash.  The book is told from the alternating perspectives of the four teens.\n\nQuestion: What is the title of this satirical realistic fiction comedy novel for children and teenagers by the author who created \"Poptropica?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"book_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the book that matches the criteria.\"\n    },\n    \"author_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the author.\"\n        },\n        \"created_poptropica\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the author created Poptropica.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"created_poptropica\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"book_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"genres\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of genres the book belongs to.\"\n        },\n        \"target_audiences\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of target audience groups for the book.\"\n        },\n        \"is_satirical\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the book is satirical.\"\n        },\n        \"is_realistic_fiction\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the book is realistic fiction.\"\n        },\n        \"is_comedy\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the book is a comedy.\"\n        }\n      },\n      \"required\": [\n        \"genres\",\n        \"target_audiences\",\n        \"is_satirical\",\n        \"is_realistic_fiction\",\n        \"is_comedy\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"book_title\",\n    \"author_details\",\n    \"book_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "book_title": {
        "type": "string",
        "description": "The title of the book that matches the criteria."
      },
      "author_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author."
          },
          "created_poptropica": {
            "type": "boolean",
            "description": "Indicates if the author created Poptropica."
          }
        },
        "required": [
          "name",
          "created_poptropica"
        ],
        "additionalProperties": false
      },
      "book_attributes": {
        "type": "object",
        "properties": {
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of genres the book belongs to."
          },
          "target_audiences": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of target audience groups for the book."
          },
          "is_satirical": {
            "type": "boolean",
            "description": "True if the book is satirical."
          },
          "is_realistic_fiction": {
            "type": "boolean",
            "description": "True if the book is realistic fiction."
          },
          "is_comedy": {
            "type": "boolean",
            "description": "True if the book is a comedy."
          }
        },
        "required": [
          "genres",
          "target_audiences",
          "is_satirical",
          "is_realistic_fiction",
          "is_comedy"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "book_title",
      "author_details",
      "book_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
