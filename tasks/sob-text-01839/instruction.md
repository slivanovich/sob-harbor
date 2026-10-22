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
Victor Buono: Victor Charles Buono (February 3, 1938January 1, 1982) was an American actor and comic and briefly a recording artist.  He was most famous for playing the villain King Tut on the television series "Batman" (1966-1968) and musician Edwin Flagg in "What Ever Happened to Baby Jane? " (1962), the latter of which earned him Academy Award and Golden Globe Award nominations.  He was a busy actor from his late teens until his death at age 43, and with his large size and sonorous voice, he made a career of playing men much older than himself.

Gus Trikonis: Gus Trikonis (born November 21, 1937) is an American actor, dancer and director.

Supercock: Supercock (also known as Bet to Kill and A Fistful of Feathers) is a 1975 comedy film directed by Gus Trikonis and starring Ross Hagen, both of whom were involved in the 1969 cult film "The Sidehackers".  The film also stars '60s sex symbol Nancy Kwan.  The plot involves an American cowboy who gets caught up in an illegal cockfighting ring in the Philippines.

Jeepers Creepers 2: Jeepers Creepers 2 is a 2003 American horror film written and directed by Victor Salva, produced by American Zoetrope, Capitol Films, Myriad Pictures and distributed by United Artists, a Metro-Goldwyn-Mayer division.  The film is a sequel to the 2001 horror film "Jeepers Creepers".  Francis Ford Coppola executive produced the film.

Evil Dead II: Evil Dead II (also known in publicity materials as Evil Dead 2: Dead by Dawn) is a 1987 American horror comedy film directed by Sam Raimi and a parody sequel to the 1981 horror film "The Evil Dead".  The film was written by Raimi and Scott Spiegel, produced by Robert Tapert, and stars Bruce Campbell as Ash Williams.

Take This Job and Shove It (film): Take This Job and Shove It is a 1981 American comedy film starring Robert Hays, Barbara Hershey, Art Carney, and David Keith, and directed by Gus Trikonis.

Castle of Evil: Castle of Evil is a 1966 American horror film directed by Francis D. Lyon and written by Charles A. Wallace.  The film stars Scott Brady, Virginia Mayo, David Brian, Lisa Gaye, Hugh Marlowe and William Thourlby.  The film was released by World Entertainment Corp. in November 1966.

Dobaara: See Your Evil: Dobaara: See Your Evil is a 2017 Bollywood supernatural horror film written and directed by Prawaal Raman.  It is an official adaptation of the 2013 American horror film "Oculus"; the original film's director and co-writer, Mike Flanagan, serves as executive producer.

The Evil (1978 film): The Evil is a 1978 American horror film directed by Gus Trikonis and starring Richard Crenna, Joanna Pettet, Andrew Prine and Victor Buono.  It is also known as "House of Evil".

Miss All-American Beauty: Miss All-American Beauty is a 1982 American television film directed by Gus Trikonis and starring Diane Lane.

Question: The Evil is an American horror film, released in which year, and directed by Gus Trikonis and includes Victor Charles Buono, an American actor and comic and briefly a recording artist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "director_details": {
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
    "featured_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the featured actor."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the actor's professions."
        }
      },
      "required": [
        "name",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_details",
    "director_details",
    "featured_actor"
  ],
  "additionalProperties": false
}
