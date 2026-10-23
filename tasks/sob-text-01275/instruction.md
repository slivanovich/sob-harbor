{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nL'Express: L'Express (] ) is a French weekly news magazine headquartered in Paris.  The weekly stands at the political center in the French media landscape, and has a lifestyle supplement, \"L'Express Styles\", and a job supplement, \"Réussir\".\n\nMartin Boudot: Martin Boudot is a French investigative journalist and documentary filmmaker based in Paris, France.  He is part of Premières Lignes Télévision, a TV press agency specialized in investigative journalism.  Since 2012, he has been working for \"Cash Investigation\", the award-winning investigative magazine broadcast on France 2, the French national TV news network.  He has won the 2015 DIG Award, the European investigative documentary of the year for \"The real price of your mobile phone\".  He was among the 2015 and 2017 finalists of the Albert Londres Prize, the highest French journalistic distinction.\n\nL'Express (disambiguation): L'Express is a French weekly news magazine.\n\nThe New Times (magazine): The New Times (Russian: Но́вые Времена́ ) is a Russian language magazine in Russia.  The magazine was founded in 1943.  The current version, established in 1988, , is a liberal, independent Russian weekly news magazine, publishing for Russia and Armenia.  (During the Soviet times it was a multi-language political magazine which followed the official party line.)  Its chief editor is Russian investigative journalist, political scientist, writer and radio host Yevgenia Albats.\n\nBenoît Bringer: Benoît Bringer (born 1979) is a French investigative journalist and documentary filmmaker based in Paris, France.  He is part of the Pulitzer Prize-winning ICIJ's Panama Papers team and director of \"Panama Papers : The hold-up of the century\", a two-hour documentary aired on France 2 TV investigative series \"Cash Investigation\".  He is also the director of \"Obama's dirty war\"\" broadcast on Canal+, an investigation in Yemen and Pakistan on civilian casualties from US drone strikes.  His film \"Primaire au PS : l'improbable scénario\", a 90-minute documentary about the first political primary race in France, which aired on Canal+, was selected for FIPA, the Festival International de Programmes Audiovisuels, held in Biarritz, France.\n\nDenis Robert: Denis Robert (born 9 May 1958 in Moyeuvre-Grande, Moselle) is a French investigative journalist, novelist and filmmaker.  He formerly worked for 12 years for the newspaper \"Libération\".  In 2008, he was involved in a polemic with Philippe Val, former director of the magazine Charlie Hebdo, and journalist Edwy Plenel.\n\nLe Pèlerin: Le Pèlerin, today simply called Pèlerin, is a French weekly news magazine published in France.\n\nLirio Abbate: Lirio Abbate (born on 26 February 1971 in Castelbuono) is an Italian journalist of the weekly news magazine L'espresso.  Before was a correspondent in Sicily for the news agency ANSA and La Stampa newspaper.\n\nVSD (French magazine): VSD is a French weekly news, celebrity and leisure magazine, published on Thursdays in France.  The name is formed from the first letters of the French names for Friday (Vendredi), Saturday (Samedi) and Sunday (Dimanche).\n\nJean-Marie Pontaut: Jean-Marie Pontaut (born 26 February 1947 in Neuilly-sur-Seine) is a French investigative journalist, working for the daily \"L'Express\", after a start and a return trip to \"Le Point\".\n\nQuestion: Jean-Marie Pontaut (born 26 February 1947 in Neuilly-sur-Seine) is a French investigative journalist, working for L'Express, a French weekly news magazine headquartered in which city in France?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"journalist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the journalist.\"\n    },\n    \"journalist_role\": {\n      \"type\": \"string\",\n      \"description\": \"The professional role of the journalist.\"\n    },\n    \"magazine_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the magazine the journalist works for.\"\n    },\n    \"magazine_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of magazine.\"\n    },\n    \"headquarters_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the magazine is headquartered.\"\n    }\n  },\n  \"required\": [\n    \"journalist_name\",\n    \"magazine_name\",\n    \"headquarters_city\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "journalist_name": {
        "type": "string",
        "description": "The name of the journalist."
      },
      "journalist_role": {
        "type": "string",
        "description": "The professional role of the journalist."
      },
      "magazine_name": {
        "type": "string",
        "description": "The name of the magazine the journalist works for."
      },
      "magazine_type": {
        "type": "string",
        "description": "The type of magazine."
      },
      "headquarters_city": {
        "type": "string",
        "description": "The city where the magazine is headquartered."
      }
    },
    "required": [
      "journalist_name",
      "magazine_name",
      "headquarters_city"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
