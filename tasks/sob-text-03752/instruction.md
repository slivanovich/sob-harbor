{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEduardo Naranjo: Eduardo Naranjo is a celebrated Spanish painter, born in 1944 in Monesterio, in the province of Badajoz, Extremadura, Spain.  His work is considered part of the 'Neo -Realism' trend of Spanish art.\n\nBejean: Bejean (ビージーン , Bijin ) is a Japanese monthly men's magazine which originally started publication under the name Beppin (ベッピン , Beppin ) .  It has been described as \"probably the best selling men's magazine\" in Japan and was called by J-List \"One of the cornerstones of Japanese AV magazines.\"  As with its sister publication \"Video Boy\", the magazine specializes in nude photo sets of present and aspiring Japanese AV Idols.\n\nBurg Kreuzenstein: Burg Kreuzenstein is a castle near Leobendorf in Lower Austria, Austria.  Burg Kreuzenstein is 265 m above sea level.  It was constructed on the remains of an early medieval castle that had fallen into disrepair and was then demolished during the Thirty Years' War.  Intended to be a family vault for the Wilczek family, it was rebuilt in the 19th century by Count Nepomuk Wilczek with money from the family's large Silesian coal mines.  Kreuzenstein is interesting in that it was constructed out of sections of medieval structures purchased by the family from all over Europe to form an authentic-looking castle.  Thus, the castle can be considered both a 'neo-' and 'original' medieval structure.\n\nTime Out (magazine): Time Out is British travel magazine published by Time Out Group.  \"Time Out\" started its publication in 1968 and has expanded its editorial recommendations to 108 cities worldwide.\n\nCrew (comics): Crew, the first regular Czech international comic magazine, started publication in 1997.  It was meant to be published every two months, but it started having long breaks after the first year.  Officially publication ended in 2003 with \"Crew 21\".\n\nAijaz Siddiqi: Aijaz (Urdu: ‎ ) Siddiqi (1911–1978) was a Urdu writer and poet.  He was the son of the famous Urdu poet, Seemab Akbarabadi.  He was born in Agra, Uttar Pradesh.  After having founded \"Qasr-ul-Adab\" in 1923, Seemab Akbarabadi had in the year 1930 started publication of a literary journal in Urdu from Agra titled Shair; he was its first editor.  A few years later i.e. in 1935, in order to concentrate on the other than more important activities of \"Qasr-ul- Adab\", he had handed over the charge of this magazine to Aijaz Siddiqi who carrying forward the tradition of his father remained its editor till 1978 long after the publication of Shair was shifted from Agra to Mumbai in 1947 and Seemab Akbarabadi had in 1951 died in Karachi.  Mahendra Nath, the Urdu short-story writer and younger brother of Krishan Chander had also joined him to compile and edit several special issues of Shair.\n\nBean Pole: Bean Pole, established in 1989, is a South Korean fashion brand owned by Samsung’s Cheil Industries.  It produces ‘neo traditional’ family fashion (Bean Pole Men, Bean Pole Ladies, and Bean Pole Kids); as well as accessories (Bean Pole Accessory), golf wear (Bean Pole Golf), and outdoors fashion/equipment (Bean Pole Outdoor).  Towards the end of 2012 they added the ‘Bike Repair Shop’ to their list of sub-brands.\n\nGSZ Stadium: GSZ Stadium or Gymnastic Club Zenon Stadium (Greek: Γυμναστικός Σύλλογος Ζήνων ; Γ.Σ.Ζ.)  is a multi-purpose stadium in Larnaca, Cyprus.  Usually it is referred to as the 'neo GSZ Stadium' to distinguish it from the old GSZ Stadium, which it replaced.  It is currently used mostly for football matches and is the home ground of AEK Larnaca FC.  The stadium holds 13,032 people.  Its owner is the Gymnastic Club Zeno which took its name from the native philosopher of Larnaca Zeno of Citium.  Before the merge of Pezoporikos and EPA Larnaca into the new football club AEK Larnaca FC, it was also the home of those two clubs.\n\nNeo Robin Hood: 'Neo' 'Robin Hood' is a Latvian hacker who became famous for leaking bank documents.  Neo says he wants to expose those profiting from other peoples pain.  He does this by passing details of leading firms accounts via Twitter to TV stations.\n\nBourgeois &amp; Maurice: Bourgeois & Maurice are a cabaret act based in London, described by \"Time Out London\" as 'neo cabaret'.  The duo, formed in 2007, consists of Liv Morris and George Heyworth.\n\nQuestion: Bourgeois & Maurice are described as 'neo cabaret' by a magazine that started publication in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_described\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that was described with a 'neo' term.\"\n    },\n    \"description_term\": {\n      \"type\": \"string\",\n      \"description\": \"The specific 'neo' term used to describe the entity.\"\n    },\n    \"magazine_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the magazine that provided the description.\"\n        },\n        \"publication_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the magazine started its publication.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"publication_start_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_described\",\n    \"description_term\",\n    \"magazine_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_described": {
        "type": "string",
        "description": "The entity that was described with a 'neo' term."
      },
      "description_term": {
        "type": "string",
        "description": "The specific 'neo' term used to describe the entity."
      },
      "magazine_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the magazine that provided the description."
          },
          "publication_start_year": {
            "type": "integer",
            "description": "The year the magazine started its publication."
          }
        },
        "required": [
          "name",
          "publication_start_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_described",
      "description_term",
      "magazine_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
