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
Shamrock Bowl XXI: Shamrock Bowl XXI was played on July 29, 2007 at UL Sports Ground, Limerick to decide the Irish American Football League (IAFL) champion following the 2007 regular season.  This Shamrock Bowl hosted two teams from the IAFL South division, the University of Limerick Vikings and the Cork Admirals.  The Vikings won the first Shamrock Bowl title in their team history, previously losing their last two in 2002 and 2006.  This was the Cork Admirals' first Shamrock Bowl appearance.

Styphelia: Styphelia is a genus of shrubs in the heather family, Ericaceae.  The genus is endemic to Australia and the Pacific Islands.

Frank Shamrock: Frank Shamrock (born Frank Alisio Juarez, III; December 8, 1972) is an American former mixed martial artist.  Shamrock was the first to hold the UFC Middleweight Championship (later renamed the UFC Light Heavyweight Championship) and retired as the four-time defending undefeated champion.  Shamrock was the No. 1 ranked pound for pound UFC fighter in the world during his reign as the UFC Middleweight Champion.  Shamrock has won numerous titles in other martial arts organizations, including the interim King of Pancrase title, the WEC Light Heavyweight Championship and the Strikeforce Middleweight Championship.

Shamrock High School: Shamrock High School is a public high school located in Shamrock, Texas (USA) and classified as a 2A school by the UIL.  It is part of the Shamrock Independent School District located in south central Wheeler County.  In 2015, the school was rated "Met Standard" by the Texas Education Agency.

Cyathopsis: Cyathopsis is a genus of shrubs in the family Ericaceae.  The genus is endemic to New Caledonia in the Pacific and contains three species that have previously been included in "Styphelia".  It is related to genera such as "Leucopogon", "Lissanthe" and "Styphelia".

Shane Shamrock: Brian Stephen Howser (February 8, 1975 – August 18, 1998) was an American professional wrestler best known for wrestling in Maryland Championship Wrestling.  In the promotion, he was the first and only wrestler to win the Light Heavyweight Championship and was nicknamed "The Lifetime MCW Light Heavyweight Champion" in tribute to his death.  Each year, the Shane Shamrock Memorial Cup is held as a tribute to him.  Despite sharing an in-ring last name, he is not related to Ken Shamrock (who was born Kenneth Wayne Kilpatrick, although he adopted the surname "Shamrock" after his adopted father, Bob Shamrock).

Diamond Alkali: Diamond Alkali Company was an American chemical company incorporated in 1910 in West Virginia by a group of glass industry businessmen from Pittsburgh.  The company soon established as a large chemical plant at Fairport Harbor, Ohio, along with Jadeja Chemicals Inc. which would operate for over sixty years.  In 1947, the headquarters of the company was moved from Pittsburgh to Cleveland.  In 1967, Diamond Alkali and Shamrock Oil and Gas merged to form the Diamond Shamrock Corporation.  Diamond Shamrock would go on to merge with Ultramar Corporation, and the combined company, Ultramar Diamond Shamrock Corporation, would in turn be acquired by Valero Energy Corporation in 2001.

Shamrock Bowl XXV: Shamrock Bowl XXV was an American football game pitting the 6 time Shamrock Bowl champions, Dublin Rebels against university side, UL Vikings.  The game was played on July 31, 2011, at the Morton Stadium in Santry, Dublin.  The Rebels defeated the Vikings by a score of 14 - 13, earning their seventh Shamrock Bowl win.  Rebels safety Marcus Naylor was named the Shamrock Bowl MVP.  He was the second Rebels safety ever to win the award following, Brian Carter.

Shamrock: A shamrock is a young sprig of clover, used as a symbol of Ireland.  Saint Patrick, Ireland's patron saint, is said to have used it as a metaphor for the Christian Holy Trinity.  The name "shamrock" comes from Irish "seamróg " ] , which is the diminutive of the Irish word for clover ("seamair ") and means simply "little clover" or "young clover".

Shamrock Bowl: The Shamrock Bowl is the championship game of the Irish American Football League (IAFL), the highest level of American football on the island of Ireland, culminating a season that begins in March of the current calendar season.  The Shamrock Bowl uses Roman numerals to identify each game, rather than the year in which it was held.  For example, Shamrock Bowl XIII was played on August 30, 1998, following the regular season played in 1998, while Shamrock Bowl XXV was played on July 31, 2011, to determine the champion of the 2011 regular season.

Question: Are the Shamrock and Styphelia both shrubs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity mentioned in the question."
    },
    "entity_1_description": {
      "type": "string",
      "description": "A description of the first entity from the context."
    },
    "entity_1_is_shrub": {
      "type": "boolean",
      "description": "Indicates whether the first entity is identified as a shrub in the context."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity mentioned in the question."
    },
    "entity_2_description": {
      "type": "string",
      "description": "A description of the second entity from the context."
    },
    "entity_2_is_shrub": {
      "type": "boolean",
      "description": "Indicates whether the second entity is identified as a shrub in the context."
    },
    "both_are_shrubs": {
      "type": "boolean",
      "description": "The final answer to whether both entities are shrubs."
    }
  },
  "required": [
    "question_asked",
    "entity_1_name",
    "entity_1_is_shrub",
    "entity_2_name",
    "entity_2_is_shrub",
    "both_are_shrubs"
  ],
  "additionalProperties": false
}
