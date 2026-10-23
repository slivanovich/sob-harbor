{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhilip Levine (poet): Philip Levine (January 10, 1928 – February 14, 2015) was an American poet best known for his poems about working-class Detroit.  He taught for more than thirty years in the English department of California State University, Fresno and held teaching positions at other universities as well.  He served on the Board of Chancellors of the Academy of American Poets from 2000 to 2006, and was appointed Poet Laureate of the United States for 2011–2012.\n\nDafydd Llwyd Mathau: Dafydd Llwyd Mathau was a 17th century Welsh poet and strolling minstrel.  It is thought he may have been from the Llangeitho area.  His works include poems written in praise of prominent Welsh families, and a number of love poems.  He is also known to have composed an awdl style verse in 1611.\n\nJ. K. Annand: James King Annand MBE (2 February 1908 – 8 June 1993) was a Scottish poet best known for his children's poems.\n\nCiṟupañcamūlam: Siruppanchamulam(Tamil: சிருப்பஞ்சமுலம்) is a Tamil poetic work of didactic nature belonging to the \"Pathinenkilkanakku\" anthology of Tamil literature.  This belongs to the 'post Sangam period' corresponding to between 100 – 500 CE.  \"Siruppanchamulam\" contains 100 poems written by the poet Kariyaasaan.  He was probably a Jain by religious persuasion.  This and the fact that he was a student of one Makkayanaar is known from the introductory poem of this book.  The poems of \"Siruppanchamulam\" are written in the Venpa meter.\n\nJejuri (poem): Jejuri is the name of a series of poems written in 1976 by Arun Kolatkar, an Indian poet who wrote in Marathi and English.  \"Jejuri\" won the Commonwealth Prize in 1977.  The poem is made up of a series of often short fragments which describe the experiences of a secular visitor to the ruins of Jejuri, a pilgrimage site in Maharashtra.  It is one of the better known poems in modern Indian literature.\n\nHorae Canonicae: Horae Canonicae is a series of poems by W. H. Auden written between 1949 and 1955.  The title is a reference to the canonical hours of the Christian Church, as are the titles of the seven poems constituting the series: \"Prime\", \"Terce\", \"Sext\", \"Nones\", \"Vespers\", \"Compline\", and \"Lauds\".  Each refers to a fixed time of the day for prayer.\n\nW. H. Auden: Wystan Hugh Auden ( ; 21 February 1907 – 29 September 1973) was an English-American poet.  Auden's poetry was noted for its stylistic and technical achievement, its engagement with politics, morals, love, and religion, and its variety in tone, form and content.  He is best known for love poems such as \"Funeral Blues\", poems on political and social themes such as \"September 1, 1939\" and \"The Shield of Achilles\", poems on cultural and psychological themes such as \"The Age of Anxiety\", and poems on religious themes such as \"For the Time Being\" and \"Horae Canonicae.\"\n\nTom Leonard (poet): Tom Leonard (born 1944) is a Scottish poet, writer and critic.  He is best known for his poems written in the Glaswegian dialect of Scots, particularly his \"Six Glasgow Poems\" and \"The Six O'Clock News\".  His work frequently deals with the relationship between language, class and culture.\n\nDioscorus of Aphrodito: Flavius Dioscorus (Greek: Φλαύϊος Διόσκορος \"Flauios Dioskoros\") lived during the 6th century A.D. in the village of Aphrodito, Egypt, and therefore is called by modern scholars Dioscorus of Aphrodito.  Although he was an Egyptian, he composed poetry in Greek, the cultural language of the Byzantine Era.  His poems are the oldest surviving poems written by the hand of a known poet.  The manuscripts, which contain his corrections and revisions, were discovered on papyrus in 1905, and are now held in museums and libraries around the world.  Dioscorus was also occupied in legal work, and legal documents and drafts involving him, his family, Aphroditans, and others were discovered along with his poetry.  As an administrator of the village of Aphrodito, he composed petitions on behalf of its citizens, which are unique for their poetic and religious qualities.  Dioscorus was a Christian (a Copt) and lived in a religiously active environment.  The collection of Greek and Coptic papyri associated with Dioscorus and Aphrodito is one of the most important finds in the history of papyrology and has shed considerable light on the law and society of Byzantine Egypt.\n\nUncle Styopa: Uncle Styopa (Russian: Дядя Стёпа ; ] ), also known as Dyadya Stepa, is a series of poems written by Russian children's poet Sergey Mikhalkov.  They were written in trochaic tetrameter.  The poems featured a brave and noble \"militsioner\" (a policeman) who was unusual due to his extreme height.  The name of the protagonist of the series was Stepan Stepanov (Russian: Степан Степанов ), or Styopa, which is a diminutive of the Russian given name Stepan.  He performed various acts of good will, such as rescuing people, preventing train crashes, helping firefighters, stopping a school bully or working as a police officer for the Soviet Militsiya.  Styopa is a wise, brave, generous, noble, fun-loving character.  He fights against injustice and serves as an inspiration to the pioneers.\n\nQuestion: What is the name of the series of poems written between 1949 and 1955 by an English-American poet best known for \"Funeral Blues\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"poem_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the series of poems.\"\n    },\n    \"poet_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the poet.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the poet.\"\n        },\n        \"known_for_poem\": {\n          \"type\": \"string\",\n          \"description\": \"A well-known poem by the poet.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"known_for_poem\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"composition_period\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the poem series' composition.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the poem series' composition.\"\n        }\n      },\n      \"required\": [\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"number_of_poems\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of poems in the series.\"\n    },\n    \"individual_poem_titles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the titles of the individual poems within the series.\"\n    },\n    \"title_reference\": {\n      \"type\": \"string\",\n      \"description\": \"The cultural or religious reference for the series title.\"\n    }\n  },\n  \"required\": [\n    \"poem_series_name\",\n    \"poet_details\",\n    \"composition_period\",\n    \"number_of_poems\",\n    \"individual_poem_titles\",\n    \"title_reference\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "poem_series_name": {
        "type": "string",
        "description": "The name of the series of poems."
      },
      "poet_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the poet."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the poet."
          },
          "known_for_poem": {
            "type": "string",
            "description": "A well-known poem by the poet."
          }
        },
        "required": [
          "name",
          "nationality",
          "known_for_poem"
        ],
        "additionalProperties": false
      },
      "composition_period": {
        "type": "object",
        "properties": {
          "start_year": {
            "type": "integer",
            "description": "The start year of the poem series' composition."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the poem series' composition."
          }
        },
        "required": [
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "number_of_poems": {
        "type": "integer",
        "description": "The total number of poems in the series."
      },
      "individual_poem_titles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the titles of the individual poems within the series."
      },
      "title_reference": {
        "type": "string",
        "description": "The cultural or religious reference for the series title."
      }
    },
    "required": [
      "poem_series_name",
      "poet_details",
      "composition_period",
      "number_of_poems",
      "individual_poem_titles",
      "title_reference"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
