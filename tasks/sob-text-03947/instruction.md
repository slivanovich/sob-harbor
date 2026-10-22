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
The Loft (film): The Loft is a 2014 American-Belgian erotic thriller mystery film directed by Erik Van Looy.  It is a remake of the 2008 Dutch-language Belgian film "Loft", which was also directed by Van Looy.  The screenplay was written by Wesley Strick, adapted from the original script by Bart De Pauw.  Starring Karl Urban, James Marsden and Wentworth Miller, it also features Matthias Schoenaerts who reprises his role from the original film.

Enter the Void: Enter the Void is a 2009 English-language French drama film written and directed by Gaspar Noé and starring Nathaniel Brown, Paz de la Huerta, and Cyril Roy.  Set in the neon-lit nightclub environments of Tokyo, the story follows Oscar, a young American drug dealer who gets shot by the police, but continues to watch subsequent events during an out-of-body experience.  The film is shot from a first-person viewpoint, which often floats above the city streets, and occasionally features Oscar staring over his own shoulder as he recalls moments from his past.  Noé labels the film a "psychedelic melodrama".

Erik Van Looy: Erik Ludovicus Maria Van Looy (] ) is a Belgian film director known for his thriller movies.  He was born on 26 April 1962.

Shades (1999 film): Shades is a 1999 Belgian film directed by Erik Van Looy and written by Looy, Paul Breuls and Guy Lee Thys.  The story is loosely inspired on the Belgian murderer and his escape from prison in 1982.

Carne (film): Carne is a 1991 French drama film written and directed by Gaspar Noé, starring Philippe Nahon and Blandine Lenoir.  It tells the story of a horse butcher with a mute daughter.  At a running time of 40 minutes, it was the first longer film directed by Noé.  The narrative was continued in Noé's 1998 full-length debut, "I Stand Alone".

The Alzheimer Case: The Alzheimer Case, also known as "The Alzheimer Affair" or "The Memory of a Killer", Dutch: "De Zaak Alzheimer" , is a 2003 film directed by Erik Van Looy, based on the novel "De Zaak Alzheimer" by Jef Geeraerts.  An American remake of the film is in development at Focus Features.  Stephane Sperry is the producer.  Matthew Michaud adapted the screenplay from the original film.

Loft (2008 film): Loft is a 2008 Belgian erotic mystery film directed by Erik Van Looy and written by Bart De Pauw, starring an ensemble cast of notable Flemish actors.

Gaspar Noé: Gaspar Noé (] ; ] ; born December 27, 1963) is an Argentinian film director and screenwriter living in France.  He is the son of Argentinian painter, writer and intellectual Luis Felipe Noé and was born in Buenos Aires in 1963.  He is mostly known for his four feature films: "I Stand Alone", "Irréversible", "Enter the Void" and "Love".

Ad Fundum: Ad Fundum is a 1993 Belgian drama film directed by Erik Van Looy.  It is his first feature-length film after the short movies 'Dr. Tritsmans' and 'Yuppies'.  It tells the story of some students studying at the university of Leuven, and who participate in some initiation rites.

Frans Van Looy: Frans Van Looy (born 26 August 1950) is a former Belgian cyclist.  Looy was professional from 1972 to 1982.  He competed in the individual road race at the 1972 Summer Olympics.

Question: Which filmmaker is from Argenitina, Gaspar Noé or Erik Van Looy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "filmmaker_name": {
      "type": "string",
      "description": "The name of the filmmaker who is from Argentina."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country of origin for the identified filmmaker."
    },
    "other_filmmaker_name": {
      "type": "string",
      "description": "The name of the other filmmaker mentioned in the question."
    },
    "other_filmmaker_country_of_origin": {
      "type": "string",
      "description": "The country of origin for the other filmmaker."
    },
    "is_from_argentina": {
      "type": "boolean",
      "description": "True if the identified filmmaker is from Argentina, false otherwise."
    }
  },
  "required": [
    "filmmaker_name",
    "country_of_origin",
    "other_filmmaker_name",
    "other_filmmaker_country_of_origin",
    "is_from_argentina"
  ],
  "additionalProperties": false
}
