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
Theo Angelopoulos: Theodoros "Theo" Angelopoulos (Greek: Θεόδωρος Αγγελόπουλος ) (27 April 1935 – 24 January 2012) was a Greek filmmaker, screenwriter and film producer.

Eleni Karaindrou: Eleni Karaindrou (Greek: Ελένη Καραΐνδρου ) is a Greek composer, born in the village of Teichio (Tichio) in Phocis, Central Greece, on November 25, 1941.  She is best known for scoring the films of the Greek director Theo Angelopoulos.

Trilogy: The Weeping Meadow: Trilogy: The Weeping Meadow (Greek: Τριλογία: Το λιβάδι που δακρύζει) is an award-winning 2004 Greek romantic historical drama film, written and directed by Theo Angelopoulos.  It stars Alexandra Aidini, Thalia Argyriou, Giorgos Armenis, Vasilis Kolovos and Nikos Poursanidis, and was released during the 2004 Berlin International Film Festival, on 11 February 2004.  It is the first film of a projected trilogy about recent events in Greek history. " The Dust of Time" (2008) is the second film of the trilogy.  In January 2012, Angelopoulos died unexpectedly, leaving the trilogy uncompleted.

Barbara Albert: Barbara Albert (born 1970 in Vienna) is an Austrian writer, film-producer and film-director.

Reconstitution (1970 film): Reconstitution (, tr.  "Anaparastasi") is a 1970 Greek dramatic black and white independent underground art film directed by Theo Angelopoulos.  It is the director's first feature film.  While based on true events, it transcends them to recall the ancient myths of the Atrides and Clytemnestra.

Landscape in the Mist: Landscape in the Mist (, translit.  "Topio stin omichli") is a 1988 Greek film directed by Theo Angelopoulos.  The film was selected as the Greek entry for the Best Foreign Language Film at the 62nd Academy Awards, but was not accepted as a nominee.  The film is the third installment in Angelopoulos' "Trilogy of Silence", following "Voyage to Cythera" (1984) and "The Beekeeper" (1986).

Eternity and a Day: Eternity and a Day (Greek: Μια αιωνιότητα και μια μέρα , "Mia aioniotita kai mia mera ") is a 1998 Greek film starring Bruno Ganz, and directed by Theo Angelopoulos.  The film won the Palme d'Or and the Prize of the Ecumenical Jury at the 1998 Cannes Film Festival.  The film was selected as the Greek entry for the Best Foreign Language Film at the 71st Academy Awards, but was not accepted as a nominee.

Ulysses' Gaze: Ulysses' Gaze (Greek: Το βλέμμα του Οδυσσέα , translit.  To Vlemma tou Odyssea) is a 1995 Greek film directed by Theo Angelopoulos.  The film was selected as the Greek entry for the Best Foreign Language Film at the 68th Academy Awards but it was not nominated.

Days of '36: Days of '36 (, tr.  "Méres tou '36") is a 1972 Greek dramatic independent underground art film directed by Theo Angelopoulos.  Its title is a tribute to Constantine P. Cavafy.

Alexander the Great (1980 film): Alexander the Great (Greek: Ο Μεγαλέξανδρος ) is a 1980 Greek film directed by Theo Angelopoulos.

Question: Which filmmaker, Theo Angelopoulos or Barbara Albert, was Greek?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "filmmaker_name": {
      "type": "string",
      "description": "The name of the filmmaker who is Greek."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the identified filmmaker."
    },
    "other_filmmaker_mentioned": {
      "type": "string",
      "description": "The name of the other filmmaker mentioned in the question."
    },
    "other_filmmaker_nationality": {
      "type": "string",
      "description": "The nationality of the other filmmaker."
    },
    "question_answered": {
      "type": "boolean",
      "description": "Indicates if the question about the Greek filmmaker was answered."
    }
  },
  "required": [
    "filmmaker_name",
    "nationality",
    "other_filmmaker_mentioned",
    "other_filmmaker_nationality",
    "question_answered"
  ],
  "additionalProperties": false
}
