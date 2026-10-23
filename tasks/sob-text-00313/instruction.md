{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCarvetii: The Carvetii were an Iron Age people and were subsequently identified as a \"civitas\" (canton) of Roman Britain living in what is now Cumbria, in North-West England.\n\nMushki: The Mushki were an Iron Age people of Anatolia who appear in sources from Assyria but not from the Hittites.  Several authors have connected them with the Moschoi (Μόσχοι) of Greek sources and the Georgian tribe of the Meskhi.  Josephus Flavius identified the \"Moschoi\" with the Biblical Meshech.  Two different groups are called \"Muški\" in Assyrian sources (Diakonoff 1984:115), one from the 12th to the 9th centuries near the confluence of the Arsanias and the Euphrates (\"Eastern Mushki\") and the other from the 8th to the 7th centuries in Cappadocia and Cilicia (\"Western Mushki\").  Assyrian sources identify the Western Mushki with the Phrygians, but Greek sources clearly distinguish between the Phrygians and the Moschoi.\n\nParisii (Gaul): The Parisii were Celtic Iron Age people who lived on the banks of the river Seine (in \"Latin\", \"Sequana\") in Gaul from the middle of the third century BC until the Roman era.  With the Suessiones, the Parisii participated in the general rising of Vercingetorix against Julius Caesar in 52 BC.  Before the Roman period the Parisii had their own gold coinage.\n\nTelmessos (Caria): Telmessos or Telmessus, also Telmissos (Ancient Greek: Τελμησσός or Τελμισσός), was a city in Caria.  It was called Telebehi in the Lycian language.\n\nBurry Holms: Burry Holms (grid reference [ SS403926] ) (Welsh: Ynys Ianwol) is a small tidal island located at the northern end of the Gower Peninsula, Wales.  9,000 years ago it was up to 12 miles (19 km) away from the sea and inhabited by nomadic Mesolithic hunters. Flint tools provided the first evidence of their existence in 1919, since when charcoal, charred hazelnut shells, and tools made out of wood and bone have also been found.  A 1998 excavation by the National Museums and Galleries of Wales found that Burry Holms was used as a Mesolithic seasonal camp.  Iron Age people subsequently built a 5 acre hillfort and ditch on the island, while in Medieval times it was home to a monastery.\n\nBronze- and Iron-Age Poland: The Bronze and Iron Age cultures in Poland are known mainly from archeological research.  Early Bronze Age cultures in Poland begun around 2300–2400 BCE, while the Iron Age commenced in approximately 700–750 BCE.  The Iron Age archeological cultures no longer existed by the start of the Common Era.  The subject of the ethnicity and linguistic affiliation of the groups living in central and eastern Europe at that time is, given the absence of written records, speculative, and accordingly there is considerable disagreement.  In Poland the Lusatian culture, spanning both the Bronze and Iron Ages, became particularly prominent.  The most famous archeological finding from that period is the Biskupin fortified settlement (gord) on the lake from which it takes its name, representing the Lusatian culture of the early Iron Age.\n\nLycian language: The Lycian language (𐊗𐊕𐊐𐊎𐊆𐊍𐊆 \"Trm̃mili\" ) was the language of the ancient <a href=\"Lycians\">Lycians the region known as <a href=\"Lycia\">Lycia</a> in <a href=\"Anatolia\">Anatolia</a> (present day <a href=\"Turkey\">Turkey</a>), during the <a href=\"Iron%20Age\">Iron Age</a>.\n\nSamad al-Shan: Samad al-Shan (22°48'N; 58°09'E) is an archaeological site in the Sharqiyah province, Oman where Late Iron Age remains were first identified, hence the Samad Period or assemblage.  The site was discovered by archaeological surveyors from Harvard University (1971).  It is located 2 km east of the village of al-Maysar (since c. 1995 al-Moyassar).  The excavation of this site (1981-1982) by Burkhard Vogt, Gerd Weisgerber and Paul Yule, (1987-1998) of the German Mining Museum, Bochum and later University of Heidelberg documented some 260 graves which span the Bronze Age to Late Iron Age in the Sultanate of Oman.  Samad is the type-site for the non-writing Late Iron Age of Central Oman in south-eastern Arabia.  This cultural assemblage evidences protoscript in the form of characters scratched onto pottery vessels.  It is preceded by the Early Iron Age which differs in terms of pottery from that distributed in the neighbouring present-day United Arab Emirates.\n\nBritish Iron Age: The British Iron Age is a conventional name used in the archaeology of Great Britain, referring to the prehistoric and protohistoric phases of the Iron Age culture of the main island and the smaller islands, typically excluding prehistoric Ireland, which had an independent Iron Age culture of its own.  The parallel phase of Irish archaeology is termed the Irish Iron Age.\n\nCeltic polytheism: Celtic polytheism, commonly known as Celtic paganism, comprises the religious beliefs and practices adhered to by the Iron Age people of Western Europe now known as the Celts, roughly between 500 BCE and 500 CE, spanning the La Tène period and the Roman era, and in the case of the Insular Celts the British and Irish Iron Age.\n\nQuestion: The city of Telmessos was called Telebehi by what Iron Age people?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The original name of the city.\"\n    },\n    \"alternative_city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name used by the specific Iron Age people for the city.\"\n    },\n    \"iron_age_people\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Iron Age people who used the alternative name.\"\n    },\n    \"era\": {\n      \"type\": \"string\",\n      \"description\": \"The historical period during which these people lived.\"\n    }\n  },\n  \"required\": [\n    \"city_name\",\n    \"alternative_city_name\",\n    \"iron_age_people\",\n    \"era\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_name": {
        "type": "string",
        "description": "The original name of the city."
      },
      "alternative_city_name": {
        "type": "string",
        "description": "The name used by the specific Iron Age people for the city."
      },
      "iron_age_people": {
        "type": "string",
        "description": "The name of the Iron Age people who used the alternative name."
      },
      "era": {
        "type": "string",
        "description": "The historical period during which these people lived."
      }
    },
    "required": [
      "city_name",
      "alternative_city_name",
      "iron_age_people",
      "era"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
