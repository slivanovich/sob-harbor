{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStephanie Edwards (singer): Stephanie Edwards (born November 5, 1987) is an American singer and was the eleventh-place finalist on sixth season of \"American Idol\".  She is from Savannah, Georgia and first began singing around the age of two or three.  After graduating from Windsor Forest High School, Edwards pursued vocal instruction for a month and then went on to appear at the Apollo Theatre in New York when she competed in \"It's Showtime at the Apollo\".  Prior to \"American Idol\", she had won most singing contests she had entered, including \"Savannah Star\" in 2005.\n\nLily Carter: Lily Carter (born April 15, 1990) is an American pornographic actress.\n\nJohn A. Dramesi: Colonel John Arthur Dramesi (born February 12, 1933) is a retired United States Air Force (USAF) officer who was held as a prisoner of war at the Hanoi Hilton in North Vietnam during the Vietnam War.  Dramesi is one of only four members of the USAF to be twice awarded the Air Force Cross, the first for the mission on which he was shot down and captured, 2 April 1967, and the second for the six-month period following his second escape and recapture, from May to November 1969, when he was beaten and tortured.  He also received an award of the Silver Star for gallantry during an escape on 10 May 1967 and the month following his recapture, when he also was beaten and tortured.\n\nHaridhos Giri: Haridhos Giri (Hari-daas), affectionately called Guruji ,was born in the month of Margali(January) in the tamil calendar with the birth star of Utharattathi.  He was born in town of Thiruvannamalai, Tamil Nadu, South India\n\nShanna Moakler: Shanna Lynn Moakler (born March 28, 1975) is an American model, actress, and reality television star.  She was the winner of the Miss New York USA pageant in 1995 and was originally the first runner-up at Miss USA 1995.  She was eventually crowned Miss USA after Chelsi Smith won Miss Universe.  Moakler began modeling at age 15 and was later chosen as a Playmate of the Month for \"Playboy\" magazine in December 2001.  She hosted E!'s \"Bridalplasty\" during its two-month run in 2010/2011.\n\nChristian Baldini: Christian Baldini is an American, Italian and Argentine opera and orchestra conductor and composer.  He was born in Mar del Plata (Argentina) on August 25, 1978.  His CD \"Mozart Arias and Overtures\" conducting the Scottish Chamber Orchestra with soprano Elizabeth Watts was chosen as \"Recording of the Month\" by the BBC Music Magazine and MusicWeb International, CD of the Week by Classic FM, and received critical acclaim with 4- and 5-star reviews on Gramophone, Sinfini, The Guardian and Opera News.\n\nWasteland (film): Wasteland is a 2012 pornographic film.  It stars Lily Carter and Lily LaBeau in the lead roles, and is written and directed by Graham Travis.  The movie is highly praised in the adult business and has won several awards including the AVN Award for Best Movie in 2013.\n\nSuzanne Engo: Africa Yoon maiden name \"Suzanne Africa Engo\"' (born 17 November 1978) is a vegan celebrity activist and star of the documentary film \"I love Africa\" which has an online new media release with MTV Networks MTV ACT arm which will show the documentary online from WORLD AIDS DAY 1 December 2011 for the entire month of December 2011.  This is a film about the Africa 101 project charity run which saw the activist lose 100 pounds and run from New York City to Chicago to raise awareness about AIDS in Africa.  Engo is also founder and executive director of the New York AIDS Film Festival and President of Girl Behind the Camera Productions.\n\nTamara Witmer: Tamara Witmer (born March 21, 1984) is an American model, actress and reality television star.  She is best known for her appearance as \"Playboy's\" Playmate of the Month, Miss August 2005, the cover girl for the October 2006 issue and appeared as Miss May in the Playboy Playmate Video Calendar of 2007.\n\nYuzuki Aikawa: Yuzuki Aikawa (愛川 ゆず季 , Aikawa Yuzuki , born May 16, 1983) is a Japanese gravure idol and retired professional wrestler.  Starting her modeling career in 2003, Aikawa went on to become one of Japan's top gravure idols, earning the nickname \"The Gravure Queen of the Next Generation\" by appearing in various men's magazines, advertising campaigns, films, television programs and video games.  In 2010, Aikawa transitioned into professional wrestling, joining the newly founded World Wonder Ring Stardom promotion, becoming its public face and the inaugural holder of the Wonder of Stardom and Goddess of Stardom Championships. Aikawa's first year in professional wrestling ended with the \"Tokyo Sports\" magazine naming her the 2011 female wrestler of the year.  A year later, having successfully defended the Wonder of Stardom Championship throughout the year, while also winning the inaugural 5★Star GP, Aikawa became the first wrestler to win the award two times in a row.  Aikawa also produced six of her own independent wrestling events under the banner of \"Yuzupon Matsuri\", in the vein of her trainer Fuka Kakimoto's old \"Fuka Matsuri\" events.  Aikawa retired from professional wrestling on April 29, 2013.  She was never defeated for either of her championships, being stripped of the Goddess of Stardom Championship in October 2012, after her partner Yoko Bito was injured, and relinquishing the Wonder of Stardom Championship a month prior to her final match.\n\nQuestion: In what month was the star of Wasteland born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the star of the film.\"\n    },\n    \"star_birth_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"birth_month\": {\n          \"type\": \"string\",\n          \"description\": \"The month in which the star was born.\"\n        },\n        \"birth_day\": {\n          \"type\": \"integer\",\n          \"description\": \"The day of the month in which the star was born.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year in which the star was born.\"\n        }\n      },\n      \"required\": [\n        \"birth_month\",\n        \"birth_day\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"star_name\",\n    \"star_birth_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "star_name": {
        "type": "string",
        "description": "The name of the star of the film."
      },
      "star_birth_details": {
        "type": "object",
        "properties": {
          "birth_month": {
            "type": "string",
            "description": "The month in which the star was born."
          },
          "birth_day": {
            "type": "integer",
            "description": "The day of the month in which the star was born."
          },
          "birth_year": {
            "type": "integer",
            "description": "The year in which the star was born."
          }
        },
        "required": [
          "birth_month",
          "birth_day",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "star_name",
      "star_birth_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
