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
Bug (1975 film): Bug is a 1975 American horror film in Panavision, directed by Jeannot Szwarc and written by William Castle and Thomas Page, from Page's 1973 novel "The Hephaestus Plague".  It was the last film Castle was involved in before his death.  The film starred Bradford Dillman, Joanna Miles and Richard Gilliland.

Somewhere in Time (film): Somewhere in Time is a 1980 American romantic science fiction drama film directed by Jeannot Szwarc.  It is a film adaptation of the 1975 novel "Bid Time Return" by Richard Matheson, who also wrote the screenplay.  The film stars Christopher Reeve, Jane Seymour, and Christopher Plummer.

Enigma (1982 film): Enigma is a 1982 Anglo-American thriller film directed by Jeannot Szwarc and starring Martin Sheen, Sam Neill, Brigitte Fossey, and Kevin McNally.  Based on Michael Barak's novel "Enigma Sacrifice", the film centers on a CIA agent that tries to infiltrate Soviet intelligence in order to stop a murderous plot.

Extreme Close-Up (film): Extreme Close-Up is a 1973 film directed by Jeannot Szwarc and written by Michael Crichton.  It deals with privacy in an ever growing technological age.

Grey Matters (Fringe): "Grey Matters" is the 10th episode of the second season of the American science fiction drama television series "Fringe".  The episode was written by Ashley Edward Miller and Zack Stentz, and directed by Jeannot Szwarc.  It centered on three mental patients who mysteriously became sane again after shapeshifters from the parallel universe removed a piece of foreign tissue from each of their brains; this tissue is later revealed to have been taken from the brain of Walter Bishop years before.  The fringe team of Olivia Dunham, Peter Bishop, and Walter investigate and face a new enemy, Thomas Jerome Newton (guest actor Sebastian Roché), whose purpose is to decipher the missing parts of Walter's brain and find out how to move between universes.

Honor Bound (film): Honor Bound (also known as Red End) is a 1988 film directed by Jeannot Szwarc.

Bill Erwin: William Lindsey Erwin (December 2, 1914 – December 29, 2010) was an American film, television and stage actor with over 250 television and film credits.  A veteran character actor, he is widely known for his 1993 Emmy Award-nominated performance on "Seinfeld", portraying the embittered, irascible retiree Sid Fields.  He also made notable appearances on shows such as "I Love Lucy" and his "".  In cinema, his most recognized role is that of Arthur, a kindly bellhop at the Mackinac Island Grand Hotel, in "Somewhere in Time" (1980).

Les Soeurs Soleil: Les Soeurs Soleil is a 1997 French comedy film directed by Jeannot Szwarc, starring and co-written by Marie-Anne Chazel.

Supergirl (film): Supergirl is a 1984 British superhero film directed by Jeannot Szwarc and written by David Odell, based on the DC Comics character of the same name and serves as a spin-off to Alexander and Ilya Salkind's "Superman" film series.  The film stars Helen Slater as Supergirl, along with Faye Dunaway, Mia Farrow and Peter O'Toole, with Marc McClure reprising his role as Jimmy Olsen from the "Superman" films.  He was the only actor to do so.  "Supergirl" was the first superhero film to feature a woman in the lead role.

La Vengeance d'une blonde: La Vengeance d'une blonde is a 1994 French comedy film directed by Jeannot Szwarc.

Question: Which film directed by Jeannot Szwarc starred an actor who later won an Emmy for his performance on Seinfield?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film directed by Jeannot Szwarc."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor in the film."
        },
        "role_in_film": {
          "type": "string",
          "description": "The character played by the actor in the film."
        },
        "seinfeld_award_status": {
          "type": "string",
          "description": "The status of the actor's Emmy award for their performance on Seinfeld (e.g., nominated, won)."
        }
      },
      "required": [
        "actor_name",
        "role_in_film",
        "seinfeld_award_status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "director_name",
    "actor_details"
  ],
  "additionalProperties": false
}
