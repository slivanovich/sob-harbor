{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKōzō Shioya: Kōzō Shioya (塩屋 浩三 , Shioya Kōzō , born August 18, 1955) is a Japanese voice actor born in Kagoshima Prefecture.  He is represented by Aoni Production.  His younger brother is voice actor Yoku Shioya.\n\nAlain Dorval: Alain Dorval (born Alain Bergé in 1946) is a French voice actor born in Algiers.  He is best known as the official dub-over artist of Sylvester Stallone, Nick Nolte, and the Disney character Pete.  His voice can also be heard on the radio stations Skyrock and ADO.\n\nTodd Haberkorn: Todd Michael Haberkorn (born August 16, 1982) is an American actor, voice actor, and ADR voice director.  He has provided voices for a number of English-language versions of Japanese anime series, as well as video games and cartoons.  While he was working in theater, he joined Funimation as a voice actor, with some minor bits in \"Black Cat\" and \"Peach Girl\".  He landed the lead roles of Death The Kid in \"Soul Eater\", Allen Walker in \"D.Gray-man\", Natsu Dragneel in \"Fairy Tail\", Ling Yao in \"\", Kimihiro Watanuki in \"xxxHolic\", Yamato Akitsuki in \"Suzuka\", and Tsukune Aono in \"Rosario + Vampire\".  He has worked in Texas and California as an actor, director, producer, and writer.\n\nEiji Kanie: Eiji Kanie (蟹江 栄司 , Kanie Eiji , November 21, 1941 – October 13, 1985) was a Japanese voice actor born in Tokyo.  He is most remembered for being the first voice of Ramenman in Kinnikuman and for playing Vrlitwhai Kridanik in The Super Dimension Fortress Macross.  He died in 1985 of a subarachnoid hemorrhage.  After his death, Banjou Ginga replaced him as Ramenman.\n\nShigezō Sasaoka: Sadao Sasaoka (笹岡 定雄 , Sasaoka Sadao , May 5, 1948 – August 31, 1998) , better known by the stage name Shigezō Sasaoka (笹岡 繁蔵 , Sasaoka Shigezō ) , was a Japanese voice actor born in Fukushima Prefecture, Japan.  After his death, his ongoing roles were replaced with other voice actors.\n\nRon Perlman: Ronald N. Perlman (born April 13, 1950) is an American actor and voice actor.  He is best known for his roles as Vincent on the television series \"Beauty and the Beast\" (1987–1990), for which he won a Golden Globe Award, as the comic book character Hellboy in both \"Hellboy\" (2004) and its sequel \"\" (2008), and Clay Morrow on the television series \"Sons of Anarchy\" (2008–2013).\n\nHideo Ishikawa: Hideo Ishikawa (石川 英郎 , Ishikawa Hideo , born December 13, 1969) is a Japanese voice actor born in Hyōgo Prefecture, Japan.  He works for Aoni Production.\n\nThe Book of Life (2014 film): The Book of Life is a 2014 American 3D computer-animated musical fantasy adventure comedy film produced by Reel FX Creative Studios and distributed by 20th Century Fox.  Co-written and directed by Jorge R. Gutierrez, it was produced by Aaron Berger, Brad Booker, Guillermo del Toro and Carina Schulze.  The film stars the voices of Diego Luna, Zoe Saldana, Channing Tatum, Christina Applegate, Ice Cube, Ron Perlman and Kate del Castillo.  Based on an original idea by Gutierrez, the story follows a bullfighter who, on the Day of the Dead, embarks on an afterlife adventure to fulfill the expectations of his family and friends.\n\nClaudio Moneta: Claudio Moneta (born April 13, 1967 in Milan) is an Italian voice actor.  Moneta contributes to voicing characters in animation, videogames, sitcoms and more.  He is very well known for providing the voice of SpongeBob SquarePants in the Italian-language version of the Nickelodeon animated series SpongeBob SquarePants.  He is also known for voicing Kakashi Hatake in Naruto and Naruto: Shippuden.  The role was temporarily filled by fellow voice actor Gianluca Iacono between 2010 and 2011, due a motorbike incident suffered by Moneta.  He was also replaced in \"Mass Effect 2\" because of that accident as well.\n\nJean Topart: Jean Topart (April 13, 1922 – December 29, 2012) was a French actor and voice actor.  He was considered one of the best known voices on French television for decades.  In addition to providing the voices and narration for television series and animated films, Topart often dubbed American and other foreign films into French.\n\nQuestion: The Book of Life stars the voices of which American actor and voice actor born on April 13, 1950?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The birth date of the actor in YYYY-MM-DD format.\"\n    },\n    \"is_voice_actor\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the individual is a voice actor.\"\n    },\n    \"starred_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film the actor starred in, as per the question.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"nationality\",\n    \"birth_date\",\n    \"is_voice_actor\",\n    \"starred_in_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "birth_date": {
        "type": "string",
        "format": "date",
        "description": "The birth date of the actor in YYYY-MM-DD format."
      },
      "is_voice_actor": {
        "type": "boolean",
        "description": "True if the individual is a voice actor."
      },
      "starred_in_film": {
        "type": "string",
        "description": "The name of the film the actor starred in, as per the question."
      }
    },
    "required": [
      "actor_name",
      "nationality",
      "birth_date",
      "is_voice_actor",
      "starred_in_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
