{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPublic Eye Magazine: The Public Eye Magazine is published by Political Research Associates in Somerville, Massachusetts.  The Magazine was founded in 1977 by the Public Eye Network.  It currently contains investigative articles about \"movements, institutions, and ideologies that undermine human rights.\"  Its primary focus is on right-wing groups in the United States.\n\nSheena Easton: Sheena Shirley Easton (née Orr; born 27 April 1959) is a Scottish singer, recording artist and stage and screen actress with dual British-American nationality.  Easton first came into the public eye as the focus of an episode in the first British musical reality television programme \"The Big Time: Pop Singer\", which recorded her attempts to gain a record contract and her eventual signing with EMI Records.\n\nPetrović: Petrović (or Petrovich) is a Slavic last and second name, found in countries with Slavic populations.  Examples of such countries are: Croatia, Serbia, Montenegro, Bosnia and Herzegovina, Slovenia, Macedonia and Russia.  This surname or last name is not tied to any nationality.  It is normal Slavic surname deriving from \"Petar\", which is equivalent to Peter in English.  The part \"ov\" designates possession: \"Petrov\" means \"Peter's\".  The suffix \"ić\" is a diminutive designation, or descendant designation.  So, the last name can be translated as \"Peter's son\", equivalent to the English last name of Peterson.\n\nPublic Eye Network: The Public Eye Network is a group of progressive investigative reporters, licensed investigators, paralegal investigators, attorneys, and activists who share information about political repression and right-wing movements that undermine civil liberties and civil rights.  It was formed in the 1970s from three pre-existing groups, the editors of the \"Public Eye Magazine,\" the magazine sponsoring organization, the Repression Information Project (RIP), and the Guild Investigative Group.  Several people who worked as editors or volunteer staff at \"CounterSpy Magazine\" joined the network.\n\nThe Public Eye (film): The Public Eye is a 1992 neo-noir film produced by Sue Baden-Powell and written and directed by Howard Franklin, starring Joe Pesci and Barbara Hershey.  Stanley Tucci and Richard Schiff appear in supporting roles.\n\nAgranov: Agranov (Russian: Агранов ; masculine) or Agranova (Агранова ; feminine) is a Russian last name.  It derives from the Russian first name Gran (from the Latin word meaning \"grain\"), which transformed into the last name Granov.  That last name transformed into \"Agranov\", as the latter is easier to pronounce.\n\nDeath Note 2: The Last Name: Death Note 2: The Last Name (デスノート the Last name , Desu Nōto the Last name ) a 2006 Japanese detective supernatural psychological horror thriller film directed by Shūsuke Kaneko.  The film is the second in a series of live-action Japanese films released in 2006 based on the \"Death Note\" manga and anime series by Tsugumi Ohba and Takeshi Obata.  The film primarily centers on a university student named Light Yagami who decides to rid the world of evil with the help of a supernatural notebook that kills anyone whose name is written in it.  The film was produced by Nippon Television, and distributed by Warner Bros.  Pictures Japan.  It was licensed by VIZ Pictures.  A spin-off, \"\", was released in 2008.  A sequel, \"\", was released in 2016.\n\nJoia Jefferson Nuri: Joia Jefferson Nuri is a communications strategist and human rights activist from the United States.  She is an expert in human rights advocacy.  She is the Director and founder of In The Public Eye Communications.  She is a consultant and senior adviser for human rights organizations and political activists.  In the past, she has worked as a Technical Director and Senior Producer for news agencies such as NBC, CBS, NPR, and C-SPAN.  Her topics of interest include racism, perceptions of minorities, sports and emerging democracies in West Africa.  Today she is a contributor to political television and radio talk shows and is the author of a video blog on how cultural and historical images shape current politics and policy.  Her client list includes Harry Belafonte, TransAfrica, the Calvert Foundation, Truly Living Well Center for Natural Urban Agriculture and SNV USA.  Her company, In The Public Eye Communications, has served as event strategists for two Presidential Inaugural galas (2009 and 2013), Smithsonian Institution fundraisers, embassy celebrations, annual conferences, seminars and press events.\n\nNanduri: Those with the last name Nanduri are said to hail from the village of Nanduru which is located near Bapatla and Ponnur (small towns in the Guntur District of Andhra Pradesh).  There is a village called Nanduru in East Godavari District of Andhra Pradesh as well which leads to some ambiguity.  Those with this last name could be Niyogi Brahmins or Sri Vaishnava Brahmins or they could also be from a caste other than the Brahmin caste.  One of the other known caste is Bhatraju.  For the most part, those with this last name are predominantly Brahmins.  Many have migrated from Nanduru and they have settled in various part of Andhra Pradesh.  Some are known to have settled in a village known as Lingala, which in located in the Khammam District of Andhra Pradesh.  Lingala is said to have been ruled by kings with the last name Nanduri hundreds of years ago.\n\nStanley Tucci: Stanley Tucci ( ; ] ; born November 11, 1960) is an American character actor, writer, producer and film director.\n\nQuestion: The Public Eye features an actor with the last name Tucci of what nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor mentioned in the film.\"\n    },\n    \"actor_last_name\": {\n      \"type\": \"string\",\n      \"description\": \"The last name of the actor.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actor_name\",\n    \"actor_last_name\",\n    \"actor_nationality\",\n    \"film_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor mentioned in the film."
      },
      "actor_last_name": {
        "type": "string",
        "description": "The last name of the actor."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "film_title",
      "actor_name",
      "actor_last_name",
      "actor_nationality",
      "film_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
