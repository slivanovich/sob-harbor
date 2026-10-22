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
The Three Caballeros: The Three Caballeros is a 1944 American live-action animated musical package film produced by Walt Disney and released by RKO Radio Pictures.  The film premiered in Mexico City on December 21, 1944.  It was released in the United States on February 3, 1945 and in the UK that March.  The seventh Disney animated feature film, the film plots an adventure through parts of Latin America, combining live-action and animation.  This is the second of the six package films released by Walt Disney Productions in the 1940s, following "Saludos Amigos" (1942).

Hot Lead and Cold Feet: Hot Lead and Cold Feet (originally titled Welcome to Bloodshy) is a 1978 American comedy-western film produced by Walt Disney Productions and starring Jim Dale, Karen Valentine, Don Knotts, Jack Elam and Darren McGavin.

José Carioca: José "Zé" Carioca ( ; ] ] ) is a Disney cartoon character drawn as an anthropomorphic parrot from Rio de Janeiro, Brazil (thus "Carioca", a term which refers to a person born there).  José was created in 1942 for the movie "Saludos Amigos" as a friend of Donald Duck, described by "Time" as "a dapper Brazilian parrot, who is as superior to Donald Duck as the Duck was to Mickey Mouse".  He returned in the 1944 film "The Three Caballeros" along with Donald and a Mexican rooster named Panchito Pistoles.

Stuart Buchanan: Stuart Buchanan (March 18, 1894 – February 4, 1974) was an American actor and deep-voice announcer, who was the casting director for the Walt Disney Company, best known for voicing Humbert the Huntsman in the 1937 Disney animated film "Snow White and the Seven Dwarfs".  He also made cameo voiceover roles as a flight attendant in "Saludos Amigos" (1942) and in "Super-Speed" (1935).  He also voiced Goofy in "The Mickey Mouse Theater of the Air" in 1938.

Saludos Amigos: Saludos Amigos (Spanish for "Greetings, Friends") is a 1942 American live-action animated package film produced by Walt Disney and released by RKO Radio Pictures.  It is the sixth Disney animated feature film and the first of the six package films produced by Walt Disney Productions in the 1940s.  Set in Latin America, it is made up of four different segments; Donald Duck stars in two of them and Goofy stars in one.  It also features the first appearance of José Carioca, the Brazilian cigar-smoking parrot.  "Saludos Amigos" was popular enough that Walt Disney decided to make another film about Latin America, "The Three Caballeros", to be produced two years later.  "Saludos Amigos" premiered in Rio de Janeiro on August 24, 1942.  It was released in the United States on February 6, 1943.  At 42 minutes, it is Disney's shortest animated feature to date.  It garnered positive reviews and was theatrically reissued in 1949, when it was shown on a double bill with the first reissue of "Dumbo".

Melody Time: Melody Time (working title All in Fun) is a 1948 American live-action animated film and the 10th theatrically released animated feature produced by Walt Disney.  It was released to theatres by RKO Radio Pictures on May 27, 1948.  Made up of several sequences set to popular music and folk music, the film is, like "Make Mine Music" before it, the popular music version of "Fantasia" (an ambitious film that proved to be a commercial disappointment upon its original theatrical release).  "Melody Time", while not meeting the artistic accomplishments of "Fantasia", was mildly successful.  It is the fifth Disney package film following "Saludos Amigos", "The Three Caballeros", "Make Mine Music", and "Fun and Fancy Free".

Karen Valentine: Karen Lynne Valentine (born May 25, 1947) is an American actress.  She is best known for her role as the idealistic schoolteacher Alice Johnson in the ABC comedy drama series "Room 222" from 1969 to 1974, for which she won Primetime Emmy Award for Outstanding Supporting Actress in a Comedy Series in 1970, and received a Golden Globe Award nomination in 1971.  She later went to star in own short-lived sitcom "Karen" (1975), and played female leading roles in films "Hot Lead and Cold Feet" (1978) and "The North Avenue Irregulars" (1979).

Panchito Pistoles: Panchito Pistoles is a cartoon character drawn as an anthropomorphized rooster.  He appeared in the film "The Three Caballeros".  Later he appeared in several Disney comics, including Don Rosa's "The Three Caballeros Ride Again" and "The Magnificent Seven (Minus 4) Caballeros".  Panchito was the only one of the Three Caballeros to never appear in "Saludos Amigos", as he did not yet exist when the 1942 film was released before he first appeared in the 1944 film.

South of the Border with Disney: South of the Border with Disney is a 1942 Disney short documentary film.  It was shot in the same occasion "Saludos Amigos" was, when Walt Disney and a group of eighteen artists, musicians and writers went to South America looking for inspirations for a movie.  While "Saludos Amigos" is the result of this voyage, alternating animated shorts to the sequences from the travel that inspired them, "South of the Border with Disney" is more of a behind-the-scenes documentary showing only the travel and the genesis of cartoons not only for "Saludos Amigos" and "The Three Caballeros", but also some others used in later occasions.  The most notable example is a female Armadillo used for a 1943 Pluto cartoon, "Pluto and the Armadillo".  Film also includes some pencil test animation.

Walt &amp; El Grupo: Walt & El Grupo is a 2008 documentary film written and directed by Theodore Thomas.  A presentation of Walt Disney Family Foundation Films, the film tells the story of Walt Disney's 1941 U.S. Government sponsored trip to South America where he and a group of artists gathered material which would be used to create two of Disney's animated feature films, "Saludos Amigos" and "The Three Caballeros".

Question: Which film did Walt Disney produce first, Saludos Amigos or Hot Lead and Cold Feet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_produced_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "production_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "production_year"
      ],
      "additionalProperties": false
    },
    "second_produced_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "production_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "production_year"
      ],
      "additionalProperties": false
    },
    "common_producer": {
      "type": "string"
    },
    "answer_film_title": {
      "type": "string"
    }
  },
  "required": [
    "first_produced_film",
    "second_produced_film",
    "common_producer",
    "answer_film_title"
  ],
  "additionalProperties": false
}
