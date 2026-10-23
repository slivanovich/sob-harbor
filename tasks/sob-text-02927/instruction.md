{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCopts: The Copts (Coptic: \"Niremenkīmi Enkhristianos \", Egyptian Arabic: أقباط‎ ‎ \"Aqbat \") are an ethno-religious group that primarily inhabit the area of modern Egypt, where they are the largest Christian denomination.  Copts are also the largest Christian adherent group in Sudan and Libya.  Historically, they spoke the Coptic language, a direct descendant of the Demotic Egyptian that was spoken during the Roman era.  The Coptic language is a focus of Coptology and remains in liturgical use, although most Copts today speak Arabic.\n\nHaya Party: The Haya Party (Arabic: حزب هيا‎ ‎ ; translated as Life Party) is a political party started by Coptic activist Mikel Mounir.\n\nCoptic Orthodox Church in Canada: The immigration of the Copts to Canada (Copts in Canada) might have started as early as the late 1950s.  Due to an increasing amount of discrimination towards Copts in Egypt in the 1970s and low income in Egypt.  Canada has been receiving a greater number of these immigrants, and the number of Coptic immigrants into Canada has been growing ever since.\n\nMariateguist Unified Party: Mariateguist Unified Party (in Spanish: \"Partido Unificado Mariateguista - PUM\") was a political party in Peru founded in 1984 by Revolutionary Vanguard (VR), Revolutionary Left Movement (MIR), Workers Revolutionary Party (PRT) and a sector of Revolutionary Communist Party (PCR).  Leaders included Javier Diez Canseco, Agustín Haya de la Torre, Santiago Pedráglio, Hugo Blanco, Eduardo Cáceres and Carlos Tapia.  Maria Elena Moyano was also a member of PUM.\n\nYouth for Egypt Party: The Youth for Egypt Party is a political party that is made up of former members of the Egyptian Muslim Brotherhood.  The coordinator of the Brotherhood Youth Alliance, Amr Emara, has requested a meeting with the Salafi Nour Party to ask that the Salafi party forms an alliance with it.  The Nour Party will instead ally with the 38 Copts Initiative.\n\nCoptic Orthodox Church in the United States: The immigration of the Copts to the United States of America started as early as the late 1940s.  After 1952, the rate of Coptic immigration from Egypt to the United States increased.  The first Coptic church in the United States is St. Mark's Coptic Orthodox Church, which was established in the late 1960s in Jersey City.\n\nMaspero demonstrations: Maspero Massacre initially started as demonstrations on October 2011 by a group dominated by Egyptian Copts in reaction to the demolition of a church in Upper Egypt claimed to be built without appropriate license.  The peaceful protesters who intended to stage a sit-in in front of the Maspiro television building were attacked by security forces and the army, resulting in 28 deaths, mostly among the Coptic protestors, and 212 injuries, most of which were sustained by Copts.\n\nHaya van Someren: Haya Victoria van Someren-Downer (born Gerarda Victoria Downer; 5 July 1926 – 12 November 1980) was a Dutch politician of the People's Party for Freedom and Democracy (VVD).  She was a Member of the House of Representatives from 20 March 1959 until 1 October 1968.  She was the People's Party for Freedom and Democracy Party chair from 29 March 1969 until 15 March 1975.  She became a Member of the Senate on 17 September 1974 and on 5 June 1976 she succeeded Harm van Riel as the Parliamentary leader of the People's Party for Freedom and Democracy in the Senate after he retired.  She died on 12 November 1980 from cancer at the age of 54.\n\nHomeland Party (Egypt): The Homeland Party () is an Islamist political party in Egypt, founded in January 2013 following a split within the al-Nour Party.  It was formed when Emad Abdel Ghaffour, the former leader of al-Nour, and 150 other party members quit in protest at the part of a dispute between Ghaffour and followers of Yasser Al Borhamy.  The party has stated that Copts will be allowed to join the party and women will be allowed on electoral lists.  In June 2013, 130 members of the party resigned in response to differences within the party leadership.  The party withdrew from the Anti-Coup Alliance on 17 September 2014, though the reason for its withdrawal was not because of political differences.\n\nPeruvian general election, 1962: General elections were held in Peru on 10 June 1962 to elect the President and both houses of the Congress.  Víctor Raúl Haya de la Torre of the Peruvian Aprista Party won the presidential election with 33% of the vote.  However, this was below the constitutional requirement of one-third of the vote.  The military, who were opposed to Haya, claimed that electoral fraud had been carried out in some districts, and the results were later annulled following a military coup on 18 July led by Ricardo Pérez Godoy.\n\nQuestion: Within the Copts, who started the Haya Party?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"party_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the political party.\"\n    },\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who started the party.\"\n    },\n    \"founder_affiliation\": {\n      \"type\": \"string\",\n      \"description\": \"The ethno-religious group or role of the founder.\"\n    }\n  },\n  \"required\": [\n    \"party_name\",\n    \"founder_name\",\n    \"founder_affiliation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "party_name": {
        "type": "string",
        "description": "The name of the political party."
      },
      "founder_name": {
        "type": "string",
        "description": "The name of the individual who started the party."
      },
      "founder_affiliation": {
        "type": "string",
        "description": "The ethno-religious group or role of the founder."
      }
    },
    "required": [
      "party_name",
      "founder_name",
      "founder_affiliation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
