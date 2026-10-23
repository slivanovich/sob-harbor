{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHouse of Anubis: House of Anubis is a mystery television series developed for Nickelodeon based on the Dutch-Belgian television series \"Het Huis Anubis\".  The series was created by Hans Bourlon and Gert Verhulst and premiered on Nickelodeon on 1 January 2011 in the United States and on 25 February 2011 in the United Kingdom.  The series is the first series from the network to be filmed outside the United States and the first telenovela-format series for the network.  The show aired from 1 January 2011 to 17 June 2013.\n\nThe Lion Guard: The Lion Guard is an American animated television series developed by Ford Riley based on Disney's 1994 film \"The Lion King.\"  The series was first broadcast with a television movie, titled The Lion Guard: Return of the Roar on Disney Channel on November 22, 2015, and began airing as a TV series on January 15, 2016, on Disney Junior and Disney Channel.  It is the second television series to be based on \"The Lion King,\" the first being \"Timon & Pumbaa\" (1995–1999).  \"The Lion Guard\" is a sequel to \"The Lion King\" and takes place during the time-gap within the 1998 film \".\"\n\nJosquin Des Pres (20th century musician): Josquin Des Pres (Born Josquin Turenne Des Pres) is a 20th-century French born American composer, bassist, author, producer, songwriter and most known for his contributions to music media books for Hal Leonard Corporation and Mel Bay instructional music books.  Josquin has written a vast library of compositions and music techniques on bass, music studies and various collections which are used by music teachers, private studies and in schools both nationally and internationally as a standard tool in the music industry.  Des Pres is also a collaborative writer with English lyricist, poet, and singer Bernie Taupin on several compositions.  Josquin Des Pres also writes musical scores and music trailers for more than 40 major TV networks and television shows including The Ellen DeGeneres Show, The Bachelor (U.S. TV series), American Idol, The Tyra Banks Show, George Lopez (TV series), Anderson Cooper, TMZ on TV, Extra (TV program), American Chopper, Pawn Stars, Deadliest Catch, CNN, NBC, HGTV, TBS (U.S. TV channel), Bravo (U.S. TV network), Food Network, Animal Planet, Discovery Channel, History (U.S. TV channel), Travel Channel, CBS Television Stations, Viacom, VH1, ABC, BET, KPBS (TV), TLC (TV network), and The CW Network.  His works are also known on MTV Networks Television Series Catfish, The Seven, When I Was Seventeen, MTV Cribs, Pimp My Ride, Teen Mom, True Life and 10 on Top.\n\nDamon Dark: Damon Dark is an independent public access TV series and web series from Australia about a heroic and obsessive investigator of UFO incidents and other strange cases, created by Australian writer, actor and film maker Adrian Sherlock.  Damon James Dark became a dedicated alien investigator after a close encounter during his teenage years.  He is associated with both the secret service and friendly aliens, including a character called Vincent Kosmos (an alien time traveller) and Trans-Dimensional Control (an alien law enforcement agency).  The character of Damon Dark has appeared in a 5-week TV series on Community TV 31 in Melbourne Australia, a self-published novel (\"Biodome\") on Amazon's createspace platform and a long running web series on YouTube.  He has also been involved in related web series \"Young Damon Dark\" and \"Vincent Kosmos.\"  He has also been the focus of a one actor stage drama.  The character of Damon Dark has been played by Adrian Sherlock, Bruce Hughes, Aiden Sherlock and Jack Knoll.  Damon Dark is a loner, dresses in black, has a huge experience of aliens and their technology.  Damon is characterized by his high intelligence, idealistic moral outlook and wry sense of humor.  His best friend in the series is the long-suffering Gary Sutton, played by actor Robert Trott.  Damon Dark began in 1999, with a five-part weekly series on Melbourne's Community TV 31, (although the pilot was shot in 1996 and the show had been in development since 1990) following a screening of a 65-minute version of the story \"Maddox\" at the 57th World Science Fiction Convention (Aussiecon Three) held in Melbourne.  The series was later revived as a YouTube webseries which inspired several related webseries, including \"The Young Damon Dark Adventures\" in which the character is played as a teenager, and Vincent Kosmos, (created by and starring Chris Heaven, , an Italian actor and musician, about a renegade alien character who is a friend of Damon.\n\nPhilippa Coulthard: Philippa Coulthard (born 25 November 1992) is an Australian television actress, best known for playing Jorjie in the \"Doctor Who\" spin-off series \"K-9\", and lead character Amber Mitchell in \"Lightning Point\".  She is married to the Spanish-American basketball player from Baskonia, Mickey Mickeal.\n\nEmerald City (TV series): Emerald City is an American fantasy television series developed for NBC by Matthew Arnold and Josh Friedman, and based on the Oz book series written by L. Frank Baum, set in the fictional Land of Oz.  Directed by Tarsem Singh and starring Adria Arjona, Oliver Jackson-Cohen, Ana Ularu and Vincent D'Onofrio, \"Emerald City\" received a 10-episode order by NBC in April 2015, which premiered on January 6, 2017, with a two-episode debut, and concluded on March 3, 2017.  On May 5, 2017, NBC canceled the series after one season.\n\nElisa Donovan: Elisa Donovan (born Lisa Adaline Donovan; February 3, 1971) is an American actress, writer, and producer.  She is most recognized as the character Amber from the 1995 film \"Clueless\", in which she starred opposite Alicia Silverstone.  She would reprise the role for the 1996-99 TV series of the same name, with Rachel Blanchard taking over Silverstone's role.  She also starred in six films in the acclaimed \"The Dog Who Saved\" saga.\n\nAna Mulvoy-Ten: Ana Maria Mulvoy-Ten (born 8 May 1992 ) is an English-born Spanish actress.  She is known for playing the character of Amber Millington on the British boarding school drama \"House of Anubis\".\n\nList of The Lion Guard episodes: \"The Lion Guard\" is an American animated television series developed by Ford Riley based on Disney's 1994 film \"The Lion King.\"  The series was first broadcast with a television movie, titled The Lion Guard: Return of the Roar on Disney Channel on November 22, 2015 and began airing as a TV series on January 15, 2016 on Disney Junior and Disney Channel.  \"The Lion Guard\" is a sequel to \"The Lion King\" and takes place during the time-gap within the 1998 film \".\"\n\nHarshad Chopra: Harshad Chopra(born May 17, 1983) is an Indian soap opera actor.  His works include the TV shows \"Humsafars\", \"Dharampatni\", \"Left Right Left (TV series)\", \"Kis Desh Mein Hai Meraa Dil\", \"Tere Liye (TV series)\", \"Mamta (TV series)\" and \"Amber Dhara\".\n\nQuestion: Ana Mulvoy-Ten plays the character Amber Millington on a tv series developed for what network?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress.\"\n    },\n    \"tv_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"network_developed_for\": {\n      \"type\": \"string\",\n      \"description\": \"The television network the series was developed for.\"\n    },\n    \"series_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the television series.\"\n    },\n    \"series_format\": {\n      \"type\": \"string\",\n      \"description\": \"The format of the television series.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_name\",\n    \"tv_series_name\",\n    \"network_developed_for\",\n    \"series_genre\",\n    \"series_format\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actress."
      },
      "tv_series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "network_developed_for": {
        "type": "string",
        "description": "The television network the series was developed for."
      },
      "series_genre": {
        "type": "string",
        "description": "The genre of the television series."
      },
      "series_format": {
        "type": "string",
        "description": "The format of the television series."
      }
    },
    "required": [
      "actor_name",
      "character_name",
      "tv_series_name",
      "network_developed_for",
      "series_genre",
      "series_format"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
