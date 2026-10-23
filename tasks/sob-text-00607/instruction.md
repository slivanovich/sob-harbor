{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMo (2010 film): Mo is a 2010 TV film about the later life and career of the British Labour Party politician Mo Mowlam, written by Neil McKay and directed by Philip Martin.\n\nChen Mo and Meiting: Chen Mo and Meiting () is a 2002 Chinese romantic drama film written and directed by Liu Hao.  It was Liu's directorial debut and stars Du Huanan and Wang Lingbo as the titular Chen Mo and Meiting.\n\nAdimakal: Adimakal is a 1969 Indian Malayalam film, directed by KS Sethumadhavan and produced by MO Joseph.  The film stars Prem Nazir, Sathyan, Sheela and Sharada in lead roles.  The film had musical score and songs composed by G. Devarajan.  It won the National Film Award for Best Feature Film in Malayalam and Filmfare Award for Best Malayalam Film.  The film is based on a novel by Pamman.  The film was remade in Telugu as \"Chilakamma Cheppindi\" (1977) with Rajinikanth and in Tamil as \"Nizhal Nijamagiradhu\" with Kamal Haasan.\n\nKillers (2014 film): Killers (Japanese: キラーズ , \"\"Kirazu\"\") is a 2014 Japanese-Indonesian psychological thriller film directed by Indonesian director duo The Mo Brothers.  This film marks the first collaboration in the thriller genre between Japan and Indonesia.  The story was written by Takuji Ushiyama with Timo Tjahjanto of The Mo Brothers.\n\nYorokobi mo kanashimi mo ikutoshitsuki: Yorokobi mo kanashimi mo ikutoshitsuki (喜びも悲しみも幾歳月 ) aka The Lighthouse (UK) or Times of Joy and Sorrow (USA) or \"Years of Joy and Sorrow\", is a 1957 color Japanese film directed by Keisuke Kinoshita.\n\nTora-san, the Expert: Tora-san, the Expert (男はつらいよ 花も嵐も寅次郎 , Otoko wa Tsurai yo: Hana mo Arashi mo Torajirō ) is a 1982 Japanese comedy film directed by Yoji Yamada.  It stars Kiyoshi Atsumi as Torajirō Kuruma (Tora-san), and Yuko Tanaka as his love interest or \"Madonna\".  \"Tora-san, the Expert\" is the thirtieth entry in the popular, long-running \"Otoko wa Tsurai yo\" series.  This became the first Tora-san film to be released on DVD with English subtitles in when the Hong Kong label Panorama did so in 2006.\n\nPo Mo Knock Knock: Po Mo Knock Knock is a 1999 experimental comedy short film written by David Ball and directed by Greg Pak.  It is performed by Ball and other members of the New York City improv comedy troupe, The Pollyannas, Bill Stiles and Vin Knight.  The title of the film refers to its subject, \"Po\"st\"Mo\"dern knock knock jokes.  The film itself is a parody of postmodernism and of postmodern experimental film, through its use of irony, internal contradictions, references to Jacques Derrida, and the Godardian use of title cards.\n\nSuna Chadhei Mo Rupa Chadhei: Suna Chadhei Mo Rupa Chadhei is a 2009 Indian Oriya film directed by Humanshu Parija.  After \"Nei Ja Re Megha Mate\", Siddhanta Mahapatra, Anubhav Mohanty & Barsha Priyadarshini paired for second time in this film.  This film is a remake of superhit Telugu film \"Nuvvostanante Nenoddantana\" directed by Prabhu Deva.\n\nMo Mowlam: Marjorie Mowlam (18 September 194919 August 2005) was an English Labour Party politician.  She was the Member of Parliament (MP) for Redcar from 1987 to 2001 and served in the Cabinet as Secretary of State for Northern Ireland, Minister for the Cabinet Office and Chancellor of the Duchy of Lancaster.\n\n92 Legendary La Rose Noire: 92 Legendary La Rose Noire is a 1992 Hong Kong comedy film written and directed by Jeffrey Lau and starring Tony Leung, Maggie Shiu, Teresa Mo, Wong Wan-sze and Fung Bo Bo.  The film was nominated for eight awards at the 12th Hong Kong Film Awards, where Leung won his second Hong Kong Film Award for Best Actor and Fung won her first Hong Kong Film Award for Best Supporting Actress.  \"92 Legendary La Rose Noire\" was ranked number 75 of the Best 100 Chinese Motion Pictures at the 24th Hong Kong Film Awards.  The film was followed two sequels, one released in 1993 titled \"Rose Rose I Love You\", where Leung reprises his role but features a new storyline, and another released in 1997 confusingly titled \"Black Rose II\", also featuring a new storyline and different cast.\n\nQuestion: Who directed the film Mo about Mo Mowlam?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_subject\": {\n      \"type\": \"string\",\n      \"description\": \"The person or topic the film is about.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_subject\",\n    \"director_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_subject": {
        "type": "string",
        "description": "The person or topic the film is about."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_subject",
      "director_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
