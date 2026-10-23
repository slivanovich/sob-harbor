{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCustard Records: Custard Records is an American record label, best known for its success with English singer-songwriter and Number 1 recording artist James Blunt.  The label is run by former 4 Non Blondes member Linda Perry and has a partnership with Warner Music Group's Atlantic Records division.\n\nLinda Perry: Linda Perry (born April 15, 1965) is an American Grammy nominated rock singer-songwriter, and record producer.  She first became known as the lead singer and primary songwriter of 4 Non Blondes and has since founded two record labels and composed and produced hit songs for several other artists.  They include: \"Beautiful\" by Christina Aguilera; \"What You Waiting For? \" by Gwen Stefani; and \"Get the Party Started\" by P!nk.  Perry has also contributed to albums by Adele, Alicia Keys, and Courtney Love, as well as signing and distributing James Blunt in the United States.  Perry was also inducted into the Songwriters Hall of Fame in 2015.\n\nMinnesota (band): Minnesota was a Eurodance group formed in Germany.  It was created by Thomas Allison and Ralf Kappmeier, two German producers.  They released two singles, their first was \"What's Up\", a cover of the 4 Non Blondes song.  It peaked at number 22 on the Swiss Singles Chart and reached number one on the \"RPM\" Dance Chart in Canada.  Their second single, \"Without You\" peaked at number 39 on the Swiss Singles Chart.\n\nDJ Miko: DJ Miko (born Monier Quartararo Gagliardo, 8 February 1973) is an Italian DJ.  He had a hit with a cover of 4 Non Blondes's \"What's Up\" in 1994.  His version, featuring the British vocalist Louise Gard, hit #58 on the \"Billboard\" Hot 100, #6 on the UK Singles Chart, #92 on the Australian ARIA singles chart, #8 on the Irish Singles Chart, #23 in New Zealand, and #17 in Sweden.\n\nLeave the Fire Behind: Leave the Fire Behind is an album of cover versions by the folk-singer John Craigie consisting of songs from the 1990s.  It includes songs from the bands Everclear, Gin Blossoms, Green Day, Marcy Playground, Blind Melon, The Wallflowers, Smashing Pumpkins, 4 Non Blondes, Red Hot Chili Peppers and The Counting Crows.\n\nWhat's Up? (song): \"What's Up?\"  is a song by American rock group 4 Non Blondes from their 1992 debut album, \"Bigger, Better, Faster, More! \".  It was released as the album's second single in 1993.  It was successful in the United States and in several European countries, peaking at number one in Austria, Belgium, Bulgaria, Germany, Ireland, the Netherlands, Norway, Poland, Sweden, and Switzerland.\n\nBigger, Better, Faster, More!: Bigger, Better, Faster, More!  is the only studio album released by alternative rock band 4 Non Blondes, released in 1992.  The first single was \"Dear Mr. President\", which bass player Christa Hillhouse told Songfacts \"was about the hierarchy of power and government.\"  The second single, What's Up? , became a #1 hit in several countries and went gold in the US.\n\nPut Your Hearts Up: \"Put Your Hearts Up\" is the debut single by American singer Ariana Grande.  She released the single under Universal Republic Records on December 12, 2011.  The song samples \"What's Up? \" by 4 Non Blondes.\n\nGo Radio: Go Radio was an American rock band from Tallahassee, Florida, formed by former Mayday Parade vocalist, guitarist and lyricist Jason Lancaster in April 2007.\n\n4 Non Blondes: 4 Non Blondes was an American rock band from San Francisco, California, formed in 1989.  The group was formed by bassist Christa Hillhouse, guitarist Shaunna Hall, drummer Wanda Day, and vocalist and guitarist Linda Perry.  Prior to the release of their first album, Roger Rocha replaced Hall on guitar, and Dawn Richardson replaced Day on drums.  They hit the charts in 1993 with \"What's Up? \", their only major hit single.  Perry left the band in 1994 to begin a solo career, and the remaining members disbanded shortly after.\n\nQuestion: Which of the following bands hit the charts in 1993 with \"What's Up?\" Go Radio or 4 Non Blondes?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that hit the charts.\"\n    },\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song that hit the charts.\"\n    },\n    \"chart_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song hit the charts.\"\n    },\n    \"band_origin\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the band was formed.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the band was formed.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the band was formed.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album the song is from.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the album.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_major_hit\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the song was a major hit for the band.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"song_title\",\n    \"chart_year\",\n    \"band_origin\",\n    \"album_details\",\n    \"is_major_hit\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band that hit the charts."
      },
      "song_title": {
        "type": "string",
        "description": "The title of the song that hit the charts."
      },
      "chart_year": {
        "type": "integer",
        "description": "The year the song hit the charts."
      },
      "band_origin": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the band was formed."
          },
          "state": {
            "type": "string",
            "description": "The state where the band was formed."
          },
          "country": {
            "type": "string",
            "description": "The country where the band was formed."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "album_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the album the song is from."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the album."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "is_major_hit": {
        "type": "boolean",
        "description": "Indicates if the song was a major hit for the band."
      }
    },
    "required": [
      "band_name",
      "song_title",
      "chart_year",
      "band_origin",
      "album_details",
      "is_major_hit"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
