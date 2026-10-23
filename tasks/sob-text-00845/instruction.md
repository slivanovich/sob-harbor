{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Wild Heart Tour: The Wild Heart Tour was a North America-only solo concert tour by Fleetwood Mac vocalist Stevie Nicks in support of her second studio album \"The Wild Heart\".  The tour began on May 27, 1983, in Las Vegas, Nevada and ended on November 24, 1983, in Columbia, South Carolina.  Three weeks before the tour, Stevie performed on “Rock Day” at the US Festival in San Bernardino, California.  Approximately 670,000 people attended the four-day music festival.\n\nKiley Dean: Kiley Dean (born April 12, 1982) is an American contemporary R&B singer.  Dean was born and raised in a small town in Arkansas.  When she was about 7 years old, her family decided to move to Orlando.  She grew up singing in school and church, which led her to singing back-up for Britney Spears' tours, \"…Baby One More Time Tour\" and \"Oops! ... I Did It Again World Tour\" as well as Madonna's tours, \"MDNA Tour\" and \"Rebel Heart Tour.\"\n\nEvery Beat of My Heart Tour: The Every Beat Of My Heart Tour was a European concert tour by British singer-songwriter Rod Stewart to promote his album \"Every Beat of My Heart\".  The tour began on 26 June 1986 in Belfast and ended on 6 November 1986 in Brighton.\n\nGypsy Heart Tour: The Gypsy Heart Tour (Spanish: Corazón Gitano Tour ) was the third concert tour by American recording artist Miley Cyrus, held in support of her third studio album \"Can't Be Tamed\" (2010).  It visited primally Latin America, Australia, and the Philippines; it began on April 29, 2011 in Quito, Ecuador and concluded on July 2, 2011 in Perth, Australia.  The tour ranked 22nd in Pollstar's \"Top 50 Worldwide Tours (Mid-Year)\", earning over $26 million.\n\nBonnie Tyler: Bonnie Tyler (born Gaynor Hopkins; 8 June 1951) is a Welsh singer, known for her distinctive husky voice.  Tyler came to prominence with the release of her 1977 album \"The World Starts Tonight\" and its singles \"Lost in France\" and \"More Than a Lover\".  Her 1978 single \"It's a Heartache\" reached number four on the UK Singles Chart, and number three on the US \"Billboard\" Hot 100.\n\nKaleidoscope Heart Tour: Kaleidoscope Heart Tour was the concert tour by American singer–songwriter Sara Bareilles, in support of her second studio album, \"Kaleidoscope Heart\".\n\nAll the Women I Am Tour: The All the Women I Am Tour is a concert tour by American recording artist, Reba McEntire.  Visiting Canada and the United States, the tour will support the singers studio album, \"All the Women I Am\".  The tour follows the co-headlining tour with George Strait and Lee Ann Womack—which became one of the biggest tours in North America in 2010 and 2011.  It will be McEntire's first solo tour since her 2007 trek, the Key to Your Heart Tour.  McEntire will begin the tour in September in Fort McMurray.  It will continue to travel throughout Canada and the U.S., ending in November.  McEntire confirmed on her Twitter she is planning to tour the United Kingdom and Germany in March 2012.  The dates were announced in October 2011, becoming McEntire's first shows in the UK in nearly 12 years.\n\nGolden Heart Tour: The Golden Heart Tour was a 1996 concert tour by British singer-songwriter and guitarist Mark Knopfler, promoting the release of his first solo album \"Golden Heart\".  The tour consisted of two legs: the British Isles and Europe.  The tour started on 24 April 1996 in Galway, Ireland, and included 84 concerts in 66 cities, ending in Antibes, France, on 4 August 1996.\n\nHide Your Heart Tour: The \"Hide Your Heart Tour\" by Bonnie Tyler, and her only UK tour to date.  The tour was arranged in promotion of Tyler's \"\"Hide Your Heart\"\" album, released in the same year.  A notable moment from the tour was when Tyler performed at Reading Festival, where she was met with a crowd hurling bottles onto the stage.\n\nRebel Heart Tour: The Rebel Heart Tour was the tenth concert tour by American singer Madonna, and was staged in support of her thirteenth studio album, \"Rebel Heart\".  Comprising 82 shows, the tour visited North America, Asia, Europe, and Oceania.  It began on September 9, 2015, in Montreal, Canada, at the Bell Centre and concluded on March 20, 2016, in Sydney, Australia at Allphones Arena.  It was officially announced on March 1, 2015, through Madonna's website and was led by Live Nation Entertainment's Global Touring Division, helmed by Arthur Fogel; this was the fifth collaboration between Madonna and Live Nation as well her third tour to be promoted by the company.  An all-arena tour, the Rebel Heart Tour visited cities where the singer has not performed before, and was her first to visit Australia since The Girlie Show World Tour (1993) more than 20 years prior.\n\nQuestion: What was the 1977 debut album of the singer who named her tour the \"Hide Your Heart Tour?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the singer associated with the tour.\"\n    },\n    \"tour_name_referenced\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the tour mentioned in the question to identify the singer.\"\n    },\n    \"debut_album\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the singer's debut album.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the debut album.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the 1977 debut album.\"\n    }\n  },\n  \"required\": [\n    \"singer_name\",\n    \"tour_name_referenced\",\n    \"debut_album\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "singer_name": {
        "type": "string",
        "description": "The name of the singer associated with the tour."
      },
      "tour_name_referenced": {
        "type": "string",
        "description": "The name of the tour mentioned in the question to identify the singer."
      },
      "debut_album": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the singer's debut album."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the debut album."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The title of the 1977 debut album."
      }
    },
    "required": [
      "singer_name",
      "tour_name_referenced",
      "debut_album",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
