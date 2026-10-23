{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrankenstein (2015 film): Frankenstein (stylised as FRANKƐN5TƐ1N) is a 2015 updated adaptation of Mary Shelley's \"Frankenstein\", directed by Bernard Rose.\n\nJeremy Suter: Jeremy Suter (born in London) is an English organist and choral director.  He was a chorister under Sir William McKie at Westminster Abbey.  He attended Harrow and later spent two years at the Royal College of Music before going to Oxford as Organ Scholar of Magdalen College under Bernard Rose.  Following a year at the University of Pennsylvania, Jeremy was invited to return to Magdalen College, Oxford, in order to direct the Chapel Choir whilst Bernard Rose took a sabbatical. In 1975 he was appointed Organist of the Civic Church of All Saints', Northampton and Director of Music at All Saints' Middle School.  Between 1981 and 1991 he was Assistant Organist at Chichester Cathedral and Director of Music at the Prebendal School.  He featured on many broadcasts and recordings made by the Choir of Chichester Cathedral.\n\nFast Film (film): Fast Film is a 2003 Austrian/Luxembourgian film directed by Virgil Widrich.  The film tells the story of a chase using scraps of other films.\n\nBernard Rose (director): Bernard Rose (born 4 August 1960) is an English film director most famous for his direction of the 1992 horror film \"Candyman\" and the 1994 historical romance film \"Immortal Beloved\".\n\nSx Tape: Sx_Tape (also stylized as SX_TAPE and sxtape) is a 2013 American found footage-horror film directed, edited, and photographed by Bernard Rose.  The film premiered on October 10, 2013 at the BFI London Film Festival and released to DVD on July 2, 2014.  It stars Caitlyn Folley and Ian Duncan as a young couple that decides to film a sex tape in an abandoned hospital, only to discover that it is not as abandoned as they believed it to be.\n\nHarold Rose: Harold Bernard Rose (May 1900 – May 1990) was an English football player and manager.\n\nVirgil Widrich: Virgil Widrich (* 16 May 1967 in Salzburg) is an Austrian director, screenwriter, filmmaker and multimedia artist.\n\nHalli Cauthery: Halli Cauthery (full name David Harald Cauthery) is a film and television composer.  His credits include the Netflix/DreamWorks animated comedy series \"Turbo F.A.S.T.\", for which he received an Emmy nomination in 2016; the thriller The East (film); Bernard Rose's 2015 adaptation of Frankenstein (2015 film); the Shrek Halloween television special \"Scared Shrekless\"; as well as the Lifetime Television film \"Living Proof\".\n\nTwo Jacks: Two Jacks is a 2012 comedy-drama film directed by Bernard Rose and starring Sienna Miller and Danny Huston.  It is an adaptation of Leo Tolstoy's short story \"Two Hussars\" and is Rose's fifth Tolstoy adaptation, which include \"Anna Karenina\" (1997), \"Ivans XTC\" (2002), \"The Kreutzer Sonata\" (2008) and \"Boxing Day\" (2012).  The film premiered in competition at the Montreal World Film Festival (August 23 to September 3, 2012).\n\nIvans Xtc: Ivans Xtc (sometimes stylized as ivansxtc) is 2000 British–American independent drama film co-written and directed by Bernard Rose and stars Danny Huston and Peter Weller.  It is based on Leo Tolstoy's novella \"The Death of Ivan Ilyich\" and is Rose's second adaptation of a work by Tolstoy, after the 1997 adaptation of \"Anna Karenina\".  The film premiered at the Toronto International Film Festival on September 12, 2000.  It was released in the United States (New York and Los Angeles) on July 7, 2002 and on July 19, 2002 in the United Kingdom.\n\nQuestion: Virgil Widrich and Bernard Rose, have which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_one\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first person.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of occupations for the first person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_two\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second person.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of occupations for the second person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mutual_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations shared by both people.\"\n    }\n  },\n  \"required\": [\n    \"person_one\",\n    \"person_two\",\n    \"mutual_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_one": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first person."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations for the first person."
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "person_two": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second person."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations for the second person."
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "mutual_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations shared by both people."
      }
    },
    "required": [
      "person_one",
      "person_two",
      "mutual_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
