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
Paranoia 1.0: Paranoia: 1.0 (originally One Point O, also known as "1.0", "One Point Zero", "Version 1.0", and "Virus 1.0") is a 2004 cyberpunk science fiction film written and directed by Jeff Renfroe and Marteinn Thorsson.  The film is a Kafkaesque nightmare in which a young computer programmer is an unwitting guinea pig in a corporate experiment to test a new advertising scheme.  The film stars Jeremy Sisto and Deborah Unger and features Lance Henriksen, Eugene Byrd, Bruce Payne and Udo Kier.

RoboCop: RoboCop is a 1987 American cyberpunk science fiction superhero action film directed by Paul Verhoeven and written by Edward Neumeier and Michael Miner.  The film stars Peter Weller, Nancy Allen, Dan O'Herlihy, Kurtwood Smith, Miguel Ferrer, and Ronny Cox.  Set in a crime-ridden Detroit, Michigan, in the near future, "RoboCop" centers on police officer Alex Murphy (Weller) who is murdered by a gang of criminals and subsequently revived by the megacorporation Omni Consumer Products (OCP) as a superhuman cyborg law enforcer known as RoboCop.

RoboCop (2014 film): RoboCop is a 2014 American cyberpunk superhero action film directed by José Padilha and written by Joshua Zetumer, Edward Neumeier and Michael Miner.  It is a remake of the 1987 film of the same name also written by Neumeier and Miner.  The film stars Joel Kinnaman as the title character, with Gary Oldman, Michael Keaton, Samuel L. Jackson, Abbie Cornish and Jackie Earle Haley in supporting roles.

Kurtwood Smith: Kurtwood Larson Smith (born July 3, 1943) is an American television and film actor.  He is known for playing Clarence Boddicker in "RoboCop" (1987) and Red Forman in "That '70s Show", as well as for his many appearances in science fiction films and television programs ("Star Trek", "The X-Files").  He also starred in the seventh season of "24".

Dead or Alive: Final: Dead or Alive: Final is a 2002 Japanese cyberpunk science fiction film directed by Takashi Miike.  It is the third in a three-part series, preceded by "Dead or Alive" in 1999 and "" in 2000.  The films are not connected in any apparent way except by director Takashi Miike and stars Riki Takeuchi and Show Aikawa.  Besides Japanese, a lot of the dialog in the film is in Cantonese and some is in English.  Often two people will talk to each other using different languages.

Guillermo del Toro: Guillermo del Toro Gómez (] ; born October 9, 1964) is a Mexican-American film director, screenwriter, producer and novelist.  In his filmmaking career, del Toro has alternated between Spanish-language dark fantasy pieces, such as the gothic horror film "The Devil's Backbone" (2001), and "Pan's Labyrinth" (2006), and more mainstream American action movies, such as the vampire superhero action film "Blade II" (2002), the supernatural superhero film "Hellboy" (2004), its sequel "" (2008), and the science fiction monster film "Pacific Rim" (2013).  His latest film, "The Shape of Water", won the Golden Lion at the Venice Film Festival and is scheduled for an American release on December 8, 2017.

Death Machine: Death Machine is a 1994 Japanese-British cyberpunk science fiction action-horror film written and directed by Stephen Norrington.  It stars Brad Dourif, Ely Pouget, William Hootkins, John Sharian, and Richard Brake.  Rachel Weisz, still early in her career at the time of the film's release, appears briefly in the role of a Junior Executive.  The film was the directorial debut of Norrington, who had previously worked as a special effects artist on films such as "Lifeforce, Aliens, Hardware", "The Witches", and "Split Second".  However, Norrington infamously expressed distaste in the original cut, and the film has undergone numerous reedits since.

Nirvana (film): Nirvana is a 1997 Italian cyberpunk science fiction film directed by Gabriele Salvatores.  The film stars Christopher Lambert, Diego Abatantuono, Sergio Rubini, and Stefania Rocca.  It was screened out of competition at the 1997 Cannes Film Festival.

Automan: Automan is an American soft science fiction superhero television series produced by Glen A. Larson.  It aired for 12 episodes (although 13 were made) on ABC between 1983 and 1984.  It consciously emulates the stylistic trappings of the Walt Disney Pictures film, "Tron", in the context of a superhero TV series.

The Supernaturalist: The Supernaturalist is a science fiction novel by Irish author Eoin Colfer.  The work was influenced by film noir and other predecessors of the cyberpunk science fiction movement.  Colfer has outlined plans for a sequel, "The Supernaturalist 2".

Question: Kurtwood Larson Smith is known for playing Clarence Boddicker in which cyberpunk science fiction superhero action film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character the actor is known for playing."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of genres the film belongs to."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "writers": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of writers for the film."
        }
      },
      "required": [
        "title",
        "year",
        "genres",
        "director",
        "writers"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "character_played",
    "film_details"
  ],
  "additionalProperties": false
}
