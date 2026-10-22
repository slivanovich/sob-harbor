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
Runway Cop: Runway Cop (, literally "Detective Cha") is a 2012 South Korean action comedy film, starring Kang Ji-hwan and Sung Yu-ri and directed by Shin Tae-ra.  It tells the story of an overzealous and overweight detective Cha Cheol-soo who goes undercover as a fashion model in order to solve a case.  It reunites the two leads since the television series "Hong Gil-dong" (2008), and is the second film Kang has worked on with Shin since "My Girlfriend Is an Agent" (2009).  It was released on May 30, 2012 by CJ Entertainment and ran for 110 minutes.

Shin Seong-il: Shin Seong-il (born May 8, 1937) is a South Korean actor, film director, producer, and former politician.  A legendary actor with 500 films in over 40 years, Shin debuted in director Shin Sang-ok's 1960 film "A Romantic Papa" and rose to fame through popular youth titles.  A star in the 1960s and 1970s, however, his status as one of Korea's top actors extended well into the 1980s.

Red Scarf (film): Red Scarf (), also known as Red Muffler and Operation Air Raid-Red Muffler, is a 1964 South Korean aviation war film set during the Korean War.  Headlined by stars Shin Young-kyun, Choi Eun-hee, Choi Moo-ryong some of the best known South Korean actors of their time, "Red Scarf" is among the most iconic of prolific director Shin Sang-ok's work, and was well received outside of South Korea.  The film was made with the cooperation of the Republic of Korea Air Force (ROKAF) and is particularly well remembered for its aerial sequences; especially the final showdown between RoKAF F-86 Sabres and Korean People's Air Force MiG-15s.  It inspired the 2012 action film "".

A.F.R.I.K.A.: A.F.R.I.K.A. () is a 2002 South Korean film in the action comedy genre, directed by Shin Seung-soo and starring Lee Yo-won, Kim Min-sun, Lee Young-jin and Jo Eun-ji.  The film's title is an acronym for "Adoring Four Revolutionary Idols Korean Association".

Lee Min-ho (actor, born 1987): Lee Min-ho (, born June 22, 1987) is a South Korean actor and singer.  He first gained widespread fame in Korea and parts of Asia with his role as Gu Jun-pyo in "Boys Over Flowers" in 2009.  The role won him a Best New Actor award at the 45th Baeksang Arts Awards.  He is noted for his leading roles in "City Hunter" (2011), "The Heirs" (2013) and "The Legend of the Blue Sea" (2016).  The success of Lee's television dramas throughout Asia established him as a top Hallyu star.  Lee starred in his first leading role in film with "Gangnam Blues" (2015), followed by his first China-produced film "Bounty Hunters" (2016).

The Sound of a Flower: The Sound of a Flower () is 2015 South Korean period drama film based on the life of Jin Chae-seon, who became Joseon's first female "pansori" singer in 1867.  Jin risks her life by cross-dressing as a man, at a time when women were forbidden to sing in public or perform on stage.  The film focuses on the relationship between Jin and her pansori teacher, Shin Jae-hyo.  The Korean title, "Dorihwaga", is a song written by Shin about his protégée after she became a court singer.

Shin Dong-wook: Shin Dong-wook (born Shin Hwa-shik on September 14, 1982) is a South Korean actor.  He is best known for his leading roles in "Soulmate" and "Cloud Stairs" (both in 2006), and his supporting role in "War of Money" (2007).  Shin stayed out of the public eye for 6 years, since 2011, when he was discharged early from mandatory military service upon diagnosis of a rare condition, complex regional pain syndrome (CRPS), a chronic disease that causes extreme bouts of pain without a known cause or cure.

Bounty Hunters (film): Bounty Hunters is a 2016 action comedy drama film directed by Shin Terra and starring Lee Min-ho, Wallace Chung, Tiffany Tang, Jones Xu, Karena Ng and Louis Fan.  A Chinese-South Korean-Hong Kong co-production, the film was released in China by Le Vision Pictures on July 1, 2016.

Sujit Mondal: Sujit Mondal (Bengali: সুজিত মন্ডল) is an Indian successful film director in Bengali cinema.  He was born in West Bengal.  He began his film career in Bollywood film industry ( mumbai), where he was an associate director to Vikram Bhatt . .  films like Ghulam, Kasoor, Raaz, Aap Mujhe Achche Lagne Lage, Jurm, Awara Paagal Deewana, Footpath, Deewane Huye Paagal, Inteha, Aetbaar, Ankahee, Elaan , 1920 etc has done ... He started Bengali film directing in 2009... shri venkatesh films and surinder films joint venture’s Family drama “Saat Paake Bandha” was his first film.  then youth comedy romance “Bolo Na Tumi Aamar” le paglu dance songs, musical romantic film 'Sedin Dekha hoyechilo'. .  khoka babu jay lal juto paye song was talk of the town , musical family drama 'Romeo' . .  first time introduced motion control camera in Tollywood in the title song "Ami Holam Romeo, romance comedy drama 'Paglu 2', P.B films comedy flick 'Bawali Unlimited', hardcore thrilling action packed 'Rocky' he introduced mimoh mithun chakrabary’s son in film rocky, reincarnetion and periodically ghost drama "Arundhati".  eskay movies youth action comedy romance "HERO 420" ... most of his film got super hit, megha hit tittled... he is the most talented and respected techniician in bengali film industry.  Now Mr. Mondal is shooting for his film 'anneswan' based on novel of great writer prafullo roy for production vabna aaj o kal……

Art of Fighting (film): Art of Fighting () is a 2006 South Korean action comedy drama film co-written and directed by Shin Han-sol.  The film was released to Korean theaters on January 5, 2006 and had 1,313,727 tickets nationwide.

Question: What is the title of the 2016 action comedy drama film directed by Shin Terra that starred the South Korean actor and singer who is known for his role in "Boys Over Flowers"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "lead_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the lead actor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the lead actor."
        },
        "known_for_role": {
          "type": "string",
          "description": "The specific role the actor is known for."
        },
        "known_for_series": {
          "type": "string",
          "description": "The television series the actor is known for."
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The occupations of the lead actor."
        }
      },
      "required": [
        "name",
        "nationality",
        "known_for_role",
        "known_for_series",
        "occupations"
      ],
      "additionalProperties": false
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres the film belongs to."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "lead_actor",
    "genres"
  ],
  "additionalProperties": false
}
