{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCasanova Wong: Casanova Wong, also known as Ka Sat Fat (卡薩伐), is a former Korean martial arts actor born in 1945 as Yong-ho Kim in Gimje, South Korea.  An expert in tae kwon do, he is a leg-fighter, and is well known for his spin kicks and was nicknamed \"The Human Tornado\" in the Republic of Korea Army.  He made many appearances in martial arts movies but is most remembered for his role as Cashier Hua in \"Warriors Two\", where he starred alongside Sammo Hung, with whom he worked several times.  Other films included \"Story of Drunken Master\" and \"Rivals of the Silver Fox\".  One of Wong's last notable movie appearances was as Kang-ho in the 1994 Korean movie \"Bloody Mafia\".\n\nHarley Cokeliss: Harley Cokeliss (born 1945) is an American director, producer, writer and actor born in San Diego.  He was born Harley Louis Cokliss, and his name is credited as Cokliss until the late 1980s, when he changed the spelling to Cokeliss.\n\nSteve Arbuckle: Stephen \"Steve\" George Arbuckle is a Canadian born actor born in the village of Donkin (Arbuckle Lane), Cape Breton Island, Nova Scotia.  He started his career as a theatre actor at Cape Breton University, then made his first move into film in 2003 with the lead role in the short film \"Todd and the Book of Pure Evil\", which also starred Julian Richings and John Bregar.  He appeared as Oliver Peele in 2010 in the pilot episode of the CBS show \"Blue Bloods\".  Arbuckle is now living in Toronto, Ontario.\n\nMiraj Grbić: Miraj Grbic is a Film, Television and Theatre actor born on July 17, 1976 in Sarajevo, Bosnia and Herzegovina.  He currently lives in Los Angeles, California.  Miraj graduated from the Academy of Performing Arts in Sarajevo at the University of Sarajevo, where he earned MA Degree in Acting.  Since 1996 he has performed in more than 60 theater plays on the main stage of the Sarajevo National Theatre.  He starred in almost 40 Feature films in Bosnian, Croatian, German, Austrian, Italian, Irish, Polish, Turkish, Macedonian, Australian, Canadian and US productions.  He starred as Bogdan in \"\", where he performed opposite Tom Cruise.  Grbic starred in television shows such as \"Ruža vjetrova\", \"Lud, zbunjen, normalan\", \"Gang Related\" and \"Viza za budućnost\".  He lives in Los Angeles since 2013.\n\nCharles Kemper: Charles Kemper (September 6, 1900 – May 12, 1950) was an American character actor born in Oklahoma.  The heavy-set actor was for decades a successful stage actor.  He made only sporadic screen appearances until 1945, when he settled in Hollywood.  Kemper had memorable supporting roles in films including \"The Southerner\" (1945), \"Scarlet Street\" (1945), \"Gallant Journey\" (1946), \"The Shocking Miss Pilgrim\" (1947), and the film noir \"On Dangerous Ground\" (as Pop Daly, his last film role).\n\nJohn Lithgow: John Arthur Lithgow ( ; born October 19 , 1945) is an American actor, musician, singer, comedian, voice actor, and author.  He has received two Tony Awards, six Emmy Awards, two Golden Globe Awards, three Screen Actors Guild Awards, an American Comedy Award, four Drama Desk Awards and has also been nominated for two Academy Awards and four Grammy Awards.  Lithgow has received a star on the Hollywood Walk of Fame and has been inducted into the American Theater Hall of Fame.\n\nTrial &amp; Error (TV series): Trial & Error (formerly known as \"The Trail\") is an American sitcom television series created by Jeff Astrof and Matt Miller for NBC.  Produced by Warner Bros.  Television, the series was commissioned in May 2016, and premiered on March 14, 2017.  It stars Nicholas D'Agosto, Jayma Mays, Steven Boyer, Krysta Rodriguez, and Sherri Shepherd, with John Lithgow also starring in the first season.  The series, which spoofs documentaries and reality legal shows, follows Northeastern lawyer Josh Segal (portrayed by D'Agosto) and his eccentric local associates (portrayed by Boyer and Shepherd) in a fictional small town in South Carolina called East Peck as he represents accused local citizens.\n\nNicholas D'Agosto: Nicholas D'Agosto (born April 17, 1980) is an American actor.  He is known for being the lead of \"Final Destination 5\" and his recurring role in \"Heroes\".  He starred in the Showtime series \"Masters of Sex\" and the Fox series \"Gotham\".  D'Agosto also stars in NBC's new show \"Trial & Error\".\n\nNikolay Bogolyubov (actor): Nikolay Ivanovich Bogolyubov (Russian: Никола́й Ива́нович Боголю́бов ; October 22, 1899 – March 9, 1980) was a Soviet actor born in Ivanovskoye, Russia and a People's Artist of the RSFSR (1945).  In 1933 he played in Boris Barnet's \"Okraina\"; in 1941, he was awarded the Stalin Prize.\n\nHarmless error: A harmless error is a ruling by a trial judge that, although mistaken, does not meet the burden for a losing party to reverse the original decision of the trier of fact on appeal, or to warrant a new trial.  Harmless error is easiest to understand in an evidentiary context.  Evidentiary errors are subject to harmless error analysis, under Federal Rule of Evidence 103(a) (\"Error may not be predicated upon a ruling which admits or excludes evidence unless a substantial right of the party is affected.\")  The general burden when arguing that evidence was improperly excluded or included is to show that the proper ruling by the trial judge may have, on the balance of probabilities, resulted in the opposite determination of fact.\n\nQuestion: What actor born in 1945 starred in the show \"Trial & Error\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the actor was born.\"\n    },\n    \"starred_in_show\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"show_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the television series the actor starred in.\"\n        },\n        \"season_details\": {\n          \"type\": \"string\",\n          \"description\": \"Specific details about the actor's involvement in the show, e.g., which season(s).\"\n        }\n      },\n      \"required\": [\n        \"show_title\",\n        \"season_details\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"birth_year\",\n    \"starred_in_show\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "birth_year": {
        "type": "integer",
        "description": "The year the actor was born."
      },
      "starred_in_show": {
        "type": "object",
        "properties": {
          "show_title": {
            "type": "string",
            "description": "The title of the television series the actor starred in."
          },
          "season_details": {
            "type": "string",
            "description": "Specific details about the actor's involvement in the show, e.g., which season(s)."
          }
        },
        "required": [
          "show_title",
          "season_details"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "birth_year",
      "starred_in_show"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
