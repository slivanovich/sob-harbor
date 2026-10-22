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
The Lost Boys: The Lost Boys is a 1987 American horror comedy film directed by Joel Schumacher and starring Jason Patric, Corey Haim, Kiefer Sutherland, Jami Gertz, Corey Feldman, Dianne Wiest, Edward Herrmann, Alex Winter, Jamison Newlander, and Barnard Hughes.

Lost Boys: The Tribe: Lost Boys: The Tribe is a 2008 horror comedy film directed by P. J. Pesce and the sequel to the 1987 film, "The Lost Boys".  The film stars Tad Hilgenbrink, Angus Sutherland, Autumn Reeser and Corey Feldman.

Busted (film): Busted is a 1997 comedy film, starring Corey Feldman, Corey Haim, Dominick Brascia and Ava Fabian.  The film marked Corey Feldman's directorial debut.  Due to his frequent absences and drug use during filming, Corey Haim was eventually fired by director Corey Feldman.  Feldman later said that this was one of the most hard and painful things he ever had to do.

Corey Feldman: Corey Scott Feldman (born July 16, 1971) is an American actor and singer.  He became well known during the 1980s, with roles as a youth in films such as the voice of Young Copper in "The Fox and the Hound" (1981), Tommy Jarvis in "" (1984), Pete Fountaine in "Gremlins" (1984), Clark 'Mouth' Devereaux in "The Goonies" (1985), Teddy Duchamp in "Stand by Me" (1986), Edgar Frog in "The Lost Boys" (1987) and Ricky Butler in "The 'Burbs" (1989).  Feldman is also the lead singer for the rock band Truth Movement.

The Zombie King: The Zombie King is a British horror comedy film starring Edward Furlong and Corey Feldman.  The film is directed by Aidan Belizaire and is based on a story by Jennifer Chippindale and Rebecca-Clare Evans.  The film is the first project from Northern Girl Productions and was released in the spring of 2013.

Bordello of Blood: Bordello of Blood (also known as Tales from the Crypt Presents: Bordello of Blood) is a 1996 horror comedy film starring Dennis Miller, Erika Eleniak, Angie Everhart, Corey Feldman and Chris Sarandon.  It is based on the HBO television series "Tales from the Crypt".  It received an "R" rating for vampire violence, gore, language and nudity.  Miller plays a private investigator who ends up in a bordello run by vampires, led by the Mother of all Vampires, Lilith (Everhart).

The Fox and the Hound: The Fox and the Hound is a 1981 American animated drama film produced by Walt Disney Productions and loosely based on the novel of the same name by Daniel P. Mannix.  The 24th Disney animated feature film, the film tells the story of two unlikely friends, a red fox named Tod and a hound dog named Copper, who struggle to preserve their friendship despite their emerging instincts and the surrounding social pressures demanding them to be adversaries.  Directed by Ted Berman, Richard Rich, and Art Stevens, the film features the voices of Mickey Rooney, Kurt Russell, Pearl Bailey, Jack Albertson, Sandy Duncan, Jeanette Nolan, Pat Buttram, John Fiedler, John McIntire, Dick Bakalyan, Paul Winchell, Keith Mitchell, and Corey Feldman.

Lost Boys: The Thirst: Lost Boys: The Thirst is a 2010 horror comedy film directed by Dario Piana and stars Corey Feldman, Casey B. Dolan, Tanit Phoenix and Jamison Newlander.  It is a sequel to "" (2008) and the third and final film of "The Lost Boys" trilogy.

The Two Coreys: The Two Coreys (also known as The Coreys) were two actors, popular in the 1980s, Corey Feldman (born 1971) and Corey Haim (1971–2010).  The two young actors appeared in many films together, most notably a number of successful teen-oriented films in the late 1980s.  Feldman starred in "Gremlins", "The Goonies", and "" while Haim starred in "Silver Bullet" and "Lucas" before the duo were paired for the first time in 1987's "The Lost Boys".

Corey Haim: Corey Ian Haim (December 23, 1971 – March 10, 2010) was a Canadian actor, known for a 1980s Hollywood career as a teen idol.  He starred in a number of films, such as "Lucas", "Silver Bullet", "Murphy's Romance", "License to Drive", "Dream a Little Dream", and "Snowboard Academy".  His best-known role was alongside Corey Feldman in "The Lost Boys", which made Haim a household name.

Question: Corey Feldman, who was an actor in the horror comedy film The Lost Boys, was also the voice of Copper a hound dog in what animated film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_voiced": {
      "type": "string",
      "description": "The name of the character voiced by the actor."
    },
    "character_species": {
      "type": "string",
      "description": "The species of the character voiced."
    },
    "animated_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the animated film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "film_type": {
          "type": "string",
          "description": "The genre or type of the film."
        },
        "production_company": {
          "type": "string",
          "description": "The production company of the film."
        },
        "directors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of directors for the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "film_type",
        "production_company",
        "directors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "character_voiced",
    "character_species",
    "animated_film"
  ],
  "additionalProperties": false
}
