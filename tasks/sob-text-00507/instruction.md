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
Down to Earth (1995 film): Down to Earth (Portuguese: "Casa de Lava" ) is a 1995 Portuguese drama film directed by Pedro Costa.  The film is set in Cape Verde Islands, a former Portuguese colony.

Colossal Youth (film): Colossal Youth (Portuguese: Juventude em Marcha , literally "Youth on the March") is a 2006 docufiction feature film directed by Portuguese director Pedro Costa.  The film was shot on DV in long, static takes and mixes documentary and fiction storytelling.  The third feature by Costa set in Lisbon's Fontainhas neighborhood (after "In Vanda's Room" and "Bones"), "Colossal Youth" is a meditation on the aftermath of the Carnation Revolution and its consequences for Portugal's poverty-stricken Cape Verdean immigrants.  It was part of the Official Competition at the 2006 Cannes Film Festival.

In Vanda's Room: In Vanda's Room (Portuguese: No Quarto da Vanda, 2000) is a docufiction (a subgenre of cinéma vérité) film by Portuguese director Pedro Costa.

Hold-Up! (2012 film): ¡Atraco!  is a 2012 Spanish-Argentine film directed by , filmed in Spain.  The script was written by the director with Pedro Costa.  The film stars Guillermo Francella, Nicolás Cabré, and Amaia Salamanca.

O Sangue: O Sangue (Blood) is the Portuguese filmmaker Pedro Costa's first feature film.  Released in 1989, in black and white, the film depicts the impoverished life of two brothers, Vicente and Nino, after their father dies.  With the help of Clara, Vicente's childhood friend, the trio struggle to survive, caught between their uncle's attempt to abduct/adopt Nino, and mobsters looking to collect the debts Vincente's father left behind.  The film was selected as the Portuguese entry for the Best Foreign Language Film at the 64th Academy Awards, but was not accepted as a nominee.

Jack Hill: Jack Hill (born January 28, 1933) is an American film director in the exploitation film genre.  Several of Hill's later films have been characterized as feminist works.

Pedro Costa: Pedro Costa (born 30 December 1958) is a Portuguese film director.

José Pedro Costa Amorim Cerqueira: José Pedro Costa Amorim Cerqueira (born 8 July 1992) simply known as Zé Pedro, is a Portuguese professional footballer playing for Académico de Viseu as a forward.

Ossos: Ossos (English: "Bones") is a 1997 Portuguese film directed by Pedro Costa.

Change Nothing: Change Nothing (French: "Ne change rien" ) is a 2009 documentary directed by Portuguese filmmaker Pedro Costa.  The documentary focuses on the French singer Jeanne Balibar in rehearsal and concert as seen through Costa's characteristically long, stark takes.

Question: Jack Hill and Pedro Costa are both what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_profession": {
      "type": "string",
      "description": "The shared profession of the individuals."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the individual."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "number_of_individuals": {
      "type": "integer",
      "description": "The total number of individuals identified."
    }
  },
  "required": [
    "common_profession",
    "individuals",
    "number_of_individuals"
  ],
  "additionalProperties": false
}
