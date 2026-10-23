{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDC Extended Universe: The Justice League Universe (JLUDCEUUJLDCE), more commonly known by its unofficial name as the DC Extended Universe (DCEU), is an American media franchise and shared universe, centered on a series of superhero films distributed by Warner Bros.  Pictures, based on characters that appear in publications by DC Comics.  The shared universe, much like the original DC Universe in comic books, was established by crossing over common plot elements, settings, cast, and characters.  The films have been in production since 2011 and in that time Warner Bros. has distributed four films with more than ten in various stages of production.  The series has grossed over $3.1 billion at the global box office, currently making it the seventeenth highest-grossing film franchise.\n\nSidney Kennon: Sidney Kennon, known as Mrs. Cannon (died 1754), was an 18th-century British midwife who delivered the babies of royalty and other great families.  She collected numerous creatures, curiosities and specimens.  Her collections were auctioned after her death and she left a large sum of money to promote the delivery of babies by women rather than men.\n\nChris Renaud (animator): Chris Renaud (born December 1966) is an American illustrator and filmmaker.  He was nominated for an Academy Award for the 2006 animated short \"No Time for Nuts\", which featured the character Scrat from the computer animated \"Ice Age\" films.  His most notable work is the \"Despicable Me\" franchise, including \"Despicable Me\" and \"Despicable Me 2\", which he co-directed with Pierre Coffin.  Along with Coffin, he also co-created and lent his voice to the Minions from \"Despicable Me\".\n\nMewtwo: Mewtwo (Japanese: ミュウツー , Hepburn: Myutsū , or) is a fictional creature from Nintendo and Game Freak's \"Pokémon\" media franchise.  Created by Ken Sugimori, it first appeared in the video games \"Pokémon Red\" and \"Blue\" and their sequels, and later appeared in various merchandise, spinoff titles, as well as animation adaptations of the franchise.  Masachika Ichimura voiced the franchise's original Mewtwo character in Japanese, and the creature's younger self is voiced by Fujiko Takimoto in the \"Sound Picture Box: Mewtwo's Origin\" CD drama and Showtaro Morikubo in the anime adaptation.  In English, Jay Goede voiced Mewtwo in \"Mewtwo Strikes Back\" and the \"Pokémon Live! \" musical.  For the former production, he was credited under the pseudonym \"Philip Bartlett\".  Dan Green provided the voice in \"Mewtwo Returns\".  Actress Reiko Takashima voices a separate Mewtwo character in the prequel special \"Mewtwo: Prologue to Awakening\" and the film \"\"; this second Mewtwo is voiced by actress Miriam Pultro in the English dub.\n\nPirates of the Caribbean: Pirates of the Caribbean is a Disney media franchise encompassing numerous theme park attractions, a series of films, and spin-off novels, as well as a number of related video games and other media publications.  The franchise originated with the Pirates of the Caribbean theme ride attraction, which opened at Disneyland in 1967 and was one of the last Disney theme park attractions overseen by Walt Disney.  Disney based the ride on pirate legends and folklore.  As of October 2016, \"Pirates of the Caribbean\" attractions can be found at five Disney theme parks.  Their related films have grossed over US$ 3.7 billion worldwide as of January 2015, putting the film franchise 11th in the list of all-time highest grossing franchises and film series.\n\nDavid Cross: David Cross (born April 4, 1964) is an American stand-up comedian, actor, director and writer, known primarily for his stand-up performances, the HBO sketch comedy series \"Mr. Show\", and his role as Tobias Fünke in the sitcom \"Arrested Development\".  Cross created, wrote, executive produced, and starred in \"The Increasingly Poor Decisions of Todd Margaret\", developed and had a prominent role in \"Freak Show\", appeared on \"Modern Family\", portrayed Ian Hawke in the \"Alvin and the Chipmunks\" film franchise, and voiced Crane in the \"Kung Fu Panda\" film franchise.\n\nList of Pokémon: The \"Pokémon\" franchise revolves around 802 eponymous fictional species of collectible monsters, each having unique designs and skills.  Conceived by Satoshi Tajiri in early 1989, Pokémon are creatures that inhabit the fictional Pokémon World.  The designs for the multitude of species can draw inspiration from anything, such as inanimate objects, real-world animals, or mythology.  Many Pokémon are capable of evolving into more powerful species, while others can undergo form changes and achieve similar results.  Originally, only a handful of artists led by Ken Sugimori designed Pokémon, however, by 2013 a team of 20 artists worked together to create new species designs.  Sugimori and Hironobu Yoshida lead the team and determine the final designs.  Each iteration of the series has brought about praise and criticism over the numerous creatures.\n\nKoffing and Weezing: Koffing and Weezing, known in Japan as Dogars (ドガース , Dogāsu ) and Matadogas (マタドガス , Matadogasu ) respectively, are two Pokémon species in Nintendo and Game Freak's \"Pokémon\" franchise linked through evolution.  Koffing evolves into Weezing after gaining enough experience in battle.  Created by Ken Sugimori, they first appeared in the video games \"Pokémon Red\" and \"Blue\" and later appear in subsequent sequels, various merchandise, spinoff titles, and animated and printed adaptations of the franchise.  In Japanese, both characters are voiced by Unshō Ishizuka; in English Koffing is voiced by Michael Haigney, while Weezing is voiced by Eric Stuart.\n\nMinions (Despicable Me): Minions are the numerous creatures that appear in the \"Despicable Me\" franchise, which began with the eponymous 2010 film.  They are also the official mascots of Illumination Entertainment, a division of Universal Studios, and have been described as being a corporate icon for Universal/Illumination's parent company Comcast on par with Disney's Mickey Mouse following Comcast's purchase of NBCUniversal.\n\nPredator (franchise): The Predator film series is a science fiction action horror film franchise based on a race of fictional extraterrestrials created by Jim Thomas and John Thomas.  Produced by 20th Century Fox, the series started in 1987 with the film \"Predator\", which led to two sequels and novel, comic book and video game spin-offs.  Related to the franchise is the \"Alien vs. Predator\", which combine the titular Predator with the creatures from the \"Alien\" film series.\n\nQuestion: Who voiced the numerous creatures that appear in a film franchise that began in 2010?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"voice_actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who voiced the creatures.\"\n    },\n    \"creature_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the numerous creatures.\"\n    },\n    \"film_franchise_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film franchise.\"\n    },\n    \"franchise_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film franchise began.\"\n    },\n    \"voice_actor_role\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Roles of the person in relation to the creatures or franchise.\"\n    }\n  },\n  \"required\": [\n    \"voice_actor_name\",\n    \"creature_name\",\n    \"film_franchise_name\",\n    \"franchise_start_year\",\n    \"voice_actor_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "voice_actor_name": {
        "type": "string",
        "description": "The name of the person who voiced the creatures."
      },
      "creature_name": {
        "type": "string",
        "description": "The name of the numerous creatures."
      },
      "film_franchise_name": {
        "type": "string",
        "description": "The name of the film franchise."
      },
      "franchise_start_year": {
        "type": "integer",
        "description": "The year the film franchise began."
      },
      "voice_actor_role": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Roles of the person in relation to the creatures or franchise."
      }
    },
    "required": [
      "voice_actor_name",
      "creature_name",
      "film_franchise_name",
      "franchise_start_year",
      "voice_actor_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
