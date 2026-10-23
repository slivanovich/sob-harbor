{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGjernes: Gjernes is a contemporary style of fine art; sculptural and decorative.  It is a spreading popular style of art, especially in Scandinavia, because the Norwegian Government's wedding gift to Princess Märtha Louise of Norway and her husband Ari Behn was two pieces of furniture work by Liv Mildrid Gjernes.\n\nWorld Fantasy Award—Short Fiction: The World Fantasy Awards are given each year by the World Fantasy Convention for the best fantasy fiction published in English during the previous calendar year.  The awards have been described by book critics such as \"The Guardian\" as a \"prestigious fantasy prize\", and one of the three most prestigious speculative fiction awards, along with the Hugo and Nebula Awards (which cover both fantasy and science fiction).  The World Fantasy Award—Short Fiction is given each year for fantasy short stories published in English.  A work of fiction is defined by the organization as short fiction if it is 10,000 words or less in length; awards are also given out for longer pieces in the Novel and Long Fiction categories.  The Short Fiction category has been awarded annually since 1975, though before 1982—when the category was instated—it was named \"Best Short Fiction\" and covered works of up to 40,000 words.  It was then renamed \"Best Short Story\" until 2016, when it was renamed to the \"Short Fiction\" category.\n\nNine Tomorrows: Nine Tomorrows is a collection of nine short stories and two pieces of comic verse by Isaac Asimov.  The pieces were all originally published in magazines between 1956 and 1958, with the exception of the closing poem, \"Rejection Slips\", which was original to the collection.  The book was first published in the United States in 1959 and in the UK in 1963.  It includes two of Asimov's favorite stories, \"The Last Question\" and \"The Ugly Little Boy\".\n\nMa Sandar: Ma Sandar (Burmese: မစန္ဒာ ; born 4 November 1947) is a well known Burmese writer.  With a clear and engaging style, her works reflect the daily struggles of the people living in Myanmar.  Her novella, \"Life's Dream, Flower's Dream\" won the 1994 Myanmar National Literature Award for novella.  Her short stories collection, \"Short Stories Collection 3\" won the 1999 Myanmar National Literature Award for Collected Short Stories.  Another novella, \"Hexagon\" won the 2002 National Literature Award for novella.  10 of her novels have been made into movies.\n\nNagen Saikia: Nagen Saikia () (born on 11 February 1939) is an Indian writer.  He was formerly a professor of Dibrugarh University.  Saikia had also been a member of the Rajya Sabha from 1986-1992 and was the vice-chairman of the Upper House from 1990-1992.  Saikia started his career as a teacher and went on to serve in different reputed institutions in various categories.  He also delivered lectures on various topics about Assamese literature, including in the US and England.  He has published numerous literary essays, short stories, novels, books and articles, to his credit.  Saikia was conferred with the Sahitya Akademi award in 1997 for his short stories collection \"Andharat Nizar Mukh\" and was honoured by the Mohan Chandra Sahitya Sabha in 1980 for \"Chinta aru Charcha\".\n\nAri Behn: Ari Mikael Behn (né Bjørshol, born 30 September 1972) is a Norwegian author.  He has written three novels, two collections of short stories and a book about his wedding.  His 1999 short stories collection \"Trist som faen\" (\"Sad as hell\") sold in about 100 000 copies and received several favourable reviews.  His books have been translated into Swedish, Danish, German, Hungarian, and Icelandic as well as French.  In the spring of 2011, Ari Behn made his debut as a playwright with \"Treningstimen\", directed by Kim Sørensen and staged at Rogaland Teater.\n\nWide-Eyed and Legless: Wide-Eyed and Legless (also known as The Wedding Gift) is a 1993 made-for-TV British drama film directed by Richard Loncraine.  It is known in the US as \"The Wedding Gift\".\n\nLiv Mildrid Gjernes: Liv Mildrid Gjernes (born 2 June 1954 in Lunde, in Telemark, Norway) is a Norwegian artist and has given name to the contemporary style of decoration, sculpture, and furniture design known as Gjernes style.  She lives and has her atelier in Eidsfoss, in Vestfold in Norway.  She studied in Bergen high-school of art and design and at the Institute for Furniture and Room.\n\nYoung Lover, New Lover: ‘\"Young Lover, New Lover\"' is a 2012 Short stories collection by Muhammad Aladdin, and has been published by Merit Publishing House in Egypt.  It is his third short stories collection followed by the novel A Well-Trained Stray in 2014.\n\nShot welding: Shot welding is a specific type of spot welding used to join two pieces of metal together.  This is accomplished by clamping the two pieces together and then passing a large electric current through them for a short period of time.  Assuming the right amount of current for the right time, this will weld the two pieces of metal together.  Shot welding was invented by Earl J. Ragsdale, a mechanical engineer at the Budd Company, in 1932 for the purposes of welding stainless steel.  This welding method was used to construct the \"Pioneer Zephyr\".\n\nQuestion: Who wrote the 1999 short stories collection, \"Trist som faen,\" and was also given two pieces of furniture by Liv Mildrid Gjernes to as a wedding gift from the Norwegian government?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"authored_work\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\"\n        },\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"title\",\n        \"publication_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"wedding_gift_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"gift_item_type\": {\n          \"type\": \"string\"\n        },\n        \"number_of_pieces\": {\n          \"type\": \"integer\"\n        },\n        \"artist_name\": {\n          \"type\": \"string\"\n        },\n        \"gift_giver\": {\n          \"type\": \"string\"\n        },\n        \"recipient_relationship_to_author\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"gift_item_type\",\n        \"number_of_pieces\",\n        \"artist_name\",\n        \"gift_giver\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"author_details\",\n    \"authored_work\",\n    \"wedding_gift_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "authored_work": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "publication_year": {
            "type": "integer"
          }
        },
        "required": [
          "type",
          "title",
          "publication_year"
        ],
        "additionalProperties": false
      },
      "wedding_gift_information": {
        "type": "object",
        "properties": {
          "gift_item_type": {
            "type": "string"
          },
          "number_of_pieces": {
            "type": "integer"
          },
          "artist_name": {
            "type": "string"
          },
          "gift_giver": {
            "type": "string"
          },
          "recipient_relationship_to_author": {
            "type": "string"
          }
        },
        "required": [
          "gift_item_type",
          "number_of_pieces",
          "artist_name",
          "gift_giver"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "author_details",
      "authored_work",
      "wedding_gift_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
