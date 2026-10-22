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
John G. Avildsen: John Guilbert Avildsen (December 21, 1935 – June 16, 2017) was an American film director.  He won the Academy Award for Best Director in 1977 for "Rocky".  Other films he directed include "Joe" (1970), "Save the Tiger" (1973), "Fore Play" (1975), "The Formula" (1980), "Neighbors" (1981), "For Keeps" (1988), "Lean on Me" (1989), "Rocky V" (1990), "The Power of One" (1992), "8 Seconds" (1994), "Inferno" (1999) and the first three "The Karate Kid" films.

Lal (actor): M. P. Michael (born 2 December 1958), better known by his stage name Lal, is an Indian film director, actor, script writer, producer, and film distributor widely known for his work in Malayalam cinema.

Alan Klingenstein: Alan Klingenstein (born 1954) is a corporate and securities attorney, an investment banker, a film distributor, and an award-winning film producer.  His feature film "Two Family House" won the Audience Award at the 2000 Sundance Film Festival.  Another feature film, "Runaway", premiered at the Tribeca Film Festival, the Toronto International Film Festival, and won Best Dramatic Feature at the 2005 Austin Film Festival.  His documentary "Trumbo" was awarded the National Board of Review's Freedom of Expression Award in 2008.  Klingenstein is currently the Chairman of FilmRise, a film and television distribution company.

Sage Stallone: Sage Moonblood Stallone (May 5, 1976 – July 13, 2012) was an American actor, film director, film producer, and film distributor.  He was the elder son of Sylvester Stallone.

China Star Entertainment Group: China Star Entertainment Limited (Traditional Chinese: 中國星集團公司) is a Hong Kong film production company and film distributor.  It was established in 1992 by film producer Charles Heung, and has been known as a huge distributor and film producer of films made mostly in Cantonese.

San Fu Maltha: San Fu Maltha (born 17 July 1958) is a Dutch film producer and film distributor.  He founded the production company Fu Works and he co-founded film distributor A-Film.

Rocky V: Rocky V is a 1990 American sports drama film.  It is the fifth film in the "Rocky" series, written by and starring Sylvester Stallone, and co-starring Talia Shire, Stallone's real-life son Sage, and real-life boxer Tommy Morrison, with Morrison in the role of Tommy Gunn, a talented yet raw boxer.  Sage played Robert Balboa, whose relationship with his famous father is explored.  After Stallone directed the second through fourth films in the series, "Rocky V" saw the return of John G. Avildsen, whose direction of "Rocky" won him an Academy Award for Best Directing.

Arthur Mayer: Arthur L. Mayer (March 28, 1886, Demopolis, Alabama - April 14, 1981, New York City) was an American film producer and film distributor who worked with Joseph Burstyn in distributing films directed by Roberto Rossellini and other famous European film directors.  Some films were distributed under the name Burstyn-Mayer Inc.  Mayer was also interviewed by Warren Beatty for Beatty's film "Reds" (1981).

Zeitgeist Films: Zeitgeist Films is an American independent film distributor based in New York City founded in 1988 by co-Presidents Nancy Gerstman and Emily Russo.  Films distributed by Zeitgeist are strongly auteur-driven by directors such as Christopher Nolan, Guy Maddin, Atom Egoyan, Todd Haynes, Nuri Bilge Ceylan, Olivier Assayas, Abbas Kiarostami, Deepa Mehta, Jan Švankmajer and the Brothers Quay.  The expansive Zeitgeist film library includes "Trouble the Water", "The Corporation", "Jellyfish", "Examined Life", "Into Great Silence", Ten and Irma Vep.  In June 2008, the MoMA honored two decades of Zeitgeist successes with a month-long, twenty film retrospective entitled "Zeitgeist: The Films of Our Time", exhibiting the distributor's twenty most critically acclaimed, intellectually stimulating titles.

Peter Gerard: Peter Gerard (born in Columbia, Missouri, United States) is a film director, film producer and film distributor.  He founded Accidental Media and Distrify.  Gerard lived in Edinburgh, Scotland, from 2000 to 2013 and moved to New York City in 2014 to work at Vimeo.

Question: What is the name of this American actor, film director, film producer, and film distributor, who starred in Rocky V with his real life dad?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professional roles held by the person."
    },
    "film_appearance": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the person starred in."
        },
        "co_star_name": {
          "type": "string",
          "description": "The name of the co-star who is the person's real-life dad."
        },
        "co_star_relationship": {
          "type": "string",
          "description": "The real-life relationship with the co-star."
        }
      },
      "required": [
        "film_title",
        "co_star_name",
        "co_star_relationship"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "nationality",
    "roles",
    "film_appearance"
  ],
  "additionalProperties": false
}
