{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEvangelicals and Catholics Together: Evangelicals and Catholics Together is a 1994 ecumenical document signed by leading Evangelical and Roman Catholic scholars in the United States.  The co-signers of the document were Charles Colson and Richard John Neuhaus, representing each side of the discussions.  It was part of a larger ecumenical rapprochement in the United States that had begun in the 1970s with Catholic-Evangelical collaboration during the Gerald R. Ford Administration and in later para-church organizations such as Moral Majority founded by Rev. Jerry Fawell at the urging of Francis Schaeffer and his son Frank Schaeffer during the Jimmy Carter administration.\n\nStella Fregelius: Stella Fregelius: A Tale of Three Destinies is a 1904 novel by British writer H. Rider Haggard about a young inventor who falls in love with a mysterious stranger while he is engaged to another woman.  As a novelist, Haggard is known primarily for his adventure novels. Among his most widely read and critically acclaimed novels are \"King Solomon's Mines\", \"Allan Quatermain\", and \"She\".  After his publication of \"She\", Haggard wrote at least one novel a year every year until his death in 1925.\n\nHeavenly Pursuits: Heavenly Pursuits (knows as Gospel According to Vic in some territories) is a 1986 Scottish comedy film written and directed by Charles Gormley and starring Tom Conti, Helen Mirren, and David Hayman.  Set in Glasgow, Scotland, the film is about a teacher at a Catholic school whose students are searching for two more miracles that would promote the late Edith Semple to sainthood.  A nonbeliever himself, the teacher's scepticism is challenged when he becomes involved in seemingly miraculous events.\n\nHow Should We Then Live?: How Should We Then Live: The Rise and Decline of Western Thought and Culture is a major Christian cultural and historical documentary film series and book.  The book was written by presuppositionalist theologian Francis A. Schaeffer and first published in 1976.  The book served as the basis for a series of ten films.  Schaeffer narrated and appeared throughout the film series, which was produced by his son Frank Schaeffer and directed by John Gonser.  In the film series, Schaeffer attacked the influences of the Renaissance, the Enlightenment, and Charles Darwin.  The films were credited with inspiring a number of leaders of the American conservative evangelical movement, including Jerry Falwell.  The complete list of materials that the Schaeffers produced under the title \"How Should We Then Live?\"  include the initial book, a study guide for the book, the ten-episode film series, and study aids for the films.\n\nEdith Schaeffer: Edith Rachel Merritt Schaeffer (née Seville) (November 3, 1914 – March 30, 2013) was a Christian author and co-founder of L'Abri, a Christian organization which hosts guests.  She was the wife of Francis Schaeffer, and the mother of Frank Schaeffer and three other children.\n\nJim Harris (writer): Jim Harris is an American novelist.  He has written three acclaimed novels in the 21st Century, one of which was nominated for a Pen USA award.  He writes comic novels about the human condition with characters who are almost always marginalized.  His style is often compared to Tom Robbins and Kurt Vonnegut but his content is rougher-edged and often compared to Jim Thompson and Cormac McCarthy with more comic overtones.  His unique approach to his characters delineates him from most other comic American male writers, as females are the lead characters in all of his novels.\n\nFrank Schaeffer: Frank Schaeffer (born August 3, 1952) is an American author, film director, screenwriter, and public speaker.  He is the son of the late theologian and author Francis Schaeffer.  He became a Hollywood film director and author, writing several internationally acclaimed novels depicting life in a strict evangelical household including \"Portofino\", \"Zermatt\", and \"Saving Grandma\".\n\nMuzaffar Iqbal: Muzaffar Iqbāl (Punjabi/Pakistan/Urdu: ) (born December 3, 1954 in Lahore, Punjab, Pakistan) is a Pakistani-Canadian Islamic scholar and author.  Iqbal earned his doctorate (1983) in Chemistry from the University of Saskatchewan and then left the field of experimental science to devote himself fully to his chosen fields: literature, history, philosophy, Islamic intellectual and spiritual traditions.  Between 1984 and 1990, he taught Urdu at the University of Wisconsin-Madison (1984–85), wrote two acclaimed novels in Urdu, Inkhila (Uprooting) and Inqta (Severance).  During 1980 and 1990, he published a number of translations of poetry of Latin American poets and wrote a series of literary essays on South American writers.  He also wrote on literary theory.\n\nArnould Galopin: Arnould Galopin (1865, Marbeuf, Eure - 1934) was a prolific French writer with more than 50 novels to his credit.  Galopin won the French Academy's Grand Prize for his \"Sur le Front de Mer\" (1918), a critically acclaimed novel about the Merchant Navy during World War I, and wrote several equally acclaimed novels about his experiences during the war.\n\nPat Conroy: Donald Patrick \"Pat\" Conroy (October 26, 1945 – March 4, 2016) was an American author who wrote several acclaimed novels and memoirs. Two of his novels, \"The Prince of Tides\" and \"The Great Santini\", were made into Oscar-nominated films.  He is recognized as a leading figure of late-20th century Southern literature.\n\nQuestion: Frank Schaeffer, son of the late Edith Schaeffer, wrote which acclaimed novels? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author.\"\n    },\n    \"parent_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author's parent.\"\n    },\n    \"relationship_to_parent\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the author to the specified parent.\"\n    },\n    \"acclaimed_novels\": {\n      \"type\": \"array\",\n      \"description\": \"A list of acclaimed novels written by the author.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"parent_name\",\n    \"relationship_to_parent\",\n    \"acclaimed_novels\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The name of the author."
      },
      "parent_name": {
        "type": "string",
        "description": "The name of the author's parent."
      },
      "relationship_to_parent": {
        "type": "string",
        "description": "The relationship of the author to the specified parent."
      },
      "acclaimed_novels": {
        "type": "array",
        "description": "A list of acclaimed novels written by the author.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "author_name",
      "parent_name",
      "relationship_to_parent",
      "acclaimed_novels"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
