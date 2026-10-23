{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLindsay Jones (composer): Lindsay Jones (born on June 9, 1969, Durham, North Carolina) is an American composer and sound designer for theater, television and film.  He has also taught and lectured at numerous universities and schools across the country.\n\nErnst R. Kroeger: Ernest R. Kroeger (August 10, 1862 – April 7, 1934) was an American composer.  He is mainly known for the pedagogical works he composed for piano; he also taught music in St. Louis, Missouri.  Today his papers are held at the Missouri Historical Society.\n\nRobert Kurka: Robert Frank Kurka (December 22, 1921 – December 12, 1957) was an American composer, who also taught and conducted his own works.\n\nGaston Dufresne: Gaston Dufresne (September 9, 1898 – December 6, 1998) was the principal bassist in the Boston Symphony Orchestra from 1927 to 1957 and with the Florida West Coast Symphony from 1963 to 1979.  He also taught solfège, a singing technique used to teach pitch.  Among his contrabass students were American composer Leroy Anderson and Boston Symphony principal trumpeter Roger Voisin.  Dufresne taught solfège to Voisin and to Boston Symphony hornist Richard Mackey.\n\nJon Appleton: Jon Howard Appleton (born January 4, 1939) is an American composer and teacher who was a pioneer in electro-acoustic music.  His earliest compositions in the medium, e.g. Chef d'Oeuvre and Newark Airport Rock attracted attention because they established a new tradition some have called programmatic electronic music.  In 1970 he won Guggenheim, Fulbright and American-Scandinavian Foundation fellowships.  When he was twenty-eight years old he joined the faculty of Dartmouth College where he established one of the first electronic music studios in the United States.  He remained there intermittently for forty-two years.  In the mid-1970s he left Dartmouth to briefly become the head of Elektronmusikstudion (EMS) in Stockholm, Sweden.  In the late 1970s, together with Sydney Alonso and Cameron Jones he helped develop the first commercial digital synthesizer called the Synclavier.  For a decade he toured around the United States and Europe performing the compositions he composed for this instrument.  In the early 1990s he helped found the Theremin Center for Electronic Music at the Moscow Conservatory of Music where he continues to teach once a year.  He has also taught at Keio University (Mita) in Tokyo, Japan, CCRMA at Stanford University and the University of California Santa Cruz.  In his later years he has devoted most of his time to the composition of instrumental and choral music in a quasi-Romantic vein which has largely been performed only in France, Russia and Japan.\n\nLouis Campbell-Tipton: Louis Campbell-Tipton (1877–1921) was an American composer; a native of Chicago, Illinois, he was resident in Paris from 1901.  He felt that the prospects for performance of large-scale American works in the United States were bleak, and claimed that he had never wished to sacrifice the energy needed to complete a large work.  Even so, at his death a number of pieces for orchestra were found among his manuscripts, as were two operas.  During his life he was known mainly for his chamber music; he also taught theory for a time in Chicago.  One of his songs, \"A Spirit Flower\", was recorded by the Swedish tenor Jussi Bjorling.\n\nWilliam Bolcom: William Elden Bolcom (born May 26, 1938) is an American composer and pianist.  He has received the Pulitzer Prize, the National Medal of Arts, a Grammy Award, the Detroit Music Award and was named 2007 Composer of the Year by Musical America.  Bolcom taught composition at the University of Michigan from 1973–2008.  He is married to mezzo-soprano Joan Morris.\n\nGregg Wager: Gregg Wager (born September 16, 1958 in Adrian, Michigan) is an American composer, pianist, and music critic.  He studied composition at the University of Southern California and the California Institute of the Arts.  His teachers included Morton Subotnick and Morten Lauridsen.  His piano teachers included Yuriy Oliynyk, Doris Stevenson, and Chester Swiatkowski.  In 1996, he earned a Ph.D. in musicology at the Free University Berlin.\n\nMorten Lauridsen: Morten Johannes Lauridsen (born February 27, 1943) is an American composer.  A National Medal of Arts recipient (2007), he was composer-in-residence of the Los Angeles Master Chorale (1994–2001) and has been a professor of composition at the University of Southern California Thornton School of Music for more than 40 years.\n\nDavid E. Spencer: David E. Spencer is a retired professor of economics at Brigham Young University.  He taught and did research in macroeconomics, econometrics, and montetary theory.  He is the author of eighteen peer-reviewed publications including Econometrica, the American Economic Review, the Review of Economics and Statistics and the Journal of Money, Credit and Banking.  Spencer is a founding member of the BYU Macroeconomics and Computational Lab.  In addition to teaching various economics classes, Spencer also taught American Heritage at BYU for several years.\n\nQuestion: What American composer who won the National Medal of Arts in 2007, also taught American composer Gregg Wager?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American composer who meets the criteria.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the composer.\"\n    },\n    \"primary_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The primary profession of the composer.\"\n    },\n    \"awards_received\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"award_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the award received.\"\n          },\n          \"award_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the award was received.\"\n          }\n        },\n        \"required\": [\n          \"award_name\",\n          \"award_year\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of awards received by the composer, including the year.\"\n    },\n    \"taught_student_composer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"student_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the student composer taught by the identified composer.\"\n        },\n        \"student_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The primary profession of the student.\"\n        }\n      },\n      \"required\": [\n        \"student_name\",\n        \"student_profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"teaching_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role in which the composer taught the student.\"\n    }\n  },\n  \"required\": [\n    \"composer_name\",\n    \"nationality\",\n    \"primary_profession\",\n    \"awards_received\",\n    \"taught_student_composer\",\n    \"teaching_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_name": {
        "type": "string",
        "description": "The name of the American composer who meets the criteria."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the composer."
      },
      "primary_profession": {
        "type": "string",
        "description": "The primary profession of the composer."
      },
      "awards_received": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "award_name": {
              "type": "string",
              "description": "The name of the award received."
            },
            "award_year": {
              "type": "integer",
              "description": "The year the award was received."
            }
          },
          "required": [
            "award_name",
            "award_year"
          ],
          "additionalProperties": false
        },
        "description": "A list of awards received by the composer, including the year."
      },
      "taught_student_composer": {
        "type": "object",
        "properties": {
          "student_name": {
            "type": "string",
            "description": "The name of the student composer taught by the identified composer."
          },
          "student_profession": {
            "type": "string",
            "description": "The primary profession of the student."
          }
        },
        "required": [
          "student_name",
          "student_profession"
        ],
        "additionalProperties": false
      },
      "teaching_role": {
        "type": "string",
        "description": "The role in which the composer taught the student."
      }
    },
    "required": [
      "composer_name",
      "nationality",
      "primary_profession",
      "awards_received",
      "taught_student_composer",
      "teaching_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
