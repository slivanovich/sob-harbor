{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPlease Send Me Someone to Love: \"Please Send Me Someone to Love\" is a blues ballad, written and recorded by Percy Mayfield in 1950, for Art Rupe's Specialty Records.  It was on the R&B chart for 27 weeks and reached the number one position; it was Mayfield's most successful song.\n\nPercy Mayfield: Percy Mayfield (August 12, 1920 – August 11, 1984) was an American rhythm-and-blues singer with a smooth vocal style.  He was also a songwriter, known for the songs \"Please Send Me Someone to Love\" and \"Hit the Road Jack\".\n\nLost Someone: \"Lost Someone\" is a song recorded by James Brown in 1961.  It was written by Brown and Famous Flames members Bobby Byrd and Baby Lloyd Stallworth.  Like \"Please, Please, Please\" before it, the song's lyrics combine a lament for lost love with a plea for forgiveness.  The single was a #2 R&B hit and reached #48 on the pop chart.  According to Brown, \"Lost Someone\" is based on the chord changes of the Conway Twitty song \"It's Only Make Believe\".\n\nHarlem Blues: Harlem Blues is an album by American jazz pianist Phineas Newborn Jr. recorded in 1969 but not released on the Contemporary label until 1975.  The album was recorded at the same sessions that produced \"Please Send Me Someone to Love\".\n\nAndy White (drummer): Andrew \"Andy\" White (27 July 1930 – 9 November 2015) was a Scottish drummer, primarily a session musician.  He was affectionately christened \"the fifth Beatle\" as he is best known for replacing Ringo Starr on drums on the Beatles' first single, \"Love Me Do\".  White was featured on the American 7\" single release of the song, which also appeared on the band's debut British album, \"Please Please Me\".  He also played on \"P.S. I Love You\", which was the B-side of \"Love Me Do\".\n\nMark Hsu Syers: Mark Hsu Syers was a Broadway actor in the 70's and 80's.  He graduated from Hopewell Valley Central High School and attended the University of New Mexico, where he acted in The Fantasticks.  He graduated Emerson College in 1974 in Boston.  He also appeared in Under Fire in New York City and Godspell in Boston.  His first major role was in \"Pacific Overtures\" where he played, among other roles, the Russian Admiral (Please Hello), the Soothsayer (Crysanthymum Tea), the Thief (Four Black Dragons), and the Warrior (Someone in a Tree).  He also had roles in \"Jesus Christ Superstar\" {King Herod} and \"Evita\" {Magaldi}.  His voice can be heard on the cast recordings of \"Pacific Overtures\" and \"Evita\".  He was featured in the TV show \"Anatomy of a Song: Someone in a Tree\" with Stephen Sondheim, Gedde Watanabe and James Dybas, which was presented by Frank Rich.\n\nList of songs recorded by Fiona Apple: American singer-songwriter Fiona Apple has recorded songs for her four studio albums and collaborated with other artists for duets and featured songs on their respective albums.  After signing a contract in 1995 with the Work Group, a division of Sony Music, eighteen-year-old Apple moved from New York to Los Angeles to record her debut album, \"Tidal\" (1996).  She wrote all of its songs, and would continue to do so for her later albums. \" Shadowboxer\" was \"Tidal\"' s lead single, later followed by \"Criminal\", which received the Grammy Award for Best Female Rock Vocal Performance and a nomination for Best Rock Song at the 40th Grammy Awards.  In 1998, Apple also recorded two cover versions for the film soundtrack \"\"Pleasantville\": \"Across the Universe\" (Lennon–McCartney) and \"Please Send Me Someone to Love\" (Percy Mayfield).\n\nThe Best of Sade: The Best of Sade is the first greatest hits album by English band Sade.  It was released in the United Kingdom on 31 October 1994 and in the United States on 4 November 1994 by Epic Records.  The retrospective was digitally remastered in 2000.  \"The Best of Sade\" chronicles Sade's first four albums, while also including non-single songs \"Jezebel\", \"Like a Tattoo\" and \"Pearls\", as well as \"Please Send Me Someone to Love\", which appeared in the soundtrack for the film \"Philadelphia\".\n\nPlease Send Me Someone to Love (album): Please Send Me Someone to Love is an album by American jazz pianist Phineas Newborn Jr. recorded in 1969 and released on the Contemporary label.  The album was recorded at the same sessions that produced \"Harlem Blues\".\n\nPhiladelphia (film): Philadelphia is a 1993 American drama film and one of the first mainstream Hollywood films to acknowledge HIV/AIDS, homosexuality, and homophobia.  It was written by Ron Nyswaner, directed by Jonathan Demme and stars Tom Hanks and Denzel Washington.\n\nQuestion: The song Please Send Me Someone to Love appeared in the soundtrack of a film directed by who ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"appearance_context\": {\n      \"type\": \"string\",\n      \"description\": \"The context in which the song appeared in relation to the film.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"film_details\",\n    \"appearance_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "director"
        ],
        "additionalProperties": false
      },
      "appearance_context": {
        "type": "string",
        "description": "The context in which the song appeared in relation to the film."
      }
    },
    "required": [
      "song_title",
      "film_details",
      "appearance_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
