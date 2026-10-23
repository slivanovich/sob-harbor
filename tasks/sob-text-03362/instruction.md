{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGaius Julius Caesar (proconsul): Gaius Julius Caesar (\"ca.\"  130 BC – 85 BC) was a Roman senator, a supporter of his brother-in-law, Gaius Marius, and the father of Gaius Julius Caesar, the dictator.\n\nAugustus (Williams novel): Born Gaius Octavius Thurinus, the young future-emperor was adopted by his great-uncle, Julius Caesar, after demonstrating promising wit and skill.  After his great-uncle's assassination, Augustus (at this time known as Gaius Julius Caesar Octavianus) took vengeance upon Caesar's murderers, and through tactical political moves, became one of Rome's three “Triumvirs\" alongside Marc Antony and Marcus Aemilius Lepidus.  After defeating the other two triumvirs, and obtaining sole power over the Roman State, Augustus (known as \"Imperator\" Caesar Divi Filius), began taking measures to secure and increase his power.  As a result, Augustus gave orders to exterminate Cleopatra's teenaged son, allegedly commenting, \"too many Caesars is no good thing.\"  (As it was the common belief that her son was of Julius Caesar's bloodline.)  In light of such orders, Cleopatra and Marc Antony—lovers at the time—committed suicide.\n\nJulii Caesares: The Julii Caesares were the most illustrious family of the patrician \"gens Julia\".  The family first appears in history during the Second Punic War, when Sextus Julius Caesar was praetor in Sicily.  His son, Sextus Julius Caesar, obtained the consulship in 157 BC; but the most famous descendant of this stirps is Gaius Julius Caesar, a general who conquered Gaul and became the undisputed master of Rome following the Civil War.  Having been granted dictatorial power by the Roman Senate and instituting a number of political and social reforms, he was assassinated in 44 BC.  After overcoming several rivals, Caesar's adopted son and heir, Gaius Julius Caesar Octavianus, was proclaimed Augustus by the senate, inaugurating what became the Julio-Claudian line of Roman emperors.\n\nCaligula: Caligula ( ), properly Gaius Julius Caesar Augustus Germanicus (31 August AD 12 – 24 January AD 41) was Roman emperor from AD 37–41.  Born Gaius Julius Caesar Germanicus (not to be confused with Julius Caesar), Caligula was a member of the house of rulers conventionally known as the Julio-Claudian dynasty.  Caligula's biological father was Germanicus, and he was the great-nephew and adopted son of Emperor Tiberius.  The young Gaius earned the nickname \"Caligula\" (meaning \"little soldier's boot\", the diminutive form of \"caliga\", hob-nailed military boot) from his father's soldiers while accompanying him during his campaigns in Germania.\n\nJulia (wife of Marius): Julia (c. 130 BC – 69 BC) was a daughter of Gaius Julius Caesar II (praetor-grandfather of Caesar) and Marcia (daughter of praetor Quintus Marcius Rex).  She was a sister of Gaius Julius Caesar III (the father of Julius Caesar) and Sextus Julius Caesar III, consul in 91 BC.\n\nDecember Bride (film): December Bride is a film produced in Ireland in 1990 and released on 29 November 1991.  It stars Saskia Reeves as the title character, with Donal McCann and Ciarán Hinds as the brothers who become her lovers in a conservative rural part of Ulster.  It is based on the novel by Sam Hanna Bell.\n\nGaius Caesar: Gaius Caesar (20BC – 21 February 4AD), formally Gaius Julius Caesar (Latin: \"Caius Caesar Augustus filius\"), was the adopted son and heir of Augustus.  He was born the son of Augustus' trusted friend and general, Marcus Vipsanius Agrippa.  His name at birth was Gaius Vipsanius Agrippa, but it later changed to Gaius Julius Caesar, following his adoption out of the \"Vipsanii\" and into the \"Julii\" by Augustus.  He along with his brother Lucius, born in 17BC, were intended to rule the Roman Empire together.\n\nCiarán Hinds: His television roles include Gaius Julius Caesar in the series \"Rome\", DCI James Langton in \"Above Suspicion\", Bud Hammond in \"Political Animals\" and Mance Rayder in the Emmy Award-winning \"Game of Thrones\".  As a stage actor, Hinds has enjoyed spells with the Royal Shakespeare Company, the Royal National Theatre in London and six seasons with Glasgow Citizens' Theatre, and he has continued to work on stage throughout his career.\n\nJulia (wife of Sulla): Julia, or possibly Ilia (c. 129 BC – c. 104 BC), was a Roman noblewoman who was the first wife of Sulla, later a Roman dictator.  Little is known of her life and sources are confused as to whether her name was \"Julia\" or \"Ilia\".  If Julia is correct, she could have been a daughter of Lucius Julius Caesar II, and therefore a sister of future consul Lucius Julius Caesar III and Gaius Julius Caesar Strabo Vopiscus.  Around 110 BC, while both were young, Julia married Sulla.  A marital connection to the Julii Caesares may have served Sulla in his political life, as when he was chosen to serve under Gaius Marius in the Jugurthine War.  Julia and Sulla had a daughter, Cornelia, who later was active in Roman society.  Julia apparently died young, and Sulla married his second wife, Aelia.\n\nLucius Aurelius Cotta (consul 65 BC): Lucius Aurelius Cotta was a Roman politician from an old noble family who held the offices of praetor (70 BC), consul (65 BC) and censor (64 BC).  Both his father and grandfather of the same name had been consuls, and his two brothers, Gaius Aurelius Cotta and Marcus Aurelius Cotta, preceded him as consul in 75 and 74 BC respectively.  His sister, Aurelia, was married to Gaius Julius Caesar, brother-in-law to Gaius Marius and possibly Lucius Cornelius Sulla, and they were the parents of the famous general and eventual dictator, Gaius Julius Caesar.\n\nQuestion: December Bride stars what actor whose television roles include Gaius Julius Caesar in the series Rome?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actor starred in.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"tv_series_role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role played by the actor in the television series.\"\n    },\n    \"tv_series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_title\",\n    \"film_release_year\",\n    \"tv_series_role\",\n    \"tv_series_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actor starred in."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "tv_series_role": {
        "type": "string",
        "description": "The specific role played by the actor in the television series."
      },
      "tv_series_title": {
        "type": "string",
        "description": "The title of the television series."
      }
    },
    "required": [
      "actor_name",
      "film_title",
      "film_release_year",
      "tv_series_role",
      "tv_series_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
