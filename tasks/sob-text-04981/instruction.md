{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMasnavi: The Masnavi, or Masnavi-i Ma'navi (Persian: مثنوی معنوی‎ ‎ ), also written Mesnevi, Mathnawi, or Mathnavi, is an extensive poem written in Persian by Jalal al-Din Muhammad Balkhi also known as Rumi, the celebrated Persian Sufi poet.  It is one of the best known and most influential works of Sufism.  The \"Masnavi\" is a series of six books of poetry that together amount to around 25,000 verses or 50,000 lines.  It is a spiritual text that teaches Sufis how to reach their goal of being truly in love with God.\n\nSufi saints of Aurangabad: Aurangabad furnished a genial soil for the spread of Islam, and was the centre of great missionary movements in the 8th century of the Hijri.  The district is home to the earliest of Sufi saints of the Deccan.  The town of Khuldabad contains the shrines of the most famous saints of the Dakhan.  Initially it was known as Rauza meaning \"garden of paradise\".  It is known as the Valley of Saints, or the Abode of Eternity, because in the 14th century, several Sufi saints chose to reside here.  The tomb of the Mughal emperor Aurangzeb and his trusted general Qamar-ud-din Khan, Asaf Jah I first Nizam of Hyderabad are located in this town, so is the tomb of Malik Ambar.\n\nKamal Khujandi: Kamal Khujandi (Persian: کمال خجندی‎ ‎ ), also Kamal Khojandi, Kamaleddin Khojandi, or Kamal-E Khojandi, was a Persian Sufi and Persian ghazal poet of the 14th century (8th century hijri).\n\nAbdal: Abdāl (\"lit\": substitutes, but which can also mean \"generous\" [\"karīm\"] and \"noble\" [\"sharīf\"]) is a term used in Islamic metaphysics and Islamic mysticism, both Sunni and Shiite, to refer to a particularly important group of God's saints.  In the tradition of Sunni Islam in particular, the concept attained an especially important position in the writings of the Sunni mystics and theologians, whence it appears in the works of Sunni authorities as diverse as Abu Talib al-Makki (d. 956), Ali Hujwiri (d. 1072), Ibn Asakir (d. 1076), Khwaja Abdullah Ansari (d. 1088), and Ibn Khaldun (d. 1406).\n\nShrine of Bayazid Bostami: The Shrine of Bayazid Bostami is a shrine in Chittagong, Bangladesh.  Bayazid Bostami was a famous Persian Sufi born in Bostam, Iran.  Its shrine area as a complex consists of a tomb surrounded by a brick structure along with an old mosque and a large pond.  There is no significant historical evidence about Bostami's visit and tomb in this area.  The whole complex is located on a hillock of Nasirabad, considered to be a holy place and attracts a large number of visitors and pilgrims daily.\n\nKhwaja Abdullah Ansari: Hazrat Shaikh Abu Ismaïl Abdullah al-Herawi al-Ansari or Khajah Abdullah Ansari of Herat (1006–1088) (Persian: خواجه عبدالله انصاری‎ ‎ ) also known as \"Pir-i Herat\" (پیر هرات ) (sage of Herat) was a famous Persian Sufi who lived in the 11th century in Herat (then Khorasan, now Herat province, Afghanistan).  One of the outstanding figures in Khorasan in the 5th/11th century: commentator of the Qur'an, traditionist, polemicist, and spiritual master, known for his oratory and poetic talents in Arabic and Persian.\n\nAbū-Sa'īd Abul-Khayr: Abusa'id Abolkhayr or Abū-Sa'īd Abul-Khayr (Persian: ابوسعید ابوالخیر‎ ‎ ) (December 7, 967 - January 12, 1049), also known as Sheikh Abusaeid or Abu Sa'eed, was a famous Persian Sufi and poet who contributed extensively to the evolution of Sufi tradition.\n\nThis too shall pass: \"This too shall pass\" (Persian: Persian: این نیز بگذرد‎ ‎ , \"īn nīz bogzarad\") is originally a Persian adage reflecting on the evanescence, or ephemerality, of the human condition.  The phrase seems to have originated in the writings of the medieval Persian Sufi poets, and is often attached to a fable of a great king who is humbled by the simple words.  The general sentiment is often expressed in wisdom literature throughout history and across cultures.  It also appears in a collection of tales by the English poet Edward Fitzgerald in the early 19th century.  It was also notably employed in a speech by Abraham Lincoln before he became the sixteenth President of the United States.  Fitzgerald's usage of the phrase is in the context of a retelling of a Persian fable.  Some versions of the fable, beginning with that of Attar of Nishapur, add the detail that the phrase is inscribed on a ring, which has the ability to make the happy man sad and the sad man happy.\n\nMahmoud Shabestari: Mahmoūd Shabestarī (1288–1340) (Persian: محمود شبستری‎ ‎ ) is one of the most celebrated Persian Sufi poets of the 14th century.\n\nRudbari: Abu Ali al-Rudbarior Abuzer Rudbari (Persian: ابو علی رودباری‎ ‎ ), known also as Rudbari, was a famous early Persian sufi saint of the 9th century.  He claimed descent from the Sassanid king Anushiravan and was a disciple of Junayd Baghdadi.\n\nQuestion: Who was a famous Persian Sufi who lived in the 11th century in Herat who's works refer to a particularly important group of God's saints?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sufi_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Persian Sufi.\"\n    },\n    \"century_lived\": {\n      \"type\": \"integer\",\n      \"description\": \"The century in which the Sufi lived.\"\n    },\n    \"city_of_residence\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the Sufi lived.\"\n    },\n    \"referenced_saints_group\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"group_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the group of saints referenced in the Sufi's works.\"\n        },\n        \"group_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the group of saints.\"\n        },\n        \"is_referenced_in_works\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the group of saints is referenced in the Sufi's works.\"\n        }\n      },\n      \"required\": [\n        \"group_name\",\n        \"group_description\",\n        \"is_referenced_in_works\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"sufi_name\",\n    \"century_lived\",\n    \"city_of_residence\",\n    \"referenced_saints_group\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sufi_name": {
        "type": "string",
        "description": "The name of the Persian Sufi."
      },
      "century_lived": {
        "type": "integer",
        "description": "The century in which the Sufi lived."
      },
      "city_of_residence": {
        "type": "string",
        "description": "The city where the Sufi lived."
      },
      "referenced_saints_group": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the group of saints referenced in the Sufi's works."
          },
          "group_description": {
            "type": "string",
            "description": "A description of the group of saints."
          },
          "is_referenced_in_works": {
            "type": "boolean",
            "description": "Indicates if the group of saints is referenced in the Sufi's works."
          }
        },
        "required": [
          "group_name",
          "group_description",
          "is_referenced_in_works"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "sufi_name",
      "century_lived",
      "city_of_residence",
      "referenced_saints_group"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
