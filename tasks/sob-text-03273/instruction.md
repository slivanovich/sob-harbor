{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nZiegfeld Follies (film): Ziegfeld Follies is a 1946 American musical comedy film released by Metro-Goldwyn-Mayer and directed by Lemuel Ayers, Roy Del Ruth, Robert Lewis, Vincente Minnelli, Merrill Pye, George Sidney and Charles Walters.  It stars many of MGM leading talents, including Fred Astaire, Lucille Ball, Lucille Bremer, Fanny Brice (the only member of the ensemble who was a star of the original Follies), Judy Garland, Kathryn Grayson, Lena Horne, Gene Kelly, James Melton, Victor Moore, William Powell, Red Skelton, and Esther Williams.\n\nFlorenz Ziegfeld Jr.: Florenz Edward Ziegfeld Jr. (March 21, 1867 – July 22, 1932), popularly known as Flo Ziegfeld, was an American Broadway impresario, notable for his series of theatrical revues, the \"Ziegfeld Follies\" (1907–1931), inspired by the \"Folies Bergère\" of Paris.  He also produced the musical \"Show Boat\".  He was known as the \"glorifier of the American girl\".  Ziegfeld is a member of the American Theater Hall of Fame.\n\nIrvin C. Miller: Irvin Colloden Miller (February 19, 1884 – February 27, 1975) was an African-American actor, playwright and vaudeville show writer and producer.  He was responsible for successful theater shows including \"Broadway Rastus\" (1921), \"Liza\" (1922), \"Dinah\" (1923), which introduced the wildly popular black bottom dance, and \"Desires of 1927\" starring Adelaide Hall.  For thirty years he directed the popular review, \"Brown Skin Models\", influenced by the \"Ziegfeld Follies\" but exclusively using black performers.  \"In the 1920s and 1930s, he was arguably the most well-established and successful producer of black musical comedy.\"\n\nA Parisian Model: A Parisian Model is a 1906 Edwardian musical comedy with music by Max Hoffman, Sr. to a book and lyrics by Harry B. Smith.  The story concerns a dressmaker's model who comes into a fortune.  It opened on Broadway in 1906, ran with success and toured.  It was produced by Frank McKee and Florenz Ziegfeld Jr., and starred Anna Held, Ziegfeld's common law wife.  Soon after the success of this piece, Ziegfeld would launch his famous series of \"Ziegfeld Follies\" revues.\n\nVera Michelena: Vera Michelena (June 16, 1885 – August 28, 1961) was a Venezuelan American actress, contralto prima donna and dancer who appeared in light opera, musical comedy, vaudeville and silent film.  She was perhaps best remembered for her starring rôles in the musicals \"The Princess Chic\", \"Flo Flo\" and \"The Waltz Dream\", her rendition of the vampire dance in the musical \"Take It From Me\" and as a \"Ziegfeld Follies\" performer.\n\nSally (musical): Sally is a musical comedy with music by Jerome Kern, lyrics by Clifford Grey and book by Guy Bolton (inspired by the 19th century show, \"Sally in our Alley\"), with additional lyrics by Buddy De Sylva, Anne Caldwell and P. G. Wodehouse.  The plot hinges on a mistaken-identity: Sally, a waif, is a dishwasher at the Alley Inn.  She poses as a famous foreign ballerina and rises to fame (and finds love) through joining the Ziegfeld Follies.  There is a rags to riches story, a ballet as a centrepiece, and a wedding as a finale.  \"Look for the Silver Lining\" continues to be one of Kern's most familiar songs.  The song is lampooned by another song, \"Look for a Sky of Blue,\" in Rick Besoyan's satirical 1959 musical \"Little Mary Sunshine\".\n\nHelen Barnes: Helen Barnes (1895–1925) was an American musical comedy actress and Ziegfeld Follies Girl.\n\nGlorifying the American Girl: Glorifying the American Girl is a 1929 American Pre-Code, musical comedy film produced by Florenz Ziegfeld that highlights Ziegfeld Follies performers.  The last third of the film (which was filmed in early Technicolor) is basically a Follies production, with cameo appearances by Rudy Vallee, Helen Morgan, and Eddie Cantor.\n\nMary Nolan: Mary Nolan (December 18, 1902 – October 31, 1948) was an American stage and film actress, singer and dancer.  She began her career as a Ziegfeld girl in the 1920s performing under the stage name Imogene \"Bubbles\" Wilson.  She was fired from the \"Ziegfeld Follies\" in 1924 for her involvement in a tumultuous and highly publicized affair with comedian Frank Tinney.  She left the United States shortly thereafter and began making films in Germany.  She appeared in seventeen German films from 1925 to 1927 using a new stage name, \"Imogene Robertson\".\n\nLucille Bremer: Lucille Bremer (February 21, 1917 – April 16, 1996) was an American film actress and dancer.\n\nQuestion: Ziegfeld Follies is a 1946 American musical comedy film starring an american film actress who was also a what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American film actress.\"\n    },\n    \"actress_additional_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The additional profession of the actress besides being a film actress.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"actress_name\",\n    \"actress_additional_profession\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the American film actress."
      },
      "actress_additional_profession": {
        "type": "string",
        "description": "The additional profession of the actress besides being a film actress."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "actress_name",
      "actress_additional_profession"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
