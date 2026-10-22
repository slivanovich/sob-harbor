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
Little Monsters (disambiguation): Little Monsters is a 1989 comedy-drama film starring Fred Savage and Howie Mandel.

Izu Ojukwu: Izu Ojukwu is a Nigerian film director.  In 2007 he won "Best Director" for "Sitanda" at the 3rd Africa Movie Academy Awards, which received nine nominations and won five awards at the event, including "Best Picture" and "Best Nigerian Film".

'76 (film): '76, formerly Lions of '76, is a 2016 Nigerian historical fiction drama film produced by Adonaijah Owiriwa and Izu Ojukwu and directed by Izu Ojukwu.  It stars Ramsey Nouah, Chidi Mokeme, Rita Dominic and Ibinabo Fiberesima.

Party Crasher (Modern Family): "Party Crasher" is the 12th episode of the fourth season of the American sitcom "Modern Family", and the series' 84th episode overall.  It aired January 16, 2013.  The episode was written by Danny Zuker & Christopher Lloyd and directed by Fred Savage.

Dinosaurs! – A Fun-Filled Trip Back in Time!: Dinosaurs!  – A Fun-Filled Trip Back in Time!  is a short film released by Golden Book Video in 1987 under their "GoldenVision" series.  It stars Fred Savage playing a grade school student named Philip who gives a class report on dinosaurs, with the help of an animated chalkboard and Will Vinton's claymation dinosaurs.

Alero's Symphony: Alero's Symphony is a 2011 Nigerian musical drama film directed by Izu Ojukwu and starring Bimbo Manuel, Ivie Okujaye and Chibuzor 'Faze' Oji.  It premiered at The Palms, Genesis Cinemas, Lagos.  The film is an upshot of the Amstel Malta Box Office 5 (AMBO 5) reality show.  It received 4 nominations at the 8th Africa Movie Academy Awards and was screened across major Nigerian cities by the Africa Film Academy.

Granny Pants: "Granny Pants" is the fifth episode in the third season, the 46th episode overall, of the American dramedy series "Ugly Betty", which aired on October 23, 2008.  The episode was written by Sheila Lawrence and directed by Fred Savage.

Across the Niger: Across the Niger is a Nigerian drama movie produced in 2004, directed by Izu Ojukwu and written by Kabat Esosa Egbon.  It starred Chiwetalu Agu, who was nominated for "best actor in a supporting role" for his part in the film at the 2008 4th annual African Movie Academy Awards.

Fred Savage: Frederick Aaron "Fred" Savage (born July 9, 1976) is an American actor, television director, and producer.  He is best known for his role as Kevin Arnold in the American television series "The Wonder Years", which ran from 1988 to 1993.  He has earned several awards and nominations, such as People's Choice Awards and Young Artist Awards.

White Waters: White Waters is a 2007 sports drama film directed by Izu Ojukwu.  The film received 12 nominations and won four awards at the 4th African Movie Academy Awards including winning Best Director, Best Cinematography, Best Sound and Best Actress award in a Supporting Role for Joke Silva.

Question: What profession does Izu Ojukwu and Fred Savage have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_profession": {
      "type": "string",
      "description": "The profession shared by both individuals."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual and their listed professions.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "professions": {
            "type": "array",
            "description": "A list of professions attributed to the individual.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the common profession was identified."
    }
  },
  "required": [
    "common_profession",
    "individuals",
    "reasoning"
  ],
  "additionalProperties": false
}
