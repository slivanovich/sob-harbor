{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe White Sheik: The White Sheik (Italian: \"Lo sceicco bianco\" ) is a 1952 Italian romantic comedy film directed by Federico Fellini and starring Alberto Sordi, Leopoldo Trieste, Brunella Bovo and Giulietta Masina.  Written by Fellini, Tullio Pinelli, Ennio Flaiano and Michelangelo Antonioni, the film is about a man who brings his new bride to Rome for their honeymoon, to gain an audience with the Pope, and to present his wife to his family.  When the young woman sneaks away to find the hero of her romance novels, the man is forced to spend hour after painful hour making excuses to his eager family who want to meet his missing bride.  \"The White Sheik\" was filmed on location in Fregene, Rome, Spoleto and Vatican City.\n\nThe Via Veneto Papers: The Via Veneto Papers is a memoir collection by Ennio Flaiano, originally published in Italian in 1973, with a new expanded edition by Rizzoli in 1989 and translated into English by John Satriano in 1992.\n\nLa Strada: La Strada (  \"The Road\" ) is a 1954 Italian drama film directed by Federico Fellini from his own screenplay co-written with Tullio Pinelli and Ennio Flaiano.  The film portrays a naïve young woman (Giulietta Masina) bought from her mother by a brutish strongman (Anthony Quinn) who takes her with him on the road.\n\nThe Syndicate: A Death in the Family: The Syndicate: A Death in the Family (Italian: Colpo rovente , also known as \"Red Hot Shot\") is a 1970 Italian crime film directed by Piero Zuffi and written by Ennio Flaiano and the same Zuffi.\n\nTime to Kill (1989 film): Time to Kill (Italian: Tempo di uccidere ) is a 1989 Italian drama film starring Nicolas Cage and Italian actors Ricky Tognazzi and Giancarlo Giannini .  It is directed by Giuliano Montaldo.  The film is set in 1936, when Ethiopia was an Italian colony, and was filmed in Zimbabwe.  It is based on the novel with the same name written by Ennio Flaiano.\n\n8½: 8½ (Italian title: Otto e mezzo ] ) is a 1963 semi-autobiographical comedy-drama film directed by Federico Fellini.  Co-scripted by Fellini, Tullio Pinelli, Ennio Flaiano, and Brunello Rondi, it stars Marcello Mastroianni as Guido Anselmi, a famous Italian film director.  Shot in black-and-white by cinematographer Gianni di Venanzo, the film features a soundtrack by Nino Rota with costume and set designs by Piero Gherardi.\n\nEnnio Flaiano: Ennio Flaiano (5 March 1910 – 20 November 1972) was an Italian screenwriter, playwright, novelist, journalist, and drama critic.  Best known for his work with Federico Fellini, Flaiano co-wrote ten screenplays with the Italian director, including \"La Strada\" (1954), \"La Dolce Vita\" (1960), and \"8½\".\n\nLa Strada (2017 stage adaptation): La Strada is a play with music based on the 1954 Italian film of the same name by Federico Fellini (with Ennio Flaiano and Tullio Pinelli).  The play was adapted by the company at the Belgrade Theatre, Coventry, with Mike Akers as the writer in the room with music by Benji Bower.  This form of theatre was applied by the same creative team for the Bristol Old Vic productions of \"Treasure Island\", \"Jane Eyre\" and \"Peter Pan\" (the latter two being co-produced with National Theatre).\n\nAutobiografía del general Franco: Autobiografía del general Franco (1992) (English, \"Autobiography of general Franco\") is a novel by Manuel Vázquez Montalbán.  In 1994 it was awarded the international prize \"Premio Internacional de Literatura Ennio Flaiano\".\n\nI Vitelloni: I Vitelloni (] ; lit.  \"The Bullocks\") is a 1953 Italian comedy-drama directed by Federico Fellini from a screenplay by Fellini, Ennio Flaiano and Tullio Pinelli.  The film launched the career of Alberto Sordi, one of post-war Italy's most significant and popular comedians, who stars with Franco Fabrizi and Franco Interlenghi in a story of five young Italian men at crucial turning points in their small town lives.  Recognized as a pivotal work in the director's artistic evolution, the film has distinct autobiographical elements that mirror important societal changes in 1950s Italy.  Recipient of both the Venice Film Festival Silver Lion in 1953, and an Academy Award nomination for Best Writing in 1958, the film's success restored Fellini's reputation after the commercial failure of \"The White Sheik\" (1952).\n\nQuestion: What 1963 semi-autobiographical comedy-drama film did Ennio Flaiano work in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"screenwriters\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of screenwriters for the film.\"\n    },\n    \"is_semi_autobiographical\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is semi-autobiographical.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"screenwriters\",\n    \"is_semi_autobiographical\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "screenwriters": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of screenwriters for the film."
      },
      "is_semi_autobiographical": {
        "type": "boolean",
        "description": "Indicates if the film is semi-autobiographical."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "screenwriters",
      "is_semi_autobiographical"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
