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
Taxandria (film): Taxandria (1994) is a partially animated fantasy film by Raoul Servais, collaborating on a script with Frank Daniel and French writer Alain Robbe-Grillet, and starring, among others, Armin Mueller-Stahl.  Being Servais's first and to date only feature film, "Taxandria" is notable for the use of Servais's distinct animation style, the "servaisgraphie", as well as its connection to the Belgian graphic novel series "Les Cités Obscures" whose creator François Schuiten was the film's production designer.

Zofia Romer: Zofia Romer (February 16, 1885 – August 23, 1972), née Zofia Dembowska was a Polish painter.  She was born in 1885 in Estonia to well-known physician Tadeusz Dembowski and his wife Matylda.  She grew up in Lithuania and Poland studying under various painters.  As a young woman she was romantically linked with Bronisław Malinowski and Stanisław Ignacy Witkiewicz.

Last Year at Marienbad: L'Année dernière à Marienbad (released in the US as Last Year at Marienbad and in the UK as Last Year in Marienbad) is a 1961 French-Italian film directed by Alain Resnais from a screenplay by Alain Robbe-Grillet.

Louis Iribarne: Louis Iribarne is a translator of Polish into English.  He has translated works by Witold Gombrowicz, Stanisław Lem, Czesław Miłosz, Bruno Schulz and Stanisław Ignacy Witkiewicz.  He has also taught Polish and Russian literature at the University of Toronto, from where he retired in 1998.

Insatiability: Insatiability (Polish: Nienasycenie ) is a novel by the Polish writer, dramatist, philosopher, painter and photographer, Stanisław Ignacy Witkiewicz (Witkacy).  "Nienasycenie" was written in 1927 and first published in 1930.  It is his third novel, considered by many to be his best.  It consists of two parts: Przebudzenie (Awakening) and Obłęd (The madness).

N. a pris les dés...: N. a pris les dés... (] , French for "N. has taken the dice...") is a 1971 French experimental independent underground drama art film directed by Alain Robbe-Grillet.

Stanisław Ignacy Witkiewicz: Stanisław Ignacy Witkiewicz (] ; 24 February 188518 September 1939), commonly known as Witkacy, was a Polish writer, painter, philosopher, playwright, novelist, and photographer active in the interwar period.

Alain Robbe-Grillet: Alain Robbe-Grillet (] ; 18 August 1922 – 18 February 2008) was a French writer and filmmaker.  He was one of the figures most associated with the "Nouveau Roman" (new novel) trend of the 1960s, along with Nathalie Sarraute, Michel Butor and Claude Simon.  Alain Robbe-Grillet was elected a member of the Académie française on 25 March 2004, succeeding Maurice Rheims at seat No. 32.  He was married to Catherine Robbe-Grillet (née Rstakian).

Daniel C. Gerould: Daniel Charles Gerould (March 28, 1928 – February 13, 2012) was the Lucille Lortel Distinguished Professor of Theatre and Comparative Literature at the CUNY Graduate Center and Director of Publications of the Martin E. Segal Theatre Center.  A scholar, teacher, translator, editor, and playwright, Gerould was a specialist in US melodrama, Central and Eastern European theatre of the twentieth century, and "fin-de-siècle" European avant-garde performance.  Gerould was one of the world’s most recognized “Witkacologists,” a leading scholar and translator of the work of Polish playwright, novelist, painter, and philosopher Stanisław Ignacy Witkiewicz ("Witkacy").  Gerould was best known for introducing English-language audiences to the writings of Witkiewicz through such work as "Stanisław I. Witkiewicz, The Beelzebub Sonata: Plays, Essays, Documents" (PAJ Publications 1980), "Witkacy: Stanisław Ignacy Witkiewicz as an Imaginative Writer" (University of Washington Press, 1981), "The Witkiewicz Reader" (Northwestern University Press, 1992), and his original translations of most of Witkiewicz’s plays.

Fiction International: Fiction International is a literary magazine devoted to innovative forms of fiction and non-fiction which addresses progressive political ideals.  Founded at St. Lawrence University in New York City by Joe David Bellamyin 1973, the magazine moved to San Diego State University in 1983, where it has been "edited by Harold Jaffe and Larry McCaffery until 1992, when Harold Jaffe assumed sole editorship".  Over the years, the magazine has published works by J.M. Coetzee, Claribel Alegría, Robert Coover, William S. Burroughs, Alberto Moravia, Malcolm X, Allen Ginsberg, Marguerite Duras, Edmund White, Kathy Acker, Eckhard Gerdes, and Alain Robbe-Grillet.

Question: What was common for both Alain Robbe-Grillet and Stanisław Ignacy Witkiewicz?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_attribute": {
      "type": "string",
      "description": "The attribute or profession common to both individuals."
    },
    "person_a_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the first person."
        },
        "notable_works_or_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of notable works or roles associated with the first person."
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    },
    "person_b_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the second person."
        },
        "notable_works_or_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of notable works or roles associated with the second person."
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "common_attribute",
    "person_a_details",
    "person_b_details"
  ],
  "additionalProperties": false
}
