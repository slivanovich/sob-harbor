{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Ambushers (film): The Ambushers is a 1967 spy comedy film filmed in Acapulco starring Dean Martin, Senta Berger and Janice Rule.  It is loosely based upon the novel of the same name by Donald Hamilton as well as \"The Menacers\" that featured UFOs and a Mexican setting.  When a government-built flying saucer is hijacked mid-flight by Jose Ortega, the exiled ruler for an outlaw nation, secret agent Matt Helm and the ship's former pilot Sheila Sommers are sent to recover it.\n\nThe End of Agent W4C: Konec agenta W4C prostřednictvím psa pana Foustky (English: The End of Agent W4C ) is a 1967 Czechoslovak film parodying the James Bond secret agent genre.  Directed by Václav Vorlíček based on the story by Oldřich Daněk.  Runtime 87 min.  Mono.  Produced by Filmové Studio Barrandov and distributed by Central Office of Film Distribution, Prague.\n\nOSS 117: Cairo, Nest of Spies: OSS 117: Cairo, Nest of Spies released in France as OSS 117 : Le Caire, nid d'espions, is a 2006 French spy comedy film directed and co-written by Michel Hazanavicius in his feature film debut.  It stars Jean Dujardin, Bérénice Bejo, and Aure Atika.  Set in 1955, the film follows the exploits the French secret agent Hubert Bonisseur de La Bath / OSS 117, as he is sent to Cairo to investigate the disappearance of his best friend and fellow spy Jack Jefferson, only to stumble into a web of international intrigue.\n\nMark Huffam: Mark Huffam is a film and television producer.  He was a producer on \"The Martian\", \"Johnny English\", and the television series \"Game of Thrones\".\n\nOSS 117: Lost in Rio: OSS 117: Lost in Rio released in France as OSS 117: Rio ne répond plus (stylized as OSS 117: Rio ne répond plus...), is a 2009 French spy comedy film directed and co-written by Michel Hazanavicius.  It is a sequel to Hazanavicius' \"\", and see Jean Dujardin reprising his role as French secret agent Hubert Bonisseur de La Bath / OSS 117.  Set in 1967, \"Lost in Rio\" sees OSS 117 sent to Brazil in order to retrieve a microfilm list of French Nazi sympathizers, only to once again unknowingly set foot into a bigger international intrigue.\n\nJohnny English: Johnny English is a 2003 British-American spy comedy film parodying the James Bond secret agent genre infused with comedy similar to Atkinson's Mr. Bean character.  The film stars Rowan Atkinson, Natalie Imbruglia, Ben Miller and John Malkovich.  The screenplay was written by Bond writers Neal Purvis and Robert Wade, with William Davies, and the film was directed by Peter Howitt.  It is the first installment of the \"Johnny English film series\".\n\nKingsman: The Secret Service: Kingsman: The Secret Service is a 2014 action spy comedy film directed and co-produced by Matthew Vaughn.  The screenplay was written by Vaughn and Jane Goldman, based on the comic book series \"Kingsman\", created by Dave Gibbons and Mark Millar.  It follows the recruitment and training of Gary \"Eggsy\" Unwin (Taron Egerton), into a secret spy organisation.  Eggsy joins a mission to tackle a global threat from Richmond Valentine (Samuel L. Jackson), a wealthy megalomaniac.  The film also stars Colin Firth, Mark Strong, and Michael Caine.\n\nJohnny English (film series): Johnny English is a British series of action comedy film parodying the James Bond secret agent genre.  It features Rowan Atkinson as the titular character, based on the screenplay was written by Neal Purvis and Robert Wade.  The series included 3 instalments: \"Johnny English\" (2003), \"Johnny English Reborn\" (2011), and the upcoming \"Johnny English 3\" which is in pre-production.  The series also infused with comedy similar to Atkinson's Mr. Bean character and grossed $320 worldwide.\n\nJohnny English Reborn: Johnny English Reborn is a 2011 British action comedy film parodying the James Bond secret agent genre.  The film is the sequel to \"Johnny English\" (2003), and stars Rowan Atkinson reprising his role as the title character and directed by Oliver Parker.  The film is the second installment of the \"Johnny English film series\".\n\nSpy Hard: Spy Hard is a 1996 American spy comedy film parody starring Leslie Nielsen and Nicollette Sheridan, parodying James Bond movies and other action films.  The introduction to the movie is sung by comedy artist \"Weird Al\" Yankovic.  It is the first film to be written by Jason Friedberg and Aaron Seltzer.  The film's title is a pun of \"Die Hard\".  The film is directed by Rick Friedberg and produced by Doug Draizin and Jeffery Knovitz.\n\nQuestion: Mark Huffam was a producer on a spy comedy film parodying what secret agent?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the producer.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film produced by the person.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"parody_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of genre or character being parodied by the film.\"\n    },\n    \"parodied_secret_agent\": {\n      \"type\": \"string\",\n      \"description\": \"The specific secret agent character that the film parodies.\"\n    }\n  },\n  \"required\": [\n    \"producer_name\",\n    \"film_title\",\n    \"film_genre\",\n    \"parody_type\",\n    \"parodied_secret_agent\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "producer_name": {
        "type": "string",
        "description": "The name of the producer."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film produced by the person."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "parody_type": {
        "type": "string",
        "description": "The type of genre or character being parodied by the film."
      },
      "parodied_secret_agent": {
        "type": "string",
        "description": "The specific secret agent character that the film parodies."
      }
    },
    "required": [
      "producer_name",
      "film_title",
      "film_genre",
      "parody_type",
      "parodied_secret_agent"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
