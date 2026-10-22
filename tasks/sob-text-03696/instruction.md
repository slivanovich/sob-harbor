Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Rodney Glunder: Rodney Glunder (born as "Rodney Faverus", March 1, 1975) is a Dutch-Surinamese semi-retired professional kickboxer, mixed martial artist, professional wrestler and boxer, current actor, entrepreneur, bodybuilder.  He has fought for M-1 Global, Cage Rage, K-1, PRIDE Fighting Championship, RINGS, Glory, Konfrontacja Sztuk Walki, It's Showtime, SuperKombat, SLAMM!!  Events and Art of War Fighting Championship.  Glunder holds notable wins over top contenders Cheick Kongo, Valentijn Overeem, Joe Riggs, Melvin Manhoef, Cyrille Diabaté, Brian Douwes and Gregory Tony.

Wolfslair MMA Academy: The Wolfslair MMA Academy is a fight team and training camp for mixed martial artists and kickboxers, headquartered in Widnes, England.  The school was founded by Liverpool MMA fans Anthony McGann and Lee Gwynn.  The academy earned publicity from their signing of former UFC light heavyweight champion Quinton Jackson, former UFC heavyweight Cheick Kongo, and current UFC middleweight champion Michael Bisping to training and managerial contracts.  With these signings, Wolfslair became noted as one of the most prominent training stables in the UK's MMA scene.

Israel Piano Trio: The Israel Piano Trio (Hebrew: שלישיית הפסנתר הישראלית‎ ‎ ) is a classical piano trio founded in 1972 by the pianist Alexander Volkov, the violinist Menahem Breuer, and the cellist Zvi Harell.

Alexander Alexandrovich Volkov (politician): Alexander Alexandrovich Volkov (Udmurt and Russian: Алекса́ндр Алекса́ндрович Во́лков ; 25 December 1951 in Bryansk – 20 May 2017) was the President of the Udmurt Republic.  As President, Volkov was the highest official in the Udmurt Republic, the head of the republic's highest executive body, and leader of its two million citizens.  Volkov took office November 3, 2000, for a five-year term after the first presidential elections in the Udmurt Republic took place on October 15, 2000.  Prior to the elections, Volkov was the speaker of the Udmurtia Republican Legislature.

Glaube Feitosa: Glaube Araújo Feitosa (born April 9, 1973) is a Brazilian former kickboxer and a kyokushin full contact karate practitioner who was competing in K-1.  In 2005, Feitosa won K-1 World Grand Prix 2005 in Las Vegas tournament and was a K-1 World Grand Prix 2005 finalist.  While living in Tokyo, Japan he fought and trained in the IKO1 Kyokushin - Team Ichigeki at the Ichigeki Plaza.  Throughout his career he was known as one of the best non-champions to fight in the K-1, a position he earned with his wins over non-champion fighters, such as Ruslan Karaev, Musashi, Gary Goodridge and Junichi Sawayashiki.  He also went the distance with some of the top fighters in his time, such as Peter Aerts, Remy Bonjasky, Semmy Schilt and Errol Zimmerman.  He holds victories over Cheick Kongo and Alistair Overeem.

1995 Kremlin Cup – Singles: Alexander Volkov was the defending champion, but lost to Daniel Vacek in the quarterfinal. Carl-Uwe Steeb won in the final 7–6, 3–6, 7–6 against Daniel Vacek.

Leonid Vladimirsky: Leonid Vladimirsky (21 September 1920 in Moscow, Russia - 18 April 2015) was a Russian illustrator who worked on fairy tales, including books by Alexander Pushkin ("Ruslan and Ludmila"), Aleksey Tolstoy ("Golden Key", 1953), and Alexander Volkov, as well as some folk tales.

Alexander Volkov (fighter): Alexander Yevgenievich Volkov (Russian: Александр Евгеньевич Волков ; born October 24, 1988) is a Russian mixed martial artist who competes in the UFC heavyweight division.  A professional MMA competitor since 2009, Volkov has competed almost exclusively for the M-1 Global promotion, as well as Bellator MMA.  He is a former Heavyweight Champion in both promotions.  He is currently ranked as the #7 contender in the official UFC rankings.

1994 Kremlin Cup – Singles: Marc Rosset was the defending champion, but lost to Chuck Adams in the semifinal. Alexander Volkov won in the final 6–2, 6–4 against Chuck Adams.

Cheick Kongo: Cheick Guillaume Ouedraogo (born May 17, 1975), more commonly known as Cheick Kongo, is a French heavyweight mixed martial artist and former kickboxer who fights in Bellator MMA.  He holds notable wins over the likes of Mirko Cro Cop, Lavar Johnson, Shawn Jordan, Matt Mitrione, Alexander Volkov and Pat Barry.  As of June 19, 2017, he is #12 in the world rankings by Sherdog.

Question: Who was born first, Cheick Kongo or ALexander Volkov?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the first person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "second_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the second person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_born_earlier_name": {
      "type": "string",
      "description": "The name of the person who was born earlier."
    },
    "year_difference": {
      "type": "integer",
      "description": "The difference in birth years between the two individuals."
    }
  },
  "required": [
    "first_person",
    "second_person",
    "person_born_earlier_name",
    "year_difference"
  ],
  "additionalProperties": false
}
