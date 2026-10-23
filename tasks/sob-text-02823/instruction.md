{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Crimson Rivers: The Crimson Rivers (French: \"Les Rivières Pourpres\" ) is a 2000 French psychological horror film starring Jean Reno and Vincent Cassel.  The film, which was directed by Mathieu Kassovitz, is based on the best-selling novel \"Les Rivières Pourpres\".  Its screenplay was co-written by the book's author, Jean-Christophe Grangé.\n\nDe plus belle: De plus belle is a 2017 French film directed by Anne-Gaëlle Daval.  A romantic comedy starring Florence Foresti and Mathieu Kassovitz, it tells the story of a breast cancer survivor's efforts to rebuild her life.  It received mixed reviews from critics.\n\nRebellion (2011 film): Rebellion (French: L'Ordre et la Morale ) is a 2011 French historical drama film directed, produced, co-written, co-edited by and starring Mathieu Kassovitz.  Set in New Caledonia but filmed in Tahiti, the film recreates a version of the Ouvéa cave hostage taking in 1988.  Kassovitz, Benoît Jaubert and Pierre Geller were collectively nominated for the 2012 Best Writing (Adaptation) César Award.\n\nBirthday Girl: Birthday Girl is a 2001 British comedy thriller film directed by Jez Butterworth.  The plot focuses on English bank clerk John Buckingham, who orders a Russian mail-order bride, Nadia.  It becomes clear upon her arrival that Nadia cannot speak English, and early into her stay, two mysterious men come to the house claiming to be her cousin and cousin's friend.  The film features Nicole Kidman, Ben Chaplin, Mathieu Kassovitz, and Vincent Cassel.  English and Russian are spoken interchangeably in the film.\n\nAmélie: Amélie (also known as Le fabuleux destin d'Amélie Poulain; ] ; English: \"The Fabulous Destiny of Amélie Poulain\" ) is a 2001 French romantic comedy film directed by Jean-Pierre Jeunet.  Written by Jeunet with Guillaume Laurant, the film is a whimsical depiction of contemporary Parisian life, set in Montmartre.  It tells the story of a shy waitress, played by Audrey Tautou, who decides to change the lives of those around her for the better, while struggling with her own isolation.  The film was a co-production between companies in France and Germany.  Taking in over $33 million in a limited theatrical release, it is to date the highest-grossing French-language film released in the United States, and one of the biggest international successes for a French movie.\n\nThe Lookout (2012 film): The Lookout (French: Le guetteur , Italian: Il cecchino ) is a French-Belgian-Italian crime film from 2012, directed by Michele Placido and starring Daniel Auteuil and Mathieu Kassovitz.  It marked Placido's directorial debut outside Italy; a result of the French box office success of his 2010 film \"Angel of Evil\".\n\nMathieu Kassovitz: Mathieu Kassovitz (born 3 August 1967) is a French director, screenwriter, producer, editor, and actor probably best known in Francophone countries for his role as Nino Quincampoix in \"Amélie\" (\"Le Fabuleux Destin d'Amélie Poulain\"; 2001).  Kassovitz is also the founder of MNP Entreprise, a film production company.\n\nMNP Entreprise: Founded in 2000 by Mathieu Kassovitz, MNP is a French film production company headed by Mathieu Kassovitz and Guillaume Colboc.\n\nXCiTés: XCiTés: the Flamingo Book of New French Writing is an anthology edited by Georgia de Chamberet of French writing in translation which \"aims to smash the stereotypes\" by a new generation of writers who were unpublished in English at the time of publication (2000).  The book includes stories by Frédéric Beigbeder, Mehdi Belhaj Kacem, Tonino Benacquista, Marie Desplechin, Ilan Duran Cohen, Agnès Desarthe, Virginie Despentes, Guillaume Dustan, Eric Faye, Michel Houellebecq, Mathieu Kassovitz, Mathieu Lindon, Mounsi, Lorette Nobécourt, Vincent Ravalec, Abdourahman Waberi.  The INDEPENDENT said of it: \"French society is diverse, richly multi-cultural - and the writing in this collection represents some of that diversity.  If a writer is clearly wonderful - Abdourahman Waberi (originally from Djibouti) or Mounsi (Algerian) - then we want more.  The last three inclusions - scenes from Mathieu Kassovitz's film La Haine, a piece on the house music scene by DJ Tov and an interview with Chelsea defender Marcel Desailly illustrate the point of this kind of new fiction which is to question traditional modes of publishing.  The French are tired of their image.\"\n\nÈ pericoloso sporgersi: È pericoloso sporgersi is a 1984 Belgian short film written and directed by Jaco Van Dormael.  The short film was shot in 1984 in Belgium.  The film starred Mathieu Chemin, Joëlle Waterkeyn and Dirk Pauwels.  It was produced by Iblis Films (Brussels). \" È pericoloso sporgersi\" tells the story of a child who has been thrust into a position where he must make an impossible decision.\n\nQuestion: Which 2001 French romantic comedy film starred Mathieu Kassovitz as Nino Quincampoix?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"role_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the role played by the actor.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"role_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"actor_details\",\n    \"director\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role_name": {
            "type": "string",
            "description": "The name of the role played by the actor."
          }
        },
        "required": [
          "actor_name",
          "role_name"
        ],
        "additionalProperties": false
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "actor_details",
      "director"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
