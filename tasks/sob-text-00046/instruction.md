{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCarmarthen Amateur Operatic Society: Carmarthen Amateur Operatic Society is a Welsh operatic society.  Established in 1891, it is the oldest musical society in Wales and the second oldest in the United Kingdom.\n\nLakeshore Light Opera: Lakeshore Light Opera (LLO), an amateur community theatre group, performs Gilbert and Sullivan operas in the West Island of Montreal, Canada.  The company produced its first show in 1955.  Early in its history, the group was directed by former D'Oyly Carte Opera Company member Doris Hemingway, and briefly conducted by her husband, former D'Oyly Carte conductor Harry Norris.  The group was known as St Paul's Operatic Society until 1980, when it changed its name to Lakeshore Light Opera.  For over 35 years, proceeds from its annual production have been contributed to the Lakeshore General Hospital.\n\nPurcell Operatic Society: The Purcell Operatic Society was a short-lived but influential London opera company devoted to the production of stage works by Henry Purcell and his contemporaries.  It was founded in 1899 by the composer Martin Shaw and folded in 1902.  Its stage director and production designer was Gordon Craig whose productions for the company marked the beginning of his career as a theatre practitioner.  Their debut production of Purcell's opera \"Dido and Aeneas\" in 1900 was one of the earliest staged performances of the work in modern times.\n\nZachary James: Zachary \"Zach\" James (born December 7, 1981) is an American actor and operatic bass.  He was the founding director of the Metropolis Opera Project, a New York City based opera company devoted to the development of new operatic works and is the General Director of Opera Ithaca in Ithaca, New York. .\n\nGeneva Amateur Operatic Society: The Geneva Amateur Operatic Society (GAOS) is claimed to be the largest English-speaking amateur operatic society in Europe.  Based in Geneva, GAOS was founded in 1971 by a small group of theatre enthusiasts.  They produce four productions per season, including their traditional English pantomime in the winter.  GAOS is a Non-profit organization, its members receive no payment and the society makes a point of giving a substantial donations to various charities around Geneva.\n\nHenry Purcell: Henry Purcell ( or ; c. 10 September 1659 – 21 November 1695) was an English composer.  Although incorporating Italian and French stylistic elements into his compositions, Purcell's legacy was a uniquely English form of Baroque music.  He is generally considered to be one of the greatest English composers; no other native-born English composer approached his fame until Edward Elgar, Ralph Vaughan Williams, William Walton and Benjamin Britten in the 20th century.\n\nGodfrey Ridout: Godfrey Ridout (6 May 1918 in Toronto – 24 November 1984 in Toronto) was a Canadian composer, conductor, music educator, and writer.  He contributed articles to numerous Canadian music publications, notably serving as the assistant editor of both \"Canadian Music\" (1940–1941) and \"Canadian Review of Music and Art\" (1942–1943).  From 1973–1984 he was the author of the Toronto Symphony Orchestra's program notes.  As a conductor he served as the music director of the Eaton Operatic Society from 1949–1958.  He was also highly involved with the Toronto Gilbert & Sullivan Society of which he was made an honorary vice-president.  As a composer, Ridout is chiefly remembered for his symphonic and choral works.  The Canadian Encyclopedia describes him thus: \"Essentially an eclectic, Ridout yet did not lack for individuality.  His music, though intensely felt, is prevailingly sunny and affirmative; it eschews the 'doom and gloom' manner and self-conscious profundity of much 20th-century concert fare.  Ridout liked fun in music and could not easily resist concluding a work with a 'good tune'.  He saw no need to strive for ever-new styles, or for a progress through styles, or for the role of musical inventor; style for him was a means of communication, not the 'message' itself.  In this aloofness from contemporary conformity, Ridout may be perceived to be more original than many innovators and one of the determined communicators of his day.\"\n\nManor Operatic Society: The Manor Operatic Society is an amateur operatic society based in Sheffield, England.\n\nNapier Operatic Society: Napier Operatic Society (often abbreviated as NOS) is an amateur theatre society based in Napier, New Zealand.  Established in 1887, Napier Operatic Society is the second oldest-existing theatrical society in New Zealand, and is nationally renowned for its critically acclaimed professional-quality productions.\n\nEaton Operatic Society: Eaton Operatic Society was a Canadian musical organization located in Toronto, Ontario that presented operas, operettas, musicals, and choral works from 1919 to 1965.  Originally a choir that specialized in mounting oratorios, the group eventually morphed into a light opera company in the early 1930s.\n\nQuestion: The Purcell Operatic Society was a company devoted to the works of which composer of Baroque-style music?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"operatic_society_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the operatic society.\"\n    },\n    \"devoted_composer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the composer whose works the society was devoted to.\"\n        },\n        \"musical_style\": {\n          \"type\": \"string\",\n          \"description\": \"The musical style associated with the composer.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the composer.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"musical_style\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"society_focus_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of what the society was devoted to producing.\"\n    }\n  },\n  \"required\": [\n    \"operatic_society_name\",\n    \"devoted_composer\",\n    \"society_focus_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "operatic_society_name": {
        "type": "string",
        "description": "The name of the operatic society."
      },
      "devoted_composer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the composer whose works the society was devoted to."
          },
          "musical_style": {
            "type": "string",
            "description": "The musical style associated with the composer."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the composer."
          }
        },
        "required": [
          "name",
          "musical_style",
          "nationality"
        ],
        "additionalProperties": false
      },
      "society_focus_description": {
        "type": "string",
        "description": "A description of what the society was devoted to producing."
      }
    },
    "required": [
      "operatic_society_name",
      "devoted_composer",
      "society_focus_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
