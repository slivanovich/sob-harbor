{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Russia House (film): The Russia House is a 1990 American spy film directed by Fred Schepisi.  Tom Stoppard wrote the screenplay based on John le Carré's novel of the same name.  The film stars Sean Connery, Michelle Pfeiffer, Roy Scheider, James Fox, John Mahoney, and Klaus Maria Brandauer.\n\nKlaus Maria Brandauer: Klaus Maria Brandauer (] ; born 22 June 1943) is an Austrian actor, film director, and professor at the Max Reinhardt Seminar in Vienna.  He is known internationally for his roles in \"Mephisto\" (1981), \"Never Say Never Again\" (1983) and \"Out of Africa\" (1985).\n\nDruids (film): Druids (French: \"Vercingétorix: La légende du druide roi\") is a French-Canadian-Belgian historical film first released on 31 August 2001, directed by Jacques Dorfmann.  It stars Christopher Lambert, Klaus Maria Brandauer, Inés Sastre, Maria Kavardjikova, Bernard-Pierre Donnadieu, and Max von Sydow.\n\nBrandauer Ingenuus Ensemble: The Brandauer Ingenuus Ensemble is a theatre group based in Europe under the artistic conduction of Golden Globe Winner and Academy Awards nominated actor and director Klaus Maria Brandauer.\n\nHanussen (1988 film): Hanussen is a 1988 Hungarian film about Erik Jan Hanussen by István Szabó.  It was nominated for the 1988 Academy Award for Best Foreign Language Film.  The German language film starred Klaus Maria Brandauer.  The film was entered into the 1988 Cannes Film Festival.\n\nNever Say Never Again: Never Say Never Again is a 1983 James Bond spy film starring Sean Connery, directed by Irvin Kershner, produced by Jack Schwartzman, and written by Lorenzo Semple Jr. with uncredited additional co-writers Dick Clement and Ian La Frenais, from a story by Kevin McClory, Jack Whittingham, and Ian Fleming.  It is the second adaptation of Fleming's \"Thunderball\", which was previously adapted as the 1965 film of the same name.  Unlike the majority of James Bond films, \"Never Say Never Again\" was not produced by Eon Productions, but by an independent production company, one of whose members was Kevin McClory, one of the original writers of the \"Thunderball\" story, who retained the filming rights of the novel following a legal dispute over them.\n\nMario and the Magician (film): Mario and the Magician (German: Mario und der Zauberer ) is a 1994 German-language drama film directed by Klaus Maria Brandauer, based on the novel of the same name.  It was entered into the 19th Moscow International Film Festival where Lajos Koltai won the Special Silver St. George for the Director of Photography.\n\nThe Lightship: The Lightship is a 1986 American drama film directed by Jerzy Skolimowski.  The film stars Klaus Maria Brandauer and Robert Duvall, with early appearances from Arliss Howard and William Forsythe.\n\nEmilio Largo: Emilio Largo is a fictional character and the main antagonist from the 1961 James Bond novel \"Thunderball\".  He appears in the 1965 film adaptation, again as the main antagonist, with Italian actor Adolfo Celi filling the role.  Largo is also the main antagonist in the 1983 unofficial James Bond movie \"Never Say Never Again\", a remake of \"Thunderball\".  In \"Never Say Never Again\", the character's name, however, was changed to Maximillian Largo and he was portrayed by the Austrian actor Klaus Maria Brandauer.\n\nMephisto (1981 film): Mephisto is the title of a 1981 film adaptation of Klaus Mann's novel \"Mephisto\", directed by István Szabó, and starring Klaus Maria Brandauer as Hendrik Höfgen.  The film was a co-production between companies in West Germany, Hungary and Austria.\n\nQuestion: Which James Bond spy film did  Klaus Maria Brandauer featured in \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor in question.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the James Bond film the actor featured in.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"character_played\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor in the film.\"\n    },\n    \"is_james_bond_film\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is a James Bond film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_title\",\n    \"film_release_year\",\n    \"character_played\",\n    \"is_james_bond_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor in question."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the James Bond film the actor featured in."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "character_played": {
        "type": "string",
        "description": "The name of the character played by the actor in the film."
      },
      "is_james_bond_film": {
        "type": "boolean",
        "description": "Indicates if the film is a James Bond film."
      }
    },
    "required": [
      "actor_name",
      "film_title",
      "film_release_year",
      "character_played",
      "is_james_bond_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
