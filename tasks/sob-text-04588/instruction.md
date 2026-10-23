{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouthern Girl City Lights: Southern Girl City Lights is the second studio album by American country music artist Jessie James Decker.  It is Decker's first full-length country album.  It is set to be released on October 13, 2017.\n\nBrandon October: Brandon Steve October (born 30 May 1977) is a South African pop singer-songwriter, who rose to fame after being runner-up in the first season of the reality television show \"South African Pop Idols\" in 2002.\n\nList of Garth Brooks concert tours: Garth Brooks is an American country pop singer-songwriter.  From his first concert series to his current record-breaking worldwide tour, Brooks has changed the face of performing from a country music perspective, adding high energy and pyrotechnics to depict a hard rock-country crossover.  Since his first tour began in 1991, Brooks has performed in a variety of concert settings, including world tours, residency shows, and benefit concerts.\n\nLuna Halo (album): Luna Halo is the self-titled release from Luna Halo on October 30, 2007 on American Recordings.  Country pop singer-songwriter Taylor Swift covered the second track, \"Untouchable\", for the platinum edition of her second studio album, \"Fearless.\"\n\nGarrett Caples: Garrett Caples (born 1972) is an American poet.  Born in Lawrence, Massachusetts, he currently lives in San Francisco, California, after fifteen years in Oakland.  An editor at City Lights Books, Caples curates the new American poetry series, City Lights Spotlight.  From 2005 to 2014, he wrote on hip hop, literature, and painting for the San Francisco Bay Guardian, and has written fiction on unusual sexual practices, like omorashi.\n\nShelby Lynne discography: Shelby Lynne is an American country pop singer-songwriter.  Her discography consists of 13 studio albums and 29 singles released between 1988 and 2012.\n\nWhen the Lights Go Down (Faith Hill song): \"When the Lights Go Down\" is a song written by Rivers Rutherford, Jeffrey Steele and Craig Wiseman, and recorded by American country pop singer Faith Hill.  It was released to country radio November 19, 2002 as the second single from her fifth studio album, \"Cry\" (2002).  The second of three songs from the album promoted to country radio, \"When the Lights Go Down\" peaked at #26 on the \"Billboard\" Hot Country Songs chart in 2003.  At the time, this was Hill's lowest position on the chart since \"But I Will\" peaked at #35 nearly a decade previously, however subsequent single \"You're Still Here\" would chart two positions lower later the same year.\n\nErika Lauren Wasilewski: Erika Lauren Wasilewski, known on-air simply as Erika Lauren, is an American radio personality, singer-songwriter and former reality television personality.  She currently serves as co-host on \"The Alan Cox Show\", an afternoon drive hot talk program on Cleveland rock station WMMS (100.7 FM).  In addition to her duties at WMMS, she is currently a member of the cover band Pop Vulture.  Wasilewski was the lead singer of the now-defunct band Hawkeye, who released their debut LP \"Ruthless\" on July 16, 2013.  From December 2009 to March 2010, she was a cast member on the MTV reality series \"\"\n\nJessie James Decker: Jessica Rose \"Jessie\" James Decker (born April 12, 1988) is an American country pop singer-songwriter and reality television personality.  At age 15, after auditioning for and being rejected by most of the country labels in Nashville, Tennessee, James began working on refining her craft with Carla Wallace of Big Yellow Dog Music.  One of her songs attracted the attention of Mercury Records which offered her a recording contract.  She released her debut album, \"Jessie James\", in 2009.  A few years later in 2013, she starred with her husband Eric Decker in the E! reality show \"Eric & Jessie: Game On\", which stopped airing in April 2014, but is returning in September 2017.  The following year, on April 18, 2014, James released an EP through iTunes with 19 Recordings entitled \"Comin' Home\".\" \"  On her new label Epic she released a 5-track EP \"Gold\" on February 17, 2017, & released a surprise live EP on June 9, 2017 titled \"Blackbird Sessions\".  On October 13, 2017 she will release her second full-length album and first for Epic Records, Southern Girl City Lights.\n\nAndy Gray (actor): Andy Gray (born 1959)is a Scottish actor and comedy writer.  He starred in the BBC Radio Scotland sketch show \"Naked Radio\", and its later television counterpart \"Naked Video\", before becoming well known as the appropriately named \"Chancer\", best friend and source of problems to Willie Melvin (Gerard Kelly) in the 1987 sitcom \"City Lights\".  He is well known for pantomime, usually co-writing the script and appearing as the dame, often alongside other former \"City Lights\" cast members.  He also appeared opposite Kelly in a production of \"The Odd Couple\"\n\nQuestion:  Southern Girl City Lights is what by an American country pop singer-songwriter and reality television personality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album.\"\n    },\n    \"album_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of album release (e.g., studio album, EP).\"\n    },\n    \"album_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the album for the artist.\"\n    },\n    \"artist_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of occupations for the artist.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_title\",\n    \"album_type\",\n    \"album_number\",\n    \"artist_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_title": {
        "type": "string",
        "description": "The title of the album."
      },
      "album_type": {
        "type": "string",
        "description": "The type of album release (e.g., studio album, EP)."
      },
      "album_number": {
        "type": "integer",
        "description": "The sequential number of the album for the artist."
      },
      "artist_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations for the artist."
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_title",
      "album_type",
      "album_number",
      "artist_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
