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
German language: German ("Deutsch" ] ) is a West Germanic language that is mainly spoken in Central Europe.  It is the most widely spoken and (co-) official language in Germany, Austria, Switzerland, South Tyrol (Italy), the German-speaking Community of Belgium, and Liechtenstein.  It is also one of the three official languages of Luxembourg.  The languages which are most similar to German are the other members of the West Germanic language branch: Afrikaans, Dutch, English, the Frisian languages, Low German/Low Saxon, Luxembourgish, and Yiddish.  German is the second most widely spoken Germanic language, after English.

Old Saxon: Old Saxon, also known as Old Low German, was a Germanic language and the earliest recorded form of Low German (spoken nowadays in Northern Germany, the northeastern Netherlands, southern Denmark, the Americas and parts of Eastern Europe).  It is a West Germanic language, closely related to the Anglo-Frisian languages.  It has been documented from the 8th century until the 12th century, when it gradually evolved into Middle Low German.  It was spoken throughout modern northwestern Germany, primarily in the coastal regions and in the eastern Netherlands by Saxons, a Germanic tribe who inhabited the region of Saxony.  It partially shares Anglo-Frisian's (Old Frisian, Old English) Ingvaeonic nasal spirant law which sets it apart from Low Franconian and Irminonic languages, such as Dutch, Luxembourgish and German.

Northwest Germanic: Northwest Germanic is a proposed grouping of the Germanic languages, representing the current consensus among Germanic historical linguists.  It does not challenge the late 19th-century tri-partite division of the Germanic dialects into North Germanic, West Germanic and East Germanic, but proposes additionally that North and West Germanic (i.e. all surviving Germanic languages today) remained as a subgroup after the southward migration of the East Germanic tribes, only splitting into North and West Germanic later.  Whether this subgroup constituted a unified proto-language, or simply represents a group of dialects that remained in contact and close geographical proximity, is a matter of debate.  The date by which such a grouping must have dissolved—in that innovations ceased to be shared—is also contentious, though it seems unlikely to have persisted after 500 AD, by which time the Anglo-Saxons had migrated to England and the Elbe Germanic tribes had settled in Southern Germany.

Dutch language: Dutch (   ) is a West Germanic language that is spoken by around 24 million people as a first language—including the population of the Netherlands and about sixty percent that of Belgium—and by another 5 million as a second language.  It is the third most widely spoken Germanic language, after English and German.

Insular Celtic languages: Insular Celtic languages are a group of Celtic languages that originated in Britain and Ireland, in contrast to the Continental Celtic languages of mainland Europe and Anatolia.  All surviving Celtic languages are from the Insular Celtic group, including that which is now spoken in Continental Europe; the Continental Celtic languages are extinct.  The six Insular Celtic languages of modern times can be divided into:

Migration Period sword: The type of sword popular during the Migration Period and the Merovingian period of European history (c. 4th to 7th centuries AD), particularly among the Germanic peoples was derived from the Roman era spatha, and gave rise to the Carolingian or Viking sword type of the 8th to 10th centuries AD.

English language: English is a West Germanic language that was first spoken in early medieval England and is now a global "lingua franca".  Named after the Angles, one of the Germanic tribes that migrated to England, it ultimately derives its name from the Anglia (Angeln) peninsula in the Baltic Sea.  It is closely related to the Frisian languages, but its vocabulary has been significantly influenced by other Germanic languages, particularly Norse (a North Germanic language), as well as by Latin and Romance languages, particularly French.

History of English: English is a West Germanic language that originated from Anglo-Frisian dialects brought to Britain in the mid 5th to 7th centuries AD by Germanic invaders and settlers from what is now northwest Germany, west Denmark and the Netherlands, displacing the Celtic languages that previously predominated.

Proto-Norse language: Proto-Norse (also called Proto-Scandinavian, Primitive Norse, Proto-Nordic, Ancient Nordic, Ancient Scandinavian, Old Nordic, Old Scandinavian, Proto-North Germanic, North Proto-Germanic or Common Scandinavian) was an Indo-European language spoken in Scandinavia that is thought to have evolved as a northern dialect of Proto-Germanic in the first centuries CE.  It is the earliest stage of a characteristically North Germanic language, and the language attested in the oldest Scandinavian Elder Futhark inscriptions, spoken around from the 2nd to 8th centuries (corresponding to the late Roman Iron Age and the Germanic Iron Age).  It evolved into the dialects of Old Norse at the beginning of the Viking Age in about 800, which later themselves evolved into modern North Germanic languages.

Terttu Nevalainen: Terttu Nevalainen (born 31 May 1952, Vuolijoki) is a Finnish linguist and the current Chair of English Philology at the University of Helsinki.  She has been a Member of the Finnish Academy of Sciences since 2001 and was inducted as a First Class Knight of the Order of the White Rose of Finland in 2015.  Nevalainen works on corpus linguistics, the History of English, and historical sociolinguistics.

Question: Terttu Nevalainen, is a Finnish linguist and the current Chair of English Philology at which organization, Nevalainen works on the History of English, English is a West Germanic language that originated from Anglo-Frisian dialects brought to Britain in the mid 5th to 7th centuries AD by Germanic invaders and settlers from what is now northwest Germany, west Denmark and the Netherlands, displacing the Celtic languages that previously predominated?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "linguist_name": {
      "type": "string",
      "description": "The name of the linguist."
    },
    "organization_of_position": {
      "type": "string",
      "description": "The organization where the linguist holds their current position."
    },
    "linguist_research_focus": {
      "type": "string",
      "description": "A specific area of research the linguist works on, as mentioned in the question."
    },
    "english_language_origin_details": {
      "type": "object",
      "properties": {
        "language_family": {
          "type": "string",
          "description": "The language family English belongs to."
        },
        "origin_source": {
          "type": "string",
          "description": "The dialects from which English originated."
        },
        "arrival_period": {
          "type": "string",
          "description": "The period when these dialects were brought to Britain."
        },
        "settler_regions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Regions from which Germanic invaders and settlers came."
        },
        "displaced_languages": {
          "type": "string",
          "description": "The languages that were displaced by the arrival of English."
        }
      },
      "required": [
        "language_family",
        "origin_source",
        "arrival_period",
        "settler_regions",
        "displaced_languages"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "linguist_name",
    "organization_of_position",
    "linguist_research_focus",
    "english_language_origin_details"
  ],
  "additionalProperties": false
}
