{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBen Whitehead: Benjamin \"Ben\" Whitehead is an English voice actor.  He has been working on films with Aardman Animations since 2005.  Along with voicing roles for characters, he is Aardman's read-in artist and is the official voice for Wallace after Peter Sallis' retirement and subsequent death.\n\nFlushed Away: Flushed Away is a 2006 British-American computer-animated action-adventure comedy film directed by David Bowers and Sam Fell, produced by Cecil Kramer, David Sproxton, and Peter Lord, and written by Dick Clement, Ian La Frenais, Chris Lloyd, Joe Keenan and William Davies.  It is the third and final film to be co-produced by Aardman Animations and DreamWorks Animation following \"Chicken Run\" (2000) and \"\" (2005), and was Aardman's first completely computer-animated feature as opposed to their usual stop-motion standard.  The film stars the voice talents of Hugh Jackman, Kate Winslet, Andy Serkis, Bill Nighy, Ian McKellen, Shane Richie and Jean Reno.\n\nMinotaur and Little Nerkin: Minotaur and Little Nerkin is a 1999 British animated short film created by Aardman Animations.  Its full name appears, according to the film itself, to be Minotaur and Little Nerkin in Bait, suggesting that its name is in fact \"Bait\", as an episode of a suggested series of films called \"Minotaur and Little Nerkin\", of which no other episodes were made, or that the name of the film is \"Bait\" and is merely stating it stars Minotaur and Little Nerkin.  Regardless, \"Minotaur and Little Nerkin\" is the name used on the packaging for the \"Aardman Classics\" DVD.\n\nGulp (film): Gulp is a 2011 British animated short film by Nokia and Aardman Animations.  Wieden + Kennedy, an agency from Portland, is responsible for the campaign.  It is considered a spiritual successor to another Aardman short, Dot.  Gulp was filmed \"on the world’s largest stop-motion set\".  The film is under 2 minutes long, and is followed by a behind-the-scenes featurette.  The co-directors were Will Studd and Sumo Science.\n\nPeter Lord: Peter Lord, CBE (born 4 November 1953) is a British animator, film producer, director and co-founder of the Academy Award-winning Aardman Animations studio, an animation firm best known for its clay-animated films and shorts, particularly those featuring plasticine duo Wallace and Gromit.  He also directed \"The Pirates!  In an Adventure with Scientists! \" which was nominated for Best Animated Feature at the 85th Academy Awards.\n\n4mations: 4mations is a website made for people to upload, view and share animated films and games.  The site was founded in 2008 by the Channel Four Television Corporation, sponsored by Aardman Animations and Lupus Films.  As the site is targeted to adults, risque animations are often featured.\n\nWallace and Gromit: Wallace and Gromit is a British clay animation comedy series created by Nick Park of Aardman Animations.  The series consists of four short films and a feature-length film.  The series centres on Wallace, a good-natured, eccentric, cheese-loving inventor, along with his companion Gromit, a silent yet loyal and intelligent anthropomorphic dog.  Wallace was originally voiced by veteran actor Peter Sallis, but as of 2011, this role has been passed on to Ben Whitehead.  Gromit remains silent, communicating only through means of facial expressions and body language.\n\nAardman Animations: Aardman Animations, Ltd., also known as Aardman Studios, or simply as Aardman, is a British animation studio based in Bristol.  Aardman is known for films made using stop-motion clay animation techniques, particularly those featuring Plasticine characters Wallace and Gromit.  After some experimental computer animated short films during the late 1990s, beginning with \"Owzat\" (1997), it entered the computer animation market with \"Flushed Away\" (2006).  Aardman films have made $973.2 million worldwide and average $163 million per film.  All of their stop motion films are among the highest-grossing stop-motion films, with their debut, \"Chicken Run\" (2000), being their top-grossing film as well as the highest-grossing stop-motion film of all time.\n\nAdam (1992 film): Adam is a 1991 British 6-minute stop motion clay animated short film written, animated and directed by Peter Lord of Aardman Animations.  It was nominated for an Academy Award for best short film, and won the equivalent award at BAFTA in 1992 as well as the Annecy International Animated Film Festival in 1993.  It is based on the beginning of the Book of Genesis.  It was distributed by Aardman Animations.\n\nRex the Runt: Rex the Runt is a British live action stop motion animated claymation pixilation comedy franchise, primarily consisting of a television show and two short films produced by Aardman Animations for BBC Bristol in association with EVA Entertainment and Egmont Imagination.  Its main characters are four plasticine dogs: Rex, Wendy, Bad Bob and Vince.\n\nQuestion: Aardman Animations is known for their films featuring the the plasticine characters created by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"animation_studio_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the animation studio.\"\n    },\n    \"known_for_characters\": {\n      \"type\": \"array\",\n      \"description\": \"A list of character series or duos the studio is known for.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"character_series_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the character series or duo.\"\n          },\n          \"character_material\": {\n            \"type\": \"string\",\n            \"description\": \"The material used for the characters, e.g., plasticine.\"\n          }\n        },\n        \"required\": [\n          \"character_series_name\",\n          \"character_material\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"character_creator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who created the specified characters.\"\n    },\n    \"creator_affiliation\": {\n      \"type\": \"string\",\n      \"description\": \"The studio or company the creator is affiliated with.\"\n    }\n  },\n  \"required\": [\n    \"animation_studio_name\",\n    \"known_for_characters\",\n    \"character_creator_name\",\n    \"creator_affiliation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "animation_studio_name": {
        "type": "string",
        "description": "The name of the animation studio."
      },
      "known_for_characters": {
        "type": "array",
        "description": "A list of character series or duos the studio is known for.",
        "items": {
          "type": "object",
          "properties": {
            "character_series_name": {
              "type": "string",
              "description": "The name of the character series or duo."
            },
            "character_material": {
              "type": "string",
              "description": "The material used for the characters, e.g., plasticine."
            }
          },
          "required": [
            "character_series_name",
            "character_material"
          ],
          "additionalProperties": false
        }
      },
      "character_creator_name": {
        "type": "string",
        "description": "The name of the individual who created the specified characters."
      },
      "creator_affiliation": {
        "type": "string",
        "description": "The studio or company the creator is affiliated with."
      }
    },
    "required": [
      "animation_studio_name",
      "known_for_characters",
      "character_creator_name",
      "creator_affiliation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
