{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDaniel Schaffer: Dan Schaffer (born 3 February 1969) is a British writer/artist working primarily in comics and film.  He is best known as the writer and illustrator of cult comic book series, \"Dogwitch\".  He is also the co-creator/artist of \"Indigo Vertigo\", a collaboration with Queenadreena / Daisy Chainsaw singer Katiejane Garside, and writer/artist of the original graphic novel The Scribbler.\n\nKatieJane Garside: Katrina Jane Garside (born 8 July 1968) is an English singer, songwriter, visual artist, and poet.  She rose to prominence as the lead vocalist of the indie noise rock band Daisy Chainsaw, which she formed in 1989 with guitarist Crispin Gray.  After quitting the band in 1993, she would reunite with Gray in 1999 to form the band Queenadreena.  She has also written and released material with her project Ruby Throat, an acoustic collaboration with Chris Whittingham, since 2007.\n\nLullabies in a Glass Wilderness: Lalleshwari/Lullabies in a Glass Wilderness is an independent solo album by the British artist KatieJane Garside.  She is also the frontwoman of Queenadreena, Ruby Throat and formerly of Daisy Chainsaw.  The name 'Lalleshwari' comes from an ancient Hindu poet.\n\nIndigo Vertigo: Indigo Vertigo is a 48-page graphic novella, written by KatieJane Garside and illustrated by \"Dogwitch\" creator, Daniel Schaffer.  It was published by Image Comics in 2005.\n\nRuby Throat: Ruby Throat is a British neofolk musical duo formed in 2007 by former Daisy Chainsaw and Queenadreena vocalist KatieJane Garside and guitarist Chris Whittingham.  The duo came together amidst the dissolution of Queenadreena, and have recorded three studio albums, beginning with \"The Ventriloquist\" (2007).\n\nDaisy Chainsaw: Daisy Chainsaw were an English alternative rock band, active between 1989 and 1995.  They originally featured KatieJane Garside as lead vocalist and lyricist on the band's early EPs and debut album, \"Eleventeen\" (1992), before her departure in 1993.  The band's live performances were noted for their wild histrionics, often featuring Garside onstage drilling doll heads and drinking juice from baby bottles.  Following Garside's departure, the group's second album and subsequent EPs featured Belinda Leith on vocals, until the band's breakup in 1995.  Guitarist Crispin Gray and Garside would later reunite to form Queenadreena in 1999.\n\nAaron Hall (singer): Aaron Hall (born August 10, 1964, The Bronx, New York City and growing up in Brooklyn and Roosevelt, Long Island), is an American soul singer and songwriter.  He is a current member of the group Guy, which he founded in the late 1980s, along with New jack swing producer Teddy Riley and songwriter Timmy Gatling, who was later replaced by Hall's brother Damion Hall.  In 1988, they released their debut album which went on to sell over a million copies being certified platinum.  Hall led the group in songs like \"Groove Me\", \"I Like\" and \"Piece Of My Love\".\n\nQueenadreena: Queenadreena were an English alternative rock band that formed in London, England in 1999.  The group were formed by vocalist KatieJane Garside and guitarist Crispin Gray, who had previously collaborated in the celebrated but short-lived band Daisy Chainsaw.  Garside and Gray, who had earned a reputation for their abrasive songwriting with Daisy Chainsaw, incorporated elements of blues rock and other genres with Queenadreena, in addition to their predominant noise rock influences.\n\nThe Ventriloquist (album): The Ventriloquist is an album by Ruby Throat, a musical act consisting of Katiejane Garside (frontwoman of Queen Adreena) and Chris Whittingham.  It was released on 8 November 2007 on a limited run of only 500 copies.  This consisted of books bound from Indian vintage red leather, the CD in a cloth pocket in the back of the book.  Another limited version of 400 copies was released on January 16, 2008, this time in a regular jewelled case and a 4-panel CD booklet.  There was a worldwide general release later in 2008, but \"Marybell\" was replaced on this edition by two new tracks, \"Consuela's Newt\" and \"Boat Song.\"  An official limited edition run of 300 gatefold double vinyl LPs were issued in Spring 2010 by Los Angeles-based label, The Lovers' Will Records & Press.\n\nThe Butcher and the Butterfly: The Butcher and the Butterfly is the third studio album by English alternative rock band Queenadreena, released in May 2005 though One Little Indian and Imperial Records.  The album features writing from frontwoman KatieJane Garside, guitarist Crispin Gray, and drummer Pete Howard, as well as contributions from Garside's sister, Melanie Garside, who also plays bass on the album.  Richard Adams, the bassist of Garside and Gray's former band, Daisy Chainsaw, also has a co-writing credit on one track.\n\nQuestion: Both KatieJane Garside and Aaron Hall share what occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_one\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_two\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"shared_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Occupations shared by both individuals.\"\n    }\n  },\n  \"required\": [\n    \"person_one\",\n    \"person_two\",\n    \"shared_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_one": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            }
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
            "type": "string"
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "shared_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Occupations shared by both individuals."
      }
    },
    "required": [
      "person_one",
      "person_two",
      "shared_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
