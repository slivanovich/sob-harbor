{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGiuseppe Frezzolini: Giuseppe Frezzolini (9 November 1789 – 16 March 1861) was an Italian operatic bass.  Born in Orvieto, he studied singing in his native city with G. Pedoto.  He began his career in 1819 and was active in Italy's leading opera houses up into the 1840s.  He is best known for creating the role of Dr Dulcamara in the world premiere of Gaetano Donizetti's \"L'elisir d'amore\" at the Teatro della Canobbiana in Milan on 12 May 1832.  He also sang parts in the world premieres of two other Donizetti operas: Pasquale in \"Olivo e Pasquale\" (7 January 1827, Teatro Valle, Rome) and Belfiore in \"Alina, regina di Golconda\" (12 May 1828, Teatro Carlo Felice, Genoa).  He died in Orvieto in 1861.  He was the father of soprano Erminia Frezzolini.\n\nHeinrich Christian Macklot: Heinrich Christian Macklot (20 October 1799, Frankfurt am Main – 12 May 1832) was a German naturalist.\n\nClack Stone: Clack Stone (fl.  1827–1839) was a captain in the 27th Regiment Illinois Militia during the 1832 Black Hawk War.  He was in charge of a company mustered into service in May 1832 from Jo Daviess County, Illinois.  Stone was in charge of the garrison at the Apple River settlement in present-day Elizabeth during two war-related incidents.  In the first event, some horses were stolen from the fort in the prelude to the Battle of Waddams Grove.  The second event was an intense battle known as the Battle of Apple River Fort.  After the war, Stone operated a general store and helped establish the village of Elizabeth.\n\nDomenico Trimarchi: Domenico Trimarchi is an Italian bass-baritone opera singer.  He was born in Naples, where he studied singing at the Conservatory.  In 1970 he made his debut at La Fenice, Venice as Belcore in \"L'elisir d'amore\".  He made his British debut at the Edinburgh Festival in 1972 and first appeared at Covent Garden in 1975 playing Bartolo in \"The Barber of Seville\".  In \"The Times\" William Mann praised him as \"ripe, rubber-faced and a virtuoso patter singer.\"  Trimarchi reprised the role there between 1978 and 1987.  He has appeared at all the major opera-houses of the world, including La Scala, Milan, the Vienna State Opera and the Metropolitan Opera in New York.\n\nL'elisir d'amore: L'elisir d'amore (The Elixir of Love, ] ) is a comic opera (\"melodramma giocoso \") in two acts by the Italian composer Gaetano Donizetti.  Felice Romani wrote the Italian libretto, after Eugène Scribe's libretto for Daniel Auber's \"Le philtre\" (1831).  The opera premiered on 12 May 1832 at the Teatro della Canobbiana in Milan.\n\nJean Alfred Fournier: Jean Alfred Fournier (12 May 1832 – 25 December 1914) was a French dermatologist who specialized in the study of venereal disease.\n\nCharles Payne (cricketer, born 1832): Charles Payne (12 May 1832 – 18 February 1909) was an English cricketer active from 1857 to 1875 who played for Sussex and Kent.  He was born in East Grinstead and died in Tonbridge.  He appeared in 88 first-class matches as a right-handed batsman who sometimes kept wicket.  He scored 2,702 runs with a highest score of 137 and took 69 catches.  His bowling type is unknown, but he took seven wickets with three for 13 his best performance.\n\nFriedrich Moritz Brauer: Friedrich Moritz Brauer (12 May 1832, Vienna – 29 December 1904) was an Austrian entomologist who was Director of the Naturhistorisches Hofmuseum, Vienna, at the time of his death.  He wrote many papers on Diptera and Neuroptera.\n\nLe donne rivali: Le donne rivali is an intermezzo in two acts by composer Domenico Cimarosa with an Italian libretto by a now unknown poet.  It is speculated that Giuseppe Petrosellini may have been the author of the libretto.  The opera premiered at the Teatro Valle in Rome during Carnival in 1780.  The original choreography was created by Alberto Cavos, the original costumes by Antonio Dian, and the original scenery by Domenico Fossati.  Music critics particularly admire the final quintet that closes the opera.  In recent years, \"Le donne rivali\" has been occasionally revived and recorded.  In 1991, the Juilliard Opera Center intertwined the work with Mozart's unfinished opera \"Lo sposo deluso\", which shares the same libretto, to make one large work.\n\nCarl von Perbandt: Carl von Perbandt (12 May 1832 – 6 April 1911) was German landscape painter, who spent most of his career in Northern California.\n\nQuestion: Which character did Domenico Trimarchi portray in the Opera that first premiered on 12 May 1832?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the opera singer.\"\n    },\n    \"character_portrayed\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character portrayed by the singer.\"\n    },\n    \"opera_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the opera.\"\n        },\n        \"premiere_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The premiere date of the opera.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"premiere_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"singer_name\",\n    \"character_portrayed\",\n    \"opera_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "singer_name": {
        "type": "string",
        "description": "The name of the opera singer."
      },
      "character_portrayed": {
        "type": "string",
        "description": "The name of the character portrayed by the singer."
      },
      "opera_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the opera."
          },
          "premiere_date": {
            "type": "string",
            "format": "date",
            "description": "The premiere date of the opera."
          }
        },
        "required": [
          "title",
          "premiere_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "singer_name",
      "character_portrayed",
      "opera_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
