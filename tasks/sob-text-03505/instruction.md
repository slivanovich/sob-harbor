{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEverybody Cha-cha-cha: Everybody Cha-cha-cha (; also known as Jolly Widows) is a South Korean romance musical drama starring Shim Hye-jin, Lee Jong-soo, Park Hae-mi, Lee Chung-ah, Park Han-byul and Jo An.  It aired on KBS1 from June 29, 2009 to January 29, 2010 on Mondays to Fridays at 20:25 for 155 episodes.\n\nEverybody Has Secrets: Everybody Has Secrets () is a 2004 South Korean romantic comedy film.  It stars Lee Byung-hun, Choi Ji-woo, Kim Hyo-jin and Chu Sang-mi.  Because it has several sex-scenes, it is generally restricted to viewers under 18 or 21.  Although the film wasn't a particularly big hit in South Korea it grossed $4,888,679 in Japan.\n\nTemptation of Wolves: Temptation of Wolves (; also known as Romance of Their Own or True Romance) is a 2004 South Korean film directed by Kim Tae-kyun, and based on a novel of the same name by Internet author Guiyeoni.  Starring Jo Han-sun, Kang Dong-won and Lee Chung-ah, the film is about an average high school girl who moves from the countryside to Seoul after her father's death only to become involved in a love triangle with the two most handsome and popular guys in town.\n\nLee Jung-gook: Lee Jung-gook (born August 20, 1957) is a South Korean film director and screenwriter.  Lee's feature debut \"Song of Resurrection\" (1990) was banned as its plot deals with the 1980 Gwangju Uprising.  However, he won critical acclaim for his second feature \"The Story of Two Women\" (1994) by winning numerous awards at the 32nd Grand Bell Awards, including Best Film, Best New Director and Best New Actress, and Best New Director at the 14th Korean Association of Film Critics Awards in 1994.  He proved his box office senses with \"The Letter\" (1997) that created a wave of melodrama in the Korean movie industry.  A Thai version of \"The Letter\" was made in 2004, with the same title.\n\nFlower Boy Ramen Shop: Flower Boy Ramen Shop () is a 2011 South Korean romantic comedy television series, starring Jung Il-woo, Lee Chung-ah, Lee Ki-woo, Park Min-woo and Cho Yoon-woo.  It aired on cable channel tvN from October 31 to December 20, 2011, on Wednesdays and Thursdays at 23:00 for 16 episodes.\n\nThe Phone (film): The Phone (Korean: 더 폰) is a 2015 South Korean fantasy thriller film directed by Kim Bong-ju.  The film is the directorial debut of the director.  It was released on October 22, 2015.  This movie is not to be confused with another South Korean movie of similar title but released in 2002 or with the American TV series and the Dutch TV reality show both of which have the same title as this movie.\n\nPure Pumpkin Flower: Pure Pumpkin Flower () is South Korean television series starring Lee Chung-ah, Bae Jong-ok, Jin Tae-hyun and Jang Hyun-sung.  It aired on SBS on Mondays to Fridays at 19:20 from November 15, 2010 to May 13, 2011 for 124 episodes.\n\nLee Chung-ah: Lee Chung-ah (born October 29, 1984) is a South Korean actress.  She is best known for her leading roles in the movies \"Temptation of Wolves\" (2004) and \"My Tutor Friend 2\" (2007), as well as the cable drama \"Flower Boy Ramen Shop\" (2011).\n\nDeath Bell: Death Bell () is a 2008 South Korean film.  The only Korean horror film released over the summer of 2008, it is the first feature by former music video director Chang (real name Yoon Hong-seung), who also co-wrote the screenplay.  \"Death Bell\" stars Lee Beom-soo in his first horror film role, and K-pop singer Nam Gyu-ri in her acting debut.  Set in a Korean high school, the film's native title refers to \"gosa\", the important midterm exams that all students are required to sit.\n\nLady Vengeance: Lady Vengeance (; lit.  \"Kind-hearted Geum-ja\"; Korean English title: Sympathy for Lady Vengeance) is a 2005 South Korean psychological thriller film by director Park Chan-wook.  The film is the third installment in Park's \"The Vengeance Trilogy\", following \"Sympathy for Mr. Vengeance\" (2002) and \"Oldboy\" (2003).  It stars Lee Young-ae as Lee Geum-ja, a woman released from prison after serving the sentence for a murder she did not commit.  The film tells her story of revenge against the real murderer.\n\nQuestion: By what other title is the 2004 South Korean movie which stars Lee Chung-ah called?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The primary title of the South Korean movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"main_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor specified in the question.\"\n    },\n    \"alternative_titles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of other titles by which the movie is known.\"\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The specific alternative title that answers the question.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"main_actor\",\n    \"alternative_titles\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The primary title of the South Korean movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "main_actor": {
        "type": "string",
        "description": "The name of the actor specified in the question."
      },
      "alternative_titles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of other titles by which the movie is known."
      },
      "answer": {
        "type": "string",
        "description": "The specific alternative title that answers the question."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "main_actor",
      "alternative_titles",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
