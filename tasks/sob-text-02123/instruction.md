{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBob Sabiston: Bob Sabiston (born 1967) is an American film art director, computer programmer, and creator of the Rotoshop software program for computer animation.  Sabiston began developing software as an undergraduate and then graduate researcher in the MIT Media Lab from 1986 to 1991.  While at MIT, and also after moving to Austin, Texas, in 1993, Sabiston used his 2D/3D software to create several short films, including \"God's Little Monkey\" (1994), \"Beat Dedication\" (1988), and \"Grinning Evil Death\" (1990).  \"Grinning Evil Death\" was widely seen on the first episode of MTV's \"Liquid Television\" show.  \"God's Little Monkey\" won the Prix Ars Electronica Golden Nica award for 1994.\n\nDescendants (2015 film): Descendants is a 2015 American musical fantasy television film directed and choreographed by Kenny Ortega.  The film stars Dove Cameron, Sofia Carson, Booboo Stewart, and Cameron Boyce as the teenage daughters and sons of Maleficent, the Evil Queen, Jafar, and Cruella De Vil, respectively.  The film follows these teenagers adjusting to life outside their island prison, while on a mission to steal the Fairy Godmother's wand and free their parents from captivity.\n\nGeoff Marslett: Geoff Marslett is an award winning American film director, writer, producer, animator and actor.  His early career started with the animated short \"Monkey vs. Robot\" which was distributed internationally by \"Spike and Mike's Classic Festival of Animation\" on video.  and \"Spike and Mike's Sick and Twisted Festival of Animation\" in theatres.  More recently he directed several successful narrative feature films including \"MARS\" and \"Loves Her Gun\", as well as producing and acting in the experimental documentary \"Yakona\".  He appears onscreen in Josephine Decker's \"Thou Wast Mild and Lovely\" which is being released theatrically in 2014.  He currently resides in Austin, Texas and splits his time between filmmaking and teaching at the University of Colorado at Boulder.\n\nMonkey Kingdom: Monkey Kingdom is a 2015 American nature documentary film directed by Mark Linfield and Alastair Fothergill and narrated by Tina Fey.  The documentary is about a family of monkeys living in ancient ruins founded in the jungles of Polonnaruwa in Sri Lanka.  The film was released by Disneynature on April 17, 2015.\n\nYuri Lowenthal: Yuri Lowenthal (born March 5, 1971) is an American actor, producer, and screenwriter known chiefly for his voice-over work in anime, cartoons and video games.  Some of his prominent roles in anime and cartoons include teenage Ben Tennyson in \"Ben 10\", Sasuke Uchiha in \"Naruto\", Jinnosuke in \"Afro Samurai\", Suzaku Kururugi in \"Code Geass\", and Simon in \"Gurren Lagann\".  In video games, he voices The Prince in Ubisoft's \"Prince of Persia\", Alucard in \"Castlevania\", Hayate/Ein in \"Dead or Alive\", Matt Miller in \"Saints Row\", and Yosuke Hanamura in \"Persona 4\".  He has a production company Monkey Kingdom Productions with his wife, Tara Platt, where they have produced several feature films and a live-action web series called \"Shelf Life\".  He co-authored the book \"Voice-Over Voice Actor\" which gives career tips.\n\nThe Real Housewives of Cheshire: The Real Housewives of Cheshire (abbreviated RHOCheshire) is a British reality television series broadcast on ITVBe.  The show premiered on 12 January 2015 and is based on \"The Real Housewives\" franchise.  It is produced and distributed by NBCUniversal International Networks, and Monkey Kingdom, one of Britain's leading production companies.  \"The Real Housewives of Cheshire\" chronicles the lives of several affluent housewives who reside in Cheshire and Greater Manchester, England.\n\nRotten to the Core (song): \"Rotten to the Core\" is a song from Disney Channel's 2015 television film \"Descendants\", whose music and lyrics were composed by Joacim Persson, Shelly Peiken and Johann Alkenas.  The song was performed in its original show-tune version in the film by the main cast – Dove Cameron, Cameron Boyce, Booboo Stewart and Sofia Carson– in their vocal roles as Mal (daughter of Maleficent), Carlos (son of Cruella de Vil), Jay (son of Jafar) and Evie (daughter of The Evil Queen).  The song peaked at number 38 in the Billboard Hot 100.  A second version, performed by actress and singer Sofia Carson, was released as a single on December 18, 2015.\n\nKristin Bauer van Straten: Kristin Bauer van Straten is an American film and television actress, perhaps best known for her roles as vampire Pamela Swynford De Beaufort on the HBO television series \"True Blood\", Jerry's girlfriend Gillian on \"Seinfeld\", and as sorceress Maleficent in the ABC series \"Once Upon a Time\".\n\nMaleficent (film): Maleficent is a 2014 American dark fantasy film directed by Robert Stromberg from a screenplay by Linda Woolverton, and starring Angelina Jolie as the titular character with Sharlto Copley, Elle Fanning, Sam Riley, Imelda Staunton, Juno Temple, and Lesley Manville in supporting roles.  Loosely based on Charles Perrault's original fairy tale and inspired by Walt Disney's 1959 animated film \"Sleeping Beauty\", the film portrays the story from the perspective of the eponymous antagonist, depicting her conflicted relationship with the princess and king of a corrupt kingdom.\n\nTara Platt: Tara Platt (born June 18, 1978) is an American actress and producer who has provided voices for dozens of English-language versions of Japanese anime films, television series, and video games.  Her notable roles in anime include Temari in \"Naruto\" and Reina in \"Rave Master\".  In video games, she has voiced Noir in \"Tales of the Abyss\" and Mitsuru Kirijo in \"\", as well as characters in \"Mortal Kombat vs. DC Universe\", \"Marvel vs. Capcom 3\", \"\", \"Soulcalibur IV\", and \"League of Legends\".  On screen she has appeared in television shows like \"Scandal\", \"Hawaii Five-0\", \"Castle\" and \"Revenge\", as well as the feature film \"The Call\".  She has a production company Monkey Kingdom Productions with her husband, Yuri Lowenthal, where they have produced several films that have made the film festival rounds, and a live-action web series called \"Shelf Life\".  They authored the book \"Voice-Over Voice Actor\" which gives career tips.\n\nQuestion: Which American film was released in 2015, Maleficent or Monkey Kingdom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comparison_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"target_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year being queried for comparison.\"\n        },\n        \"films_evaluated\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"film_title\": {\n                \"type\": \"string\",\n                \"description\": \"The title of the film.\"\n              },\n              \"release_year\": {\n                \"type\": \"integer\",\n                \"description\": \"The release year of the film.\"\n              },\n              \"is_american\": {\n                \"type\": \"boolean\",\n                \"description\": \"Indicates if the film is American.\"\n              }\n            },\n            \"required\": [\n              \"film_title\",\n              \"release_year\",\n              \"is_american\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of films evaluated for the comparison.\"\n        }\n      },\n      \"required\": [\n        \"target_release_year\",\n        \"films_evaluated\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the American film released in the target year.\"\n    },\n    \"answer_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the answer film.\"\n    }\n  },\n  \"required\": [\n    \"comparison_details\",\n    \"answer_film_title\",\n    \"answer_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comparison_details": {
        "type": "object",
        "properties": {
          "target_release_year": {
            "type": "integer",
            "description": "The release year being queried for comparison."
          },
          "films_evaluated": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "film_title": {
                  "type": "string",
                  "description": "The title of the film."
                },
                "release_year": {
                  "type": "integer",
                  "description": "The release year of the film."
                },
                "is_american": {
                  "type": "boolean",
                  "description": "Indicates if the film is American."
                }
              },
              "required": [
                "film_title",
                "release_year",
                "is_american"
              ],
              "additionalProperties": false
            },
            "description": "A list of films evaluated for the comparison."
          }
        },
        "required": [
          "target_release_year",
          "films_evaluated"
        ],
        "additionalProperties": false
      },
      "answer_film_title": {
        "type": "string",
        "description": "The title of the American film released in the target year."
      },
      "answer_release_year": {
        "type": "integer",
        "description": "The release year of the answer film."
      }
    },
    "required": [
      "comparison_details",
      "answer_film_title",
      "answer_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
