{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDouglas Scott (writer): Douglas Scott is an author of thriller fiction, mostly published during the 1980s.\n\nSomething Upstairs: Something Upstairs (also published as \"Something Upstairs: A Tale of Ghosts\") is a young adult historical thriller fiction novel written by Avi first published in 1988.  It concerns a 12-year-old boy named Kenny Huldorf who has moved to a new area and discovers a ghost, Caleb, in a room.  Caleb was the slave of a previous owner of the home, and is stuck there until someone can help set him free.  Kenny travels back in time with Caleb to find his murderer and comes to a dilemma on whether he can return to the present or save his new friend.  The novel has won several awards in children's writing.\n\nThe Rozabal Line: The Rozabal Line is a thriller fiction that deals with the subject of Jesus having survived the crucifixion and having settled down in India.  The fictional element reads in the same vein as Dan Brown's \"The Da Vinci Code\" whereas the historical basis is derived from several other books on the subject including \"Jesus Lived in India\" by Holger Kersten and \"The Unknown Life of Jesus\" by Nicolas Notovich.\n\nDan Brown: Daniel Gerhard \"Dan\" Brown (born June 22, 1964) is an American author of thriller fiction, most notably the novels \"Angels & Demons\" (2000), \"The Da Vinci Code\" (2003), and \"Inferno\" (2013).  Brown's novels are treasure hunts set in a 24-hour period, and feature the recurring themes of cryptography, keys, symbols, codes, and conspiracy theories.  His books have been translated into 52 languages, and as of 2012, sold over 200 million copies.  Three of them, \"Angels & Demons\" (2000), \"The Da Vinci Code\" (2003), and \"Inferno\" (2013), have been adapted into films.\n\nMichael MacConnell: Michael MacConnell is an Australian author.  His first fiction novel, \"Maelstrom\", was released in October 2007 by Hachette Livre.  The first sequel novel \"Splinter\", was released in July 2008.  Both novels have been published in the United Kingdom, Germany, Australia and New Zealand.  He is a member of the International Thriller Writers Organization.  An avid reader of crime and thriller fiction since he was a child, some of his greatest writing influences were David Morrell, Raymond E. Feist, Alex Kava, Daniel Silva, Dean Koontz, Lee Child, Michael Cordy, and Steven Pressfield.  His first novel, \"Maelstrom\", made the Ned Kelly Award long list in the Best Debut Novel category.\n\nStephen White (author): Stephen Walsh White (born 1951) is an author of psychological thriller fiction best known for his Dr. Alan Gregory series.\n\nDafydd ab Hugh: Dafydd ab Hugh (, born David Friedman, on October 22, 1960) is a U.S. science fiction author.  He is known for writing fiction in media franchises in the 1990s, including several novels for the \"Star Trek\" franchise.  He also co-wrote four novels associated with the game \"Doom\" with fellow science fiction author Brad Linaweaver.  His novelette, \"The Coon Rolled Down and Ruptured His Larinks, A Squeezed Novel by Mr. Skunk\", was nominated for the Hugo Award and Nebula Award and is perhaps his best-known work.\n\nKaren Maitland: Karen Maitland (born 1956, in England) is a British author of medieval thriller fiction.  Maitland has an honours degree in Human Communication and doctorate in Psycholinguistics.\n\nRose Line: Rose Line is a fictional name given to the Paris Meridian and to the sunlight line defining the exact time of Easter on the Gnomon of Saint-Sulpice, marked by a brass strip on the floor of the church, where the two are conflated, by Dan Brown in his 2003 novel \"The Da Vinci Code\".  Brown based this on material found in the Priory of Sion documents of the 1960s, where neither the Zero Meridian nor the sunlight line in St Sulpice are called Rose Line.\n\nFinancial thriller: Financial thriller is a subgenre of thriller fiction in which the financial system and economy play a major role.  The novel \"The Financier\" (1912) by Theodore Dreiser displays elements of a financial thriller.  Paul Erdman helped popularize the modern financial thriller, with \"The Billion Dollar Sure Thing\" (1973).  The former president of a Swiss bank, he penned the novel while in jail awaiting trial on fraud charges related to speculating in the cocoa market.\n\nQuestion: What is the nationality of the thriller fiction author who used the Rose Line as inspiration for his well known 2003 novel?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the thriller fiction author.\"\n    },\n    \"author_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the author.\"\n    },\n    \"author_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of fiction written by the author.\"\n    },\n    \"novel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel mentioned in the question.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The publication year of the novel.\"\n        },\n        \"inspiration_source\": {\n          \"type\": \"string\",\n          \"description\": \"The specific concept or element that served as inspiration for the novel.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\",\n        \"inspiration_source\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"author_nationality\",\n    \"author_genre\",\n    \"novel_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The name of the thriller fiction author."
      },
      "author_nationality": {
        "type": "string",
        "description": "The nationality of the author."
      },
      "author_genre": {
        "type": "string",
        "description": "The primary genre of fiction written by the author."
      },
      "novel_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the novel mentioned in the question."
          },
          "publication_year": {
            "type": "integer",
            "description": "The publication year of the novel."
          },
          "inspiration_source": {
            "type": "string",
            "description": "The specific concept or element that served as inspiration for the novel."
          }
        },
        "required": [
          "title",
          "publication_year",
          "inspiration_source"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "author_name",
      "author_nationality",
      "author_genre",
      "novel_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
