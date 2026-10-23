{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRobot Chicken: Robot Chicken is an American stop motion sketch comedy television series, created and executive produced for Adult Swim by Seth Green and Matthew Senreich along with co-head writers Douglas Goldstein and Tom Root.  The writers, especially Green, also provide many of the voices.  Senreich, Goldstein, and Root were formerly writers for the popular action figure hobbyist magazine \"ToyFare\".  \"Robot Chicken\" has won an Annie Award and five Emmy Awards.\n\nStar Wars Detours: Star Wars Detours is an American computer-animated television series produced by Lucasfilm Animation in collaboration with \"Robot Chicken\" creators Seth Green and Matthew Senreich.  Although roughly two seasons of the show exist, they have never been released to the public.  Since The Walt Disney Company's acquisition of Lucasfilm in 2012, the show has been on hiatus, to allow Lucasfilm Animation to focus fully on the next entries in the \"Star Wars\" film saga, Episodes VII-IX.  It is unclear if the finished episodes will be released at some point in the future.\n\nLegion M: Legion M was founded by Paul Scanlan and Jeff Annison in March, 2016.  Legion M is the world's first entertainment studio that allows fans to invest in and be part of the creation of new movies, television shows, virtual reality and other pieces of entertainment content.  Scanlan and Annison were able to create Legion M after the SEC passed Title IV of the JOBS Act, which allowed non-accredited investors to make investments in small businesses.  Legion M is currently partnered with Seth Green, co-creator of Emmy-winning TV series \"Robot Chicken\", Gaston Dominguez of Meltdown Entertainment, and gaming studio Animal Repair Show.\n\nTitan Maximum: Titan Maximum is an American stop motion animated television series created by Tom Root and Matthew Senreich.  The series premiered on Cartoon Network's late night programing block, Adult Swim, on September 27, 2009 with its finale airing on November 22, 2009.  A teaser premiered during the \"\"Robot Chicken\" on Wheels\" tour and at the 2009 San Diego Comic-Con International.  It is a parody of the \"Super Robot\" anime style produced using stop motion animation.\n\nStoopid Monkey: Stoopid Monkey, LLC (stylized as sTOoP!d MoNkEy) is the production company of Seth Green and Matthew Senreich, established in 2005.  It is one of the producers of the Adult Swim animated television series \"Robot Chicken\" and \"Titan Maximum\".\n\nBaDoinkVR: BaDoinkVR is a virtual reality porn production company founded in 2006.  The company is part of \"CM Productions (CMP Group)\", and sister site to \"BaDoink VIP\".  BaDoinkVR is headquartered in Rochester, New York with satellite offices in Barcelona, Spain and Silicon Valley.  The company was the first to drive mass consumer trial by seeding the market with 20,000 free virtual reality cardboard goggles.  According to Piper Jaffray, adult entertainment will be the number three driver of all virtual reality content behind movies and games, and the porn VR business will grow into a $1 billion industry by 2020.\n\nMatthew Senreich: Matthew Ian \"Matt\" Senreich ( ; born June 17, 1974) is an American screenwriter, television producer and director, best known for his work with animated television series \"Robot Chicken\", which he co-created with business partner Seth Green.\n\nJingle All the Way (2011 film): Jingle All the Way is a 2011 American stop motion animated children's television special produced for Hallmark Channel, directed by Chel White and produced at Bent Image Lab.  In reviewing the 2011 television holiday special programs, Mike Hale of \"The New York Times\" called \"Jingle All the Way\" \"...by far the best of the bunch.  In addition to its charming art and pleasantly low-key storytelling, “Jingle” stands apart from the other holiday programs by not focusing on the manufacturing or delivery of toys.\"  Hale also mentions, \"For some honest emotion, and a combination of retro holiday spirit with adventurous animation, tune in for \"Jingle All the Way\"...(it) looks like something you’d see at a European animation festival or late at night on Adult Swim, but it is also gentle and completely Hallmark-appropriate.\"\n\nThe New Adventures of Pinocchio (TV series): The New Adventures of Pinocchio is a syndicated stop motion animated television series produced by Rankin/Bass Productions in the United States and made by Dentsu Studios in Japan.  Created by Arthur Rankin, Jr. and his partner Jules Bass, it was based on the book \"The Adventures of Pinocchio\" written by Italian author, Carlo Collodi.  The series was Rankin/Bass' first production to be made in \"Animagic\", a stop motion puppet technique which, in association with the company, was done by Tadahito Mochinaga's MOM Productions (before Mochinaga leaves for China after the finished animation for \"Mad Monster Party? \").  A total of 130 five-minute \"chapters\" were produced in 1960–61.  These segments made up a series of five-chapter, 25-minute episodes.  During 1963–64, the series was also aired in Japan on Fuji TV as part of another stop motion TV series, \"Prince Ciscorn\" (シスコン王子, lit.  \"Ciscorn Ōji\"), based on the manga by Fujiko Fujio and also produced by Tadahito Mochinaga for Studio KAI and Dentsu.\n\nBuddy Thunderstruck: Buddy Thunderstruck is an American stop motion comedy television series created by Ryan Wiesbrock as a Netflix Original series, produced by American Greetings Entertainment and Stoopid Buddy Stoodios and written by Tom Krajewski.  The series stars Brian Allen, Ted Raimi, Harry Chaskin and Debi Derryberry.  The first season was released on Netflix on March 10, 2017.\n\nQuestion: Legion M is the world's first entertainment studio that allows fans to invest in and be part of the creation of new movies, television shows, virtual reality and other pieces of entertainment content, Legion M is currently partnered with Seth Green, co-creator of which Emmy-winning TV series, an American stop motion sketch comedy television series, created and executive produced for Adult Swim by Seth Green and Matthew Senreich?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"is_emmy_winning\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the series has won an Emmy Award.\"\n    },\n    \"animation_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of animation used for the series.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the television series.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network the series was produced for.\"\n    },\n    \"co_creators\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the co-creators of the series.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"is_emmy_winning\",\n    \"animation_type\",\n    \"genre\",\n    \"network\",\n    \"co_creators\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "is_emmy_winning": {
        "type": "boolean",
        "description": "Indicates if the series has won an Emmy Award."
      },
      "animation_type": {
        "type": "string",
        "description": "The type of animation used for the series."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the television series."
      },
      "network": {
        "type": "string",
        "description": "The television network the series was produced for."
      },
      "co_creators": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the co-creators of the series."
      }
    },
    "required": [
      "series_name",
      "is_emmy_winning",
      "animation_type",
      "genre",
      "network",
      "co_creators"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
