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
Robin Hood and the Pirates: Robin Hood and the Pirates (Italian: "Robin Hood e i pirati" ) is a 1960 Italian adventure film directed by Giorgio Simonelli and starring Lex Barker and Jackie Lane.

Peter Weir: Peter Lindsay Weir, AM ( ; born 21 August 1944) is an Australian film director.

Two Hearts Among the Beasts: Two Hearts Among the Beasts (Italian: Due cuori fra le belve) is a 1943 Italian comedy film directed by Giorgio Simonelli and starring Totò, Vera Carmi and Enrico Glori.  A dancing master takes part in an expedition to Africa find a missing anthropologist whose daughter he is in love with.

Giorgio Simonelli: Born in Rome, Simonelli obtained a high school diploma in business studies, then he started working as a journalist, and even as a film critic, for the weekly magazines "Avvenimento" and "Gente nostra".  In 1928, at 22, he made his directorial debut co-directing with Nicola Fausto Neroni "Maratona" and two years later he was among the screenwriters of the first Italian talking film, "The Song of Love" by Gennaro Righelli.  From 1934 Simonelli mainly devoted himself to the film editing, then, since 1940, he reprised his activity as a director specializing in comedy films of great commercial success, in which he directed some of the more popular actors of the period, including Totò, Eduardo and Peppino De Filippo, Nino Taranto, Renato Rascel, Walter Chiari, Ugo Tognazzi, Macario, Alberto Sordi and Aldo Fabrizi.  He concluded his career by signing many successful works interpreted by the comedy duo Franco Franchi and Ciccio Ingrassia.  His last film was the western-parody "Two Sons of Ringo", in which just before the end of filming he was replaced by Giuliano Carnimeo for health reasons.

Carlo Bellero: Carlo Bellero (1911–1988) was an Italian cinematographer active between 1941 and 1964.  He is notable for his work with several directors, including Giorgio Simonelli, Turi Vasile, Ermanno Olmi, Mario Amendola, Domenico Paolella, Giorgio Capitani and Francesco De Robertis ("La nave bianca" and "Uomini sul fondo").

It Happened at the Police Station: It Happened at the Police Station (Italian: Accadde al commissariato) is a 1954 Italian comedy film directed by Giorgio Simonelli and starring Nino Taranto, Alberto Sordi and Walter Chiari.

Noi siamo due evasi: Noi siamo due evasi is a 1959 Italian crime-comedy film directed by Giorgio Simonelli.

Saluti e baci: Saluti e baci is a Franco-Italian comedy-drama film directed by Maurice Labro and Giorgio Simonelli and released in 1953.

Passionate Song: Passionate Song (Italian: Canzone appassionata) is a 1953 Italian musical drama film directed by Giorgio Simonelli and starring  Nilla Pizzi, Gérard Landry and Vira Silenti.

Ursus in the Land of Fire: Ursus in the Land of Fire (Italian: "Ursus nella terra di fuoco" ), released directly to U.S. television as Son of Hercules in the Land of Fire, is a 1963 Italian peplum film directed by Giorgio Simonelli and starring Ed Fury as Ursus, and Adriano Micantoni as the evil usurper, Amilcare.

Question: Are Giorgio Simonelli and Peter Weir both directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_directors": {
      "type": "boolean",
      "description": "True if both individuals are identified as directors, false otherwise."
    },
    "individuals_involved": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_a_director": {
            "type": "boolean",
            "description": "True if the individual is identified as a director in the context."
          },
          "known_profession": {
            "type": "string",
            "description": "The primary profession explicitly stated for the individual in the context."
          }
        },
        "required": [
          "name",
          "is_a_director",
          "known_profession"
        ],
        "additionalProperties": false
      }
    },
    "reasoning_summary": {
      "type": "string",
      "description": "A brief summary of the evidence supporting the answer."
    }
  },
  "required": [
    "are_both_directors",
    "individuals_involved",
    "reasoning_summary"
  ],
  "additionalProperties": false
}
