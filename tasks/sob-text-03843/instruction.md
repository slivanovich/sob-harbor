{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJamil: Jamil (Arabic: جميل‎ ‎ ) is an Arabic given name.  It means \"beautiful\" in Arabic.  The Latin spelling variants include Gamil (used mainly in Egypt), Cemil (in Turkish), Djemil or Djamel (mainly in North African countries influenced by French spelling), Djamil and Jameel (mainly among African Americans influence by English spelling).  Yamil, which is the Spanish variant of the name Jamil, has the same pronunciation in Spanish, but different spelling.  The feminine equivalent is Jamila (also Gamila, Cemila, Djemila, Djamila, Jameela, Yamila, Jamyla, and Jamily).\n\nPetar Kanavelić: Pietro Canavelli (in Italian, his personal spelling; known as Petar Kanavelić in Croatian; 27 December 1637 – 16 January 1719) was a Croatian writer who wrote poems in Croatian and Italian.  He is regarded as one of the greatest Croatian writers of the 17th century.\n\nSusana (given name): Susana is a feminine given name.  Like its variants, which include the names Susanna and Susan, it is derived from Σουσάννα, \"Sousanna\", the Greek form of the Hebrew שושנה, \"Shoshannah\", which could have been derived from the Aramaic language.  ܫܘܫܢ, \"Shoshan\" means \"lily\" in Syriac.  سوسن, \"Susan\", is the Persian spelling of this name.  The spelling \"Susanna\" is used in Sweden, Italy, the Netherlands and Finland, as well as much of the English-speaking world.  \"Zuzana\" is used in Czech Republic and Slovakia, and the spelling is \"Zsuzsanna\" in Hungary.  In Polish it is \"Zuzanna\".  In addition to its use in English, the spelling \"Susana\" is also common in countries such as Spain and Portugal.\n\nKatarina (given name): Katarina is a feminine given name.  It is the standard Swedish, Croatian, Bosnian, Serbian, and Slovenian form of Katherine, and a variant spelling in several other languages.  In Croatia, it is the fourth most common female given name, or third if combined with the short form Kata, and in Serbia it is within the 10 most popular names for girls born since 1991.  It may refer to:\n\nMatteo: Matteo is the Italian form of the given name Matthew.  Another form is Mattia.  The Hebrew meaning of Matteo is 'gift of God.'  Matteo can also be used as a patronymic surname, often in the forms of de Matteo, De Matteo or DeMatteo, meaning \"[descendant] of Matteo\".\n\nTudjmanism: Tudjmanism (Croatian: \"tuđmanizam\" ) is a form of Croatian nationalism.  Franjo Tuđman defined it as non-Communist nationalism with \"re-examined Croatian history\".  According to Croatian historian Ivo Banac, Tudjmanism unites all forms of the Croatian anti-liberalism, that is Croatian fascism and the Croatian communism.  Croatian political scientist Slaven Ravlić defines Tuđmanism to be the name both for an ideology and for a regime.  According to Ravlić, the ideology contains elements of deification of the Croatian people started by Ante Starčević, a continuation of the 20th-century conservative tradition that rejects liberal democracy, and a mix of ideas represented by neoconservatism.  The resulting regime was authoritarian, it created a form of crony capitalism, and engaged in the creation of an ideological hegemony.\n\nMateo (given name): Mateo is the Spanish form of Matthew.  This form is also sometimes used in Croatian, from the Italian form Matteo.  It may refer to:\n\nFran (given name): Fran is a Spanish, Italian, Croatian, and Albanian unisex name (respectively Francisca/Francisco, Francesca/Francesco and Fran(j)o), and a common short form (hypocorism) of the English names Frances and Francis.  The Spanish and Italian Fran is more common for men, while the English name is mostly used for women.  The Croatian and Albanian Fran is used only for men.\n\nSusanna (given name): Susanna is a feminine first name.  It is not very common in the US, and is found there predominantly among the American Jewish community.  It is the name of women in the Biblical books of Daniel and Luke.  It is often spelled Susannah, although Susanna is the original spelling.  It is derived from Σουσάννα (\"Sousanna\"), the Greek form of the Hebrew שושנה \"Shoshannah\", meaning lily (from Lilium family).  سوسن (Susan) is the Persian spelling of this name.  The spelling Susanna is used in Sweden, Italy, the Netherlands and Finland, as well as in the English-speaking world.  The spelling Zuzana is used in Czech Republic and Slovakia and spelling Zsuzsanna in Hungary.  In Poland it is Zuzanna.  Even though very uncommon, it is also spelled Susana in Spain and Portugal, where it is more common.\n\nCharter of Duke Trpimir: Charter of Duke Trpimir (Croatian: \"Povelja kneza Trpimira\" ), also known as Trpimir's deed of donation (Croatian: \"Trpimirova darovnica\" ) is the oldest preserved document of the Croatian law, the oldest from the court of one of the Croatian rulers and the first national document which mentions the Croatian name.  Charter, dated to 4 March 852, is not preserved in its original form but in five subsequent transcripts out of which the oldest is from year 1568.\n\nQuestion: What name is similar in spelling in the Spanish, Croatian, Italian, and Hebrews form\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"name\": {\n      \"type\": \"string\",\n      \"description\": \"The base name that has similar forms across the specified languages.\"\n    },\n    \"language_forms\": {\n      \"type\": \"array\",\n      \"description\": \"List of forms of the name in different languages, highlighting their spellings.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"language\": {\n            \"type\": \"string\",\n            \"description\": \"The language of the name form.\"\n          },\n          \"form\": {\n            \"type\": \"string\",\n            \"description\": \"The spelling of the name in that specific language.\"\n          },\n          \"derivation_note\": {\n            \"type\": \"string\",\n            \"description\": \"Additional notes on the derivation or usage of the form, if available.\"\n          }\n        },\n        \"required\": [\n          \"language\",\n          \"form\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"hebrew_origin\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the name's Hebrew origin, specifically its meaning as the Hebrew spelling is not provided.\",\n      \"properties\": {\n        \"meaning\": {\n          \"type\": \"string\",\n          \"description\": \"The Hebrew meaning of the name.\"\n        }\n      },\n      \"required\": [\n        \"meaning\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"name\",\n    \"language_forms\",\n    \"hebrew_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The base name that has similar forms across the specified languages."
      },
      "language_forms": {
        "type": "array",
        "description": "List of forms of the name in different languages, highlighting their spellings.",
        "items": {
          "type": "object",
          "properties": {
            "language": {
              "type": "string",
              "description": "The language of the name form."
            },
            "form": {
              "type": "string",
              "description": "The spelling of the name in that specific language."
            },
            "derivation_note": {
              "type": "string",
              "description": "Additional notes on the derivation or usage of the form, if available."
            }
          },
          "required": [
            "language",
            "form"
          ],
          "additionalProperties": false
        }
      },
      "hebrew_origin": {
        "type": "object",
        "description": "Details about the name's Hebrew origin, specifically its meaning as the Hebrew spelling is not provided.",
        "properties": {
          "meaning": {
            "type": "string",
            "description": "The Hebrew meaning of the name."
          }
        },
        "required": [
          "meaning"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "name",
      "language_forms",
      "hebrew_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
