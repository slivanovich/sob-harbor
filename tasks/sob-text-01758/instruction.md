{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDalton Delan: Dalton Delan (born August 5, 1954) is an American writer, editor, and television producer.  His works with WETA, PBS and Sundance have won him numerous awards for his documentaries and primetime shows.  A number of his projects include working alongside Robert Redford.  He is executive producer of In Performance at the White House; bringing Bob Dylan in 2010, and Paul McCartney to the White House in 2011, with Mick Jagger performing in 2012.  So far, Delan has worked with presidents Barack Obama, George W. Bush and Bill Clinton in making the In Performance at the White House possible.  Delan is also an executive producer of the Mark Twain Prize for American Humor, presented by the Kennedy Center to notable names in humor and comedy.  Delan is also Co-Creator and an Executive Producer of the Library of Congress Gershwin Prize for Popular Music, whose first recipient was Paul Simon, in a ceremony at the Warner Theater.  He then arranged the relocation of the ceremony to the White House as part of the In Performance at the White House series on PBS, with subsequent honorees Stevie Wonder, Paul McCartney, Burt Bacharach and Hal David, and Carole King in 2013.\n\nRocko's Modern Life: Rocko's Modern Life is an American animated sitcom created by Joe Murray for Nickelodeon.  The series centers on the surreal life of an anthropomorphic Australian-immigrant wallaby named Rocko as well as his friends: the gluttonous steer Heffer, the neurotic turtle Filburt, and Rocko's faithful dog Spunky.  It is set in the fictional town of O-Town.  Throughout its run, the show was controversial for its adult humor, including double entendre, innuendo, and satirical social commentary, similar to \"The Ren & Stimpy Show\".\n\nDave Miller (footballer, born 1964): David Brian Miller (born 8 January 1964) is an English former professional footballer who played as a defender.  He played for seven different clubs in the Football League, including Wigan Athletic during Dave Whelan's takeover of the club as well as having two spells in non-league football.  He is the son of former Burnley player and manager Brian Miller, brother-in-law of teammate and club captain Derek Scott and uncle of Chris & Paul Scott who also played for Burnley\n\nBrian A. Miller: Brian A. Miller is an American television producer and the current Senior Vice President and General Manager of Cartoon Network Studios in Burbank, California, having assumed the title in 2000.  He was formerly Vice President of Production at Nickelodeon Animation Studio, Vice President of Production at Hanna-Barbera, and Vice President of Production at DIC Entertainment.  He also served as a production supervisor for \"Alvin and the Chipmunks\".  He was also the executive in charge of production for various shows in the 1990s and early 2000s such as \"Dexter's Laboratory\", \"CatDog\", \"Hey Arnold! \", \"The Angry Beavers\", \"ChalkZone\", \"\", \"The Powerpuff Girls\", \"Captain Planet and the Planeteers\", \"Adventures of Sonic the Hedgehog\", \"Cow and Chicken\", \"Johnny Bravo\", and the first season of \"SpongeBob SquarePants\".\n\nIn Living Color: In Living Color is an American sketch comedy television series that originally ran on Fox from April 15, 1990, to May 19, 1994.  Brothers Keenen and Damon Wayans created, wrote and starred in the program.  The show was produced by Ivory Way Productions in association with 20th Century Fox Television and was taped at stage 7 at the Fox Television Center on Sunset Boulevard in Hollywood, California.  The title of the series was inspired by the NBC announcement of broadcasts being presented \"in living color\" during the 1960s, prior to mainstream color television.  It also refers to the fact that most of the show's cast were black, unlike other sketch comedy shows such as \"Saturday Night Live\" whose casts are mostly white.  It was controversial due to the Wayans' decision to portray African-American humor from the ghetto in a time when mainstream American tastes regarding black comedy had been set by more upscale shows such as \"The Cosby Show\", causing an eventual feud for control between Fox executives and the Wayans.\n\nSadie Miller: Sadie Isabelle Amy Miller (born 25 February 1985) is an English actress and author.  She is known for her portrayal of Natalie Redfern in the \"Sarah Jane Smith\" audio drama series by Big Finish, her novel, \"Moon Blink\", from Candy Jar Books's series, \"Lethbridge-Stewart\", as well as her association with the science fiction series, \"Doctor Who\".  She is the only daughter of actors Brian Miller and Elisabeth Sladen.\n\nDeathbomb Arc: Deathbomb Arc is an independent record label based in Los Angeles, CA.  It was started in 1998 by Brian Miller, originally to release music by the band Turbine.  Miller's cat Leroy Brown was the label's acting CEO until his death in 2014.\n\nBMX XXX: BMX XXX is a sports video game developed by Z-Axis and published by Acclaim Entertainment under their AKA Acclaim banner for the Xbox, PlayStation 2 and GameCube.  While primarily a BMX-based action sports title, it earned most of its notoriety for containing nudity, foul language and adult humor.  The game allows the player to create female characters that are fully topless and view live-action video clips of real life strippers, also with bare breasts.  Consequently, \"BMX XXX\" was initially denied classification in Australia.  In North America, while the game is available uncensored on the GameCube and Xbox, all naked breasts are covered in the PlayStation 2 version.  While the adult content garnered a great deal of publicity for the game, it was almost entirely negative, and it was eventually released to mediocre reviews and poor sales.\n\nDerek Scott (footballer): Derek Edward Scott (born 8 February 1958) is an English former professional footballer.  He played as a right-sided full-back and was club captain.  He married manager Brian Miller's daughter and played alongside Dave Miller.  His two sons Chris and Paul also went on to play for Burnley.\n\nJohnny Bravo: Johnny Bravo is an American animated television series created by Van Partible for Cartoon Network, and the second of the network's Cartoon Cartoons.  The series centers on the title character, a muscular and boorish young man who tries to get women to date him, though he is usually unsuccessful.  He ends up in bizarre situations and predicaments, often accompanied by celebrity guest characters such as Donny Osmond or Adam West.  Throughout its run, the show was controversial for its adult humor, pop culture references, and sly adult-oriented jokes.\n\nQuestion: whoch cartoon was Brian Miller the executive producer for and it was also controversial due to its adult humor and language?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cartoon_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cartoon series.\"\n    },\n    \"producer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"producer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the producer.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the producer for the cartoon.\"\n        }\n      },\n      \"required\": [\n        \"producer_name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"controversy_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_controversial\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the cartoon was controversial.\"\n        },\n        \"reasons\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Specific reasons for the cartoon's controversy.\"\n        }\n      },\n      \"required\": [\n        \"is_controversial\",\n        \"reasons\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"cartoon_name\",\n    \"producer_details\",\n    \"controversy_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cartoon_name": {
        "type": "string",
        "description": "The name of the cartoon series."
      },
      "producer_details": {
        "type": "object",
        "properties": {
          "producer_name": {
            "type": "string",
            "description": "The full name of the producer."
          },
          "role": {
            "type": "string",
            "description": "The role of the producer for the cartoon."
          }
        },
        "required": [
          "producer_name",
          "role"
        ],
        "additionalProperties": false
      },
      "controversy_details": {
        "type": "object",
        "properties": {
          "is_controversial": {
            "type": "boolean",
            "description": "Indicates if the cartoon was controversial."
          },
          "reasons": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Specific reasons for the cartoon's controversy."
          }
        },
        "required": [
          "is_controversial",
          "reasons"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "cartoon_name",
      "producer_details",
      "controversy_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
