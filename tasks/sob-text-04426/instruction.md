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
Drunk Parents: Drunk Parents is an upcoming American comedy film directed by Fred Wolf and written by Peter Gaulke and Fred Wolf.  The film stars Alec Baldwin, Salma Hayek, Bridget Moynahan, Joe Manganiello, Natalia Cigliuti, Jim Gaffigan and Ben Platt.

Magic Mike: Magic Mike is a 2012 American comedy-drama film directed by Steven Soderbergh and starring Channing Tatum, Alex Pettyfer, Matt Bomer, Joe Manganiello, and Matthew McConaughey.  The plot revolves around Adam, a 19-year-old who enters the world of male stripping, guided by Mike Lane, who has been in the business for six years.

Rampage (2018 film): Rampage is an upcoming American action adventure monster film directed by Brad Peyton and written by Ryan Engle.  It is based on the 1980s arcade video game of the same name.  The film stars Dwayne Johnson, Naomie Harris, Malin Åkerman, Joe Manganiello, Jake Lacy, Marley Shelton, and Jeffrey Dean Morgan.  New Line Cinema will release the film on April 20, 2018 in 3D and IMAX.

Joe Manganiello: Joseph Michael Manganiello ( ; ] ; born December 28, 1976) is an American actor.  He played Flash Thompson in Sam Raimi's "Spider-Man" trilogy and had various recurring roles in television on "ER", "How I Met Your Mother", and "One Tree Hill", before landing his breakout role as werewolf Alcide Herveaux on the HBO television series "True Blood".  In 2011, he was voted "Favorite Pop-Culture Werewolf of All Time" by the readers of "Entertainment Weekly", and one of "Men's Health"'s "100 Fittest Men of All Time".

Adam G. Sevani: Adam G. Sevani (born June 29, 1992) is an American actor and dancer, known for playing Robert Alexander III / "Moose" in Step Up (film series).

Tumbledown (2015 film): Tumbledown is a 2015 American romantic comedy film directed by Sean Mewshaw and written by Desiree Van Til.  The film stars Jason Sudeikis, Rebecca Hall, Dianna Agron, and Joe Manganiello.  The film was released on February 5, 2016, by Starz Digital.

Magic Mike XXL: Magic Mike XXL is a 2015 American comedy-drama film directed by Gregory Jacobs, written by Reid Carolin and starring Channing Tatum, Matt Bomer, Kevin Nash and Joe Manganiello.  A sequel to 2012's "Magic Mike", the film was released on July 1, 2015, received mixed to positive reviews from critics and grossed $122 million.

Smurfs: The Lost Village: Smurfs: The Lost Village is a 2017 American 3D computer-animated comedy-adventure film produced by Sony Pictures Animation and The Kerner Entertainment Company, with animation by Sony Pictures Imageworks, for Columbia Pictures.  Sony, LStar Capital and Wanda Pictures co-financed the film.  It is based on "The Smurfs" comic book series created by the Belgian comics artist Peyo, and is a reboot unrelated to Sony's previous live-action/animated films based on the series.  It was written by Stacey Harman and Pamela Ribon and directed by Kelly Asbury, and stars the voices of Demi Lovato, Rainn Wilson, Joe Manganiello, Mandy Patinkin, Jack McBrayer, Danny Pudi, Michelle Rodriguez, Ellie Kemper, Ariel Winter, Meghan Trainor, Jake Johnson and Julia Roberts.  In the film, a mysterious map prompts Smurfette, Brainy, Clumsy and Hefty to find a lost village before Gargamel does.

Guild of Italian American Actors: The Guild of Italian American Actors (GIAA) was founded in 1937 as the Italian Actors Union (IAU) to protect the rights of Italian American actors, and renamed in 1998.  The guild has jurisdiction over Italian language professional theater, and works to preserve and promote awareness of Italian culture and heritage.  GIAA also provides a casting resource to directors and producers seeking Italian American actors.

List of Italian-American actors: To be included in this list, the person must have a Wikipedia article showing they are Italian American actors or must have references showing they are Italian American actors and are notable.  As discussed in the 2005 book "Hollywood Italians" by Peter E. Bondanella, as well as numerous other sources, Italian-American actors have made a significant impact.  The Guild of Italian American Actors was founded in 1937.

Question: Are Joe Manganiello and Adam G. Sevani both American actors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals are American actors, false otherwise."
    },
    "actors_details": {
      "type": "array",
      "description": "Details for each actor mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "is_american": {
            "type": "boolean",
            "description": "Indicates if the actor is American."
          },
          "is_actor": {
            "type": "boolean",
            "description": "Indicates if the individual is an actor."
          }
        },
        "required": [
          "name",
          "is_american",
          "is_actor"
        ],
        "additionalProperties": false
      }
    },
    "conclusion_reasoning": {
      "type": "string",
      "description": "Explanation for the final answer based on the details of each actor."
    }
  },
  "required": [
    "question_asked",
    "answer",
    "actors_details",
    "conclusion_reasoning"
  ],
  "additionalProperties": false
}
