{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAuric Goldfinger: Auric Goldfinger is a fictional character and the main antagonist in the James Bond film \"Goldfinger\", based on Ian Fleming's novel of the same name.  His first name, Auric, is an adjective meaning of gold.  Fleming chose the name to commemorate the architect Ernő Goldfinger, who had built his home in Hampstead, near Fleming's; it is possible, though unlikely, that he disliked Goldfinger's style of architecture and destruction of Victorian terraces and decided to name a memorable villain after him.  According to a 1965 \"Forbes\" article and \"The New York Times\", the Goldfinger persona was based on gold mining magnate Charles W. Engelhard, Jr.\n\nProspect Hill Cemetery Building: Prospect Hill Cemetery Building is a historic burial vault located in Prospect Hill Cemetery at Guilderland in Albany County, New York.  It was built in 1863 and is a small one story cobblestone building.  It has a slate covered gable roof.  It is built of coursed cobblestones with smooth ashlar quoins and a stone lintel above the door.\n\nWeiskittel-Roehle Burial Vault: Weiskittel-Roehle Burial Vault is a historic burial vault located in Section P, Loudon Park Cemetery, Baltimore, Maryland.  It is a rectangular structure made of cast iron built into the side of a hill, constructed to look like ashlar masonry and painted gray.  It was made as the tomb of Anton W. Weiskittel who died in 1884, a Baltimore iron founder.\n\nUnited States Bullion Depository: The United States Bullion Depository, often known as Fort Knox, is a fortified vault building located within the United States Army post of Fort Knox, Kentucky.  The vault is used to store a large portion of United States official gold reserves and occasionally other precious items belonging or entrusted to the federal government.  It is estimated to hold roughly 2.3% of all the gold ever refined throughout human history.\n\nGuilderland Cemetery Vault: Guilderland Cemetery Vault is a historic burial vault located in Guilderland Cemetery at Guilderland in Albany County, New York.  It was built in 1872 and is a small one story cobblestone building.  It is built of coursed cobblestones with smooth ashlar quoins and rounded arch door.\n\nMcKayla Maroney: McKayla Rose Maroney (born December 9, 1995) is an American former artistic gymnast.  She was a member of the U.S. women's gymnastics team dubbed the Fierce Five at the 2012 Summer Olympics, where she won a gold medal in the team and an individual silver medal in the vault event.  Maroney was also a member of the gold-winning American team at the 2011 World Championships where she won gold medals in the team and vault competitions.  She defended her World title and won the gold medal on vault at the 2013 World Championships, becoming the first U.S. female gymnast to defend a World Championships vault title.  A photograph of her with a \"not impressed\" expression, taken after winning silver in the 2012 Olympics, became an Internet meme.  She decided in 2016 to no longer compete in gymnastics due to health issues.\n\nBrandon Richards: Brandon Richards (born February 6, 1967) is an American Track and Field athlete.  He was the national high school record holder in the pole vault and a son of double Olympic Gold Medalist in the pole vault, Bob Richards.  He is the third of four of Richards' sons who all excelled at the pole vault—Bob Jr. finished second in 1968 and Tom won the CIF California State Meet in the pole vault.\n\nTulskaya (Moscow Metro): Tulskaya (Russian: Tульская ) is a station of the Serpukhovsko-Timiryazevskaya Line of the Moscow Metro.  It was opened in 1983 as part of the pilot stage of the line.  The station is a single vault located underneath the Tulskaya square, named after the city of Tula.\n\nGoldfinger (film): Goldfinger (1964) is the third spy film in the James Bond series produced by Eon Productions, and the third to star Sean Connery as the fictional MI6 agent James Bond.  It is based on the novel of the same name by Ian Fleming.  The film also stars Honor Blackman as Bond girl Pussy Galore and Gert Fröbe as the title character Auric Goldfinger, along with Shirley Eaton as the iconic Bond girl Jill Masterson.  \"Goldfinger\" was produced by Albert R. Broccoli and Harry Saltzman and was the first of four Bond films directed by Guy Hamilton.\n\nGoldfinger (novel): Goldfinger is the seventh novel in Ian Fleming's James Bond series, first published in the UK by Jonathan Cape on 23 March 1959.  \"Goldfinger\" originally bore the title \"The Richest Man in the World\" and was written in January and February 1958.  The story centres on the investigation by MI6 operative James Bond into the gold smuggling activities of Auric Goldfinger, who is also suspected by MI6 of being connected to SMERSH, the Soviet counter-intelligence organisation.  As well as establishing the background to the smuggling operation, Bond uncovers a much larger plot, with Goldfinger planning to steal the gold reserves of the United States from Fort Knox.\n\nQuestion: The novel \"Goldfinger\" the title character plans to steal the gold from a vault located in what state?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel.\"\n    },\n    \"antagonist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the main antagonist in the novel.\"\n    },\n    \"theft_target\": {\n      \"type\": \"string\",\n      \"description\": \"The item or reserves the antagonist plans to steal.\"\n    },\n    \"vault_location_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific vault or depository targeted.\"\n    },\n    \"vault_location_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the targeted vault is located.\"\n    }\n  },\n  \"required\": [\n    \"novel_title\",\n    \"antagonist_name\",\n    \"theft_target\",\n    \"vault_location_name\",\n    \"vault_location_state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "novel_title": {
        "type": "string",
        "description": "The title of the novel."
      },
      "antagonist_name": {
        "type": "string",
        "description": "The name of the main antagonist in the novel."
      },
      "theft_target": {
        "type": "string",
        "description": "The item or reserves the antagonist plans to steal."
      },
      "vault_location_name": {
        "type": "string",
        "description": "The name of the specific vault or depository targeted."
      },
      "vault_location_state": {
        "type": "string",
        "description": "The state where the targeted vault is located."
      }
    },
    "required": [
      "novel_title",
      "antagonist_name",
      "theft_target",
      "vault_location_name",
      "vault_location_state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
