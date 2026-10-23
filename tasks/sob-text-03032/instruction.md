{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMesopotamia (EP): Mesopotamia is an EP by new wave band the B-52's.  It was produced by David Byrne of Talking Heads and was originally planned to be the band's third studio album.  Due to conflicts with Byrne and record label pressure, recording sessions were aborted prematurely and only six of ten songs to be completed were released as a shorter than originally intended LP.  The record was distributed as a 12\" EP by Warner Bros. in the US and by Island Records on both CD and vinyl in the UK and other non-US markets.\n\nTrue Stories (film): True Stories is a 1986 American film that spans the genres of musical, art, and comedy, directed by and starring David Byrne of the band Talking Heads.  It co-stars John Goodman, Swoosie Kurtz, and Spalding Gray.  Byrne has described the film as, \"A project with songs based on true stories from tabloid newspapers.  It's like \"60 Minutes\" on acid.\"\n\nLove This Giant: Love This Giant is a studio album made in collaboration between David Byrne and St. Vincent, released on 4AD and Todo Mundo on September 10, 2012, in the United Kingdom and a day later in the United States.  Byrne and Annie Clark began working together in late 2009, using a writing and promotion process that Byrne had previously used on his 2008 collaboration with Brian Eno \"Everything That Happens Will Happen Today\".  The duo had previously played together live at a St. Vincent show and on the album \"Here Lies Love\".  The performers enlisted a variety of brass musicians to augment their songwriting and toured over the following year to promote the album.\n\nJamie Dalglish: Jamie Dalglish (born 1947 in Bryn Mawr, Pennsylvania) is an American painter.  He attended the Cincinnati Academy of Art and Rhode Island School of Design and received a 2006–2007 Pollock-Krasner Foundation grant.  He has exhibited in galleries including O.K. Harris, Match artspace, Barbara Braathen, and Florence Lynch.  Dalglish's morphoglyphs have been cited by art writer Lee Klein, among the works of Jackson Pollock and David Reed, as part of the trans-filmic lead into the art of Hyper-texture.  He was included in the exhibition \"I colori del rock,\" which ran in 2009, from January 29 through March 3, at Pavesi Fine Arts in Milan, Italy.  When Dalglish first moved to New York City, he was a housemate of David Byrne, the former Talking Heads lead singer, solo musical artist, and visual practitioner.  Byrne moved to New York in May 1974.\n\nWhammy!: Whammy!  is the third studio album by American new wave band the B-52's.  It was recorded at Compass Point Studios in Nassau, Bahamas, in December 1982 and was produced by Steven Stanley.  The record was refined and mastered at Sterling Sound, New York City.  It was released on April 27, 1983 in the United States, with Warner Bros.  Records as the primary label.  Sales for \"Whammy!\"  were generally weaker than their previous album, but overall successful, spawning the popular singles \"Legal Tender,\" \"Whammy Kiss,\" and \"Song for a Future Generation.\"  The album entered the \"Billboard\" 200 twice in 1983, reaching both number 29 and 171 throughout the year, while \"Legal Tender\" reached the \"Billboard\" Hot 100 chart, as well as the \"Billboard\" Hot Dance Club Play Singles chart alongside its two respective singles.\n\nTalking Heads: Talking Heads were an American rock band formed in 1975 in New York City and active until 1991.  The band comprised David Byrne (lead vocals, guitar), Chris Frantz (drums), Tina Weymouth (bass), and Jerry Harrison (keyboards, guitar).  Described by critic Stephen Thomas Erlewine as \"one of the most critically acclaimed bands of the '80s,\" the group helped to pioneer new wave music by integrating elements of punk, art rock, funk, and world music with avant-garde sensibilities and an anxious, clean-cut image.\n\nClose to the Bone (Tom Tom Club album): Close to the Bone is an album by the Tom Tom Club that was released in 1983.  The Tom Tom Club's musicians were: Wally Badarou, Tyrone Downie, Chris Frantz, Roddy Frantz, Rupert Hine, Raymond Jones, Steve Scales, Steven Stanley, Alex Weir; and sisters Lani, Laura and Tina Weymouth.  The album was released on compact disc for the first time on May 19, 2009, as a part of a two-CD deluxe package with the band's first album, \"Tom Tom Club\", as part of Universal Music's deluxe editions series.\n\nArt of Dying (band): Art of Dying is a Canadian rock band fronted by Jonny Hetherington.  The band is currently signed to Better Noise Records.  Bassist Cale Gontier is the cousin of Adam Gontier, the lead singer of Saint Asonia and former lead singer of Three Days Grace.  Prior to joining the band, Gontier and guitarist Tavis Stanley played in another band, Thornley.\n\nSteven Stanley: Steven J. C. Stanley (born July 11, 1958), is a Jamaican audio engineer, record producer and keyboardist who has worked in the reggae, dub and rock music genres since 1975, most notably with Talking Heads, Tom Tom Club and Black Uhuru.\n\nThis Must Be the Place (Naive Melody): \"This Must Be the Place (Naive Melody)\" is a song by new wave band Talking Heads, released in November 1983 as the second single from their fifth album \"Speaking in Tongues\".  The lyrics were written by David Byrne, and the music was written by Byrne and the other members of the band, Chris Frantz, Tina Weymouth and Jerry Harrison.\n\nQuestion: In which city was the band formed in which Steven Stanley played with David Byrne?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band where both individuals played or worked.\"\n    },\n    \"formation_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the band was formed.\"\n    },\n    \"members_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the members mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the band member.\"\n          },\n          \"role_in_band\": {\n            \"type\": \"string\",\n            \"description\": \"The role of the member in the band (e.g., lead vocals, producer, engineer).\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"role_in_band\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"formation_city\",\n    \"members_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band where both individuals played or worked."
      },
      "formation_city": {
        "type": "string",
        "description": "The city where the band was formed."
      },
      "members_involved": {
        "type": "array",
        "description": "Details about the members mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the band member."
            },
            "role_in_band": {
              "type": "string",
              "description": "The role of the member in the band (e.g., lead vocals, producer, engineer)."
            }
          },
          "required": [
            "name",
            "role_in_band"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "band_name",
      "formation_city",
      "members_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
