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
John Tuggle: John Davis Tuggle (January 13, 1961August 30, 1986) was a running back in the National Football League.  Tuggle was the last selection of the 1983 NFL Draft, selected by the New York Giants.  The nickname given to the last player selected in the draft is "Mr. Irrelevant."  He played that season with the team.  He would go on to be awarded the New York Giants Special Teams Player of the Year that season.

Maximiliano Bajter: Maximiliano 'Pipi' Bajter Ugollini (born 1 March 1986 in Montevideo) is a Uruguayan football player currently playing for colombian club Deportivo Pereira.  He is also known as "Pipi", or "Pitón", nickname given to him by his former coach at Peñarol, Julio Ribas, since he consider "Pipi" "was not a proper nickname for a gladiator"

Molly Pitcher: Molly Pitcher was a nickname given to a woman said to have fought in the American Battle of Monmouth, who is generally believed to have been Mary Ludwig Hays.  Since various Molly Pitcher tales grew in the telling, many historians regard Molly Pitcher as folklore rather than history, or suggest that Molly Pitcher may be a composite image inspired by the actions of a number of real women.  The name itself may have originated as a nickname given to women who carried water to men on the battlefield during War.

Miley (given name): Miley is a feminine given name.  It was the 278th most popular name given to baby girls born in the United States in 2007, the first year that the name or any of its variants appeared in the top 1,000 names given to baby girls, and rose to 128th in popularity in 2008, though it dropped back down to 189th place in 2009 and to 217th place in 2010.  Its popularity is attributed to the fame of actor, singer and songwriter Miley Ray Cyrus (born Destiny Hope Cyrus), whose name originated as a childhood nickname given to her by her father because she was so "smiley."  Cyrus played Miley Stewart on her sitcom "Hannah Montana".

Mitsos: Mitsos, or Mitso, is a popular Greek nickname given to males named Dimitri, Dimitrios or Jim.  This nickname is used especially when referring to manly individuals having the aforementioned names.

Christopher Boykin: Christopher "Big Black" Boykin (January 13, 1972 – May 9, 2017) was an American television personality and musician best known for his role on MTV's "Rob & Big", which followed him and his co-star, skateboarder Rob Dyrdek.

Reshawn Davis: Reshawn "Bam Bam" Davis (born August 3, 1978) is a professional bodyguard, but is best known for his role on MTV's "Rob & Big", which followed him and his co-star/best friend Christopher Boykin.

Brat Pack (actors): The Brat Pack is a nickname given to a group of young actors who frequently appeared together in teen-oriented in the 1980s.  First mentioned in a 1985 "New York" magazine article, it is now usually defined as the cast members of two specific films released in 1985—"The Breakfast Club" and "St. Elmo's Fire"—although other actors are sometimes included.  The "core" members are considered to be Emilio Estevez, Anthony Michael Hall, Rob Lowe, Andrew McCarthy, Demi Moore, Judd Nelson, Molly Ringwald, and Ally Sheedy.

Yosemite Sam (shortwave): Yosemite Sam is the nickname given by DXers to a number station that first surfaced on December 19, 2004.  It transmits on several shortwave frequencies in dual side band: 3700 kHz, 4300 kHz, 6500 kHz, and 10500 kHz.  The nickname is taken from the Looney Tunes character Yosemite Sam, whose voice is played as part of the unusual transmission.

Little Foot: "Little Foot" (Stw 573) is the nickname given to a nearly complete Australopithecus fossil skeleton found in 1994–1998 in the cave system of Sterkfontein, South Africa.  [1] The fossils were found in a limestone formation in Sterkfontein.  The nickname "little foot" was given to the fossil in 1995.  From the structure of the four ankle bones they were able to ascertain that the owner was able to walk upright.  The recovery of the bones proved extremely difficult and tedious, because they are completely embedded in concrete-like rock.  It is due to this that the recovery and excavation of the site took around 15 years to complete.

Question: What was the nickname given to Reshawn Davis's co-star on "Rob & Big"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "relationship_to_reshawn_davis": {
          "type": "string",
          "description": "The relationship of this person to Reshawn Davis."
        }
      },
      "required": [
        "name",
        "relationship_to_reshawn_davis"
      ],
      "additionalProperties": false
    },
    "show_name": {
      "type": "string",
      "description": "The name of the television show they co-starred in."
    },
    "nickname": {
      "type": "string",
      "description": "The nickname given to the person of interest."
    }
  },
  "required": [
    "person_of_interest",
    "show_name",
    "nickname"
  ],
  "additionalProperties": false
}
