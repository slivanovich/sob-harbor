{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRicardo Darín: Ricardo Darín (] ; born January 16, 1957) is an Argentine actor, screenwriter and film director.  Widely considered as one of the best and most prolific actors of Argentine cinema.\n\nMoon Hee: Moon Hee (born July 16, 1947) is a South Korean actress active since 1965.  She was born in Busan, South Korea in 1947.  While attending Seorabeol Art College with a film and theater major, Moon applied for recruiting new actors by KBS TV.  When she was attending for a camera test, Moon was picked up by an assistant director of Lee Man-hee .  Moon was cast to star in Lee's film \"Heukmaek\".  Moon was commonly referred to as one of the \"Troika\" along with her rival actresses, Yoon Jeong-hee and Nam Jeong-im of the 1960s and early 1970s.  Moon Hee retired from the acting career when she married Jang Gang-jae, the vice president of Hankook Ilbo in November 1971 who later became the chair of the newspaper company.\n\nMoon of Avellaneda: Moon of Avellaneda (Spanish: \"Luna de Avellaneda\" , also known as \"Avellaneda's Moon\" in English) is a 2004 Argentine film directed by Juan José Campanella, and written by Campanella, Fernando Castets and Juan Pablo Domenech.  The film stars Ricardo Darín in his third collaboration with Campanella and Eduardo Blanco in his fourth collaboration, as well as Mercedes Morán and Valeria Bertuccelli.\n\nDubber Side of the Moon: Dubber Side of the Moon is the second dub reggae tribute to the Pink Floyd album, \"The Dark Side of the Moon\", by New York-based band Easy Star All-Stars.  The album features bass-heavy dub remixes by prominent dub producers of its predecessor, Easy Star Records' 2003 release \"Dub Side of the Moon\".  \"Dubber Side of the Moon\" debuted at #2 on the Billboard Reggae charts.\n\nPierre Alonzo (footballer): Pierre Alonzo (born 23 March 1940) is a former French football midfielder who played for Aïn-Temouchent, Avellaneda, Perpignan, Red Star, Cannes and Rapid de Menton.\n\nSailor Moon R: The Movie: Sailor Moon R: The Movie, known in Japan as Pretty Soldier Sailor Moon R: The Movie, is a 1993 Japanese anime fantasy film directed by Kunihiko Ikuhara and written by Sukehiro Tomita based on the \"Sailor Moon\" manga series written by Naoko Takeuchi.  The film takes its name from the second arc of the \"Sailor Moon\" anime, \"Sailor Moon R\", as Toei Company distributed it around the same time.  The events portrayed seem to take place somewhere in the very end of the series, as Chibiusa knows about the identities of the Sailor Guardians, the characters are in the present rather than the future, and Mamoru and Usagi are back together.  The film centers on the arrival of an alien named Fiore on Earth, who has a past with Mamoru and wishes to reunite with him.  Unfortunately, Fiore is being controlled by an evil flower called Xenian Flower, forcing Usagi and her friends to save Mamoru and the Earth from destruction.\n\nDub Side of the Moon: Dub Side of the Moon is a dub reggae tribute to the Pink Floyd album, \"The Dark Side of the Moon\", co-produced by Easy Star All-Stars founder's Michael G (Michael Goldwasser) and Ticklah (Victor Axelrod).  \"Dub Side of the Moon\" has remained on the Billboard Reggae Charts since its release in 2003.  Easy Star All Stars released \"Dub Side of the Moon: Special Anniversary Edition\" on September 16, 2014.\n\nSailor Moon S: The Movie: Sailor Moon S: The Movie, known in Japan as Pretty Soldier Sailor Moon S The Movie (劇場版 美少女戦士セーラームーンＳ , Gekijōban Bishōjo Senshi Sērā Mūn Sūpā ) and Sailor Moon S the Movie: Hearts in Ice in the Pioneer English adaptation, is a 1994 Japanese anime fantasy film directed by Hiroki Shibata and written by Sukehiro Tomita.  It is the second film in the \"Sailor Moon\" series.  The film is adapted from a side story of the original manga series created by Naoko Takeuchi, \"The Lover of Princess Kaguya\".  The storyline is loosely based on \"The Snow Queen\" fairytale by Hans Christen Andersen.\n\nBAFTA Rising Star Award: Rising Star Award (known from 2013 as EE Rising Star Award, previously known as Orange Rising Star Award) is one of the award categories for the British Academy of Film and Television Arts (BAFTA) which acknowledges new talents in the acting industry.  The award was created after Mary Selway's death in 2004.  She has been recognised for her successful role as a casting director and has helped many new actors and actresses to their claim to fame.  The five nominees have been chosen regardless of gender, nationality and whether they have made a breakthrough in television, film or both.  Despite the nominees being chosen by the BAFTA juries, the winner is chosen entirely by the public votes via text, internet or phone.  This award was sponsored by Orange UK until 2012.  From 2013, it was sponsored by EE.  The first winner was James McAvoy in 2006.\n\nScott Bartlett: Scott Bartlett (1943 – September 29, 1990 in San Francisco, CA) was one of the premiere abstract/experimental movie makers of the late 1960s and the 1970s.  His acclaimed work, such as his intense abstract 16mm movie Moon 1969, is greatly admired by many filmmakers, including Francis Ford Coppola and George Lucas.  His notable abstract movies and visual avant-garde films include \"Serpent\", \"Medina\", \"Metanomen\", \"Lovemaking\", and the poignant interior documentary \"1970\".  His 1967 experiment \"OffOn\", shot on 16mm, was groundbreaking for its use of new video imagery technologies.\n\nQuestion: What nationality is the star of the movie Moon of Avellaneda?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"star_actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the star actor in the movie.\"\n        },\n        \"actor_nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the star actor.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"actor_nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the film itself.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"star_actor_details\",\n    \"film_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "star_actor_details": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the star actor in the movie."
          },
          "actor_nationality": {
            "type": "string",
            "description": "The nationality of the star actor."
          }
        },
        "required": [
          "actor_name",
          "actor_nationality"
        ],
        "additionalProperties": false
      },
      "film_nationality": {
        "type": "string",
        "description": "The nationality of the film itself."
      }
    },
    "required": [
      "movie_title",
      "star_actor_details",
      "film_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
