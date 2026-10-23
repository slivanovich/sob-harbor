{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWanda Media: Wanda Media () is a Chinese film production company and distributor.  In 2014, the company was the largest Chinese private film production company and second-largest overall Chinese production company in China by market share, with 3.17%, and the fifth-largest film distributor, with 5.2% of the market.\n\nSaga Studios: Saga Studio (or Saga Film A/S) was a film production company in Denmark founded by John Olsen.  Several years after Olsen co-founded ASA Film Studio with Lau Lauritzen Jr. and Henning Karmark, there was a falling out between the partners over financial issues.  Olsen took his interests and opened Saga Studio as a separate company in 1942, which included a film studio, film rental business and the Saga Cinema, becoming the fourth largest film production company in Denmark and known for their comedy films.  More than 80 films were produced by the studio from 1942 through 1974.  Some of its most successful films were the popular comedies of Danish comedian Dirch Passer.\n\nSri Venkateswara Creations: Sri Venkateswara Creations (Telugu: శ్రీ వెంకటేశ్వర క్రియేషన్స్) is an Indian film production company established by Dil Raju, an Indian film producer.  The company is based in Hyderabad.  The company was established in 2003.  Raju has produced several Telugu films under this company.  The company also has a subsidiary distribution company called Sri Venkateswara Film Distributors under which several films have been distributed.  Telugu movies produced by the company include \"Arya\" (2004), \"Bhadra\" (2005), \"Bommarillu\" (2006), \"Mr. Perfect\" (2011) and \"Seethamma Vakitlo Sirimalle Chettu\"(2013).  The company also has another subsidiary film production company called Matinee Entertainments under which movies including \"Maro Charitra\" and \"Gaganam\" have been produced.\n\nPrince Entertainment P4: Prince Entertainment P4 is an Indian film production company operating from Kolkata, West Bengal.  \"Prince Entertainment P4\" is doing full length Bengali feature film production and distribution.  Pijush Saha is the head of the company.  Along with film production, this company is doing production of various Bengali television serials.\n\nSouthern International Productions: Southern International Productions was an Australian film production company established in the 1950s by Lee Robinson and Chips Rafferty.  For a few years it was the most prolific film production company in Australia, pioneering international co-productions with France, but a series of box office failures starting with \"Dust in the Sun\" caused it to be liquidated.  Rafferty left producing but Lee Robinson later formed another company, Fauna, with actor John McCallum.\n\nThe Foster Photoplay Company: The Foster Photoplay Company was a film production company based in Chicago, Illinois.  It was founded in 1910 by William Foster (also known as Juli Jones).  It is widely considered to be the first film production company established by an African-American featuring all African-American casts.  The company released a number of critically acclaimed films, including \"The Railroad Porter\" (1913), \"The Fall Guy\" (1913), and \"The Butler\" (1913).  After the release of \"The Railroad Porter\" and \"The Fall Guy\", the company also became known for their films' slapstick-style comedy.\n\nUltra Media &amp; Entertainment: Ultra Media & Entertainment earlier known as Ultra Distributors, is an Indian Film production company established in year 1982.  It started as Home Video distribution and gradually forayed into film production & theatrical distribution.  It is also engaged in multiple aspects of entertainment, including post production service and film distribution.  Ultra has a library of over 1500 titles of award winning and blockbuster feature films, TV Dramas, Animation, Music and digital content.  The company is into post production services such as Scanning, Restoration, Colorization, 2D to Stereoscopic 3D Conversion and Merchandising.\n\nKate &amp; Leopold: Kate & Leopold is a 2001 romantic-comedy fantasy that tells a story of a duke who travels through time from New York in 1876 to the present and falls in love with a woman in modern New York.  The film is directed by James Mangold and stars Meg Ryan, Hugh Jackman and Liev Schreiber.\n\nSeed Productions: Seed Productions was a film production company associated with 20th Century Fox, started by Australian actors Hugh Jackman and Deborra-Lee Furness, with producer and business partner John Palermo.\n\nHugh Jackman: Hugh Michael Jackman (born 12 October 1968) is an Australian actor, singer, and producer.  Jackman has won international recognition for his roles in a variety of film genres.  He is known for his long-running role as Wolverine in the \"X-Men\" film series, as well as for his lead roles in films such as the romantic-comedy fantasy \"Kate & Leopold\" (2001), the action-horror film \"Van Helsing\" (2004), the magic-themed drama \"The Prestige\" (2006), the epic fantasy drama \"The Fountain\" (2006), the epic historical romantic drama \"Australia\" (2008), the film version of \"Les Misérables\" (2012), and the thriller \"Prisoners\" (2013).  His work in \"Les Misérables\" earned him his first Academy Award nomination for Best Actor and his first Golden Globe Award for Best Actor – Motion Picture Musical or Comedy in 2013.\n\nQuestion: This film production company was started by an Australian who had a lead role in what 2001 romantic-comedy fantasy?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_production_company\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film production company.\"\n    },\n    \"founder_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Australian actor who started the company.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"lead_role_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film in which the actor had a lead role.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_production_company\",\n    \"founder_actor\",\n    \"lead_role_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_production_company": {
        "type": "string",
        "description": "The name of the film production company."
      },
      "founder_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Australian actor who started the company."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actor."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "lead_role_film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film in which the actor had a lead role."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "title",
          "year",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_production_company",
      "founder_actor",
      "lead_role_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
