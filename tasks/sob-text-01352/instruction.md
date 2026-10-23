{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPeople's Revolutionary Army (Argentina): The People's Revolutionary Army (Spanish: \"Ejército Revolucionario del Pueblo\" , abbreviated as ERP) was the military branch of the communist Partido Revolucionario de los Trabajadores (PRT, Workers' Revolutionary Party) in Argentina.\n\nOberdan Sallustro: Oberdan Sallustro (1915 in Asunción, Paraguay - 1972 in Buenos Aires) was an Italian-Paraguayan entrepreneur, Director General of FIAT Concord in Argentina.  He was kidnapped and killed in 1972 by the Ejército Revolucionario del Pueblo (ERP) guerrilla group, according to newspaper reports.\n\nVictor Samuelson: Victor E. Samuelson (born 1937) was an Exxon United States oil company refinery manager who was kidnapped by Argentine guerrillas of the Marxist People's Revolutionary Army, also known as Ejército Revolucionario del Pueblo in Campana, Buenos Aires province, on December 3, 1973, who threatened to execute him for the \"crimes\" of multinational corporations.  On March 13, 1974, Exxon paid US$14.2 million in $100 bills for his release (a record for a kidnapping ransom), and he was released unharmed on April 29.\n\nOperativo Independencia: Operativo Independencia (Spanish for \"Operation Independence\") was the code-name of the Argentine military operation in the Tucumán Province, started in 1975 to crush the ERP —\"Ejército Revolucionario del Pueblo\" or \"People's Revolutionary Army\"—, a Guevarist guerrilla group, which tried to create a Vietnam-style war front in the Tucumán Province, in northwestern Argentina.  It was the first large-scale military operation of the Dirty War.\n\nDirty War: The \"Dirty War\" (Spanish: \"Guerra Sucia\" ), was the name used by the Argentine Military Government for a period of state terrorism in Argentina from roughly 1974 to 1983 (some sources date the beginning to 1969), during which military and security forces and right-wing death squads in the form of the Argentine Anticommunist Alliance (Triple A) hunted down and killed left-wing guerrillas, political dissidents, and anyone believed to be associated with socialism.  About 30,000 people disappeared, many of which were impossible to be formally reported due to the nature of the issue: state terrorism.  The targets were left-wing activists, guerrillas and militants, trade unionists, students, journalists and Marxists and Peronist guerrillas and their support network in the Montoneros believed to be 150,000-250,000-strong and 60,000-strong in the ERP, as well as alleged sympathizers.  Some 10,000 of the \"disappeared\" were guerrillas of the Montoneros (MPM) and the Marxist People's Revolutionary Army (ERP) although the lowest estimate is that the Montoneros and ERP had a combined strength of 5,000.  The \"disappeared\" included those thought to be a political or ideological threat to the military junta, even vaguely, and they were killed in an attempt by the junta to silence the opposition and break the determination of the guerrillas.  The worst repression reportedly occurred after the guerillas were largely defeated in 1977, when the church, labor unions, artists, intellectuals and university students and professors were targeted.  Although the Montoneros reported having carried out some 600 armed attacks in 1977, the guerrilla threat had greatly declined.  The junta justified this mass terror by exaggerating the guerrilla threat, and even staged attacks to be blamed on guerillas and used frozen dead bodies of guerilla fighters that had been kept in storage for this purpose.  In late 1979, Amnesty International accused the Videla military government of being responsible for the disappearance of 15,000 to 20,000 Argentine citizens since the 1976 coup.  That year, a special study by the New York City Bar concluded that around 10,000 Argentines had disappeared since the coup.  According to \"Registro Unificado de Víctimas del Terrorismo de Estado\" (Ruvte), 662 were disappeared under the presidency of Isabel Perón and 6,348 were disappeared during the military dictatorship.\n\nEjército Revolucionario del Pueblo: Ejército Revolucionario del Pueblo (ERP) or Ejército Popular Revolucionario (PER) may refer to:\n\nPeople's Revolutionary Army (El Salvador): The People's Revolutionary Army (in Spanish: Ejército Revolucionario del Pueblo (ERP)) was one of five leftist guerrilla organizations that comprised the Farabundo Martí National Liberation Front (FMLN).  Formed on October 10, 1980, the FMLN was one of the main participants in the Salvadoran Civil War (1979-1992).\n\nOperation Gardel: Operation Gardel was the codename given by the Peronist guerrilla organization Montoneros to the downing of a Lockheed C-130 Hercules, belonging to the 1st Transport Group of the 1st Air Brigade, as it took off the old \"Teniente General Benjamín Matienzo\" International Airport, carrying 114 Gendarmerie personnel as part of the Operativo Independencia.\n\nMario Roberto Santucho: Mario Roberto Santucho (August 12, 1936 in Santiago del Estero – July 19, 1976 in Villa Martelli) was an Argentine revolutionary and guerrilla combatant, founder of the Partido Revolucionario de los Trabajadores (Workers' Revolutionary Party, PRT) and leader of Argentina's largest marxist guerrilla group, the Ejército Revolucionario del Pueblo (People's Revolutionary Army, ERP).\n\nPeople's Revolutionary Army (Colombia): The People's Revolutionary Army (Spanish: \"Ejército Revolucionario del Pueblo\" ERP) was a small marxist guerrilla organization in Colombia.  The group originated in the municipality of Venadillo, Tolima Department in c. 1985 as a splinter group of the National Liberation Army and was commanded by its founder Édgar Castellanos, a.k.a. \"Gonzalo\" until his death in January 2007.  The group became a military objective of the larger guerrilla Revolutionary Armed Forces of Colombia whom declared the group as an enemy and was persecuted by paramilitary.  The Colombian government wanted the group for rebellion, kidnappings and extortion crimes.\n\nQuestion: Operation Gardel was the codename given by the Peronist guerrilla organization Montoneros to the downing of a Lockheed C-130 Hercules, carrying 114 Gendarmerie personnel as part of the Operativo Independencia, was the code-name of the Argentine military operation in the Tucumán Province, started in what year, to crush the ERP —\"Ejército Revolucionario del Pueblo\" or \"People's Revolutionary Army\"—, a Guevarist guerrilla group?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"operation_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the military operation.\"\n    },\n    \"start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the military operation started.\"\n    },\n    \"target_group\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the guerrilla group targeted by the operation.\"\n        },\n        \"abbreviation\": {\n          \"type\": \"string\",\n          \"description\": \"The abbreviation of the guerrilla group's name.\"\n        },\n        \"ideology\": {\n          \"type\": \"string\",\n          \"description\": \"The ideological alignment of the guerrilla group.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"abbreviation\",\n        \"ideology\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The province where the operation took place.\"\n    }\n  },\n  \"required\": [\n    \"operation_name\",\n    \"start_year\",\n    \"target_group\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "operation_name": {
        "type": "string",
        "description": "The name of the military operation."
      },
      "start_year": {
        "type": "integer",
        "description": "The year the military operation started."
      },
      "target_group": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the guerrilla group targeted by the operation."
          },
          "abbreviation": {
            "type": "string",
            "description": "The abbreviation of the guerrilla group's name."
          },
          "ideology": {
            "type": "string",
            "description": "The ideological alignment of the guerrilla group."
          }
        },
        "required": [
          "name",
          "abbreviation",
          "ideology"
        ],
        "additionalProperties": false
      },
      "location": {
        "type": "string",
        "description": "The province where the operation took place."
      }
    },
    "required": [
      "operation_name",
      "start_year",
      "target_group",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
