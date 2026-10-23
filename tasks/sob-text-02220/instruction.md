{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBonnie Rotten: Bonnie Rotten is the stage name of Alaina Hicks (born May 9, 1993), an American pornographic actress, feature dancer, fetish model, director, and producer.  She has been nominated for and has won many awards for her pornographic endeavors.  In 2014, she became the first alt porn star to win the AVN Award for Female Performer of the Year.\n\nStephanie Swift: Stephanie Swift (born February 7, 1972) is a former American pornographic actress who starred in over 300 adult movies between 1995 and 2009, when she was diagnosed with breast cancer and left the industry.  She is a member of both the AVN and XRCO Halls of Fame.  Swift now works with XXXchurch.com, a Christian outreach group that offers to help pornographic actors leave the industry and help compulsive porn users overcome their porn addiction.\n\nHollie Stevens: Hollie Stevens (January 4, 1982 – July 3, 2012) was the stage name of an American pornographic actress, wrestler, model and writer.  She was considered a pioneer of the porn genre known as \"clown porn\", which features actors in clown makeup.\n\nThyrsa Frazier Svager: Thyrsa Anne Frazier Svager (June 16, 1930 – July 23, 1999) was an American academic who was one of the first African-American women to gain a PhD in mathematics.  Born in Ohio, she graduated from high school at the age of 16, going to Antioch College in Ohio and then doing her postgraduate degrees at Ohio State University.  Frazier Svager was the head of the Department of Mathematics at Central State University (CSU) in Ohio for decades, ending her academic career as provost and dean for academic affairs.  She and her husband, physics professor Aleksandar Svager, invested one of their salaries during their careers to build a legacy for scholarships.  After her death, the Thyrsa Frazier Svager Fund was established to provide scholarships for African-American women majoring in mathematics.\n\nJeannie Pepper: Jeannie Pepper (born July 9, 1958 in Chicago, Illinois) is an American pornographic actress.  She began in the business in 1982 at age 24 and has appeared in over 200 adult films.  She was still an active actress as recently as 2007, participating in the mature adult genre.\n\nGeorgia Caldwell Smith: Georgia Caldwell Smith (1909–1961) was one of the first African-American women to gain a bachelor's degree in mathematics.  When she was 50, she went on to earn one of the early PhDs in mathematics by an African-American women, awarded posthumously in 1961.  Smith was the head of the Department of Mathematics at Spelman College.\n\nAngel Kelly: Angel Kelly is a retired pornographic actress.  With Jeannie Pepper and Heather Hunter, Kelly was among the first African-American women to \"cross over\" into mainstream porn video.  She is a member of the AVN Hall of Fame.\n\nDanyel Smith: Danyel Smith (born June 23, 1965) is an American magazine editor and journalist.  Smith is a 2014 John S. Knight Journalism Fellow at Stanford University.  She is also writing a history of African-American women in pop music.  Smith is also the former editor of \"Billboard\" and the first African-American editor of the magazine.  Also, she is the former chief content officer of Vibe Media Group and former editor-in-chief of \"Vibe\" and vibe.com.  She was the first African-American, and first female editor of \"Vibe\".\n\nOlivia O'Lovely: Olivia O'Lovely is a former American pornographic actress born in Santa Fe, New Mexico.  Her ethnic background is Italian, Spanish, Chilean and French.\n\nBree Olson: Rachel Marie Oberlin (born October 7, 1986 ), also known by her stage name Bree Olson, is an American glamour model, actress, national spokesperson, web personality, former pornographic actress and \"Penthouse\" Pet.  She performed in over 281 pornographic films from 2006 to 2011 before changing to mainstream acting.  Since leaving the industry, she has become vocally critical of the porn industry and the stigma attached to being a former porn actress.\n\nQuestion: What is the name of the American pornographic actress born in 1958 that, along with two other actresses, was among the first African-American women to \"cross over\" into mainstream porn video?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American pornographic actress.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actress.\"\n    },\n    \"is_african_american\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the actress is African-American.\"\n    },\n    \"pioneer_crossover_mainstream\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the actress was among the first African-American women to cross over into mainstream porn video.\"\n    },\n    \"other_pioneer_crossover_actresses\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the other actresses who were also among the first African-American women to cross over into mainstream porn video with her.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"birth_year\",\n    \"is_african_american\",\n    \"pioneer_crossover_mainstream\",\n    \"other_pioneer_crossover_actresses\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the American pornographic actress."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the actress."
      },
      "is_african_american": {
        "type": "boolean",
        "description": "Indicates if the actress is African-American."
      },
      "pioneer_crossover_mainstream": {
        "type": "boolean",
        "description": "True if the actress was among the first African-American women to cross over into mainstream porn video."
      },
      "other_pioneer_crossover_actresses": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the other actresses who were also among the first African-American women to cross over into mainstream porn video with her."
      }
    },
    "required": [
      "actress_name",
      "birth_year",
      "is_african_american",
      "pioneer_crossover_mainstream",
      "other_pioneer_crossover_actresses"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
