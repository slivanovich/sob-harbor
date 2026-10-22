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
Andrea Palma (actress): Guadalupe Bracho Pérez-Gavilán, better known as Andrea Palma (16 April 1903 in Durango, Mexico – 6 October 1987 in Mexico City, Mexico) was a Mexican film stage and television actress.  She was considered the first major female star of the Mexican cinema after her role in the Mexican film "La Mujer del Puerto" (1934).

Sunshine (1999 film): Sunshine is a 1999 historical drama film directed by István Szabó and written by Israel Horovitz and Szabó.  It follows five generations of a Hungarian Jewish family, originally named Sonnenschein (German: ""sunshine"" ), later changed to Sors (Hungarian: ""fate"" ), during changes in Hungary, focusing mostly on the three generations from the late 19th century through the mid-20th century.  The family story traverses the creation of the Austro-Hungarian Empire through to the period after the 1956 Revolution, while the characters are forced to surrender much of their identity and endure family conflict.  The central male protagonist of all three generations is portrayed by Ralph Fiennes.  The film's stars include Rachel Weisz and John Neville, with the real-life daughter and mother team of Jennifer Ehle and Rosemary Harris playing the same character across a six-decade storyline.

Flóra Kádár: Flóra Kádár (] ) (August 4, 1928 in Budapest – January 3, 2003 in Budapest) was a Hungarian stage, film, television and voice actress.  She died on January 3, 2003 at the age of 74.  She was known for her roles of "Mrs. Hackl" in the film Sunshine, of "Redl's sister" in the film Colonel Redl, and of "Erzsi, Jóska's wife" in the film Adoption.

Manfish: Manfish is a 1956 adventure film, released by United Artists in 1956 and originally filmed in DeLuxe Color.  Filmed in Jamaica, it was released in Great Britain as "Calypso".  It was based on the stories "The Gold-Bug" and "The Tell-Tale Heart" by Edgar Allan Poe.  Actor John Bromfield starred as Captain Brannigan and Lon Chaney Jr. played the role of Swede.  The leading female star was Tessa Prendergast, who played Alita.  Tessa later became a fashion designer and designed the white bikini of Ursula Andress for "Dr. No".  The film also featured the motion picture debut of Barbara Nichols.

Billie Ritchie: Billie Ritchie (14 September 1878 – 6 July 1921) was a Scottish comedian who first gained transatlantic fame as a performer for British music hall producer Fred Karno—this, a full decade before Stan Laurel and Charlie Chaplin took a similar career path.  Ritchie is best recalled today for the silent comedy shorts he made between 1914 and 1920 for director/producer Henry Lehrman's L-KO Kompany and Fox Film Sunshine Comedy unit.

Rachel Weisz: Rachel Hannah Weisz ( "vice"; born 7 March 1970) is a British actress.

Louise Lester: Louise Lester (August 8, 1867 – November 18, 1952) was an American silent film actress.  She was the first female star of Western films.

The Bigamist (1953 film): The Bigamist is a 1953 American drama film noir directed by Ida Lupino starring Joan Fontaine, Ida Lupino, Edmund Gwenn and Edmond O'Brien.  Producer/Screenwriter Collier Young was married to Fontaine at the time and had previously been married to Lupino.  "The Bigamist" has been cited as the first film in which a female star of the film directed herself.

Katharine Hepburn: Katharine Houghton Hepburn (May 12, 1907 – June 29, 2003) was an American actress.  Known for her fierce independence and spirited personality, Hepburn was a leading lady in Hollywood for more than 60 years.  She appeared in a range of genres, from screwball comedy to literary drama, and she received four Academy Awards—a record for any performer—for Best Actress.  In 1999, Hepburn was named by the American Film Institute as the greatest female star of Classic Hollywood Cinema.

Kay Francis: Kay Francis (January 13, 1905 – August 26, 1968) was an American stage and film actress.  After a brief period on Broadway in the late 1920s, she moved to film and achieved her greatest success between 1930 and 1936, when she was the number one female star at the Warner Brothers studio and the highest-paid American film actress.  Some of her film-related material and personal papers are available to scholars and researchers in the Wesleyan University Cinema Archives.

Question: Where is the female star in film sunshine from

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "female_stars": {
      "type": "array",
      "description": "A list of female stars in the film.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the female star."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the female star."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "primary_star_nationality": {
      "type": "string",
      "description": "The nationality of the primary female star identified in the context for the film."
    }
  },
  "required": [
    "film_title",
    "female_stars",
    "primary_star_nationality"
  ],
  "additionalProperties": false
}
