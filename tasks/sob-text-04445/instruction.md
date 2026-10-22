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
Mariano Lazcano: Mariano Lazcano or Lescano (c.1770–1840s) was an Argentine politician, notary and accountant of the Aduana of Buenos Aires.  He had outstanding performance as a government official during the Viceroyalty of Rio de la Plata, serving in the Real Aduana of Buenos Aires, presided by Justo Pastor Lynch.

Kevin Crawford: Kevin Crawford (born 6 December 1967 in Birmingham, England) is an English flute, tin whistle, Low whistle and bodhrán player.  He was born in England to Irish emigrant parents from Milltown Malbay, County Clare.  He later moved to West Clare to improve his music and become more exposed to traditional Irish music.

Mary from Dungloe (festival): The Mary From Dungloe International Festival is a popular Irish music festival held annually, usually at the end of July in the small town of Dungloe, County Donegal.  The festival is centred on a pageant to find out which contestant has the spirit of the festival, who is then crowned "Mary From Dungloe".  The winner of the contest holds this title for a year and acts as an ambassador for the festival.  Irish emigrant communities from around the world as well as some Irish counties and towns participate by nominating a young woman, endearingly titled a "Mary", to represent their community at the contest.  The festival has grown in popularity over the years and now regularly attracts tens of thousands of visitors to the area.  The festival is inspired by the song "Mary from Dungloe" as the Rose of Tralee festival is by "The Rose of Tralee".  2016 seen the festival celebrate it's 49th anniversary, building huge anticipation for the 50th anniversary in 2017 to be the most successful festival to date.

Estanislao Lynch: Estanislao José Antonio Lynch y Roo, was a naval officer and wealthy Argentine, the brother of the famous landowner of the "Rio de la Plata" captain Patricio Lynch and the grandson of an Irish immigrant, also Patrick Lynch.  Estanislao was the third son of Justo Pastor Lynch (1755–1830) and Ana Bernardo Roo (d.1836).

Justo Almario: Justo Pastor Almario Gómez (born 18 February 1949) is a Colombian-born, Los Angeles-based flutist, saxophonist and Latin jazz group leader.  He was among several Colombian musicians recruited by Mongo Santamaria for his band in the 1970s, notably on the album, "Afro–Indio" (1975).

Justo Pastor Lynch: Justo Pastor Lynch (1755–1830), an Argentine landowner, was born in Buenos Aires on the family ""estancia"", a ranch by the River de la Plata.  He was the eldest surviving son of Patrick Lynch of Lydican Castle in Claregalway Ireland, and Rosa de Galaya de la Camera.  At times his name was recorded as Pastorin or Pastorino Lynch in reference to the large landowned by his family dedicated to horses.

Justo Jacquet: Justo Pastor Jacquet Muñoz (born 9 September 1961 in Asunción) is a retired football (soccer) defender from Paraguay, who played as a left back during his career.  He played professional football for Cerro Porteño in Paraguay and also had spells in Argentina, Brazil and Peru.

The Irish Emigrant: The Irish Emigrant was a weekly Irish emigrant newspaper published electronically from 1987 to 2012.

Neck (band): Neck is a six-piece London-Irish Celtic punk band from the North London neighbourhood of 'County Holloway' (known informally thus due to its Irish population).  Following Leeson O'Keeffe's cathartic 'Tour of Duty' as a former member of Shane MacGowan and the Popes, Neck were formed during late-night drinking sessions (known colloquially as being 'born in a bottle') in 1994 by a mixture of Irish emigrant and second-generation Irish drinking buddies.  The band takes their lead, both musically and ideologically, from two other London bands: The Clash and The Pogues, blending the electric energy of punk rock with the swirl of traditional Irish music, to play a London-Irish style known as 'Psycho-Ceilídh'.

Patrick Lynch (Argentina): Patrick Lynch (born 1715, date of death unknown) was an Irish emigrant who became a significant landowner in Rio de la Plata, which is now part of Argentina.  He was born in Galway and was the second son of Captain Patrick Lynch of Lydycan Lydican Castle and Agnes Blake.  The Lynches and the Blakes were two of the fourteen tribes of Galway, who dominated the political, commercial, and social life of the city of Galway in western Ireland between the mid-13th and late-19th centuries.  The Lynches had been leaving Ireland since their defeat at the hands of Cromwell's forces and later those of William of Orange, Patrick left in the 1740s for Bilbao, Spain, and travelled from there to Rio de la Plata, where he settled and was a "regidor" (royal representative ) and captain in the "Milicias".  In 1749, in Buenos Aires, he married Rosa de Galayn y de la Camara, a wealthy heiress.  He was successful enough to pass on substantial lands to his eldest surviving son, Justo Pastor Lynch who was a customs official under Viceroy Cisneros, also a captain and regidor.  He was confirmed in his post by the revolutionary government on account of his well-known probity.

Question: What Irish emigrant was the father of Justo Pastor Lynch? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person whose father is being identified."
        },
        "role": {
          "type": "string",
          "description": "The role of the person of interest in the relationship (e.g., 'son')."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "father_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the father."
        },
        "is_irish_emigrant": {
          "type": "boolean",
          "description": "Indicates if the father was an Irish emigrant."
        },
        "birth_place": {
          "type": "string",
          "description": "The birth place of the father."
        },
        "settlement_location": {
          "type": "string",
          "description": "The location where the father settled as an emigrant."
        }
      },
      "required": [
        "name",
        "is_irish_emigrant",
        "birth_place",
        "settlement_location"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of the relationship between the father and the person of interest."
    }
  },
  "required": [
    "person_of_interest",
    "father_details",
    "relationship_description"
  ],
  "additionalProperties": false
}
