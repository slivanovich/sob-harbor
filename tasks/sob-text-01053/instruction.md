{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKanika Maheshwari: Kanika Maheshwari (born 24 April 1981) is an Indian television actress.  She is best known for her roles in serials like \"Kahaani Ghar Ghar Kii\", \"Raja Ki Aayegi Baraat\", \"Kabhi Aaye Na Judaai\", \"Viraasat\", \"Geet - Hui Sabse Parayi\" and \"Diya Aur Baati Hum\".  Kanika won Zee Gold Awards (2012-2013) and Star Parivaar Award (2012) for Best Actress in a Negative Role of Meenakshi in \"Diya Aur Baati Hum\".\n\nKabhi Aaye Na Judaai: Kabhi Aaye Na Judaai meaning \"Let Separation Never come\" was an Indian Hindi daily soap opera on STAR Plus.  It is a story of a united family which finds itself confronted with the biggest temptation of all times - money.  The show used to air every Monday to Thursday at 2pm and was produced by Deepti Bhatnagar.  It was replaced by Ekta Kapoor's show Kesar in 2004.\n\nKa Karoon Sajni Aaye Na Baalam: Ka Karoon Sajni Aye Na Baalam is a classical song of Hindustani classical music.  It is a Thumri sung in the raaga, Sindh Bhairavi Thumri.  It was popularised by legendary Hindustani vocalist, Bade Ghulam Ali Khan, Barkat Ali Khan, Bismillah Khan on shehnai, Pandit Ajoy Chakrabarty etc.\n\nBismillah Khan: He was awarded India's highest civilian honour, the Bharat Ratna, in 2001, becoming the third classical musician after M. S. Subbulakshmi and Ravi Shankar to be accorded this distinction.\n\nBismarck Myrick: Bismarck Myrick (born December 23, 1940) is a former U.S. Ambassador to the Republic of Liberia (1999–2002) and Lesotho (1995–1998).  He is a career member of the Senior Foreign Service and a decorated Vietnam War hero.  He represented the U.S. at the swearing in of South Africa’s first democratic parliament, led by Nelson Mandela.  The Kingdom of Lesotho conferred on him the Kingdom's highest honor to a non-citizen.  Liberia’s major newspapers and civil society organizations named him “Diplomat of the Year” or “Man of the Year” for three consecutive years.  The City Council appointed him Goodwill Ambassador for Goree Island, Senegal in 2008.  He was Political Officer in Liberia during the government of Samuel Doe.  He completed study projects in southern and western Africa every other year:2006-2012.  He graduated from the University of Tampa with honors and earned an M.A. degree from Syracuse University.  Spelman College awarded him a Doctor of Humane Letters degree.  Dr. Myrick is co-author of Three Aspects of Crisis in Colonial Kenya ; author of “The United States and Liberia” in The African Experience: Past, Present, and Future and author of scores of official documents.  Portsmouth, VA named two streets in his honor in 2001 and selected him as a 2006 “Portsmouth Notable” – the city’s highest honor.  He is featured in the March, 2013 edition of “The Citizen of Chesapeake” Newspaper.  Active in community service, he is on a number of boards, such as the World Affairs Council.\n\nJohn Levitow: John Lee Levitow (November 1, 1945 – November 8, 2000) was a United States Air Force (USAF) Loadmaster who received the Medal of Honor for exceptional heroism during wartime.  He was awarded the Medal of Honor for his acts of heroism while serving on board a Douglas AC-47 Spooky gunship of the 3d Special Operations Squadron USAF on February 24, 1969.  He became the lowest ranked serviceman in the Air Force to receive the Medal of Honor, the United States military's highest honor.\n\nMary Whyte: Mary Whyte (b.1953 Cleveland, Ohio) is an American watercolor artist, a traditionalist preferring a representational style, and the author of six published books, who has earned awards for her large-scale watercolors.  In 2016, the Portrait Society of America chose Whyte as the 2016 recipient of the Society’s Gold Medal, their highest honor.  In 2013, Whyte was awarded by the state of South Carolina, as the recipient of the South Carolina Arts Commission’s Elizabeth O'Neill Verner Governor’s Award for the Arts; the highest honor given to an artist in South Carolina.\n\nCharles Brown (Medal of Honor): Corporal Charles Brown (born 1849) was a US Marine who received the United States's highest honor for bravery, the Medal of Honor.  He was born in New York City, and enlisted in the Marine Corps from Hong Kong in June 1870, aboard the USS \"Ashuelot\" .  His Medal of Honor was approved under General Order No. 169, dated 8 February 1872.  There is no record of Brown having received his medal, as he deserted from the Marine Corps in October 1871, before the medal was approved.\n\nTansen (film): Tansen (Hindi: तानसेन) is a 1943 Indian Bollywood film directed by Jayant Desai and featuring K. L. Saigal and Khursheed Bano in the lead roles.  The film was based on Tansen, the 16th century musician in the court of Mughal emperor, Akbar. The film featured 13 hit songs, performed by the leads, including \"More Balapan Ke Saathi\", \"Rum Jhum Rum Jhum Chal Tihari\", \"Kahe Guman Kare Gori\", \"Bina Pankh Ka Panchhi\", \"Sapt Suran Teen Gram\", \"Diya Jalao\" and \"Baag Laga Doon Sajni\".  It was the second highest grossing Indian film of 1943.  In 2009 it was reported that another film based on the life of Tansen would be directed by Satish Kaushik.\n\nReidar Finsrud: Reidar Finsrud (born 5 March 1946, in Drøbak) is a Norwegian artist.  He was educated at the Norwegian National Academy of Craft and Art Industry majoring in graphical arts.  His 1970 thesis project \"Venezia\" received the honor \"commended to the King\" (\"laudabilis cum litteris commendatitiis\"), this was only the third time in the history of the school a student received this highest honor.\n\nQuestion: Ka Karoon Sajni Aaye Na Baalam was popularized by the artist who received what Indian highest honor in 2001?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"popularizing_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist who popularized the song.\"\n        },\n        \"award_received\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the highest honor received by the artist.\"\n            },\n            \"year\": {\n              \"type\": \"integer\",\n              \"description\": \"The year the honor was received.\"\n            },\n            \"description\": {\n              \"type\": \"string\",\n              \"description\": \"A description of the honor, indicating its significance.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"year\",\n            \"description\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"award_received\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"highest_honor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the highest Indian honor received by the artist in 2001.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"popularizing_artist\",\n    \"highest_honor_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "popularizing_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist who popularized the song."
          },
          "award_received": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the highest honor received by the artist."
              },
              "year": {
                "type": "integer",
                "description": "The year the honor was received."
              },
              "description": {
                "type": "string",
                "description": "A description of the honor, indicating its significance."
              }
            },
            "required": [
              "name",
              "year",
              "description"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "award_received"
        ],
        "additionalProperties": false
      },
      "highest_honor_name": {
        "type": "string",
        "description": "The name of the highest Indian honor received by the artist in 2001."
      }
    },
    "required": [
      "song_title",
      "popularizing_artist",
      "highest_honor_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
