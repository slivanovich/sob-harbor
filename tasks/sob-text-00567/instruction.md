{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWinfred Blevins: Win Blevins (born October 21, 1938) is a New York Times Bestselling American author of historical fiction, narrative non-fiction, historical fantasy, and non-fiction books, as well as short stories, novellas, articles, reviews, and screenplays.  He has written many books about the western mountain trappers, and is known for his \"mastery of western lore.\"  His notable works include Stone Song, So Wild a Dream, and Dictionary of the American West.  According to WorldCat, the Dictionary of the American West is held in 728 libraries.  Blevins has won numerous awards, including being named winner of the Owen Wister Award for Lifetime Achievement in writing literature of the West, being selected for the Western Writers Hall of Fame, being twice named 'Writer of the Year' by Wordcraft Circle of Native Writers, and winning two Spur Awards for Novel of the West.\n\nKristin Hannah: Kristin Hannah (born September 25, 1960) is an award-winning and bestselling American writer, who has won numerous awards, including the Golden Heart, the Maggie, and the 1996 National Reader's Choice award.\n\nThe Nightingale (2015 novel): The Nightingale is a historical fiction novel, written by Kristin Hannah and published in 2015.  It tells the story of two sisters in France on the eve of World War II, and their struggle to survive and resist the German occupation of France.  It was inspired by the story of a Belgian woman, Andrée de Jongh, who helped downed Allied pilots to escape Nazi territory.  The book sold well, earning places on several bestseller lists, and was optioned for a screen adaptation by TriStar Pictures in March 2015.\n\nRed Queen (novel): Red Queen is a young adult fantasy novel written by American writer Victoria Aveyard.  It was her first series and her first novel.  It was published in February 2015.  Its sequels are \"Glass Sword\" and \"King's Cage\".  Red Queen won the 2015 Goodreads Choice Award for Debut Goodreads Author and was nominated for the 2015 Goodreads Choice Award for Young Adult Fantasy & Science Fiction.\n\nSarah Addison Allen: Sarah Addison Allen (also known under the pen name Katie Gallagher) is an American and New York Times bestselling author.  She grew up in Asheville, North Carolina and attended the University of North Carolina at Asheville, where she graduated with a degree in literature.  In early 2011 Allen was diagnosed with breast cancer and completed a round of chemotherapy by October of the same year.  Addison has won numerous awards for her work including; 2008 SIBA Book Award for fiction for her novel garden spells, Best Women's Fiction of 2007 by the American Library Association's Reading List, 2008 RT Reviewers Choice Award for Women's Fiction for her novel the sugar queen and, the department of Literature at UNC Asheville named Addison the 2015 Goodman Endowed Artist.  As a child she aspired to be a waste management technician but decided to pursue writing once she graduated from college.  When asked about her writing process she said; \"I start with a loose storyline, then see where it goes\" Her books have been translated into 30 languages and sold nearly 2 million copies\n\nCarolly Erickson: Carolly Erickson (born January 1, 1943) is an American author of historical fiction and non-fiction.  She lives in Hawaii.  In 2008, her book \"The Tsarina's Daughter\" won the RT Reader's Choice Award for best Historical Fiction.\n\nRobin House Wells: Robin Rouse Wells is an American author of romance novels.  She received her entry into the publishing world in 1995, when she won the Romance Writers of America's Golden Heart Award for previously unpublished writers.  Silhouette Books promptly purchased her winning novel, \"The Wedding Kiss\".  Within seven months, they had purchased two additional novels from her.  She has since twice won the National Reader's Choice Award, given by the Oklahoma Romance Writers of America.  She has also won the Holt Medallion from the Virginia Romance Writers of America and the Award of Excellence from the Colorado Romance Writers of America.\n\nEd Lin: Ed Lin is a Taiwanese-American writer, actor and novelist.  He is the first author to win three Asian American Literary Awards.  His first novel, \"Waylaid\" (2002) won a Members' Choice Award at the Asian American Literary Awards and also a Booklist Editors' Choice Award in Fiction in 2002.  Lin has written a series of crime novels revolving around Chinese-American cop Robert Chow set in 1976 New York City Chinatown, which begins in \"This Is A Bust\" (2007) (Kaya Press), which won a Members' Choice Award at the Asian American Literary Awards, and continues with \"Snakes Can't Run\" (2010) (Minotaur Books) and \"One Red Bastard\" (2012) (Minotaur Books).\n\nThe Queen's Fool: The Queen's Fool by Philippa Gregory is a 2004 historical fiction novel.  Set between 1548 and 1558, it is part of Philippa Gregory's Tudor series.  The series includes \"The Boleyn Inheritance\".  The novel chronicles the changing fortunes of Mary I of England and her half-sister Elizabeth through the eyes of the fictional Hannah Green, a Marrano girl escaping to England from Spain where her mother was burned at the stake for being Jewish.  Hannah is discovered by Robert Dudley and John Dee and subsequently begged as a fool to Edward VI.  She witnesses and becomes caught up the intrigues of the young king's court, and later those of his sisters.  As Mary, Elizabeth, and Robert Dudley use Hannah to gather information on their rivals and further their own aims, the novel can plausibly present each side in the complex story.  \"The Queen's Fool\" follows Hannah from ages fourteen to nineteen, and her coming-of-age is interspersed among the historical narrative (see Bildungsroman).  The book reached # 29 on the \"New York Times\" Best Seller list and had sold 165,000 copies within three weeks of its release.\n\nDeb Caletti: Deb Caletti (born June 16, 1963) is an American writer of young adult and adult fiction.  Caletti is a National Book Award finalist, as well as the recipient of other numerous awards including the PEN USA finalist award, the Washington State Book Award, and SLJ Best Book award.  Caletti's books feature the Pacific Northwest, and her young adult work is popular for tackling difficult issues typically reserved for adult fiction.  Her first adult fiction novel, \"He's Gone\", was published by Random House in 2013 and was followed by her second book for adults, \"The Secrets She Keeps\" in 2015.\n\nQuestion: The Nightingale is a historical fiction novel, published in 2015, and written by Kristin Hannah, an award-winning and bestselling American writer, who has won numerous awards, including the Golden Heart, the Maggie, and the National Reader's Choice award, in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author.\"\n    },\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award won by the author.\"\n    },\n    \"award_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the author won the specified award.\"\n    },\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel mentioned in the question.\"\n    },\n    \"novel_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the novel.\"\n    },\n    \"novel_publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the novel.\"\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"award_name\",\n    \"award_year\",\n    \"novel_title\",\n    \"novel_genre\",\n    \"novel_publication_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The name of the author."
      },
      "award_name": {
        "type": "string",
        "description": "The name of the award won by the author."
      },
      "award_year": {
        "type": "integer",
        "description": "The year the author won the specified award."
      },
      "novel_title": {
        "type": "string",
        "description": "The title of the novel mentioned in the question."
      },
      "novel_genre": {
        "type": "string",
        "description": "The genre of the novel."
      },
      "novel_publication_year": {
        "type": "integer",
        "description": "The publication year of the novel."
      }
    },
    "required": [
      "author_name",
      "award_name",
      "award_year",
      "novel_title",
      "novel_genre",
      "novel_publication_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
