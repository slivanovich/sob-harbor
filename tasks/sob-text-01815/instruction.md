{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJacopo Corsi: Jacopo Corsi (17 July 1561 – 29 December 1602) was an Italian composer of the late Renaissance and early Baroque and one of Florence's leading patrons of the arts, after only the Medicis.  His best-known work is \"Dafne\" (1597/98), whose score he wrote in collaboration with Jacopo Peri.  Six fragments of the score have survived, two by Corsi and four by Peri.  The libretto, by Ottavio Rinuccini, has survived intact.  Despite priority quibbles at the time, Dafne is generally accepted as the first opera.\n\nLa Dafne: La Dafne (\"Daphne\") is an early Italian opera, written in 1608 by the Italian composer Marco da Gagliano from a libretto by Ottavio Rinuccini.  It is described as a \"favola in musica\" (fable set to music) composed in one act and a prologue.  The opera is based on the myth of Daphne and Apollo as related by Ovid in the first book of the \"Metamorphoses\".  An earlier version of the libretto had been set to music in 1597–98 by Jacopo Peri, whose \"Dafne\" is generally considered to be the first opera.\n\nList of major opera composers: This list provides a guide to opera composers, as determined by their presence on a majority of compiled lists of significant opera composers.  (See the \"Lists Consulted\" section for full details.)  The composers run from Jacopo Peri, who wrote the first ever opera in late 16th century Italy, to John Adams, one of the leading figures in the contemporary operatic world.  The brief accompanying notes offer an explanation as to why each composer has been considered major.  Also included is a section about major women opera composers, compiled from the same lists.  For an introduction to operatic history, see opera.  The organisation of the list is by birthdate.\n\nDafne: Dafne is the earliest known work that, by modern standards, could be considered an opera.  The libretto by Ottavio Rinuccini survives complete; the mostly-lost music was completed by Jacopo Peri, but at least two of the six surviving fragments are by Jacopo Corsi.  \"Dafne\" was first performed during Carnival of 1598 (1597 old style) at the Palazzo Corsi.\n\nLa Flora: La Flora, o vero Il natal de' fiori (Flora, or The Birth of Flowers) is an opera in a prologue and five acts composed by Marco da Gagliano and Jacopo Peri to a libretto by Andrea Salvadori.  It was first performed on 14 October 1628 at the Teatro Mediceo in Florence to celebrate the marriage of Margherita de' Medici and Odoardo Farnese, Duke of Parma.  Based on the story of Chloris and Zephyrus in Book V of Ovid's \"Fasti\", Salvadori's libretto contains many allegorical references to the transfer of political power, the beauty of Tuscany, and the strength of the Medici dynasty.  The score of \"La Flora\" is one of only two still in existence out of Gagliano's 14 published stage works.  Several of its arias are still performed as concert pieces.\n\nL'Orfeo: L'Orfeo (SV 318) (] ), sometimes called La favola d'Orfeo ] , is a late Renaissance/early Baroque \"favola in musica\", or opera, by Claudio Monteverdi, with a libretto by Alessandro Striggio.  It is based on the Greek legend of Orpheus, and tells the story of his descent to Hades and his fruitless attempt to bring his dead bride Eurydice back to the living world.  It was written in 1607 for a court performance during the annual Carnival at Mantua.  While Jacopo Peri's \"Dafne\" is generally recognised as the first work in the opera genre, and the earliest surviving opera is Peri's \"Euridice\", \"L'Orfeo\" is the earliest that is still regularly performed.\n\nJacopo Peri: Jacopo Peri (Zazzerino) (20 August 156112 August 1633) was an Italian composer and singer of the transitional period between the Renaissance and Baroque styles, and is often called the inventor of opera.  He wrote the first work to be called an opera today, \"Dafne\" (around 1597), and also the first opera to have survived to the present day, \"Euridice\" (1600).\n\nEuridice (Peri): Euridice (also Erudice or Eurydice) is an opera by Jacopo Peri, with additional music by Giulio Caccini.  It is the earliest surviving opera, Peri's earlier \"Dafne\" being lost.  (Caccini wrote his own \"Euridice\" even as he supplied music to Peri's opera, published this version before Peri's was performed, in 1600, and got it staged two years later.)  The libretto by Ottavio Rinuccini is based on books X and XI of Ovid's \"Metamorphoses\"\n\nEuridice (Caccini): Euridice is an opera in a prologue and one act by the Italian composer Giulio Caccini.  The libretto, by Ottavio Rinuccini, had already been set by Caccini's rival Jacopo Peri in 1600.  Caccini's version of \"Euridice\" was first performed at the Pitti Palace, Florence on 5 December 1602.  Caccini hurriedly prepared the score for the press and published it six weeks before Peri's version appeared.\n\nAmbroise Thomas: Charles Louis Ambroise Thomas (5 August 1811 – 12 February 1896) was a French composer, best known for his operas \"Mignon\" (1866) and \"Hamlet\" (1868, after Shakespeare) and as Director of the Conservatoire de Paris from 1871 till his death.\n\nQuestion: Who lived earlier Ambroise Thomas or Jacopo Peri?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_1_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"composer_2_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"composer_who_lived_earlier\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the composer who was born earlier.\"\n    },\n    \"earlier_composer_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the composer who was born earlier.\"\n    }\n  },\n  \"required\": [\n    \"composer_1_details\",\n    \"composer_2_details\",\n    \"composer_who_lived_earlier\",\n    \"earlier_composer_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_1_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_year": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "composer_2_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_year": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "composer_who_lived_earlier": {
        "type": "string",
        "description": "The name of the composer who was born earlier."
      },
      "earlier_composer_birth_year": {
        "type": "integer",
        "description": "The birth year of the composer who was born earlier."
      }
    },
    "required": [
      "composer_1_details",
      "composer_2_details",
      "composer_who_lived_earlier",
      "earlier_composer_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
