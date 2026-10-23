{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHidden Figures: Hidden Figures is a 2016 American biographical drama film directed by Theodore Melfi and written by Melfi and Allison Schroeder, based on the non-fiction book of the same name by Margot Lee Shetterly about black female mathematicians who worked at the National Aeronautics and Space Administration (NASA) during the Space Race.  The film stars Taraji P. Henson as Katherine Johnson, a mathematician who calculated flight trajectories for Project Mercury and other missions.  The film also features Octavia Spencer as NASA supervisor Dorothy Vaughan and Janelle Monáe as NASA engineer Mary Jackson, with Kevin Costner, Kirsten Dunst, Jim Parsons, Glen Powell, and Mahershala Ali in supporting roles.\n\nList of accolades received by Hidden Figures: \"Hidden Figures\" is a 2016 American biographical comedy-drama film directed by Theodore Melfi, and written by Melfi and Allison Schroeder, who adapted the screenplay from the non-fiction book \"Hidden Figures\" by Margot Lee Shetterly.  The film's plot focuses on female African-American mathematicians at NASA, specifically Katherine Johnson (played by Taraji P. Henson), who calculated flight trajectories for Project Mercury and the 1969 Apollo 11 flight to the Moon, Dorothy Vaughan (Octavia Spencer), and engineer Mary Jackson (Janelle Monáe).  Kevin Costner plays the supporting role of Al Harrison and Jim Parsons plays the role of Paul Stafford.  20th Century Fox gave the film a limited release from December 25, 2016, before a wide release on January 6, 2017.\n\nDorothy Vaughan: Dorothy Johnson Vaughan (September 20, 1910 – November 10, 2008) was an African American mathematician and human computer who worked for the National Advisory Committee for Aeronautics (NACA), and NASA, at Langley Research Center in Hampton, Virginia.  In 1949, she became acting supervisor of the West Area Computers, the first African-American woman to supervise a group of staff at the center.\n\nA Short Film About Wong Kar Wai: Harun has suddenly been abandoned by his long-time girlfriend whom he would have aimed to marry.  Following this heartbreak while wondering around, he came across a street film seller Erhan.  Erhan is a person who willing to make people happy with his films and change their vision and as well as having his own internal journey.  Harun dazzled by Wong Kar Wai movies (Chungking Express, In the mood for love, 2046, Happy Together) given to him by Erhan and become acting the characters in the movies.  He starts applying some of the scenes from the movies in his daily life and has tragicomic events.\n\nSudie L. Williams: Sudie Lawrence Williams (November 11, 1872–July 21, 1940) was a music educator in the public schools of Dallas, Texas.  She was born in Bellville, Texas to Dr. and Mrs. Otis Laurence Williams.  She began teaching in the Dallas schools in 1894, became assistant supervisor of music for the schools in 1910, acting supervisor in 1913 (the year the Dallas schools acquired their first phonograph), and supervisor in 1914.\n\nWest Area Computers: The West Area Computing Unit (West Area Computers) was an all-African American group of female mathematicians who worked as human computers at the Langley Research Center of NACA (predecessor of NASA) from 1943 through 1958.  The group, a subset of the hundreds of female mathematicians who began careers in aeronautical research during World War II, was originally subject to Virginia's Jim Crow laws, requiring them to use segregated bathrooms and cafeterias.\n\nBenjamin Wallfisch: Benjamin Wallfisch (born August 7, 1979) is an English composer, conductor, and pianist.  Since the mid-2000s, he has composed and contributed to music for over 60 feature films.  His compositions include original scores for \"A Cure For Wellness\", \"Hidden Figures\", \"Lights Out\", \"Desert Dancer\", and \"It\".  In 2017, he was jointly nominated with Pharrell Williams and Hans Zimmer for Best Original Score at the 74th Golden Globe Awards for his work on \"Hidden Figures\".\n\nMargot Lee Shetterly: Margot Lee Shetterly (born 1969) is an American nonfiction writer who has also worked in investment banking and media startups.  Her first book, \"Hidden Figures: The Story of the African-American Women Who Helped Win the Space Race\" (2016), is about African-American women mathematicians working at NASA who were instrumental to the success of the United States space program.  She sold the movie rights while still working on the book, and it was adapted as a feature film of the same name, \"Hidden Figures\" (2016).  For several years Shetterly and her husband lived and worked in Mexico, where they founded and published \"Inside Mexico,\" a magazine directed to English-speaking expats.\n\nCarefree Black Girls: Carefree Black Girls is a concept and movement that reportedly first emerged on the Tumblr platform; writer Zeba Blay was the first person to use the expression as a hashtag on Twitter in May 2013.  Danielle Hawkins soon launched a blog on Tumblr by the same name.  Writing at \"The Root\", Diamond Sharp describes \"carefree black girls\" as an idea black women \"have used...to anchor expressions of individuality and whimsy in the face of the heavy stereotypes and painful realities that too often color discussions of their demographic.\"  At \"Refinery29\", Jamala Johns said it was \"a way to celebrate all things joyous and eclectic among brown ladies.  Cultivated online and driven by social media, it’s one telling piece of a much wider development of inspiration assembled by and for black women.\"  At \"Jezebel\", Hillary Crosley Coker says \"ladies like Chiara de Blasio (with her hippie flower headband), Solange [Knowles] and her eclectic style and Janelle Monae's futurism are their patron saints.\"\n\nMarshal of the Senate of the Republic of Poland: The Marshal of the Senate of the Republic of Poland (Polish: Marszałek Senatu Rzeczypospolitej Polskiej ) is a presiding officer of the Senate of Poland.  He or she is also third person according to the Polish order of precedence, after President of the Republic of Poland and Sejm Marshal, and second in line to become Acting President of the Republic of Poland (after Sejm Marshal; in period 1935-1939 Senate Marshal was the first).\n\nQuestion: In what year did the person Janelle Monae portrayed in Hidden Figures become acting supervisor of the West Area Computers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_from_question\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person portrayed by the actor mentioned in the question.\"\n        },\n        \"portrayed_by_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who portrayed the person.\"\n        },\n        \"role_in_film\": {\n          \"type\": \"string\",\n          \"description\": \"The role or profession of the person in the film context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"portrayed_by_actor\",\n        \"role_in_film\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"supervisor_event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the supervisory event.\"\n        },\n        \"actual_supervisor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who actually became acting supervisor of the West Area Computers.\"\n        },\n        \"year_of_supervision\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the person became acting supervisor of the West Area Computers.\"\n        }\n      },\n      \"required\": [\n        \"event_description\",\n        \"actual_supervisor_name\",\n        \"year_of_supervision\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"clarification_note\": {\n      \"type\": \"string\",\n      \"description\": \"A note clarifying the relationship between the person from the question and the supervisor event.\"\n    }\n  },\n  \"required\": [\n    \"person_from_question\",\n    \"supervisor_event_details\",\n    \"clarification_note\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_from_question": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person portrayed by the actor mentioned in the question."
          },
          "portrayed_by_actor": {
            "type": "string",
            "description": "The name of the actor who portrayed the person."
          },
          "role_in_film": {
            "type": "string",
            "description": "The role or profession of the person in the film context."
          }
        },
        "required": [
          "name",
          "portrayed_by_actor",
          "role_in_film"
        ],
        "additionalProperties": false
      },
      "supervisor_event_details": {
        "type": "object",
        "properties": {
          "event_description": {
            "type": "string",
            "description": "Description of the supervisory event."
          },
          "actual_supervisor_name": {
            "type": "string",
            "description": "The name of the person who actually became acting supervisor of the West Area Computers."
          },
          "year_of_supervision": {
            "type": "integer",
            "description": "The year the person became acting supervisor of the West Area Computers."
          }
        },
        "required": [
          "event_description",
          "actual_supervisor_name",
          "year_of_supervision"
        ],
        "additionalProperties": false
      },
      "clarification_note": {
        "type": "string",
        "description": "A note clarifying the relationship between the person from the question and the supervisor event."
      }
    },
    "required": [
      "person_from_question",
      "supervisor_event_details",
      "clarification_note"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
