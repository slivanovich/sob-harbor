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
Flagellation: Flagellation (Latin "flagellum", "whip"), flogging, whipping or lashing is the act of beating the human body with special implements such as whips, lashes, rods, switches, the cat o' nine tails, the sjambok, etc.  Typically, flogging is imposed on an unwilling subject as a punishment; however, it can also be submitted to willingly, or performed on oneself, in religious or sadomasochistic contexts.

Break the World: "Break the World" is the lead single by alternative rock band Nine Lashes from their third album, "From Water to War".  It was released on October 29, 2013 by Tooth & Nail Records.  The song was the No. 1 "Billboard" Christian Rock song on January 25, 2014 chart.

Nine Lashes: Nine Lashes is an American Christian rock band from Birmingham, Alabama formed in 2006.  They independently released their first album, "Escape", in 2009 before Trevor McNevan of Thousand Foot Krutch brought them to the attention of Tooth & Nail Records.  Upon signing to the label, the band recorded their second album "World We View" and released it on February 14, 2012.  The album sold well, making several "Billboard" charts.  The band released their third album, "From Water to War" on January 21, 2014.  After a change in direction, the band released their fourth album, the Pop/Electric/Worship styled "Ascend" on March 11, 2016.

Ascend (Nine Lashes album): Ascend is the fourth studio album from Nine Lashes.  BEC Recordings are releasing the album on March 11, 2016.

Heshmat Tabarzadi: Heshmatollah Tabarzadi (Persian: حشمت‌الله طبرزدی‎ ‎ ; born March 21, 1959) is an Iranian democratic activist.  Tabarzadi has been arrested several times on charges related to his political activities, most recently in December 2009.  In October 2010, a court sentenced him to nine additional years in jail and 74 lashes, a sentence that was reduced to eight years on appeal.

Catatonia (band): Catatonia were an alternative rock band from Wales who gained popularity in the mid- to late 1990s.  The band formed in 1992 after Mark Roberts met Cerys Matthews.  The first major lineup featured Dafydd Ieuan on drums, Clancy Pegg on keyboard, Owen Powell on guitar and Paul Jones on bass.  They recorded two EPs, "For Tinkerbell" and "Hooked".

From Water to War: From Water to War is the third studio album by the American Christian rock band Nine Lashes.  The album was released on January 21, 2014, through Tooth & Nail Records.  It was produced by Jasen Rauch and Aaron Sprinkle.

Escape (Nine Lashes album): Escape is the debut studio album by the American Christian rock band Nine Lashes, released on June 5, 2009.  Recorded before the group signed to Tooth & Nail Records, the album was released through the independent record label Collide Records and produced by Travis Wyrick, and has a slightly darker sound than their second album and Tooth & Nail debut, "World We View".  While the album itself failed to chart, the songs "Words of Red" and "Word of Advice" made "Billboard"' s Christian rock chart.

Travis Wyrick: Travis Wyrick is a music producer and owner of Lakeside Studios in Knoxville, Tennessee.  He is particularly known for his work with bands such as P.O.D., Pillar, 10 Years, Nine Lashes, and Disciple, and artists such as TobyMac and Dolly Parton.  Throughout his career, he has produced over 30 No. 1 radio singles.  Prior to becoming a producer, Wyrick was lead guitarist with the band Sage.  In 1998, he released the industrial rock album "Mental Floss" under the mononym Wyrick.  Two years later, he released "Aggressive State..." as the project's sophomore effort.

World We View: World We View is the second studio album by the American Christian rock band Nine Lashes, released on February 14, 2012 through Tooth & Nail Records.  It is the follow-up to their independent debut album "Escape" and was co-produced by Aaron Sprinkle and Trevor McNevan, the latter of whom was instrumental in getting the group signed and contributes guest vocals to the song "Adrenaline".

Question:  Catatonia and Nine Lashes are both examples of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_names": {
      "type": "array",
      "description": "The names of the entities being compared.",
      "items": {
        "type": "string"
      }
    },
    "shared_category": {
      "type": "string",
      "description": "The common category or type that both entities belong to."
    },
    "entity_details": {
      "type": "array",
      "description": "Specific details for each entity related to their category.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "genre": {
            "type": "string",
            "description": "The specific genre of the entity."
          },
          "origin": {
            "type": "string",
            "description": "The geographical origin of the entity."
          }
        },
        "required": [
          "name",
          "genre",
          "origin"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "entity_names",
    "shared_category",
    "entity_details"
  ],
  "additionalProperties": false
}
