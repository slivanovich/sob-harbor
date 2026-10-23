{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnime Himitsu no Hanazono: Anime Himitsu no Hanazono is an anime television series aired in Japan from 1991 to 1992.  It is an adaptation of the novel \"The Secret Garden\" by Frances Hodgson Burnett.\n\nThe Secret Garden (musical): The Secret Garden is a musical based on the 1911 novel of the same name by Frances Hodgson Burnett.  The musical's script and lyrics are by Marsha Norman, with music by Lucy Simon.  It premiered on Broadway in 1991 and ran for 709 performances.\n\nThe Secret Garden (1919 film): The Secret Garden is a lost 1919 American drama silent film directed by Gustav von Seyffertitz and written by Frances Hodgson Burnett and Marion Fairfax.  The film stars Lila Lee, Spottiswoode Aitken, Clarence Geldart, Richard Rosson, Fay Holderness and Ann Malone.  The film was released on January 12, 1919, by Paramount Pictures.\n\nThe Secret Garden: The Secret Garden is a children's novel by Frances Hodgson Burnett first published as a book in 1911, after a version was published as an American magazine serial beginning in 1910.  Set in England, it is one of Burnett's most popular novels and is considered a classic of English children's literature.  Several stage and film adaptations have been made.\n\nThe Secret Garden (1949 film): The Secret Garden is a 1949 US drama film.  It is the second screen adaptation of the classic 1911 novel by Frances Hodgson Burnett (the first adaption was a silent version filmed in 1919) which starred Lila Lee and Spottiswoode Aitken.  The screenplay by Robert Ardrey was directed by Fred M. Wilcox.  It centers on a young orphan who is thrust into the dark and mysterious lives of her widowed uncle and his crippled son when she comes to live with them in their isolated country house in Yorkshire, England.  A 1987 \"Hallmark Hall of Fame\" TV film, \"The Secret Garden\" stars Gennie James and Jadrien Steele.  A later adaptation \"The Secret Garden\" was made starring Kate Maberly and Heydon Prowse.\n\nGarden sanctuary: The concept of the Garden Sanctuary follows on from the popular understanding of a therapeutic \"Secret Garden\" first imagined by Frances Hodgson Burnett.\n\nThe Secret Garden (1993 film): The Secret Garden is a 1993 American-British drama fantasy film directed by Agnieszka Holland and starring Kate Maberly, Heydon Prowse, Andrew Knott, John Lynch and Maggie Smith.  It was written by Caroline Thompson and based on the novel of the same name by Frances Hodgson Burnett.  There are two previous film adaptations: a 1949 US drama film; and the screen adaptation as a silent version filmed in 1919, which starred Lila Lee and Spottiswoode Aitken.\n\nMine for Keeps: Mine for Keeps is a 1962 book by the Canadian children's author Jean Little.  At the time she wrote \"Mine for Keeps\", Little was teaching in a school for the disabled and she had written the book after becoming tired of reading her students books in which disabled child characters either meet deaths or recover completely (like Clara in \"Heidi\", or Colin in \"The Secret Garden\").\n\nAnn Thwaite: Ann Thwaite (born 4 October 1932) is a British writer who is the author of five major biographies.  \"AA Milne: His Life\" was the Whitbread Biography of the Year, 1990.  \"Edmund Gosse: A Literary Landscape\" (Duff Cooper Prize,1985) was described by John Carey as \"magnificent - one of the finest literary biographies of our time\".  \"Glimpses of the Wonderful\" about the life of Edmund's father, Philip Henry Gosse, was picked out by DJ Taylor in the Independent as one of the \"Ten Best Biographies\" ever.  Frances Hodgson Burnett was originally published (1974) as \"Waiting for the Party\" and reissued in 2007 with the sub-title \"Beyond the Secret Garden\".  \"Emily Tennyson, The Poet's Wife\" (1996) was reissued by Faber Finds for the Tennyson bicentenary in 2009.\n\nThe Secret Garden (opera): The Secret Garden is an opera by Nolan Gasser with a libretto (based on the novel by Frances Hodgson Burnett) written by Carey Harrison.  Commissioned by the San Francisco Opera and presented in partnership with Cal Performances, it premiered on March 1, 2013, at Zellerbach Hall at the University of California, Berkeley.\n\nQuestion: The 1962 children's novel Mine for Keeps was written by which  Canadian children's author as a different plot twist after Frances Hodgson Burnett's The Secret Garden?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"book_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the book being discussed.\"\n    },\n    \"author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the book.\"\n    },\n    \"author_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the author.\"\n    },\n    \"publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the book was published.\"\n    },\n    \"inspired_by_novel\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel that influenced the author's approach.\"\n    },\n    \"reason_for_different_approach\": {\n      \"type\": \"string\",\n      \"description\": \"The author's motivation for writing a different plot twist or approach compared to the inspired novel, specifically regarding disabled characters.\"\n    }\n  },\n  \"required\": [\n    \"book_title\",\n    \"author\",\n    \"author_nationality\",\n    \"publication_year\",\n    \"inspired_by_novel\",\n    \"reason_for_different_approach\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "book_title": {
        "type": "string",
        "description": "The title of the book being discussed."
      },
      "author": {
        "type": "string",
        "description": "The author of the book."
      },
      "author_nationality": {
        "type": "string",
        "description": "The nationality of the author."
      },
      "publication_year": {
        "type": "integer",
        "description": "The year the book was published."
      },
      "inspired_by_novel": {
        "type": "string",
        "description": "The title of the novel that influenced the author's approach."
      },
      "reason_for_different_approach": {
        "type": "string",
        "description": "The author's motivation for writing a different plot twist or approach compared to the inspired novel, specifically regarding disabled characters."
      }
    },
    "required": [
      "book_title",
      "author",
      "author_nationality",
      "publication_year",
      "inspired_by_novel",
      "reason_for_different_approach"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
