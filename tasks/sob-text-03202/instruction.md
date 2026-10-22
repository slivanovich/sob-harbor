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
Godwin, Earl of Wessex: Godwin of Wessex (Old English: "Godƿin" ; 100115 April 1053) was one of the most powerful earls in England under the Danish king Cnut the Great and his successors.  Cnut made him the first Earl of Wessex.  Godwin was the father of King Harold Godwinson and Edith of Wessex, wife of King Edward the Confessor.

Gytha Thorkelsdóttir: Gytha Thorkelsdóttir (Old English: "Gȳða Þorkelsdōttir" , 997 – c. 1069), also called Githa, was a Danish noblewoman.  She was the mother of King Harold Godwinson and of Edith of Wessex, queen consort of King Edward the Confessor of England.

Leofwine Godwinson: Leofwine Godwinson (c. 1035 – 14 October 1066) was a younger brother of King Harold Godwinson, the fifth son of Earl Godwin.

Gyrth Godwinson: Gyrth Godwinson (Old English: Gyrð Godƿinson) ( 1032 – 14 October 1066) was the fourth son of Earl Godwin, and thus a younger brother of Harold Godwinson.  He went with his eldest brother Swegen into exile to Flanders in 1051, but unlike Swegen he was able to return with the rest of the clan the following year.  Along with his brothers Harold and Tostig, Gyrth was present at his father's death-bed.

Edith the Fair: Edith the Fair (Old English: "Ealdgȳð Swann hnesce" , "Edyth the Gentle Swan"; c. 1025 – c. 1086), also known as Edith Swanneck, was the first wife of King Harold Godwinson.  "Swanneck" (or Swan-Neck) comes from the folk etymology which made her in Old English as "swann hnecca", "swan neck", which was actually most likely a corrupted form of "swann hnesce, ""Gentle Swan"" ".  She is sometimes confused with Ealdgyth, daughter of Earl Ælfgar of Mercia, who was queen during Harold's reign.

Battle of Stamford Bridge: The Battle of Stamford Bridge took place at the village of Stamford Bridge, East Riding of Yorkshire, in England on 25 September 1066, between an English army under King Harold Godwinson and an invading Norwegian force led by King Harald Hardrada and the English king's brother Tostig Godwinson.  After a bloody battle, both Hardrada and Tostig along with most of the Norwegians were killed.  Although Harold Godwinson repelled the Norwegian invaders, his army was defeated by the Normans at Hastings less than three weeks later.  The battle has traditionally been presented as symbolising the end of the Viking Age, although major Scandinavian campaigns in Britain and Ireland occurred in the following decades, such as those of King Sweyn Estrithson of Denmark in 1069–1070 and King Magnus Barefoot of Norway in 1098 and 1102–1103.

Cultural depictions of Harold Godwinson: Fictional accounts based on the events surrounding Harold Godwinson's brief reign as king of England have been published, notably the play "Harold", by Alfred, Lord Tennyson, in 1876; and the novel "Last of the Saxon Kings", by Edward Bulwer-Lytton, in 1848.  Rudyard Kipling wrote a short story, included in his 1910 collection, "Rewards and Fairies", where an aged King Harold meets Henry I and dies in the arms of a Saxon knight.

Edith Walks: Edith Walks is a 2017 documentary film directed by Andrew Kötting which imagines a journey by Edith the Fair, wife of English king Harold Godwinson, from Waltham Abbey where he is buried to near the site of the Battle of Hastings and the invasion of England by William the Conqueror in 1066.  It includes contributions from the writers Alan Moore and Iain Sinclair, the torch singer Claudia Barton, and the musician Jem Finer.

Edith Weston: Edith Weston is a village and civil parish in the county of Rutland in the East Midlands of England.  The population of the civil parish was 1,042 at the 2001 census, including Normanton and increasing to 1,359 at the 2011 census.  It is on the south-eastern shore of Rutland Water and is home of the main sailing club and a fishing lodge.  The village is named after Edith of Wessex (1029–1075), the queen of Edward the Confessor and sister of Harold Godwinson.

Tostig Godwinson: Tostig Godwinson ( 1026 – 25 September 1066) was an Anglo-Saxon Earl of Northumbria and brother of King Harold Godwinson.  After being exiled by his brother, Tostig supported the Norwegian king Harald Hardrada's invasion of England, and was killed at the Battle of Stamford Bridge.

Question: Which wife of Harold Godwinson was the subject of the film Edith Walks? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "subject_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who is the subject of the film."
        },
        "relationship_to_harold_godwinson": {
          "type": "string",
          "description": "The relationship of the subject person to Harold Godwinson."
        },
        "other_known_names": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other names or epithets by which the subject person is known."
        }
      },
      "required": [
        "name",
        "relationship_to_harold_godwinson"
      ],
      "additionalProperties": false
    },
    "harold_godwinson_role": {
      "type": "string",
      "description": "The role or title of Harold Godwinson mentioned in relation to the subject."
    }
  },
  "required": [
    "film_title",
    "subject_person",
    "harold_godwinson_role"
  ],
  "additionalProperties": false
}
