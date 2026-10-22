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
Shiv (weapon): Shiv (possibly from the Romani word "chivomengro", "knife"), also "chiv", is a slang term for any sharp or pointed implement used as a knife-like weapon.  The "Oxford English Dictionary" suggests "shive", a razor, documented in 1915, as the root word.  In the 1920s, "shiv" was also a common slang term for a bladed weapon, mostly a knife.  In the United States, an improvised prison knife is also often called a shank.

Dongo: Dongo may refer to: The mix between a dingo and any other dog is referred to as a "Dongo" and also is a slang term for male genitalia.  Dongo is also reported to be, but is not widely used, as a slang term in Australia as a substitute for the color orange.

Gweilo: Gweilo or gwailou (, pronounced ] ) is a common Cantonese slang term for Westerners.  In its unmodified form, it applies only to European ethnicities and has a history of racially deprecatory use.  Cantonese speakers frequently use "gwailou" to refer to Westerners in general use, in a non-derogatory context, although whether this type of usage is offensive is disputed by both Cantonese and Westerners alike.

Shmohawk: Shmohawk or schmohawk is a slang term that might have derived from "schmo", a slang term meaning "fool".  The HBO television show "Curb Your Enthusiasm" gave the word recent notoriety, and HBO even sells a "Curb Your Enthusiasm" schmohawk mug.  Earlier uses of the word can be found in the "Crusader Rabbit" animated cartoon "Crusader and the Schmohawk Indians", released in 1950 and in Saul Bellow's 1958 novel "Henderson the Rain King".

Ars (slang): Ars (Hebrew: ערס‎ ‎ "`ars "), or Arsim (the plural in Hebrew) is a derogatory Hebrew slang term for the Israeli stereotype of a low-class young man.  The stereotype may also refer to personal effects such as flashy jewelry and clothing.  A woman fitting this stereotype is an "Arsit" (though this usually implies masculinity in the woman), the word formed by adding the Hebrew feminine ending "it" to the Arabic word "Ars" (Arabic: عرص‎ ‎ , "ʿarṣ ").  Another term used for women is "Freḥa" (פרחה), originally a female Moroccan first name popular in the 1950s and the 1960s, during the large immigration wave from Morocco to Israel.  The Ars subculture traditionally was associated with young Jews of Middle Eastern origin, but in recent years has expanded to a broader range of ethnicities.  In particular, the term "Freḥa" is nowadays used in reference to intellectually shallow girls of all ethnicities, like bimbo or airhead in English.

Ducking (slang): "Ducking" is a prison slang term for a technique through which prisoners modify the behavior of correctional officers and other prison staff members using manipulation and coercion.  The prison slang term for a prison staff member that has been manipulated is a "duck".

Beard (companion): Beard is a slang term describing a person who is used, knowingly or unknowingly, as a date, romantic partner (boyfriend or girlfriend), or spouse either to conceal infidelity or to conceal one's sexual orientation.  The American slang term originally referred to anyone who acted on behalf of another, in any transaction, to conceal a person's true identity.  The term can be used in heterosexual and homosexual contexts, but is especially used within LGBT culture.  References to beards are seen in mainstream television and films, and other entertainment.

Homie: Homie (from "homeboy") is an English language slang term found in American urban culture, whose origins etymologists generally trace to Mexican-American Spanglish from the late 19th century, with the word "homeboy" meaning a male friend from back home.  The words originated from the late 1930s/early 1940s and continuing up to the present.  As slang terms, the words have come to have variations in meaning, depending on local subcultures in a region, without the stability provided for dictionary-defined words.  The term has also been traced to military slang .

Zips: Zips (also Siggies or Geeps) is a slang term often used as a derogatory slur by Italian American and Sicilian American mobsters in reference to newer immigrant Sicilian and Italian mafiosi.  The name is said to have originated from mobsters' inability to understand the faster-speaking Sicilian dialects, which appeared to "zip" by.  Other theories include pejorative uses such as Sicilians' preference for silent, homemade zip guns.  According to still another theory, the term is a contraction of the Sicilian slang term for "hicks" or "primitives."  The older Sicilian mafiosi of pre-Prohibition known as "Mustache Petes" (who eventually were deposed by American-born mobsters during the Castellammarese War) were also referred to as zips.

Ghosts (2006 film): Ghosts is a 2006 drama film directed by Nick Broomfield, based on the 2004 Morecambe Bay cockling disaster.  The title is a reference to the Cantonese slang term "Gweilo" (鬼佬), meaning "ghost man", used for white people.

Question: Ghosts comes from a slang term that applies to what type of ethnicities?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "slang_term_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the slang term."
        },
        "language": {
          "type": "string",
          "description": "The language of origin for the slang term."
        },
        "applies_to_ethnicities": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of ethnicities to which the slang term applies in its unmodified form."
        }
      },
      "required": [
        "name",
        "language",
        "applies_to_ethnicities"
      ],
      "additionalProperties": false
    },
    "film_reference": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film that references the slang term."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of how the film's title relates to the slang term."
    }
  },
  "required": [
    "slang_term_details",
    "film_reference",
    "relationship_description"
  ],
  "additionalProperties": false
}
