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
Nicholas Rawlins: Nicholas Rawlins is a British experimental psychologist.  He was born in 1949, and was married to the philosopher Susan Hurley from 1986 until her death on 16 August 2007.  He is the only son of Sir John Rawlins and the grandson of Stuart Rawlins.  He was educated at Westbury House School and Winchester College before reading for a BA in Psychology, Physiology and Philosophy at University College, Oxford.  He was awarded first class honours in 1971.  He subsequently studied for a D.Phil at Oxford under the supervision of Jeffrey Alan Gray.

Lupo!: Lupo!  is a 1970 film directed by Menahem Golan.  The script was co-written by Golan and Ken Globus.

Tevye and His Seven Daughters: Tevye and His Seven Daughters (Hebrew: טוביה ושבע בנותיו‎ ‎ , translit.  Tuvia Vesheva Benotav) is a 1968 Israeli drama film directed by Menahem Golan.  The film is about a poor Russian Jew named Tevye who tries to make a living.  When he slowly lands money, he attempts to get his daughters married.  It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.  It is based on stories by Sholom Aleichem, which are also the basis for the stage musical and 1971 film "Fiddler on the Roof".

John Rawlins (director): John Rawlins (June 9, 1902 – May 20, 1997) was an American film editor and film director.  He directed 44 films between 1932 and 1958.  He was born in Long Beach, California and died in Arcadia, California.

Deadly Heroes: Deadly Heroes is a direct to video 1993 action film starring Michael Paré, Jan-Michael Vincent and Billy Drago.  Directed by Menahem Golan, "Deadly Heroes" is notable for being one of the last films released under Golan's 21st Century Film Corporation banner.  The company went bankrupt shortly thereafter.  "Deadly Heroes" is also one of the last films starring actor Jan-Michael Vincent.

Escape to the Sun: Escape to the Sun is a 1972 drama film written and directed by Menahem Golan and starring Laurence Harvey, Josephine Chaplin, John Ireland, Lila Kedrova and Jack Hawkins.  The film was a co-production between Israel, France and West Germany.

Menahem Golan: Menahem Golan (Hebrew: מנחם גולן‎ ‎ ; May 31, 1929 – August 8, 2014) was an Israeli director and producer.  He is best known as the co-owner, with his cousin Yoram Globus, of The Cannon Group, a company that specialized in low-to-mid budget American films during the 1980s after Golan and Globus achieved significant success as filmmakers in their native Israel during the 1970s.

Kazablan (film): Kazablan is a 1974 Israeli musical film directed by Menahem Golan and written by Menahem Golan and Haim Hefer.  The film stars Yehoram Gaon, Efrat Lavie, Arieh Elias, Etti Grotes and Yehuda Efroni.  The film was released on May 8, 1974, by Metro-Goldwyn-Mayer.

Lost Lagoon (film): Lost Lagoon is a 1958 American drama film directed by John Rawlins and written by Milton Subotsky, John Rawlins and Jeffrey Lynn.  The film stars Jeffrey Lynn, Lelia Barry, Peter Donat, Don Gibson, Roger Clark and Jane Hartley.  The film was released on February 1, 1958, by United Artists.

Richard L. Albert: Richard Albert was president of the award-winning motion picture advertising agency Design Projects, Inc. from 1978 to 1992.  Clients included major studios such as Universal Pictures, MGM, 20th Century Fox, Warner Bros., and Columbia Pictures, as well as major independent and international distributors such as Cannon Films, Trimark Pictures, CBS Theatrical Films, Goldcrest, and Lorimar.  Albert's firm was responsible for the movie poster designs for many films, including MacArthur, Sorcerer, Hard to Hold, The Final Countdown, Mutant, and Nightmares.  Albert consulted regularly with Menahem Golan at Cannon Films on how to market and pre-sell Cannon's films, and successfully launched the foreign campaigns for Death Wish 2, New Year's Evil, Lady Chatterly's Lover, Enter the Ninja, and many others.  Later, when Golan started 21st Century Films, he collaborated with Albert, who produced though his Sawmill Entertainment Corp. the Lambada dance movie The Forbidden Dance for Golan's foreign distribution, and Columbia Pictures' U.S. theatrical release.  Albert hunt ed down the management for the band Kaoma when they were touring in the United States, and licensed their hit song "Lambada" for the film.  He also tried to book the band to appear in the movie, however the band's schedule did not fit with the fast production schedule, so he hired Kid Creole and the Coconuts to perform in the final scenes.

Question: Menahem Golan and John Rawlins, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals being compared."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "occupation_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the person."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of all occupations/roles mentioned for this person."
          }
        },
        "required": [
          "person_name",
          "roles"
        ],
        "additionalProperties": false
      },
      "description": "Detailed list of occupations for each person."
    }
  },
  "required": [
    "person_names",
    "mutual_occupation",
    "occupation_details"
  ],
  "additionalProperties": false
}
