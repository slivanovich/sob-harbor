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
Flight of the Intruder: Flight of the Intruder is a 1991 war film co-written and directed by John Milius, and starring Danny Glover, Willem Dafoe, and Brad Johnson.  It is based on the novel of the same name by former Grumman A-6 Intruder pilot Stephen Coonts.  The film received negative review upon release, and as of 2017 is Milius' final theatrical release as a director.

Farewell to the King: Farewell to the King is a 1989 American action adventure drama film written and directed by John Milius.  It stars Nick Nolte, Nigel Havers, Frank McRae, and Gerry Lopez and is loosely based on the 1969 novel "L'Adieu au Roi" by Pierre Schoendoerffer.  Longtime Milius collaborator Basil Poledouris composed the musical score.

Michael Caton-Jones: Michael Caton-Jones (born Michael Jones; 15 October 1957 in Broxburn, West Lothian, Scotland) is a Scottish film director.

Fred Rexer: Fred L. Rexer, Jr. is a U.S. Army Vietnam combat veteran and Hollywood actor and screenwriter.  He is best known as the military advisor for "Apocalypse Now" and as Spiritual Advisor for "Conan the Barbarian".  (Rexor, the Ben Davidson character in "Conan", was named after Fred.)  In the opening scenes of "Red Dawn", he played the paratroop commander, and later the knife-wielding Russian tank commander gunned down at the service station.  Fred Rexer has contributed numerous passages to the screenplay of that film and other films written or directed by John Milius and Walter Hill.  Milius has named Rexer as the real-life prototype of Captain Willard, the protagonist of "Apocalypse Now".  (See Peter Cowie, "The Apocalypse Now Book", Da Capo Press, 2001.)

Marcello, I'm So Bored: Marcello, I'm So Bored is a 1966 short animated film co-directed by John Milius and John Strawbridge.  It was made when Milius was a student at USC and was a parody of Italian cinema.

Big Wednesday: Big Wednesday is a 1978 American coming of age film directed by John Milius.  Co-written by Milius and Dennis Aaberg, it is loosely based on their own experiences at Malibu and a short story Aaberg had published in a 1974 "Surfer Magazine" entitled "No Pants Mance."  The picture stars Jan-Michael Vincent, William Katt, and Gary Busey as California surfers facing life and the Vietnam War against the backdrop of their love of surfing.

John Milius: John Frederick Milius (born April 11, 1944) is an American screenwriter, director, and producer of motion pictures.  He was one of the writers for the first two "Dirty Harry" films, received an Academy Award nomination as screenwriter of "Apocalypse Now," and wrote and directed "The Wind and the Lion", "Conan the Barbarian" and "Red Dawn."

Red Dawn: Red Dawn is a 1984 American war film directed by John Milius, filmed in Metrocolor and Panavision, and co-written by Milius and Kevin Reynolds.  It stars Patrick Swayze, C. Thomas Howell, Lea Thompson, Charlie Sheen, and Jennifer Grey.  It was the first film to be released in the US with a PG-13 rating.

Apocalypse Now: Apocalypse Now is a 1979 American epic war film directed, produced, and co-written by Francis Ford Coppola.  It was co-written by John Milius with narration written by Michael Herr.  It stars Marlon Brando, Robert Duvall, Martin Sheen, Frederic Forrest, Albert Hall, Sam Bottoms, Larry Fishburne, and Dennis Hopper.  The screenplay, written by Milius, adapts the story of Joseph Conrad's novella "Heart of Darkness", changing its setting from late nineteenth-century Congo to the Vietnam War.  It draws from Herr's "Dispatches" and Werner Herzog's "Aguirre, the Wrath of God" (1972).  The film revolves around Captain Benjamin L. Willard (Sheen) on a secret mission to assassinate Colonel Kurtz, a renegade who is presumed insane.

Milius (film): Milius is a 2013 documentary film about the writer, producer, director John Milius directed by Joey Figueroa and Zak Knutson.

Question: Are both Michael Caton-Jones and John Milius film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_directors": {
      "type": "boolean",
      "description": "True if both individuals are film directors, false otherwise."
    },
    "person_1_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "is_director": {
          "type": "boolean",
          "description": "True if the person is a film director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the person."
        }
      },
      "required": [
        "name",
        "is_director",
        "nationality"
      ],
      "additionalProperties": false
    },
    "person_2_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "is_director": {
          "type": "boolean",
          "description": "True if the person is a film director."
        },
        "other_professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other known professions of the person."
        }
      },
      "required": [
        "name",
        "is_director",
        "other_professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "is_both_directors",
    "person_1_details",
    "person_2_details"
  ],
  "additionalProperties": false
}
