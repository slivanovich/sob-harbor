{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBattle of Argoed Llwyfain: The Battle of Argoed Llwyfain was fought between the forces of the Kingdom of Rheged under the command of Urien and Owain mab Urien and the forces of the Kingdom of Bernicia under \"Fflamddwyn\" (Firestealer or Flamebearer).\n\nYwain: Sir Ywain , also called Owain, Yvain, Ewain or Uwain, is a Knight of the Round Table and the son of King Urien and Morgan le Fay in Arthurian legend.  The historical Owain mab Urien, on whom the literary character is based, was the king of Rheged in Great Britain during the late 6th century.\n\nOwain ap Dyfnwal (died 1015): Owain ap Dyfnwal (died 1015) may have been an eleventh-century ruler of the Kingdom of Strathclyde.  He seems to have been a son of Dyfnwal ab Owain, King of Strathclyde, and may well have succeeded Dyfnwal's son, Máel Coluim, King of Strathclyde.  During Owain's reign, he would have faced a massive invasion by Æthelræd II, King of the English.  Owain's death is recorded in 1015, and seems to have been succeeded by Owain Foel, a man who may have been his nephew.\n\nPictish language: Pictish is the extinct language, or dialect, spoken by the Picts, the people of eastern and northern Scotland from the late Iron Age to the Early Middle Ages.  There is virtually no direct attestation of Pictish, short of a limited number of geographical and personal names found on monuments and the contemporary records in the area controlled by the Kingdom of the Picts.  Such evidence, however, points to the language being closely related to the Brittonic language spoken prior to Anglo-Saxon settlement in what is now southern Scotland, England and Wales.  A minority view held by a few scholars claims that Pictish was at least partially non-Indo-European or that a non-Indo-European and Brittonic language coexisted.\n\nUrien: Urien , often referred to as Urien Rheged or Uriens, was a late 6th-century king of Rheged, an early British kingdom of the \"Hen Ogledd\" (northern England and southern Scotland).  His power and his victories, including the battles of Gwen Ystrad and Alt Clut Ford, are celebrated in the praise poems to him by Taliesin, preserved in the \"Book of Taliesin\".  He became the \"King Urien of Gorre\" of later Arthurian legend and his son Owain mab Urien was later known as Ywain.\n\nOwain Gwynedd: Owain ap Gruffudd (c. 1100   23 or 28 November 1170) was King of Gwynedd, North Wales, from 1137 until his death in 1170, succeeding his father Gruffudd ap Cynan.  He was called \"Owain the Great\" (Welsh: \"Owain Mawr\") and the first to be styled \"Prince of Wales\".  He is considered to be the most successful of all the North Welsh princes prior to his grandson, Llywelyn the Great.  He became known as Owain Gwynedd (Middle Welsh: \"Owain Gwyned\" , \"Owain of Gwynedd\") to distinguish him from the contemporary king of Powys Wenwynwyn, Owain ap Gruffydd ap Maredudd, who became known as Owain Cyfeiliog.\n\nOwain mab Urien: Owain mab Urien (or Owein) (died c. 595) was the son of Urien, king of Rheged c. 590, and fought with his father against the Angles of Bernicia.  The historical figure of Owain became incorporated into the Arthurian cycle of legends where he is also known as Ywain, Yvain, Ewain or Uwain.  In his legendary guise he is the main character in Chrétien de Troyes's \"Yvain, the Knight of the Lion\" and the Welsh Romance \"Owain, or the Lady of the Fountain\", which corresponds to Chrétien's poem.\n\nOwain Foel: Owain Foel (fl.  1018), also known as Owen the Bald, and Eugenius Calvus, was an eleventh-century King of Strathclyde.  He may have been a son of Máel Coluim, son of Dyfnwal ab Owain, two other rulers of the Kingdom of Strathclyde.  Owain Foel is recorded to have supported the Scots at the Battle of Carham in 1018.  Although it is possible that he died in the conflict, no source states as much, and it is uncertain when he died.  Owain Foel may be an ancestor—perhaps the father—of a certain Máel Coluim who is described as the \"son of the king of the Cumbrians\" in the 1050s.\n\nRheged: Rheged (] ) was one of the kingdoms of the \"Hen Ogledd\" (\"Old North\"), the Brittonic-speaking region of what is now Northern England and southern Scotland, during the post-Roman era and Early Middle Ages.  It is recorded in several poetic and bardic sources, although its borders are not described in any of them.  Some modern scholars have suggested that it included what is now Cumbria in North West England and possibly extended into Lancashire and Scotland.  In some sources, Rheged is intimately associated with the king Urien Rheged and his family.  Its inhabitants spoke Cumbric, a Brittonic dialect closely related to Old Welsh.\n\nCadfan ap Cadwaladr: Cadfan ap Cadwaladr, Lord of Ceredigion (c. 1140 - c. 1215) was the elder son of Cadwaladr ap Gruffydd, the brother of Owain Gwynedd, King of Gwynedd and overlord of all Wales.  His mother was his father's first wife, Gwerfel ferch Gwrgan.  He was probably born in Ceredigion, where his father held extensive estates.  His father was banished in 1144.  He should not be confused with Cadell ap Gruffydd, King of Deheubarth, who took Ceredigion from Hywel ab Owain Gwynedd, son of Owain Gwynedd, in 1150.  Cadfan probably spent the rest of his life in exile in England.  He married Gwenllian, a daughter of Owain Cyfeiliog.  He is known to have had only one daughter: Tangwystl ferch Cadfan (born c. 1212).\n\nQuestion: What Brittonic dialect was spoken in the kingdom who had the father of Owain mab Urien as king?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"kingdom_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the kingdom.\"\n    },\n    \"king_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the king who was the father of Owain mab Urien.\"\n    },\n    \"king_reign_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period during which the king reigned.\"\n    },\n    \"brittonic_dialect_spoken\": {\n      \"type\": \"string\",\n      \"description\": \"The Brittonic dialect spoken in the identified kingdom.\"\n    }\n  },\n  \"required\": [\n    \"kingdom_name\",\n    \"king_name\",\n    \"king_reign_period\",\n    \"brittonic_dialect_spoken\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "kingdom_name": {
        "type": "string",
        "description": "The name of the kingdom."
      },
      "king_name": {
        "type": "string",
        "description": "The name of the king who was the father of Owain mab Urien."
      },
      "king_reign_period": {
        "type": "string",
        "description": "The period during which the king reigned."
      },
      "brittonic_dialect_spoken": {
        "type": "string",
        "description": "The Brittonic dialect spoken in the identified kingdom."
      }
    },
    "required": [
      "kingdom_name",
      "king_name",
      "king_reign_period",
      "brittonic_dialect_spoken"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
