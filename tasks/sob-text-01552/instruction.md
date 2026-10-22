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
Topaze (1933 French film): Topaze is a 1933 French comedy film directed by  Louis J. Gasnier and starring  Louis Jouvet, Simone Héliard and Marcel Vallée.  It is based on the 1928 play "Topaze" by Marcel Pagnol.  The same year an American version of the play "Topaze" was released, starring John Barrymore.  In 1936 Pagnol himself remade the film in France.

Lady Paname: Lady Paname was a 1950 drama film, directed and written by Henri Jeanson, and starring Louis Jouvet, Suzy Delair, Henri Guisol and Henri Crémieux.

Topaze (1933 American film): Topaze is a 1933 American Pre-Code film based on the French play of the same name by Marcel Pagnol.  Another film version of "Topaze", this one made in the original French was also released that year, starring Louis Jouvet in the title role.  Subsequently Pagnol himself directed a 1936 adaptation.

The Heart of a Nation: The Heart of a Nation (French: Untel père et fils ) is a 1943 French drama film directed by Julien Duvivier who co-wrote screenplay with Marcel Achard and Charles Spaak.  The film stars Raimu, Michèle Morgan and Louis Jouvet.

Louis Jouvet: Louis Jouvet (24 December 1887 – 16 August 1951) was a renowned French actor, director, and theatre director.

Mick Jackson (director): Mick Jackson (born 4 October 1943 in Grays, England, United Kingdom) is a British film director and television producer.  Between 1973 and 1987, Jackson directed many documentary and drama productions for BBC TV and Channel 4.  Relocating to Hollywood, he directed feature films, including "The Bodyguard" starring Kevin Costner and Whitney Houston.  In 2010, Jackson won an Emmy for Outstanding Directing for a Miniseries, Movie or a Dramatic Special for the dramatised biographical TV film "Temple Grandin".

Théâtre de l'Athénée: The Théâtre de l'Athénée is a theatre at 7 rue Boudreau, in the 9th arrondissement of Paris.  Renovated in 1996 and classified a historical monument, it is among the most beautiful buildings in Paris.  In addition to its architectural treasures, the Athénée inherits an artistic tradition marked by the figure of Louis Jouvet who directed the theatre from 1934 to 1951.  During the period when he was director, it became known as the Athenée Théâtre Louis-Jouvet.

The Infernal Machine (play): The Infernal Machine, or La Machine Infernale is a French play by the dramatist Jean Cocteau, based on the ancient Greek myth of Oedipus.  The play initially premiered on April 10, 1934 at the Theatre Louis Jouvet in Paris, France, under the direction of Louis Jouvet himself, with costumes and scene design by Christian Bérard.  "The Infernal Machine," as translated by Albert Bermel, was first played at the Phoenix Theatre, New York, on February 3, 1958, under the direction of Herbert Berghof, with scenery by Ming Cho Less, costumes by Alvin Colt, and lighting by Tharon Musser.

Dr. Knock: Dr. Knock (original title "Knock") is a French comedy film from 1951, directed by Guy Lefranc, written by Georges Neveux, and starring by Louis Jouvet.  It also features an uncredited appearance by Louis de Funès.  The movie is based on the 1923 theatre play "Knock ou le Triomphe de la médecine" ("Knock or The Triumph of Medicine") by Jules Romain.

Jean Hugo: Jean Hugo (19 November 1894 – 21 June 1984) was a painter, illustrator, theatre designer and author.  He was born in Paris and died in his home at the Mas de Fourques, near Lunel, France.  Brought up in a lively artistic environment, he began teaching himself drawing and painting and wrote essays and poetry from a very early age.  His artistic career spans the 20th century, from his early sketches of the First World War, through the creative ferment of the Parisian interwar years, and up to his death in 1984.  He was part of a number of artistic circles that included Jean Cocteau, Raymond Radiguet, Pablo Picasso, Georges Auric, Erik Satie, Blaise Cendrars, Marie-Laure de Noailles, Paul Eluard, Francis Poulenc, Charles Dullin, Louis Jouvet, Colette, Marcel Proust, Jacques Maritain, Max Jacob, Carl Theodor Dreyer, Marie Bell, Louise de Vilmorin, Cecil Beaton and many others.

Question: Are both Louis Jouvet and Mick Jackson a filmmaker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question": {
      "type": "string",
      "description": "The original question asked."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals are filmmakers, false otherwise."
    },
    "analysis": {
      "type": "object",
      "properties": {
        "mick_jackson": {
          "type": "object",
          "properties": {
            "is_filmmaker": {
              "type": "boolean",
              "description": "Indicates if Mick Jackson is identified as a filmmaker."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Specific roles Mick Jackson holds in the film/television industry."
            }
          },
          "required": [
            "is_filmmaker",
            "roles"
          ],
          "additionalProperties": false
        },
        "louis_jouvet": {
          "type": "object",
          "properties": {
            "is_filmmaker": {
              "type": "boolean",
              "description": "Indicates if Louis Jouvet is identified as a filmmaker."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Specific roles Louis Jouvet holds in the film/theatre industry."
            }
          },
          "required": [
            "is_filmmaker",
            "roles"
          ],
          "additionalProperties": false
        },
        "overall_conclusion": {
          "type": "string",
          "description": "A summary explaining the determination of the answer."
        }
      },
      "required": [
        "mick_jackson",
        "louis_jouvet",
        "overall_conclusion"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "question",
    "answer",
    "analysis"
  ],
  "additionalProperties": false
}
