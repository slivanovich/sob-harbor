Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Meir bar Hiyya Rofe: Meir bar Hiyya Rofe (17th century; the "Encyclopedia Judaica" article gives the years of 1610 and 1690 as the possible years of birth and death respectively) was a Hebron rabbi, known among other things for his tours of Europe as an emissary from the Holy Land on behalf of the Jewish community of Hebron.  His father, Hiyya Rofe, was a very learned rabbi from Safed.  Orphaned at a young age, Meir studied in Hebron, leaving about 1648 as an emissary to Italy, Holland, and Germany.  On his return journey, he stayed for two years in Italy to publish "Ma'aseh Ḥiyya" (Venice, 1652), his father's talmudic novellae and responsa.  In Amsterdam he had influenced the wealthy Abraham Pereyra to found a "yeshiva" in Hebron to be called "Hesed le-Avraham", of which Meir himself became the head scholar.

Actantial model: In structural semantics, the actantial model, also called the actantial narrative schema, is a tool used to analyze the action that takes place in a story, whether real or fictional.  It was developed in 1966 by semiotician Algirdas Julien Greimas.

Lauri Pilter: Lauri Pilter (also known as Larats Pilter; born 15 October 1971 in Tallinn) is an Estonian writer, translator and literary scientist.

DICE model: The Dynamic Integrated Climate-Economy model, referred to as the DICE model or Dice model, is a computer-based integrated assessment model developed by William Nordhaus that “integrates in an end-to-end fashion the economics, carbon cycle, climate science, and impacts in a highly aggregated model that allows a weighing of the costs and benefits of taking steps to slow greenhouse warming."  Nordhaus also developed the RICE model (Regional Integrated Climate-Economy model), a variant of the DICE model that was updated and developed alongside the DICE model.  Others who collaborated with Nordhaus to develop the model include David Popp, Zili Yang, Joseph Boyer, and other colleagues.

Square Books: Square Books is a general independent bookstore in three separate historic buildings (about 100 feet apart) on the town square of Oxford, Mississippi, widely known among readers as the hub of William Faulkner's "postage stamp of native soil," Yoknapatawpha.  The main store, Square Books, is in a two-story building with a cafe and balcony on the second floor; Off Square Books is a few doors down from the main store and has lifestyle sections such as gardening and cookbooks; and Square Books Jr, the children's bookstore, is in a building adjacent to the historic Neilson's Department Store, which has continuously operated since 1839.  Square Books is known for its strong selection of literary fiction, books on the American South and by Southern writers, a large inventory of bargain books, and its emphasis on books for children.  The store hosts the popular Thacker Mountain radio show and over 150 author events a year, and is a founding co-sponsor of the Oxford Conference for the Book.

Algirdas Julien Greimas: Algirdas Julien Greimas (] ; born "Algirdas Julius Greimas"; 9 March 1917 – 27 February 1992), was a French-Lithuanian literary scientist, known among other things for the Greimas Square ("le carré sémiotique").  He is, along with Roland Barthes, considered the most prominent of the French semioticians. With his training in structural linguistics, he added to the theory of signification and laid the foundations for the Parisian school of semiotics.  Among Greimas's major contributions to semiotics are the concepts of isotopy, the actantial model, the narrative program, and the semiotics of the natural world.  He also researched Lithuanian mythology and Proto-Indo-European religion, and was influential in semiotic literary criticism.

Actant: In narrative theory, actant is a term from the actantial model of semiotic analysis of narratives.  The term also has uses in linguistics, sociology, computer programming theory, and astrology.

Yevgeny Bokarev: Yevgeny Alekseyevich Bokarev (Russian: Евгений Алексеевич Бокарёв , ] ) (25 February 1904 - 11 March 1971) was a Soviet linguist known among other things for his work on the Northeast Caucasian languages and his interlinguistics works; he was a member of the Academy of Esperanto.

Semiotic square: The semiotic square, also known as the Greimas square, is a tool used in structural analysis of the relationships between semiotic signs through the opposition of concepts, such as feminine-masculine or beautiful-ugly, and of extending the relevant ontology.

10 Things You Don't Know About: 10 Things You Don't Know About is an American history/biography television series on H2.  It was initially presented by historian David Eisenbach for one season.  Eisenbach was succeeded as host by musician Henry Rollins for the next two seasons.  Each episode of the show presents ten facts about a particular historical figure, group, event, or aspect that are not widely known among the general public.  Each fact is accompanied by relevants clips and, during Rollins's tenure, interviews with experts, as well as man-on-the-street interviews.  The first season also featured results of an online poll surrounding the ten facts.

Question: French-Lithuanian literary scientist, known among other things for the Greimas Square, also developed the Actantial model in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "nationality": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The nationalities of the person."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the person."
        },
        "other_known_contribution": {
          "type": "string",
          "description": "Another significant contribution or work the person is known for."
        }
      },
      "required": [
        "name",
        "nationality",
        "occupation",
        "other_known_contribution"
      ],
      "additionalProperties": false
    },
    "model_developed": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the model developed."
        },
        "development_year": {
          "type": "integer",
          "description": "The year the model was developed."
        }
      },
      "required": [
        "name",
        "development_year"
      ],
      "additionalProperties": false
    },
    "is_developer": {
      "type": "boolean",
      "description": "Indicates if the person is the developer of the model."
    }
  },
  "required": [
    "person",
    "model_developed",
    "is_developer"
  ],
  "additionalProperties": false
}
