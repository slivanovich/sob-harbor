{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSleeping with the Past: Sleeping with the Past is the 22nd studio album by the English singer-songwriter Elton John, released on 29 August 1989.  It is his best-selling album in Denmark (where it was recorded) and is dedicated to his longtime writing partner Bernie Taupin.  The album features his first solo number-one single, \"Sacrifice\", in his home country of the UK, which helped the album also hit number one there, his first since 1974's \"Elton John's Greatest Hits\".  John and Taupin meant for the songs to reflect the style of 1960s R&B icons such as Marvin Gaye, Otis Redding and Sam Cooke, whom they admired.  It also became his first platinum album in the UK since 1983.  In the US it was certified gold in October 1989 and platinum in April 1990 by the RIAA.  Guy Babylon made his debut on this album and would continue to play keyboards with John for the next 20 years, while Fred Mandel left the band shortly after.  John went into rehabilitation in 1990.\n\nMade in England (Elton John album): Made in England is the twenty-fifth studio album by English singer-songwriter Elton John, released in 1995 and produced by him and Greg Penny, the first time since \"Leather Jackets\" without Chris Thomas.  It was dedicated to John's boyfriend and future civil partner David Furnish.  It was also dedicated to the memory of Denis Gauthier and Peter Williams.  It was the last album to feature regular percussionist Ray Cooper until 2016's \"Wonderful Crazy Night\".  Bob Birch became John's full-time recording and touring bass player and continued that role until his death in 2012.\n\nTumbleweed Connection: Tumbleweed Connection is the third studio album by English singer-songwriter Elton John.  It is a concept album based on country and western/Americana themes.\n\nRay Cooper: Raymond Thomas \"Ray\" Cooper (born 19 September 1947) is an English virtuoso percussionist.  He is a session and road-tour percussionist, and occasional actor, who has worked with several musically diverse bands and artists including George Harrison, Billy Joel, Rick Wakeman, Eric Clapton, Pink Floyd and Elton John.  Cooper absorbed the influence of rock drummers from the 1960s and 1970s such as Ginger Baker, Carmine Appice, and John Bonham.  Incorporation of unusual instruments (for rock drummers of the time) such as cowbells, glockenspiel, and tubular bells, along with several standard kit elements, helped create a highly varied setup.  Continually modified to this day, Cooper's percussion set offers an enormous array of percussion instruments for sonic diversity such as the tambourine, congas, crash cymbals, cowbells, roto toms, tubular bells, the gong, snare and timpani.  For two decades Cooper honed his technique; In the 1990s, he reinvented his style.  He is known for the 7-minute percussion and drum solos he performed during the years 1990–1991 for Eric Clapton and for the 7-minute percussion and drum solos during all the 1994 Face to Face Tours with Billy Joel, and Elton John, and the tours with the Elton John band during the years of 1994–1995.\n\nWonderful Crazy Night: Wonderful Crazy Night is the 32nd studio album by British singer-songwriter Elton John.  It is John's first album since 2006's \"The Captain & the Kid\" to feature the Elton John Band, and was written and recorded in 17 days.  John's long-standing percussionist, Ray Cooper, makes his first appearance on any of John's albums since \"Made in England\" in 1995.  This is Kim Bullard's first appearance on keyboards replacing Guy Babylon, and Matt Bissonette replacing Bob Birch on bass.\n\nDuets (Elton John album): Duets is the twenty-fourth studio album by the English singer-songwriter Elton John, released in 1993.\n\nThe One (Elton John album): The One is the twenty-third studio album by the English singer-songwriter Elton John, released on 22 June 1992.  It was recorded at Studio Guillame Tell in Paris, produced by Chris Thomas and managed by John Reid.  The album was dedicated to Vance Buck, and its cover artwork was designed by Gianni Versace.\n\nElton John (album): Elton John is the second studio album by English singer-songwriter Elton John, released on 10 April 1970 by DJM Records.  It was released by Uni Records as John's debut album in the United States; many people there assumed it was his first album, as \"Empty Sky\" was not released in that country until 1975.  \"Elton John\" includes his breakthrough single \"Your Song\", and helped to establish his career during what was considered the \"singer-songwriter\" era of popular music.  In the US, it was certified gold in February 1971 by the Recording Industry Association of America (RIAA).  In the same year, it was nominated for the Grammy Award for Album of the Year.\n\nThe Diving Board: The Diving Board is the 31st studio album by British singer-songwriter Elton John.  It is the second of his studio releases since 1979's \"Victim of Love\" without any of his regular band members.  The album was released in the United Kingdom on 16 September 2013, and debuted at No. 3 on the UK album chart, his highest charting studio album in that country since 2001's \"Songs from the West Coast\", and at No. 4 on the \"Billboard\" 200.  It is also his highest-charting solo album in the United States since \"Blue Moves\" in 1976.  However, after just eight weeks the album fell off the charts completely.\n\nElton John albums discography: The albums discography of English musician/singer-songwriter Elton John consists of 30 studio albums, 4 live albums, 7 soundtrack albums, 16 compilation albums and 3 extended plays, as well as 2 other albums.  John has sold more than 200 million albums worldwide.  Elton John, is The Highest Selling British Solo Artist of All Time\n\nQuestion: Made in England is the twenty-fifth studio album by English singer-songwriter Elton John, released in 1995, it was the last album to feature which regular English virtuoso percussionist, born on 19 September 1947?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album was released.\"\n    },\n    \"percussionist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the percussionist.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The birth date of the percussionist in YYYY-MM-DD format.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the musician.\"\n        },\n        \"last_album_feature_context\": {\n          \"type\": \"string\",\n          \"description\": \"Context regarding this album being the last to feature the percussionist.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"birth_date\",\n        \"role\",\n        \"last_album_feature_context\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_name\",\n    \"release_year\",\n    \"percussionist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the album was released."
      },
      "percussionist": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the percussionist."
          },
          "birth_date": {
            "type": "string",
            "format": "date",
            "description": "The birth date of the percussionist in YYYY-MM-DD format."
          },
          "role": {
            "type": "string",
            "description": "The role of the musician."
          },
          "last_album_feature_context": {
            "type": "string",
            "description": "Context regarding this album being the last to feature the percussionist."
          }
        },
        "required": [
          "full_name",
          "birth_date",
          "role",
          "last_album_feature_context"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_name",
      "release_year",
      "percussionist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
