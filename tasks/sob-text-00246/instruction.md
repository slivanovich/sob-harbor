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
Love Crime: Love Crime (French: "Crime d'amour" ) is a 2010 French psychological suspense thriller starring Ludivine Sagnier and Kristin Scott Thomas.  It is the last film directed by Alain Corneau, and was released posthumously after the director's death from cancer.

National Film Award for Best Supporting Actress: The National Film Award for Best Supporting Actress (also known as the Rajat Kamal Award for the Best Supporting Actress) (] ), is an honour presented annually at the National Film Awards of India since 1984 to an actress for the best performance in a supporting role within Indian cinema.  The National Film Awards were established in 1954 and are presented by the Directorate of Film Festivals, the organization set up by Ministry of Information and Broadcasting, India.  The National Film Awards instituted the "Best Supporting Actress" category in 1984 as the "Rajat Kamal Award for the Best Supporting Actress".

Marius and Jeannette: Marius and Jeannette (French: Marius et Jeannette ) is a 1997 French film directed by Robert Guédiguian.  It won the Louis Delluc Prize and the César Award for Best Actress, and received César nominations for Best Film, Best Director, Best Supporting Actor, Best Supporting Actress, Most Promising Actress and Best Writing.  It was screened in the Un Certain Regard section at the 1997 Cannes Film Festival.

Little Lili: Little Lili (French: "La petite Lili" ) is a 2003 French film by French director Claude Miller.  The film stars Ludivine Sagnier, Bernard Giraudeau, Nicole Garcia, Julie Depardieu and Jean-Pierre Marielle.

Emmanuelle Seigner: Emmanuelle Seigner (born 22 June 1966) is a French actress, former fashion model, and singer.  She is known for her roles in "The Diving Bell and the Butterfly" (2007), "The Ninth Gate" (1999) and "Frantic" (1988).  She has been nominated for a César Award for Best Actress for "Venus in Fur" (2013), and for two César Awards for Best Supporting Actress in "Place Vendôme" (1998) and "La Vie En Rose" (2007).  She is married to French-Polish director Roman Polanski.

Emmanuelle Béart: Emmanuelle Béart (born 14 August 1963) is a French film actress, who has appeared in over 60 film and television productions since 1972.  An eight-time César Award nominee, she won the César Award for Best Supporting Actress for the 1986 film "Manon des Sources".  Her other film roles include "La Belle Noiseuse" (1991), "A Heart in Winter" (1992), "Nelly and Mr. Arnaud" (1995), "" (1996) and "8 Women" (2002).

Anne Consigny: Anne Consigny (born 25 May 1963) is a French actress who has been active since 1981.  She received a César Award nomination for Best Actress for her role in the film "Not Here to Be Loved" (2005).  She is also known for her role as Claude in the 2007 drama "The Diving Bell and the Butterfly" and as Elizabeth in the 2008 film "A Christmas Tale", for which she was nominated for the César Award for Best Supporting Actress.

Peter Pan (2003 film): Peter Pan is a 2003 American-British-Australian fantasy adventure film released by Universal Pictures, Columbia Pictures, and Revolution Studios.  It was the first authorized and faithful film or television adaptation of J.M. Barrie's play "Peter Pan, or The Boy Who Wouldn't Grow Up" in half a century, after Disney's version in 1953.  P. J. Hogan directed a screenplay co-written with Michael Goldenberg which is based on the play and novel by J. M. Barrie.  Jason Isaacs plays the dual roles of Captain Hook and George Darling, Olivia Williams plays Mrs. Darling, while Jeremy Sumpter plays Peter Pan, Rachel Hurd-Wood plays Wendy Darling, and Ludivine Sagnier plays Tinker Bell.  Lynn Redgrave plays a supporting role as Aunt Millicent, a new character created for the film.

Ludivine Sagnier: Ludivine Sagnier is a French actress and model, who has appeared in films since 1989.  She was nominated for two César Awards for Best Supporting Actress in "Swimming Pool" (2003) and "Un secret" (2007).

Swimming Pool (film): Swimming Pool is a 2003 French-British erotic thriller film directed by François Ozon and starring Charlotte Rampling and Ludivine Sagnier.  The plot focuses on a British crime novelist, Sarah Morton, who travels to her publisher's upmarket summer house in Southern France to seek solitude in order to work on her next book.  However, the arrival of Julie, who claims to be the publisher's daughter, induces complications and a subsequent crime.

Question: Who was the director of the film that had actress Ludivine Sagnier nominated for a César Award for Best Supporting Actress in 2003?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who received the nomination."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award."
        },
        "category": {
          "type": "string",
          "description": "The specific category of the award nomination."
        },
        "nomination_year": {
          "type": "integer",
          "description": "The year the actress was nominated for the award."
        }
      },
      "required": [
        "award_name",
        "category",
        "nomination_year"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film for which the actress was nominated."
        },
        "director_name": {
          "type": "string",
          "description": "The director of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "film_title",
        "director_name",
        "release_year"
      ],
      "additionalProperties": false
    },
    "final_answer_director": {
      "type": "string",
      "description": "The name of the director of the film that led to the specified nomination."
    }
  },
  "required": [
    "actress_name",
    "award_details",
    "film_details",
    "final_answer_director"
  ],
  "additionalProperties": false
}
