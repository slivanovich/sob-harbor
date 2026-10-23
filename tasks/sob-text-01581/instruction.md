{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNew school hip hop: The new school of hip hop was a movement in hip hop music starting 1983–84 with the early records of Run–D.M.C. and LL Cool J.  Like the hip hop preceding it, it came predominantly from New York City.  The new school was initially characterized in form by drum machine led minimalism, often tinged with elements of rock.  It was notable for taunts and boasts about rapping, and socio-political commentary, both delivered in an aggressive, self-assertive style.  In image as in song its artists projected a tough, cool, street b-boy attitude.  These elements contrasted sharply with the funk and disco influenced outfits, novelty hits, live bands, synthesizers and party rhymes of artists prevalent in 1984, and rendered them old school.  New school artists made shorter songs that could more easily gain radio play, and more cohesive LPs than their old school counterparts.  By 1986 their releases began to establish the hip hop album as a fixture of the mainstream.\n\nAlessandra Marc: Alessandra Marc (born July 29, 1957) is an American dramatic soprano who has appeared at many of the world's opera houses and orchestras.  Marc is particularly known for her interpretations of the works of Richard Strauss, Richard Wagner, Giuseppe Verdi, music of the Second Viennese School, and the title role in Puccini's \"Turandot\".\n\nStephen Cohn: Stephen Cohn is an American composer of concert and film music living in Los Angeles, California.  His compositional style embraces an expanded tonality with a 21st-century perspective.\n\nAdam Schoenberg: Adam Schoenberg (born November 15, 1980) is one of the most performed living American composers.  A member of the Atlanta School of Composers, his works have been performed by the Amarillo Symphony, Atlanta Symphony Orchestra, Buffalo Philharmonic Orchestra, Charleston Symphony Orchestra, Charlotte Symphony Orchestra, The Cleveland Orchestra, Dallas Symphony Orchestra, The Florida Orchestra, Fort Worth Symphony Orchestra, Grand Rapids Symphony, Jacksonville Symphony, Kansas City Symphony, Knoxville Symphony Orchestra, Lake Forest Symphony Orchestra, Lexington Philharmonic, Los Angeles Philharmonic, National Symphony Orchestra, New West Symphony, New World Symphony (orchestra), New York Philharmonic, Orlando Philharmonic Orchestra, Pacific Symphony, Phoenix Symphony, Rochester Philharmonic Orchestra, San Diego Symphony, South Carolina Philharmonic, Tallahassee Symphony Orchestra, Waterloo-Cedar Falls Symphony, among other ensembles.  Schoenberg was the 2010-2012 guest composer for the Aspen Music Festival, the 2012-2013 composer-in-residence for the Kansas City Symphony, the 2013-2014 composer-in-residence for the Lexington Philharmonic, and the 2015-2017 composer-in-residence for the Fort Worth Symphony.  Schoenberg's honors include a 2009 and 2010 MacDowell Colony fellowship, the 2007 Morton Gould Young Composer Award from ASCAP, and the 2006 Charles Ives Prize from the American Academy of Arts & Letters.\n\nErwin Stein: Erwin Stein (7 November 188517 July 1958) was an Austrian musician and writer, prominent as a pupil and friend of Schoenberg, with whom he studied between 1906 and 1910.  He was one of Schoenberg's principal assistants in organizing the Society for Private Musical Performances.  In 1924 it was Stein to whom Schoenberg entrusted the delicate as well as important task of writing the first article – \"Neue Formprinzipien\" ('New Formal Principles') – on the gradual evolution of what was soon to be explicitly formulated as 'twelve tone technique'.  Until 1938 he lived in Vienna, where he was respected as a music teacher and conductor as well as a writer active on behalf of the music and composers he valued.\n\nSecond Viennese School: The Second Viennese School (German: Zweite Wiener Schule, Neue Wiener Schule ) is the group of composers that comprised Arnold Schoenberg and his pupils and close associates in early 20th century Vienna, where he lived and taught, sporadically, between 1903 and 1925.  Their music was initially characterized by late-Romantic expanded tonality and later, following Schoenberg's own evolution, a totally chromatic expressionism without firm tonal centre, often referred to as atonality; and later still, Schoenberg's serial twelve-tone technique.  Though this common development took place, it neither followed a common time-line nor a cooperative path.  Likewise, it was not a direct result of Schoenberg's teaching—which, as his various published textbooks demonstrate, was highly traditional and conservative.  Schoenberg's textbooks also reveal that the Second Viennese School spawned not from the development of his serial method, but rather from the influence of his creative example.\n\nBrown–Vialetto–Van Laere syndrome: Brown-Vialetto-Van-Laere syndrome (BVVL), sometimes known as Brown's Syndrome, is a rare degenerative disorder often initially characterized by progressive sensorineural deafness.\n\nSergio Nasca: Born in Rome, Nasca started his career in 1965 as assistant director of Enzo Battaglia in \"Idoli controluce\", then he worked as a production manager.  He made his film debut in 1974 with \"Il saprofita\", a film which raised several controversities for its violence.  His cinema was initially characterized by violent provocations gradually tempered by bittersweet tones.  He died at the age of 52 of an incurable disease.\n\nHenri Sauguet: Henri Sauguet (18 May 1901 – 22 June 1989), was a French composer.  Born in Bordeaux as Henri-Pierre Poupard, he adopted his mother's maiden name as his pseudonym.  His output includes operas, ballets, four symphonies (1945, 1949, 1955, 1971), concertos, chamber and choral music and numerous songs, as well as film music.  Although he experimented with musique concrète and expanded tonality, he remained opposed to particular systems and his music evolved little: he developed tonal or modal ideas in smooth curves, producing an art of clarity, simplicity and restraint.\n\nMarilyn Cotlow: Marilyn Cotlow (born January 10, 1924) is an American lyric coloratura soprano best remembered for originating the role of Lucy in Gian Carlo Menotti's \"The Telephone\".  She sang professionally during the 1940s and 1950s in the United States and Europe, performing with such companies as the Metropolitan Opera.  After retiring from the stage, Cotlow taught voice at the Peabody Conservatory and currently teaches privately out of her home.  Several of her students have gone on to have successful careers, including Alessandra Marc and Jennifer Wilson.\n\nQuestion: What school is a group of composers, interpreted by the soprano Alessandra Marc and was initially characterized by expanded tonality and Schoenberg's own evolution? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musical school or movement.\"\n    },\n    \"school_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of group or movement the school represents.\"\n    },\n    \"location_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The primary city where the school originated or was active.\"\n    },\n    \"initial_characteristics\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Key musical characteristics that initially defined the school's style.\"\n    },\n    \"evolution_influenced_by\": {\n      \"type\": \"string\",\n      \"description\": \"The composer whose evolution influenced the school's later development.\"\n    },\n    \"known_interpreters\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"artist_name\": {\n            \"type\": \"string\"\n          },\n          \"artist_role\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"artist_name\",\n          \"artist_role\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Artists known for interpreting the works of this school.\"\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"school_type\",\n    \"location_of_origin\",\n    \"initial_characteristics\",\n    \"evolution_influenced_by\",\n    \"known_interpreters\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The name of the musical school or movement."
      },
      "school_type": {
        "type": "string",
        "description": "The type of group or movement the school represents."
      },
      "location_of_origin": {
        "type": "string",
        "description": "The primary city where the school originated or was active."
      },
      "initial_characteristics": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Key musical characteristics that initially defined the school's style."
      },
      "evolution_influenced_by": {
        "type": "string",
        "description": "The composer whose evolution influenced the school's later development."
      },
      "known_interpreters": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "artist_name": {
              "type": "string"
            },
            "artist_role": {
              "type": "string"
            }
          },
          "required": [
            "artist_name",
            "artist_role"
          ],
          "additionalProperties": false
        },
        "description": "Artists known for interpreting the works of this school."
      }
    },
    "required": [
      "school_name",
      "school_type",
      "location_of_origin",
      "initial_characteristics",
      "evolution_influenced_by",
      "known_interpreters"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
