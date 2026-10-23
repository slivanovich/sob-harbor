{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSanta Lucia Luntana: \"Santa Lucia Luntana\" is a Neapolitan song written by E. A. Mario in 1919.  (There is also a different Neapolitan song transcribed by Cottreau into Italian as \"Santa Lucia\"; \"Santa Lucia Luntana\" is sometimes referred to as \"Santa Lucia\", leading to confusion.)  The song is very popular in the repertoire of many singers.  Mario Lanza (\"Mario!  Lanza at His Best,\" 1959); Luciano Pavarotti [\"The Best (Disc 2),\" 2005]; and Russell Watson (\"Reprise,\" 2003) recorded notable versions.  Italian-American tenor Sergio Franchi covered it in 1963 on his RCA Victor Red Seal album, \"Our Man From Italy.\"  Also recorded by Mario Frangoulis in his CD \"Passione - Mario sings Mario\", recorded in 2007 with the Ossipov National Orchestra of Russia, with Vladimir Ponkin as the conductor.\n\nSanta Lucia Cloud Forest: Santa Lucia Cloud Forest (Spanish: \"Bosque Nublado Santa Lucía\" ) is a cloud forest reserve, located about 80 km northwest of Quito, in the province of Pichincha, in Ecuador.  This is at the far south of the southern phase of the Choco-Andean Rainforest Corridor.  Rainforest Concern works with the Santa Lucia co-operative, a community-based conservation organisation dedicated to conservation and to sustainable development so that they can make a modest living whilst conserving their remaining cloud forest.\n\nBattle of Santa Lucia: The battle of Santa Lucia was an episode in the First Italian War of Independence.  On 6 May 1848, when the king of Sardinia, Carlo Alberto, sent I Corps of the Sardinian army to assault the fortified positions held before the walls of Verona by the Austrian army under field marshal Josef Radetzky.  The Austrian army, though outnumbered, managed to withstand the attack and hold their positions.  The battle is named after the Santa Lucia district of Verona.  Franz Joseph (then only 17 years old) assisted at the battle.\n\nLos Padres Council: The Los Padres Council was founded in 1917 as the Santa Barbara Council.  The SBC changed its name in 1929 to the Mission Council and stayed that way until 1994.  In 1994, the Santa Lucia Area Council merged with the Mission Council to form the Los Padres Council.  The Santa Lucia Area Council (#056) was founded in 1933, as the San Luis Obispo County Council.  The Central Coast Counties council (#025), founded in 1922 merged into Santa Barbara in 1924.\n\nRibes sericeum: Ribes sericeum is a species of currant known by the common name Lucia gooseberry, or Santa Lucia gooseberry; its Latin epithet of \"sericeum\" means \"of silk\".  It is endemic to California, where it is known only from the Santa Lucia Mountains along the Central Coast and an additional isolated population in Santa Barbara County.\n\nLotería Santa Lucía: The \"Loteria Santa Lucia\"' (Santa Lucia Lottery) is one of the largest lotteries in Guatemala, which many people support and play to help the deafblind across the country.  The payout of the Santa Lucia lottery is determined by the proportion of deafblind people who were born in Guatemala, against the proportion of people with other problems.  According to Guatemalan studies, over 50 million people, over 50 years, have helped the deafblind.\n\nFranz Joseph I of Austria: Franz Joseph I or Francis Joseph I (German: \"Franz Josef I.\" , Hungarian: \"I. Ferenc József\" , , Romanian: \"Francisc Iosif\" , Slovene: \"Franc Jožef I.\" , Italian: \"Francesco Giuseppe\" , Croatian: \"Franjo Josip I.\" ) (18 August 1830 – 21 November 1916) was Emperor of Austria and King of Hungary, King of Bohemia and many others (see grand title of the Emperor of Austria) from 2 December 1848 until his death on 21 November 1916.  From 1 May 1850 to 24 August 1866 he was also President of the German Confederation.  He was the longest-reigning Emperor of Austria and King of Hungary, as well as the third longest-reigning monarch of any country in European history, after Louis XIV of France and Johann II of Liechtenstein.\n\nTerritorial Prelature of Santa Lucia del Mela: The Territorial Prelature of Santa Lucia del Mela was a Roman Catholic territorial prelature in Italy, located in the city of Santa Lucia del Mela, a major \"commune\" (municipality) in the administrative Province of Messina in the insular south Italian region of Sicily.  In 1986, it was suppressed and merged, together with the Diocese of Lipari into the Metropolitan Archdiocese of Messina to form the Archdiocese of Messina-Lipari-Santa Lucia del Mela.\n\nSanta Lucia de' Magnoli Altarpiece: The Santa Lucia de' Magnoli Altarpiece (Italian: \"Pala di Santa Lucia de' Magnoli\") is a painting by the Italian painter Domenico Veneziano, dated to around 1445–1447.  Once placed at the high altar of the church of Santa Lucia dei Magnoli, Florence, it is now in the Uffizi Gallery in the same city.  The large panel had originally a predella, which has been divided between museums in Washington, Berlin and Cambridge.\n\nSanta Lucia in Selci: The Church of Saint Lucy in Selci (Italian: \"Santa Lucia in Selci\" , also known as \"Santa Lucia in Silice \" or \"Santa Lucia in Orfea (in Orphea, in Orthea) \") is an ancient Roman Catholic church, located in Rome, dedicated to Saint Lucy, a 4th-century virgin and martyr.\n\nQuestion: What person born in 1830 assisted at the Battle of Santa Lucia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who assisted at the battle.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person.\"\n    },\n    \"event_assisted_at\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event the person assisted at.\"\n    },\n    \"person_age_at_event\": {\n      \"type\": \"integer\",\n      \"description\": \"The age of the person when they assisted at the event.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"birth_year\",\n    \"event_assisted_at\",\n    \"person_age_at_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who assisted at the battle."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the person."
      },
      "event_assisted_at": {
        "type": "string",
        "description": "The name of the event the person assisted at."
      },
      "person_age_at_event": {
        "type": "integer",
        "description": "The age of the person when they assisted at the event."
      }
    },
    "required": [
      "person_name",
      "birth_year",
      "event_assisted_at",
      "person_age_at_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
