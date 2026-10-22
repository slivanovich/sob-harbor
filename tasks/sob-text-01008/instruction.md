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
Predestination (film): Predestination is a 2014 Australian science fiction thriller film written and directed by Michael and Peter Spierig.  The film stars Ethan Hawke, Sarah Snook and Noah Taylor, and is based on the short story ""—All You Zombies—"" by Robert A. Heinlein.

Holding the Man (film): Holding the Man is a 2015 Australian romantic drama film adapted from Timothy Conigrave's 1995 memoir of the same name.  It was directed by Neil Armfield and stars Ryan Corr and Craig Stott, with supporting performances from Guy Pearce, Anthony LaPaglia, Sarah Snook, Kerry Fox and Geoffrey Rush.  The screenplay was written by Tommy Murphy who also adapted the memoir for the stage play.

How to Make an American Quilt: How to Make an American Quilt is a 1995 American drama film based on the 1991 novel of the same name by Whitney Otto.  Directed by Jocelyn Moorhouse, the film stars Winona Ryder, Anne Bancroft, Ellen Burstyn, Kate Nelligan and Alfre Woodard.  The film received a nomination for the Screen Actors Guild Award for Outstanding Performance by a Cast in a Motion Picture.

The Dressmaker (2015 film): The Dressmaker is a 2015 Australian revenge comedy-drama film written and directed by Jocelyn Moorhouse, based on the novel of the same name by Rosalie Ham.  It stars Kate Winslet as a femme fatale in the titular role of the dressmaker, Myrtle "Tilly" Dunnage, who returns to a small Australian town to take care of her ailing, mentally unstable mother.  The film explores the themes of revenge and creativity and was described by Moorhouse as "Clint Eastwood's "Unforgiven" with a sewing machine."

The Glass Castle (film): The Glass Castle is a 2017 American biographical drama film directed by Destin Daniel Cretton and written by Cretton, Andrew Lanham, and Marti Noxon, based on Jeannette Walls's 2005 memoir of the same name.  Depicting Walls's real-life childhood spent squatting in homes and living in poverty, the film stars Brie Larson as Walls with Naomi Watts, Woody Harrelson, Max Greenfield, and Sarah Snook in supporting roles.  The film was released on August 11, 2017, by Lionsgate and received mixed reviews from critics, who praised the performances of its cast (particularly Larson and Harrelson) but criticized the mishandled tones and material.

Proof (1991 film): Proof is a 1991 Australian comedy-drama film written and directed by Jocelyn Moorhouse, and starring Hugo Weaving, Geneviève Picot and Russell Crowe.  The film was released in Australia on 15 August 1991.  It was chosen as "Best Film" at the 1991 Australian Film Institute Awards, along with 5 other awards, including Moorhouse for "Best Director", Weaving for "Best Leading Actor", and Crowe for "Best Supporting Actor".

Sarah Snook: Sarah Snook (born 28 July 1987) is an Australian actress, widely known for her roles in "Predestination", "Holding the Man", "The Dressmaker", and "Steve Jobs".

A Thousand Acres (film): A Thousand Acres is a 1997 American drama film directed by Jocelyn Moorhouse and starring Michelle Pfeiffer, Jessica Lange, Jennifer Jason Leigh and Jason Robards.

Not Suitable for Children: Not Suitable for Children is an 2012 Australian romantic comedy film directed by Peter Templeman and written by Michael Lucas.  It was released on 12 July 2012.  It stars Ryan Kwanten, Sarah Snook, and Ryan Corr.

Jessabelle: Jessabelle is a 2014 American supernatural horror film directed by Kevin Greutert and written by Ben Garant.  The film stars Sarah Snook, Mark Webber, Joelle Carter, David Andrews, Amber Stevens and Ana de la Reguera.  The film was released on November 7, 2014 by Lionsgate.

Question: What film did Sarah Snook star in that was a revenge comedy-drama film written and directed by Jocelyn Moorhouse?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "writer": {
      "type": "string",
      "description": "The writer of the film."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre description of the film."
    },
    "starring_actor": {
      "type": "string",
      "description": "The actor whose involvement was a key part of the query."
    },
    "actor_confirmed_in_film": {
      "type": "boolean",
      "description": "Indicates if the actor's role in this specific film was explicitly mentioned in the film's description or the actor's biography."
    }
  },
  "required": [
    "film_title",
    "director",
    "writer",
    "genre",
    "starring_actor",
    "actor_confirmed_in_film"
  ],
  "additionalProperties": false
}
