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
Red-Headed Woman: Red-Headed Woman is a 1932 American pre-Code romantic comedy film, produced by Metro-Goldwyn-Mayer, based on a novel of the same name by Katherine Brush, and with a screenplay by Anita Loos.  It was directed by Jack Conway, and stars Jean Harlow as a woman who uses sex to advance her social position.  During the course of the film, Harlow breaks up a marriage, has multiple affairs and pre-marital sex, and attempts to kill a man.

Girl Talk (Neal Hefti song): "Girl Talk" is a popular song composed by Neal Hefti, with lyrics written by Bobby Troup.  It was written for the 1965 film "Harlow", a biographical film about Jean Harlow, starring Carroll Baker.

The Aviator (2004 film): The Aviator is a 2004 American epic biographical drama film directed by Martin Scorsese, written by John Logan.  It stars Leonardo DiCaprio as Howard Hughes, Cate Blanchett as Katharine Hepburn and Kate Beckinsale as Ava Gardner.  The supporting cast features Ian Holm, John C. Reilly, Alec Baldwin, Jude Law as Errol Flynn, Gwen Stefani as Jean Harlow, Kelli Garner as Faith Domergue, Willem Dafoe, Alan Alda, and Edward Herrmann.

Jean Harlow: Jean Harlow (born Harlean Harlow Carpenter; March 3, 1911 – June 7, 1937) was an American film actress and sex symbol of the 1930s.

Red Dust (1932 film): Red Dust is a 1932 American pre-Code, romantic drama film directed by Victor Fleming and starring Clark Gable, Jean Harlow, and Mary Astor.  The film is based on the 1928 play of the same name by Wilson Collison, and was adapted for the screen by John Mahin.  "Red Dust" is the second of six movies Gable and Harlow made together, and was produced during the pre-code era of Hollywood.  More than 20 years later, Gable starred in a remake, "Mogambo" (1953), with Ava Gardner starring in a variation on the Harlow role and Grace Kelly playing a part similar to one portrayed by Mary Astor in "Red Dust".

Harlow (Paramount film): Harlow is a 1965 American biographical film directed by Gordon Douglas about the life of film star Jean Harlow.  It stars Carroll Baker in the title role, and Raf Vallone, Red Buttons, Angela Lansbury, Peter Lawford, Martin Balsam, and Leslie Nielsen in supporting roles.  It was released by Paramount Pictures, shortly after another film with the same title and subject.  Although the film failed commercially, it was successful in launching the hit song, "Girl Talk" by Neal Hefti.

Personal Property (film): Personal Property is a 1937 American romantic comedy film starring Jean Harlow and Robert Taylor and directed by W.S. Van Dyke.  It is based on the play "The Man in Possession" by H. M. Harwood.  It was the last film released with Harlow in it during her lifetime.

This Thing Called Love (1929 film): This Thing Called Love is a 1929 American romantic comedy film starring Edmund Lowe, Constance Bennett, Ruth Taylor, Roscoe Karns, ZaSu Pitts, and Jean Harlow.  Harlow appears in a cameo role, as she was not yet famous.  The film is based on the play "This Thing Called Love, a Comedy in Three Acts", by Edwin J. Burke.

Hell's Angels (film): Hell's Angels is a 1930 independently made American epic aviation war film, directed and produced by Howard Hughes, that stars Ben Lyon, James Hall, and Jean Harlow.  The film, which was written by Harry Behn and Howard Estabrook, was released by United Artists.  Originally shot as a silent film, Hughes retooled "Hell's Angels" over a lengthy gestation period.  Most of the film is in black-and-white, but there is one color sequence, the only color footage of Harlow's career.

Harlow (Magna film): Harlow is a fictionalized drama based on the life of film star Jean Harlow, released in 1965 with Carol Lynley in the title role.  It was released shortly before Paramount Pictures' film on the same subject.  This was Ginger Rogers' last film appearance.  The film was directed by Alex Segal.

Question: "Girl Talk" is a popular song composed by who, and was written for the 1965 film "Harlow", a biographical film about Jean Harlow, who was an American film actress and sex symbol of the 1930s?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "composer": {
      "type": "string",
      "description": "The composer of the song."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the song was written for."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "film_type": {
          "type": "string",
          "description": "The type of the film (e.g., biographical)."
        },
        "subject_details": {
          "type": "object",
          "properties": {
            "subject_name": {
              "type": "string",
              "description": "The name of the person the biographical film is about."
            },
            "profession": {
              "type": "string",
              "description": "The profession of the film's subject."
            },
            "era_of_prominence": {
              "type": "string",
              "description": "The decade when the subject was prominent."
            }
          },
          "required": [
            "subject_name",
            "profession",
            "era_of_prominence"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "film_title",
        "release_year",
        "film_type",
        "subject_details"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "composer",
    "film_details"
  ],
  "additionalProperties": false
}
