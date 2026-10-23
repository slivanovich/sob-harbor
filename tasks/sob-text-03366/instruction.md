{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBike for Three!: Bike for Three!  is a \"cross-continental collaboration\" between Canadian alternative hip hop artist Buck 65 (born Rich Terfry) and Belgian producer Greetings from Tuskan (born Joëlle Phuong Minh Lê).\n\nJohn Seward Johnson I: John Seward Johnson I (July 14, 1895 – May 23, 1983) was one of the sons of Robert Wood Johnson I (co-founder of Johnson & Johnson).  He was also known as J. Seward Johnson, Sr. and Seward Johnson.  He founded the Harbor Branch Oceanographic Institution (HBOI), and was the grandfather of Jamie Johnson, who directed the documentary \"Born Rich\".\n\nDutchman (play): Dutchman is a play written by African-American playwright Amiri Baraka, born Everett LeRoi Jones.  Dutchman was first presented at the Cherry Lane Theatre in Greenwich Village, New York City, on March 1964.  The play, which won an Obie Award.  was made into a film in 1967, starring Shirley Knight and Al Freeman Junior.  \"Dutchman\" was the last play produced by Baraka under his birth name, LeRoi Jones.  At the time, Baraka was in the process of divorcing his Jewish wife, Hettie Jones and embracing Black Nationalism.  The Dutchman may be described as a political allegory depicting black and white relations during the time Baraka wrote it.\n\nList of 2 Broke Girls episodes: \"2 Broke Girls\" is an American television sitcom created by Michael Patrick King and Whitney Cummings, who also serve as executive producers.  It airs on the CBS network.  The series stars Kat Dennings as Max Black, who comes from a poor underclass family, and Beth Behrs as Caroline Channing, who was born rich but is now down on her luck, working together at a restaurant in the Brooklyn neighborhood of Williamsburg.  Each episode ends with a running tally of the money earned out of the $250,000 the girls need to open a cupcake business, whether it increases or decreases.\n\nBeyond the Realm of Conscience: Beyond the Realm of Conscience is a 2009 Hong Kong television series.  Produced by Mui Siu-ching, the serial is one of two TVB productions to celebrate along with the channel's 42nd anniversary, the other being \"Born Rich\".  The drama aired five days a week on the TVB network with 45-minute episodes starting October 19, 2009.\n\nMore Heart Than Brains: More Heart Than Brains is the debut album by Bike for Three! , a collaboration between Canadian alternative hip hop artist Buck 65 (born Rich Terfry) and Belgian electronica producer Greetings from Tuskan (born Joëlle Phuong Minh Lê).  It was released on May 26, 2009 on Anticon.\n\nProvocateur (TV series): Provocateur () is a 2017 Hong Kong television drama produced by Wong Wai-sing and TVB.  It premiered on TVB Jade in Hong Kong, Hub Drama First in Singapore and Astro On Demand in Malaysia on 6 March 2017.  It stars Gallen Lo in his first TVB drama since 2009's \"Born Rich\".\n\nBaraka (film): Baraka is a 1992 non-narrative documentary film directed by Ron Fricke.  The film is often compared to \"Koyaanisqatsi\", the first of the Qatsi films by Godfrey Reggio for which Fricke served as the cinematographer.  \"Baraka\" is also the first film ever to be restored and scanned at 8K resolution.\n\nBorn Rich (TV series): Born Rich (Traditional Chinese: , literally \"Gate of Wealth\") is a 2009 Hong Kong television drama produced by TVB under executive producer Chong Wai-kin.  The drama was promoted as TVB's \"grand production\" for 2009.  Running for 39 episodes, the last two episodes were of two hours each.\n\nBorn Rich (film): Born Rich is a 2003 documentary film (filmed primarily between 1999-2001) about the experience of growing up in wealthy families.  It was created by Jamie Johnson, an heir to the Johnson & Johnson fortune.  The film consists primarily of Johnson interviewing 10 other young heirs.  These interviews are offset by Johnson's exploration of his own experience and family as he comes into a large inheritance on his 21st birthday.  He seeks out how to be a productive person, avoiding the dysfunction that he sees affecting many of the very rich.  The film explores the taboo the ultra rich have against about talking about their wealth.  Johnson believes this secrecy about wealth causes the wealthy to be dysfunctional, and exists because the discussion of their wealth challenges the notion that America is a meritocracy and their right to have their wealth.\n\nQuestion: Which documentary was released first, Baraka or Born Rich?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"documentaries_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\"\n          },\n          \"release_year\": {\n            \"type\": \"integer\"\n          },\n          \"is_documentary\": {\n            \"type\": \"boolean\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"release_year\",\n          \"is_documentary\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"earlier_release_film_title\": {\n      \"type\": \"string\"\n    },\n    \"year_difference\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in years between the release dates of the two films.\"\n    }\n  },\n  \"required\": [\n    \"documentaries_compared\",\n    \"earlier_release_film_title\",\n    \"year_difference\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "documentaries_compared": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "release_year": {
              "type": "integer"
            },
            "is_documentary": {
              "type": "boolean"
            }
          },
          "required": [
            "title",
            "release_year",
            "is_documentary"
          ],
          "additionalProperties": false
        }
      },
      "earlier_release_film_title": {
        "type": "string"
      },
      "year_difference": {
        "type": "integer",
        "description": "The difference in years between the release dates of the two films."
      }
    },
    "required": [
      "documentaries_compared",
      "earlier_release_film_title",
      "year_difference"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
