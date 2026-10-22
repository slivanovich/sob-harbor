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
Patrick Magee (actor): Patrick George McGee (31 March 192214 August 1982), known professionally as Patrick Magee, was a Northern Irish actor and director.  He was known for his collaborations with Samuel Beckett and Harold Pinter, as well as creating the role of the Marquis de Sade in the original stage and screen productions of "Marat/Sade".  He also appeared in horror films and in two Stanley Kubrick films, "A Clockwork Orange" and "Barry Lyndon".

La Bête (film): The Beast (French: "La Bête" ) is a 1975 X rated French erotic fantasy horror film written, edited, and directed by Walerian Borowczyk.  Although sometimes compared with "Beauty and the Beast", there are no parallels in the plot except that it features the relationship between a beast (monster) and a woman.  The film was noted for its explicit sexual content upon its initial release.  It has become a cult film.

Walerian Borowczyk: Walerian Borowczyk (21 October 1923 – 3 February 2006) was an internationally known Polish film director described by film critics as a 'genius who also happened to be a pornographer'.  He directed 40 films between 1946 and 1988.  Borowczyk settled in Paris in 1959.  His career as a film director was mainly in France.

Docteur Jekyll et les femmes: Docteur Jekyll et les femmes, also known as Blood of Dr. Jekyll, is a 1981 French–West German horror film directed by Walerian Borowczyk.  The film is a variation on Robert Louis Stevenson's story "Strange Case of Dr Jekyll and Mr Hyde" and stars Udo Kier, Marina Pierro, Patrick Magee, Howard Vernon and Gérard Zalcberg.

Lisbeth Hummel: Lisbeth Hummel (born 1952 in Copenhagen, Denmark) is a Danish film actress.  She is known for the controversial film "The Beast", directed by Walerian Borowczyk, and "" and "Dangerous Women", both directed by her husband .  She is now working as an artist, and lives in Denmark and Italy.

Mr. and Mrs. Kabal's Theatre: Mr. and Mrs. Kabal's Theatre ("Théâtre de Monsieur & Madame Kabal") is a 1967 French animated film directed by Walerian Borowczyk.  It is Borowczyk's first feature-length film and his last animated film.  It consists of a sequence of loosely connected scenes, much like a vaudeville program, in which Mr. and Mrs. Kabal perform absurd, surreal, and sometimes cruel acts.  Borowczyk introduced the personnel in his short film "Le Concert de Monsieur et Madame Kabal" in 1962.

Immoral Tales (film): Immoral Tales (French: "Contes immoraux" ) is a 1973 French anthology film directed by Walerian Borowczyk.  The film was Borowczyk's most sexually explicit at the time.  The film is split into four erotic-themed stories that involve the loss of virginity, masturbation, bloodlust, and incest.

The Margin (film): The Margin (French: "La Marge" , also known as "The Streetwalker" and "Emmanuelle 77") is a 1976 French erotic drama film written and directed by Walerian Borowczyk and starring Sylvia Kristel.  It is loosely based on the novel "The Margin" by André Pieyre de Mandiargues.

Immoral Women: Immoral Women (French: "Les héroïnes du mal" ) is a 1979 French erotic drama directed by Walerian Borowczyk, written by Borowczyk and André Pieyre de Mandiargues and starring Jean-Claude Dreyfus, Marina Pierro and Françoise Quéré.

Goto, Island of Love: Goto, Island of Love (French: Goto, l'île d'amour ) is a 1968 French drama film directed by Walerian Borowczyk and starring Pierre Brasseur.

Question: The actor Patrick George McGee died a year after starring in the release what Walerian Borowczyk directed film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the actor."
        },
        "death_year": {
          "type": "integer",
          "description": "The year the actor died."
        }
      },
      "required": [
        "name",
        "death_year"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director_name": {
          "type": "string",
          "description": "The name of the film's director."
        },
        "genre": {
          "type": "string",
          "description": "The primary genre of the film."
        },
        "starring_actors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of actors starring in the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "director_name",
        "genre",
        "starring_actors"
      ],
      "additionalProperties": false
    },
    "temporal_relationship": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "description": "Description of the temporal relationship between the film's release and the actor's death."
        },
        "years_before_actor_death": {
          "type": "integer",
          "description": "The number of years the film was released before the actor's death."
        }
      },
      "required": [
        "description",
        "years_before_actor_death"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_details",
    "film_details",
    "temporal_relationship"
  ],
  "additionalProperties": false
}
