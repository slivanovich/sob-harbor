{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTemple of Diana (Rome): The Temple of Diana in ancient Rome was a Roman temple which, according to the early semi-legendary history of Rome, was built in the 6th century BC during the reign of the king Servius Tullius.\n\nRoman Kingdom: The Roman Kingdom, or regal period, was the period of the ancient Roman civilization characterized by a monarchical form of government of the city of Rome and its territories.\n\nPorta Esquilina: The Porta Esquilina (or Esquiline Gate) was a gate in the Servian Wall Tradition dates it back to the 6th century BC, when the Servian Wall was said to have been built by the Roman king Servius Tullius, however modern scholarship and evidence from archaeology indicates a date in the fourth century BC.\n\nServian constitution: The Servian constitution is the military and political organization of ancient Rome attributed by Roman tradition to the semi-legendary sixth king of Rome, Servius Tullius (578–534 BC).  Most of the Servian reforms extended voting rights to certain groups, in particular to Rome's citizen-commoners who were minor landholders or landless citizens hitherto disqualified from voting by ancestry, status or ethnicity—collectively, the \"plebs\" as distinguished from the hereditary patricians.  These reforms thus redefined the fiscal and military obligations of all Roman citizens.  The so-called Servian constitution probably represents a long-drawn, complex and piecemeal process extending from Servius' predecessors, Ancus Marcius and Tarquinius Priscus, to his successor Tarquinius Superbus, and into the Middle and Late Republic.  Rome's military and territorial expansion and the consequent changes in its population made franchise regulation and reform an ongoing necessity.  The wholesale attribution of these measures to Servius \"cannot be taken at face value\".\n\nServius Tullius: Servius Tullius was the legendary sixth king of Rome, and the second of its Etruscan dynasty.  He reigned 575–535 BC.  Roman and Greek sources describe his servile origins and later marriage to a daughter of Lucius Tarquinius Priscus, Rome's first Etruscan king, who was assassinated in 579 BC.  Servius is said to have been the first Roman king to accede without election by the Senate, having gained the throne by popular support; and the first to be elected by the Senate alone, without reference to the people.\n\nAes signatum: Asses signata (Latin, \"stamped bronze\", singular aes signatum) consisted of cast lumps of bronze of measured quality and weight, embossed with a government stamp, used as currency in Rome and central Italy before the introduction of the aes grave in the mid 4th century BC.  When exactly they were first made is uncertain.  Popular tradition ascribes them to Servius Tullius, but due to the high quality of art found on even the earliest specimens, this seems very unlikely.  A date in the midst of the 5th century BC is generally agreed on.  Designs featured are that of a bull, an eagle, and other religious symbols.\n\nPorta Collina: The Colline Gate (Latin Porta Collina) was a landmark in ancient Rome, supposed to have been built by Servius Tullius, semi-legendary king of Rome 578–535 BC.  The gate stood at the north end of the Servian Wall, and past it were two important streets, the Via Salaria and Via Nomentana.  Within this area the Alta Semita linked the Quirinal with the Porta Carmentalis.  Several temples were located near the gate, including temples of Venus Erycina and Fortuna.  To a person facing the gate in the 3rd century AD, the Gardens of Sallust would have been on the left, with the Baths of Diocletian on the right.\n\nTullia Minor: Tullia Minor is a semi-legendary figure in Roman history.  She was the last queen of Rome.  The younger daughter of Rome's sixth king, Servius Tullius, she married Lucius Tarquinius.  Along with her husband, she arranged the overthrow and murder of her father, securing the throne for her husband.  Her actions made her an infamous figure in ancient Roman culture.\n\nAdsidui: In ancient Rome, adsidui (also \"assidui\"; sg.  \"adsiduus\" or \"assiduus\", Latin for \"diligent, loyal\", and collectively, \"tax-payers\") were the citizens who were liable to military service in the main line of battle, that is, for much of the history of the Roman republic, as legionaries.  The \"adsidui\" were the members of the first five census classes, which were, according to the Roman historian Livy, created under the reign of Servius Tullius, the sixth legendary king of ancient Rome.  Under Tullius' original organisation, the first class was made of the richest, and thus best-equipped citizens, with helmet, shield, greaves, cuirass, spear and sword.  As one went down through the classes and the corresponding levels of wealth, equipment went lighter and lighter.  According to Peter Connolly, the goal of Tullius' reform was to base military service on wealth, and not race, thus better integrating the Etruscans, who at that time ruled Rome, and the Romans themselves ; he points out, however, that in the beginning most members of the richest first class must have been Etruscans.\n\nHistory of the Roman Empire: The history of the Roman Empire covers the history of Ancient Rome from the fall of the Roman Republic in 27 BC until the abdication of the last Western emperor in 476 AD.  Rome had begun expanding shortly after the founding of the Republic in the 6th century BC, though it did not expand outside of the Italian Peninsula until the 3rd century BC.  Civil war engulfed the Roman state in the mid 1st century BC, first between Julius Caesar and Pompey, and finally between Octavian and Mark Antony.  Antony was defeated at the Battle of Actium in 31 BC.  In 27 BC the Senate and People of Rome made Octavian \"imperator\" (\"commander\") thus beginning the Principate, the first epoch of Roman imperial history usually dated from 27 BC to 284 AD; they later awarded him the name Augustus, \"the venerated\".  The success of Augustus in establishing principles of dynastic succession was limited by his outliving a number of talented potential heirs: the Julio-Claudian dynasty lasted for four more emperors—Tiberius, Caligula, Claudius, and Nero—before it yielded in 69 AD to the strife-torn Year of Four Emperors, from which Vespasian emerged as victor.  Vespasian became the founder of the brief Flavian dynasty, to be followed by the Nerva–Antonine dynasty which produced the \"Five Good Emperors\": Nerva, Trajan, Hadrian, Antoninus Pius and the philosophically inclined Marcus Aurelius.  In the view of the Greek historian Dio Cassius, a contemporary observer, the accession of the emperor Commodus in 180 AD marked the descent \"from a kingdom of gold to one of rust and iron\"—a famous comment which has led some historians, notably Edward Gibbon, to take Commodus' reign as the beginning of the decline of the Roman Empire.\n\nQuestion: The Temple of Diana in ancient Rome was a Roman temple which, according to the early semi-legendary history of Rome, was built in the 6th century BC during the reign of the king Servius Tullius, the regal period, also called what, was the period of the ancient Roman civilization characterized by a monarchical form of government of the city of Rome and its territories?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"regal_period_alternative_name\": {\n      \"type\": \"string\",\n      \"description\": \"The alternative name for the regal period of ancient Rome.\"\n    },\n    \"period_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the characteristics of this historical period.\"\n    },\n    \"associated_historical_figure\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the king associated with this period and the temple.\"\n        },\n        \"reign_start_year_bc\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the king's reign in BC.\"\n        },\n        \"reign_end_year_bc\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the king's reign in BC.\"\n        },\n        \"associated_structures\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"structure_name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of a structure built during the king's reign.\"\n              },\n              \"construction_century_bc\": {\n                \"type\": \"integer\",\n                \"description\": \"The century BC when the structure was said to be built.\"\n              }\n            },\n            \"required\": [\n              \"structure_name\",\n              \"construction_century_bc\"\n            ],\n            \"additionalProperties\": false\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"reign_start_year_bc\",\n        \"reign_end_year_bc\",\n        \"associated_structures\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"regal_period_alternative_name\",\n    \"period_description\",\n    \"associated_historical_figure\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "regal_period_alternative_name": {
        "type": "string",
        "description": "The alternative name for the regal period of ancient Rome."
      },
      "period_description": {
        "type": "string",
        "description": "A description of the characteristics of this historical period."
      },
      "associated_historical_figure": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the king associated with this period and the temple."
          },
          "reign_start_year_bc": {
            "type": "integer",
            "description": "The start year of the king's reign in BC."
          },
          "reign_end_year_bc": {
            "type": "integer",
            "description": "The end year of the king's reign in BC."
          },
          "associated_structures": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "structure_name": {
                  "type": "string",
                  "description": "The name of a structure built during the king's reign."
                },
                "construction_century_bc": {
                  "type": "integer",
                  "description": "The century BC when the structure was said to be built."
                }
              },
              "required": [
                "structure_name",
                "construction_century_bc"
              ],
              "additionalProperties": false
            }
          }
        },
        "required": [
          "name",
          "reign_start_year_bc",
          "reign_end_year_bc",
          "associated_structures"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "regal_period_alternative_name",
      "period_description",
      "associated_historical_figure"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
