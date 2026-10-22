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
Cethlenn: In Irish mythology, Cethlenn (Old Irish), Cethleann (Modern Irish, or Cethlenn of the Crooked Teeth) was the wife of Balor of the Fomorians and, by him, the mother of Ethniu.  She was also a prophetess and warned Balor of his impending defeat by the Tuatha Dé Danann in the second battle of Magh Tuiredh.  During that battle she wounded the Dagda.

Kjartan: Kjartan (] ; ] ) is a masculine given name found in the Nordic countries, and is most prominently in Iceland and Norway.  The Old Norse name "Kjartan " was a shortening of "Mýrkjartan ", from Old Irish: "Muirchertach" , the name of an Irish king whose daughter Melkorka (Old Irish "Mael Curcaigh ", "servant of Curcach") was brought to Iceland as a slave.  The Irish name Muirchertach, meaning "mariner", is modernised to "Muircheartach ", anglicised as Murtagh.

Old Irish: Old Irish (Old Irish: "Goídelc" ; Irish: "Sean-Ghaeilge" ; Scottish Gaelic: "Seann Ghàidhlig" ; Manx: "Shenn Yernish" ; sometimes called Old Gaelic) is the name given to the oldest form of the Goidelic languages for which extensive written texts are extant.  It was used from 600 to 900.  The primary contemporary texts are dated 700–850; by 900 the language had already transitioned into early Middle Irish.  Some Old Irish texts date from the 10th century, although these are presumably copies of texts composed at an earlier time period.  Old Irish is thus the ancestor of Modern Irish, Manx, and Scottish Gaelic.

Kevin: Kevin ( ) is the anglicized form of the Irish masculine given name Caoimhín (] , Middle Irish: "Caoimhghín" ] , Old Irish: "Cóemgein" ] , latinized "Coemgenus"), composed of Irish "" (Old Irish "cóem") "dear; noble" and "-gin" (Old Irish "gein") "birth".

Uraicecht Becc: Uraicecht Becc (Old Irish for "Small Primer"; "uraicecht" is a variant of "airaiccecht" ["air"- 'before' + "aiccecht" 'instruction,' from Latin "acceptum"], 'primer') is an Old Irish legal tract on status.  Of all status tracts, it has the greatest breadth in coverage, including not only commoners, kings, churchmen and poets, but also a variety of other professional groups, including judges.  However, it does not go into as much detail for each group and level as do other status tracts.  T.M. Charles-Edwards suggests that it is "almost certainly of Munster origin", as it asserts the supremacy of the king of Munster above other Irish kings and makes reference to the monasteries of Emly and Cork.

Creidhne: In Irish mythology, Credne (Old Irish) or Creidhne (Modern Irish – pronounced "creynya") was a son of Brigid and Tuireann and the goldsmith of the Tuatha Dé Danann, but he also worked with bronze and brass.  He and his brothers Goibniu and Luchtaine were known as the "Trí Dée Dána", the three gods of art, who forged the weapons which the Tuatha Dé used to battle the Fomorians.

Fomorians: The Fomorians (Old Irish: Fomoire , Modern Irish: Fomhóraigh ) are a supernatural race in Irish mythology.  They are often portrayed as hostile and monstrous beings who come from the sea or underground.  Later, they were portrayed as giants and sea raiders.  They are enemies of Ireland's first settlers and opponents of the Tuatha Dé Danann, the other supernatural race in Irish mythology.  However, their relationship with the Tuath Dé is complex and some of their members intermarry and have children.  The Fomorians have thus been likened to the jötnar of Norse mythology.

John Strachan (linguist): John Strachan (1862–1907) was a scholar of Sanskrit, Ancient Greek and the Celtic languages.  He was a professor at Owens College and the Victoria University of Manchester.  He is best remembered for the "Thesaurus Palaeohibernicus", a collection of material in Old Irish that he edited together with Whitley Stokes, and for the textbook "Old Irish Paradigms and Selections from the Old Irish Glosses", first published in 1904–05 and later revised by Osborn Bergin.  Both of these works are still in print.

Conn (name): Conn is a masculine English- and Irish-language given name, as well as an English-language surname.  The origin of the given name is uncertain.  It may be related to the Old Irish "cond" ("intellect" or "mind"), or perhaps to the Old Irish "cenn" ("head", "chief").  The latter word-origin may have resulted from a popular, but incorrect etymology, applied to the Old Irish terms "Leth Cuinn" and "Dál Cuinn"; these terms originally meant "half of the chief" and "tribe of the chief" but were mistakenly regarded to mean "half of "Conn"" and "tribe of "Conn"".  In some cases the given name is as a short form of non Irish-language names that begin with the first syllable "Con-" (such as the names "Conor" and "Connor").

Balor: In Irish mythology, Balor (modern spelling: Balar) was king of named Fomorians, a group of supernatural beings.  He is often described as a giant with a large eye in his forehead that wreaks destruction when opened.  He has been interpreted as a god or personification of drought and blight.

Question: What is the relation between Cethlenn (Old Irish) and the king of named Fomorians who is a interpreted as a god?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "language_origin": {
          "type": "string",
          "description": "The language origin of the name."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Roles or titles held by the person."
        }
      },
      "required": [
        "name",
        "language_origin",
        "roles"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "title": {
          "type": "string",
          "description": "The title of the second person."
        },
        "associated_group": {
          "type": "string",
          "description": "The group the second person is associated with."
        },
        "divine_interpretation": {
          "type": "string",
          "description": "How the second person is interpreted divinely."
        }
      },
      "required": [
        "name",
        "title",
        "associated_group",
        "divine_interpretation"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of relationship between the two persons."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the relationship."
        }
      },
      "required": [
        "type",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_1",
    "person_2",
    "relationship"
  ],
  "additionalProperties": false
}
