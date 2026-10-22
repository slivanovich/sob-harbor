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
Bachelor Mother (1932 film): Bachelor Mother is a 1932 Pre-Code action film directed by Charles Hutchison.

Charles Hutchison: Charles Hutchison (December 3, 1879 – May 30, 1949) was an American film actor, director and screenwriter.  He appeared in 49 films between 1914 and 1944.  He also directed 33 films between 1915 and 1938.  Though he directed numerous independent silent features, he is best remembered today as Pathé's leading male serial star from 1918 to 1922.  In 1923 he went to Britain and made two films "Hutch Stirs 'em Up" and "Hurricane Hutch in Many Adventures" for the Ideal Film Company.  He made one last serial in 1926, "Lightning Hutch", for Arrow Film Company.  It was meant to be a comeback vehicle, but the production company went into bankruptcy just as it was released.

The Coward (1915 film): The Coward is a 1915 American silent historical war drama film directed by Reginald Barker and produced by Thomas H. Ince.  Ince also wrote the film's story and scenario with C. Gardner Sullivan.  The film stars Frank Keenan and Charles Ray.  John Gilbert also appears in an uncredited bit part.  A copy of "The Coward" is preserved at the Museum of Modern Art.

Reginald Barker: Reginald C. Barker (April 2, 1886 – February 23, 1945) was a pioneer film director.

The Wrath of the Gods (1914 film): The Wrath of the Gods is a 1914 American silent drama film directed by Reginald Barker, and starring Sessue Hayakawa, Tsuru Aoki, Frank Borzage, Thomas Kurihara and Henry Kotani in the lead roles.  This was the first feature film appearance of Hayakawa and the directorial debut of Barker.

Out of Singapore: Out of Singapore is a 1932 American drama film directed by Charles Hutchison.  The film was re-released by Astor Pictures in 1941 as Gangsters of the Sea.

Hutch Stirs 'em Up: Hutch Stirs 'em Up is a 1923 British silent comedy action film directed by Frank Hall Crane and starring Charles Hutchison, Joan Barry and Malcolm Tod.  It was based on the novel "The Hawk of Rede" by Harry Harding.

Forbidden Heaven: Forbidden Heaven is a 1935 American drama film directed by Reginald Barker and written by Sada Cowan and Jefferson Parker.  The film stars Charles Farrell, Charlotte Henry, Beryl Mercer, Fred Walton, Eric Wilton and Phyllis Barry.  The film was released on October 5, 1935, by Republic Pictures.

Phantom Patrol: Phantom Patrol is a 1936 American film directed by Charles Hutchison.

Hurricane Hutch in Many Adventures: Hurricane Hutch in Many Adventures is a 1924 British silent comedy action film directed by Charles Hutchison and starring Charles Hutchison, Warwick Ward and Malcolm Tod.

Question: Charles Hutchison and Reginald Barker, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals for whom the mutual occupation is sought."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "individuals_occupations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the individual."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of occupations for the individual as mentioned in the context."
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "description": "Details of each individual and their listed occupations."
    }
  },
  "required": [
    "person_names",
    "mutual_occupation",
    "individuals_occupations"
  ],
  "additionalProperties": false
}
