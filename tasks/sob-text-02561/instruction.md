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
Frito Bandito: The Frito Bandito was the cartoon mascot for Fritos corn chips from 1967 to 1971.  The Bandito was created by the Foote, Cone & Belding Agency, and animated by Tex Avery.  The character was voiced by Mel Blanc, who used an exaggerated Mexican accent not unlike another character of his, Speedy Gonzales.  The Frito Bandito spoke broken English and robbed people of their Fritos corn chips, a reference to the "Mexican bandit" stereotype in western movies.  He also complained that he was being pursued by the "Frito Bureau of Investigation."

Mexicali Shmoes: Mexicali Shmoes is a 1959 "Looney Tunes" cartoon short directed by Friz Freleng and starring Speedy Gonzales and the singing cats Jose and Manuel.  Voice actors include Mel Blanc as the voices of Speedy Gonzales and Jose plus an uncredited Tom Holland as the voice of Manuel.

Speedy Gonzales (song): "Speedy Gonzales" is a 1961 David Dante alias David Hess song (RCA 8056) about Speedy Gonzales, "the fastest mouse in all Mexico".  It was written by Buddy Kaye, Ethel Lee and David Hess.  The David Dante original briefly entered the US Music Vendor chart in April 1961.

Cat-Tails for Two: Cat-Tails for Two is a 1953 (1961 Blue Ribbon Re-issue) Warner Bros. "Merrie Melodies" cartoon, directed by Robert McKimson and written by Tedd Pierce starring Bennie the fat cat and George.  It was animated in 1952.  Voices by Mel Blanc and music by Carl Stalling.  It was the first appearance of Speedy Gonzales, in a prototype form.  Because this cartoon's rendition of Speedy Gonzales looked rather coarse, they redesigned him for future cartoon releases.

Speedy Gonzales: Speedy Gonzales is an animated cartoon character in the Warner Brothers "Looney Tunes" and "Merrie Melodies" series of cartoons.  He is portrayed as "The Fastest Mouse in all Mexico" with his major traits being the ability to run extremely fast and speaking with an exaggerated Mexican accent and also speaking Spanish.  He usually wears a yellow "sombrero", white shirt and trousers (which was a common traditional outfit worn by men and boys of rural Mexican villages), and a red kerchief, similar to that of some traditional Mexican attires.  To date, there have been 46 cartoons made either starring or featuring this character.

Road to Andalay: Road to Andalay is a 1964 Merrie Melodies animated short featuring Speedy Gonzales and Sylvester.  It was released subcontractedly in different box dates of both 1963 and 1964 dates.  It was also the final cartoon to co-star Speedy Gonzales and Sylvester (in terms of release order).

Chili Weather: Some Mexican mice see the Guadalajara Food Processing Plant and try to enter but are prevent by Sylvester guarding the place.  The hungry mice summon Speedy Gonzales to help them get food.  Speedy steals some cheese, but when he goes back, Sylvester starts chasing him.  They end up on a conveyor belt, where Sylvester gets shaved by some chopping blades.  Speedy spreads some grease on a platform, and Sylvester skids into a vat of Tabasco Sauce.  He melts a block of ice to recover.  On another conveyor belt, Sylvester gets a bottle cap pressed onto his head.  He pries it off with a bottle opener, but Speedy "yee-ha's" him into the ceiling where it gets stuck again, and Speedy hides his bottle opener.  Sylvester wanders off, trying to club Speedy but unable to because of his lack of sight, and his aimless wandering lands him in a dehydrator.  He emerges from the dehydrator in a miniature size (finally able to remove the bottle cap), but then Speedy, who is now larger than the cat, greets him prompting the tiny Sylvester to run away in fright.

Mucho Locos: Mucho Locos is a 1966 Merrie Melodies animated short featuring Speedy Gonzales and Daffy Duck.  In the short, Speedy highlights some of his and Daffy's previous exploits.  It was the only cartoon in the series where Daffy gets the upper hand at the end.  It was also the final appearance of Porky Pig in the Golden Age of Animation.  Porky appears in the "Robin Hood Daffy" segment.  It is the only cartoon to have Porky Pig and Speedy Gonzales paired together, although unseen together.

The Unhanged: The Unhanged (Finnish: Hirttämättömät) is a 1971 Finnish western comedy film directed by Spede Pasanen and Vesa-Matti Loiri.  It is the sequel to the 1970 film "Speedy Gonzales - noin 7 veljeksen poika".  In addition to featuring Pasanen and Loiri (originally set to appear in "Speedy Gonzales", but unable to appear due to an injury), the film also stars Pasanen's other stock actors, such as Simo Salminen and Olavi Ahonen.  The two main characters are parody versions of The Lone Ranger and his sidekick Tonto.

Speedy Gonzales – noin 7 veljeksen poika: Speedy Gonzales – noin 7 veljeksen poika (English: Speedy Gonzales - The son of about seven brothers ) (1970) is a Finnish western comedy directed by Ere Kokkonen, and written by Kokkonen with Spede Pasanen and Vesa-Matti Loiri.  The title refers to Pasanen's 1968 film "Noin seitsemän veljestä", though the movie does not otherwise link to it in any way.  Neither has it anything to do with the cartoon character Speedy Gonzales.

Question: What stereotypes provide the personas for Frito Bandito and Speedy Gonzales?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "stereotype_nationality": {
      "type": "string",
      "description": "The nationality that forms the basis of the stereotypes for the characters."
    },
    "stereotype_origin_country": {
      "type": "string",
      "description": "The country associated with the stereotype."
    },
    "characters_details": {
      "type": "array",
      "description": "Details about each character and how their persona reflects the stereotype.",
      "items": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character."
          },
          "persona_attributes": {
            "type": "string",
            "description": "Key attributes of the character's persona that reflect the stereotype, as described in the context."
          },
          "explicit_stereotype_name": {
            "type": "string",
            "description": "The specific name of the stereotype mentioned in the context for this character, if any."
          }
        },
        "required": [
          "character_name",
          "persona_attributes"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "stereotype_nationality",
    "stereotype_origin_country",
    "characters_details"
  ],
  "additionalProperties": false
}
