{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHarry von Meter: Harry von Meter (March 20, 1871 in Malta Bend, Missouri – June 2, 1956 in Sawtelle, California) was an American silent film actor.  He was signed by the Thanhouser Company based in New Rochelle, New York in 1912, moving to American Film Studios a year or two later, and starred in about 200 films until 1929.  He appeared in the 1923 film \"The Hunchback of Notre Dame\" as Mons.  Neufchatel.\n\nMaryada Ramanna: Maryada Ramanna is a 2010 Telugu action comedy film directed by S. S. Rajamouli starring Sunil and Saloni Aswani in lead roles.  This film is inspired from Buster Keaton's 1923 film, \"Our Hospitality\".  This is the second film for Sunil as a hero, and is an important example of a director casting against the norm in the Telugu film industry.  The film opened to favourable reviews by critics.\n\nThe Tale of a Manor: The Tale of a Manor (Swedish: En herrgårdssägen ) is an 1899 novel by the Swedish writer Selma Lagerlöf.  It tells the story of a young woman who tries to rescue the man she loves from madness, caused by shame and sorrow.  It was published in English in 1923, in a portmanteau volume titled \"The Tale of a Manor and Other Sketches\".  The 1923 film \"The Blizzard\" by Mauritz Stiller is loosely based on the novel.\n\nThe Savur Grave: The Savur Grave (Georgian:Savur-Mogila) is a 1926 Soviet silent adventure film directed by Ivane Perestiani.  It is the sequel to the 1923 film \"Red Devils\".\n\nIf Winter Comes: If Winter Comes is a 1947 drama film released by MGM.  The movie was directed by Victor Saville, based on the novel by A.S.M. Hutchinson.  The film tells the story of an English textbook writer who takes in a pregnant girl.  The novel had previously been made into the 1923 film \"If Winter Comes\".\n\nA Doll's House: A Doll's House (Bokmål: \"Et dukkehjem\" ; also translated as \"A Doll House\") is a three-act play written by Henrik Ibsen.  It premiered at the Royal Theatre in Copenhagen, Denmark, on 21 December 1879, having been published earlier that month.  The play is set in a Norwegian town circa 1879.\n\nNora (1923 film): Nora is a 1923 German silent drama film directed by Berthold Viertel and starring Olga Tschechowa, Carl Ebert and Fritz Kortner.  It is an adaptation of the 1879 play \"A Doll's House\" by Henrik Ibsen.  It premiered in Berlin on 2 February 1923.  The film's art direction was by Walter Reimann.\n\nBella Donna (1923 film): Bella Donna is a 1923 American silent film produced by Famous Players-Lasky and released by Paramount Pictures.  The film is based on a novel, \"Bella Donna\", by Robert Smythe Hichens which was later adapted for a 1912 Broadway play starring Alla Nazimova.  This film is also a remake of the 1915 Paramount film \"Bella Donna\" starring Pauline Frederick.  The 1923 film was directed by George Fitzmaurice and starred Pola Negri in her first American film.\n\nTo the Last Man (1933 film): To the Last Man is a 1933 American Pre-Code Western film starring Randolph Scott and Esther Ralston, which was and directed by Henry Hathaway from a screenplay by Jack Cunningham based on a story by Zane Grey.  The Paramount property was previously made as a silent film, Victor Fleming's 1923 film version of the same title.  The supporting cast of Hathaway's version features Jack La Rue, Buster Crabbe, Barton MacLane, Noah Beery, Sr., Shirley Temple, Fuzzy Knight, Gail Patrick and John Carradine.  Child actors Delmar Watson and Shirley Temple were praised by \"Variety\" (Edwards, 41).\n\nThe Scarlet Car: The Scarlet Car is a 1917 American silent drama film directed by Joe De Grasse and featuring Lon Chaney.  The film is based upon the novel \"The Scarlet Car\" by Richard Harding Davis, which also was the basis of a 1923 film of the same name.  A print of the 1917 film exists and has been released on DVD.\n\nQuestion: In what country did the play of which the 1923 film \"Nora\" is an adaptation premier?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"adapted_play_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the play from which the film was adapted.\"\n    },\n    \"play_premiere_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the adapted play premiered.\"\n    },\n    \"play_premiere_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the adapted play premiered.\"\n    },\n    \"play_premiere_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date when the adapted play premiered.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"adapted_play_title\",\n    \"play_premiere_country\",\n    \"play_premiere_city\",\n    \"play_premiere_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "adapted_play_title": {
        "type": "string",
        "description": "The title of the play from which the film was adapted."
      },
      "play_premiere_country": {
        "type": "string",
        "description": "The country where the adapted play premiered."
      },
      "play_premiere_city": {
        "type": "string",
        "description": "The city where the adapted play premiered."
      },
      "play_premiere_date": {
        "type": "string",
        "description": "The date when the adapted play premiered."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "adapted_play_title",
      "play_premiere_country",
      "play_premiere_city",
      "play_premiere_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
