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
The Baytown Outlaws: The Baytown Outlaws is a 2012 action comedy film directed by Barry Battles in his directorial debut, and written by Battles and Griffin Hood.  The film stars Andre Braugher, Clayne Crawford, Daniel Cudmore, Travis Fimmel, Eva Longoria, Paul Wesley, and Billy Bob Thornton.  The film follows the Oodie brothers-Brick, Lincoln and McQueen-who act as vigilante killers for the local sheriff.  When the trio accept a job to rescue a young boy from his godfather, plans quickly fall apart as the brothers aim to deliver the boy to safety while pursued by groups of assassins.

Daniel Cudmore: Daniel Cudmore (born January 20, 1981) is a Canadian actor and stuntman.  He is perhaps best known for his roles as the mutant Piotr Rasputin / Colossus in the "X-Men" film franchise, and as the Volturi Felix in the "Twilight Saga" films.

Bending the Rules: Bending the Rules is a 2012 action comedy film directed by Artie Mandelberg, produced by WWE Studios, and starring Adam "Edge" Copeland and Jamie Kennedy.  The film was released on March 9, 2012 in select theaters in the United States for a limited time.

Shakti (2012 film): Shakti is a 2012 action Kannada film directed by Anil Kumar starring Malashri and P. Ravi Shankar.  This is Ramu Enterprises 32nd film produced by Ramu.  The film released across Karnataka on 6 January 2012.  The film was dubbed and released in Telugu as "Bommali".

Mark Wahlberg: Mark Robert Michael Wahlberg (born June 5, 1971) is an American actor, producer, businessman, former model, and former rapper.  Wahlberg was known as Marky Mark in his early career as frontman for the group Marky Mark and the Funky Bunch, releasing the albums "Music for the People" and "You Gotta Believe".  Wahlberg later transitioned to acting, appearing in films such as the drama "Boogie Nights" and the satirical war comedy-drama "Three Kings" during the 1990s.  In the 2000s, he starred in the biographical disaster drama "The Perfect Storm", the science fiction film "Planet of the Apes", the heist film "The Italian Job", and the Martin Scorsese-directed neo-noir crime drama "The Departed", for which he received an Academy Award nomination for Best Supporting Actor.  In the 2010s, he starred in the action comedy "The Other Guys" alongside Will Ferrell, the biographical sports drama "The Fighter" (for which he earned an Academy Award nomination as a producer for Best Picture), the comedy "Ted", the war film "Lone Survivor", the crime comedy "Pain & Gain", the science fiction action film "" and the sequel "", the comedy "Daddy's Home", the disaster film "Deepwater Horizon", and the thriller "Patriots Day".

The Bounty (2012 film): The Bounty is a 2012 action comedy film featuring the directorial debut of Fung Chi Keung and starring Chapman To, Fiona Sit and Alex Man.  In November, the film received the Hong Kong Film Development Fund's "Film Development Foundation Film Production Finance Project" to provide HK$2,605,711 of finance.  This is the 13th film financed by The Hong Kong Film Development Fund.

Tony Scott: Anthony David Leighton Scott (21 June 1944 – 19 August 2012) was an English film director and producer.  His films come from a broad range of genres, including the action drama "Top Gun" (1986), action comedy "Beverly Hills Cop II" (1987), auto racing film "Days of Thunder" (1990), action comedy "The Last Boy Scout" (1991), romantic dark comedy crime film "True Romance" (1993), submarine action film "Crimson Tide" (1995), psychological thriller "The Fan" (1996), spy thriller "Enemy of the State" (1998), spy film "Spy Game" (2001), action thriller "Man on Fire" (2004), sci-fi action thriller "Déjà Vu" (2006), thriller "The Taking of Pelham 123" (2009), and the action thriller "Unstoppable" (2010).

Salute Your Solution: "Salute Your Solution" is a song by The Raconteurs.  It is the first single from their second album "Consolers of the Lonely".  It was released on March 25, 2008 the same day as the album release.  Jack White and Brendan Benson share lead vocal duties on the track.  The song is featured in the commercials for "NFL on Fox", the 2009 comedy film "Zombieland", 2012 action film "Premium Rush" , 2017 Power Rangers film , and is available as downloadable content for the music video games "Guitar Hero World Tour" and "Rock Band 2", and it is featured in the launch trailer for "".  The song was also in the documentary "Warren Miller's Children of Winter".

Julai (soundtrack): Julai is the feature film soundtrack of the 2012 action comedy film of the same name starring Allu Arjun, Ileana D'Cruz, Sonu Sood and Rajendra Prasad.  Directed by Trivikram Srinivas, the film's music and background score was composed by Devi Sri Prasad marking his second collaboration after "Jalsa" in 2008.  The Official Soundtrack Album consists of 6 songs composed by Devi Sri Prasad and Ramajogayya Sastry, Sri Mani and Devi Sri Prasad himself penning the lyrics.  Being recorded in 2012, the film's Soundtrack Album was launched on June 10, 2012 in a grand promotional event at Hitex Exhibition Center in Madhapur, Hyderabad on Aditya Music label.  The audio received positive response from both critics and audience alike.

Frank Kush: Frank Joseph Kush (January 20, 1929 – June 22, 2017) was an American football player and coach.  He served as the head coach at Arizona State University from 1958 to 1979, compiling a record of 176–54–1.  Kush was also the head coach of the Canadian Football League's Hamilton Tiger-Cats in 1981, the National Football League's Baltimore/Indianapolis Colts from 1982 to 1984, and the Arizona Outlaws of the United States Football League in 1985.  He was inducted into the College Football Hall of Fame as a coach in 1995.  Kush is of Polish descent and was inducted into the National Polish-American Sports Hall of Fame.

Question: The Baytown Outlaws is a 2012 action comedy film, which Canadian actor, that starred in it, was born on January 20, 1981

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "actor_nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "actor_birth_date": {
          "type": "string",
          "description": "The birth date of the actor in 'Month Day, Year' format."
        },
        "other_notable_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other well-known roles of the actor."
        }
      },
      "required": [
        "actor_name",
        "actor_nationality",
        "actor_birth_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_genres",
    "actor_details"
  ],
  "additionalProperties": false
}
