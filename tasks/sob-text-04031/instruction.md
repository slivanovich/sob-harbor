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
Sebastian Gutierrez: Sebastian Gutierrez (born September 10, 1974) is a Venezuelan film director, screenwriter and film producer.  known for writing the screenplays to the films "Gothika", "Snakes on a Plane", "The Eye" and "The Big Bounce", and writing and directing two independent female-driven ensemble comedies, "Women in Trouble" and "Elektra Luxx".

Can She Bake a Cherry Pie?: Can She Bake a Cherry Pie?  is a 1983 American comedy film directed by Henry Jaglom.  It was screened in the Un Certain Regard section at the 1983 Cannes Film Festival.  The film takes place in and was filmed in the New York City borough of Manhattan.  It was released on home video and received mixed reviews.

Henry Jaglom: Henry David Jaglom (born January 26, 1938) is an American actor, film director and playwright.

Hollywood Dreams: Hollywood Dreams is a 2006 American comedy-drama film written and directed by Henry Jaglom.  The film stars Tanna Frederick, Justin Kirk, David Proval, Karen Black, Eric Roberts, and Seymour Cassel.

Sitting Ducks (film): Sitting Ducks is a 1980 American comedy film directed by Henry Jaglom.  The film follows the adventures of two small-time hoods (Zack Norman and Michael Emil, Jaglom’s real-life brother) who steal a considerable amount of cash from a gambling syndicate.  While fleeing by car down the U.S. eastern seaboard for a chartered airplane that will take them to Central America, they pick up a pair of vivacious young ladies and an unsuccessful singer-songwriter.

Irene in Time: Irene in Time is a 2009 American independent film directed by Henry Jaglom.  It marked the second collaboration between director Jaglom and actress Tanna Frederick, who also starred in "Hollywood Dreams", Jaglom's 2006 film.  "Irene" also starred Victoria Tennant, Lanre Idewu, and Andrea Marcovicci.

Déjà Vu (1997 film): Déjà Vu is a 1997 American dramatic romance film directed by Henry Jaglom.  It stars Stephen Dillane, Victoria Foyt, and Vanessa Redgrave.  It premiered at the American Film Institute Festival on 25 October 1997 and was released theatrically on 22 April 1998.

Eating (film): Eating is a 1990 American comedy-drama film starring Nelly Alard, Lisa Blake Richards, Frances Bergen, Mary Crosby, Gwen Welles, Elizabeth Kemp, Marina Gregory and written and directed by Henry Jaglom.

Venice/Venice: Venice/Venice is an American film starring Henry Jaglom, Nelly Alard, Melissa Leo, Suzanne Bertish, Daphna Kastner, David Duchovny, John Landis and written and directed by Henry Jaglom.

Tracks (1977 film): Tracks is a 1977 American drama film written and directed by Henry Jaglom.  The film stars Dennis Hopper, Taryn Power and Dean Stockwell.  The story involves a returned Vietnam veteran escorting a fellow soldier's coffin across the United States for burial.

Question: Who is older, Sebastian Gutierrez or Henry Jaglom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "older_person_name": {
      "type": "string",
      "description": "The name of the person who is older."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in birth years between the two people."
    }
  },
  "required": [
    "person_1",
    "person_2",
    "older_person_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
