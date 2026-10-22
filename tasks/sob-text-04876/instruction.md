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
Albatros L 76: The Albatros L 76 Aeolus was a military reconnaissance aircraft built by Albatros Flugzeugwerke in 1927.  The plane had wooden dual-spar wings with plywood skins supported by N-type struts and a fabric-covered fuselage made of welded steel tubing.  The aircraft was used for testing, as well as the training of the Soviet Air Force.  It was difficult to fly, and killed many people, including Emil Thuy, who crashed near Smolensk on June 11, 1930, and Paul Jeschonnek, who crashed near Berlin on June 13, 1929.  As a result, it had to be improved, leading to the production of the Albatros L 77v, designed by Ernst Heinkel Flugzeugwerke.

Albatros L 59: The Albatros L 59 was a single-seat German utility aircraft of the 1920s.  It was a single-engine low-wing cantilever monoplane with large, spatted wide track undercarriage attached, unusually for the time not to the fuselage but to the wing roots.  The whole aircraft was covered in 3-ply.

Albatros L 60: The Albatros L 60 was a two-seat German utility aircraft of the 1920s developed from the Albatros L 59.  It was a single-engine low-wing cantilever monoplane with large, spatted undercarriage.

Kobold: The kobold (occasionally cobold) is a sprite stemming from Germanic mythology and surviving into modern times in German folklore.

Odin: In Germanic mythology, Odin (from Old Norse Óðinn) is a widely revered god.  In Norse mythology, from which stems most of the information about the god, Odin is associated with healing, death, royalty, the gallows, knowledge, battle, sorcery, poetry, frenzy, and the runic alphabet, and is the husband of the goddess Frigg.  In wider Germanic mythology and paganism, Odin was known in Old English as Wōden, in Old Saxon as Wōdan, and in Old High German as Wuotan or Wōtan, all stemming from the reconstructed Proto-Germanic theonym wōđanaz.

King Goldemar: King Goldemar (also spelled Goldmar, Vollmar, and Volmar) is a dwarf or kobold from Germanic mythology and folklore.  By the Middle Ages, Goldemar had become the king of the dwarfs in German belief.  In the fairy tale "The Friendship of the Dwarfs", the author Villamaria depicts Goldemar as a "mighty dwarf king" with a queen and a court of dwarf nobles at his service.  He has long, silver hair and beard and wears a crown and a purple mantle.  In one tale, he runs away with the daughter of a human king.  Fragments of an epic poem by Albrecht von Kemenaten called "Goldemar" survive.  The poem tells of Dietrich's encounter with the dwarf king.  The king also features in ""Der junge König und die Schafërin"" ("The Prince and the Shepherdess") by German poet Ludwig Uhland.  Goldemar's brothers, Alberich or Elberich and Elbegast, feature in other poems.

Extra EA-260: The Extra 260 is a single-seat aerobatic aircraft derived from the Extra 230 and first flown in 1986.  Designed by aerobatic pilot Walter Extra based on the layout of the Extra 230, the Extra 260 is a higher performance version of its predecessor.  One EA-260 was flown by Patty Wagstaff to victory in two U.S. National Aerobatic Championships, (1991 and 1992), and then retired for an Extra 300S.

Albatros L 79: The Albatros L 79 Kobold was a single-seat German aerobatic aircraft of the 1920s and 1930s.  It was a single-bay biplane with unstaggered, equal-span wings that had a symmetrical airfoil intended to ensure performance during inverted flight.

Jurgis Kairys: Jurgis Kairys (born May 6, 1952 in Krasnoyarsk) is a Lithuanian aerobatic pilot and aeronautical engineer.  He has won many awards for his flying and has invented several maneuvers, including the "Kairys Wheel."  He helped develop the Sukhoi Su-26, -29, and -31 aerobatic aircraft, and also has manufactured his own aerobatic aircraft, called the "Juka."

Germanic mythology: Germanic mythology consists of the body of myths native to the Germanic peoples.  Commonly featuring narratives focused on Germanic deities and a large variety of other entities, Germanic mythology dates from the Proto-Germanic period and reaches beyond the Christianization of the Germanic peoples and into modern Germanic folklore.  Germanic mythology includes Norse mythology, Anglo-Saxon mythology, and Continental Germanic mythology.

Question: The Albatros L 79 Kobold was a single-seat German aerobatic aircraft of the 1920s and 1930s, the kobold (occasionally cobold) is which type of entity, stemming from Germanic mythology, and surviving into modern times in German folklore?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the entity being described."
    },
    "entity_type": {
      "type": "string",
      "description": "The classification or type of the entity."
    },
    "mythological_origin": {
      "type": "string",
      "description": "The mythology from which the entity stems."
    },
    "folklore_status": {
      "type": "string",
      "description": "Describes the entity's presence in modern folklore."
    }
  },
  "required": [
    "entity_name",
    "entity_type",
    "mythological_origin",
    "folklore_status"
  ],
  "additionalProperties": false
}
