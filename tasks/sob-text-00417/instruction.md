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
Am I Beautiful?: Am I Beautiful?  (German: "Bin ich schön?" )  is a 1998 German comedy film directed by Doris Dörrie.

Naked (2002 film): Naked ("Nackt" in German) is a German comedy film about the relationship problems of three young couples in Berlin, who meet for a dinner party which does not go well.  Released in 2002, it was directed by Doris Dörrie who also wrote the screenplay.

Men...: Men… (German: "Männer…" ) is a 1985 West German comedy film directed by Doris Dörrie.  It was chosen as West Germany's official submission to the 59th Academy Awards for Best Foreign Language Film, but did not manage to receive a nomination.

Cherry Blossoms (film): Cherry Blossoms (German: "Kirschblüten – Hanami" ) is a 2008 German drama film directed by Doris Dörrie.  This film, starring Elmar Wepper, Hannelore Elsner and Aya Irizuki, tells the story of Rudi: terminally ill, he travels to Japan after the sudden death of his wife Trudi – in order to make up for missed opportunities in life.

Doris Dörrie: Doris Dörrie (] ; born 26 May 1955) is a German film director, producer and author.

The Hairdresser: The Hairdresser (German: "Die Friseuse" ) is a 2010 German comedy film directed by Doris Dörrie.

Hal Ashby: Hal Ashby (September 2, 1929 – December 27, 1988) was an American film director and editor associated with the New Hollywood wave of filmmaking.

Pierre Sanoussi-Bliss: Pierre Sanoussi-Bliss (born 17 August 1962, Berlin-Mitte) is a German actor and director.  He has appeared in television and films for over 20 years.  He played a leading role in Doris Dörrie's 1994 film, "Keiner liebt mich".  He also plays a leading role in the comedy series "Alles wird gut".

Enlightenment Guaranteed: Erleuchtung garantiert ("Enlightenment Guaranteed") is a 2000 German film directed by Doris Dörrie about two brothers, Uwe (Uwe Ochsenknecht) and Gustav (Gustav-Peter Wöhler), who travel to Japan to sort out the mess of their lives.  Their plan is to visit the Sojiji Monastery in Monzen, near Tokyo.  On their way there, in a rather literal Buddhist moment, they lose all of their belongings.  When they at last make it to the monastery, they find that even there, enlightenment can be elusive.

The Thing About Men: The Thing About Men is a musical with music by Jimmy Roberts and lyrics and book by Joe DiPietro.  It is based on the 1985 German film Men by Doris Dörrie.  The plot revolves around a love triangle and shows what men will do to keep their pride and love affairs intact.

Question: Hal Ashby and Doris Dörrie, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals being compared."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "occupation_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the person."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All occupations listed for the person in the context."
          }
        },
        "required": [
          "person_name",
          "occupations"
        ],
        "additionalProperties": false
      },
      "description": "Detailed list of occupations for each person."
    }
  },
  "required": [
    "person_names",
    "mutual_occupation",
    "occupation_details"
  ],
  "additionalProperties": false
}
