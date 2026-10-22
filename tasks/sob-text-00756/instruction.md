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
The Shaggy D.A.: The Shaggy D.A. is a 1976 American comedy film and a sequel to "The Shaggy Dog" (1959) produced by Walt Disney Productions.  It was directed by Robert Stevenson and written by Don Tait, based on the original film and inspired by the long out-of-print Felix Salten novel, "The Hound of Florence."

List of Walt Disney Animation Studios films: This is a list of films from Walt Disney Animation Studios, an American animation studio headquartered in Burbank, California.  It creates animated feature films and is owned by The Walt Disney Company.  The studio has produced 56 feature films, beginning with "Snow White and the Seven Dwarfs" (1937)—one of the first full-length animated feature films and the first one made in the United States—and most recently "Moana" (2016).  Four feature films are in development, with "" set for release on November 21, 2018, "Frozen 2" on November 27, 2019, "Gigantic" on November 25, 2020, and an untitled film set for a November 24, 2021 release.

Bonnee Buttered Beef Steaks: Bonnee Buttered Beef Steaks were the flagship product of the Bonnee Frozen Products Company, which also produced frozen tamales and cubed steaks.  Bonnee Buttered Beef Steaks consisted of “finely chopped beef, molded, frozen, sliced and buttered.”  They were sold in packages which each contained four frozen 2-ounce beef patties and four frozen pats of 94-score butter.

Shaggy God story: A shaggy God story is a minor science fiction genre characterized by an attempt to explain Biblical concepts with science fiction tropes.  The term was coined by writer and critic Brian W. Aldiss in a pseudonymous column in the October 1965 issue of "New Worlds".  The term is a pun on the concept of a shaggy dog story.

Frozen 2: Frozen 2 is an upcoming American computer-animated film produced by Walt Disney Animation Studios and will be released by Walt Disney Pictures.  It is a sequel to the 2013 film, "Frozen".

The Shaggy Dog (1959 film): The Shaggy Dog is a black-and-white 1959 Walt Disney film about Wilby Daniels, a teenage boy who by the power of an enchanted ring of the Borgias is transformed into the title character, a shaggy Old English Sheepdog.  The film was based on the story "The Hound of Florence" by Felix Salten.  It is directed by Charles Barton and stars Fred MacMurray, Tommy Kirk, Jean Hagen, Kevin Corcoran, Tim Considine, Roberta Shore, and Annette Funicello.  This was Walt Disney's first live-action comedy.

The Shaggy Dog (2006 film): The Shaggy Dog is a 2006 American family comedy film directed by Brian Robbins and written by Geoff Rodkey, Jack Amiel, Michael Begler, Cormac Wibberley and Marianne Wibberley.  It is the second remake of the 1959 film of the same name, which was first remade as a television film in 1994.  Both the 1959 and 1994 features, as well as the 1976 theatrical sequel and the 1987 television sequel, had a character named Wilby Daniels transforming into an Old English Sheepdog, whereas this remake presents a character named Dave Douglas transforming into a Bearded Collie.  It stars Tim Allen, Robert Downey, Jr., Kristin Davis, Danny Glover, Spencer Breslin, Jane Curtin, Zena Grey and Philip Baker Hall.

Shaggy &amp; Friends: Shaggy & Friends is the ninth studio album released by Jamaican dancehall artist Shaggy, released exclusively via digital download on January 19, 2011.  It is Shaggy's first album ever not to be issued physically.  The album is first studio album in four years, following 2007's "Intoxication".  The album was entirely produced by Shaggy.  The album featured collaborations with Shaggy's long-time collaborators Rayvon and RikRok.

Itbarak: Itbaraks (English: Shaggy Dog) or just Baraks are Turkic mythological creatures.  They were "dog headed, dark coloured manly creatures".  According to the Oghuz Khagan Narratives, their country was in the "unknown northwest".  We can say it's around today's northern Russia.  Oghuz tried to invade them but couldn't success, so he had to retreat to a small island.

The Return of the Shaggy Dog: The Return of the Shaggy Dog is a 1987 American two-part made-for-television comedy film produced by Walt Disney Television.  The film is set in the 17 years between the events portrayed in "The Shaggy Dog" (1959) and "The Shaggy D.A." (1976).  It was broadcast on November 1 and 8, 1987 as a "Disney Sunday Movie" presentation on ABC.

Question: Which studio released the most recently released between The Shaggy Dog and Frozen 2?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "most_recent_film_info": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the most recently released film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the most recently released film."
        },
        "producing_studio": {
          "type": "string",
          "description": "The studio that produced the most recently released film."
        }
      },
      "required": [
        "title",
        "release_year",
        "producing_studio"
      ],
      "additionalProperties": false
    },
    "comparison_scope": {
      "type": "string",
      "description": "A description of the films included in the comparison."
    },
    "films_considered": {
      "type": "array",
      "description": "A list of all films considered in the comparison, with their details.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "producing_studio": {
            "type": "string",
            "description": "The studio that produced the film, if explicitly mentioned."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "most_recent_film_info",
    "comparison_scope",
    "films_considered"
  ],
  "additionalProperties": false
}
