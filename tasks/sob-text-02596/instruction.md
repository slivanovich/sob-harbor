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
Julieta (film): Julieta is a 2016 Spanish film written and directed by Pedro Almodóvar based on three short stories from the book "Runaway" by Alice Munro.  The film marks Almodóvar's 20th feature and stars Emma Suárez and Adriana Ugarte as older and younger versions of the film's protagonist, Julieta, alongside Daniel Grao, Inma Cuesta, Darío Grandinetti, Michelle Jenner and Rossy de Palma.

Enemies of Women: Enemies of Women is a 1923 silent romantic drama film directed by Alan Crosland and starring Lionel Barrymore, Alma Rubens, Gladys Hulette, Pedro de Cordoba, and Paul Panzer.  The film was produced by William Randolph Hearst through his Cosmopolitan Productions.  Pre-fame actresses Clara Bow and Margaret Dumont have uncredited bit roles.

Alan Crosland: Alan Crosland (August 10, 1894 – July 16, 1936) was an American stage actor and film director.

Pedro Almodóvar: Pedro Almodóvar Caballero (] ; born 25 September 1949) is a Spanish film director, screenwriter, producer and former actor.  He came to prominence as a director and screenwriter during La Movida Madrileña, a cultural renaissance that followed the death of Spanish dictator Francisco Franco.  His first few films characterised the sense of sexual and political freedom of the period.  In 1986, he established his own film production company, El Deseo, with his younger brother Agustín Almodóvar, responsible for producing all of his films since "Law of Desire" (1987).

Lady Tubbs: Lady Tubbs is a 1935 American comedy film directed by Alan Crosland and written by Barry Trivers.  The film stars Alice Brady, Douglass Montgomery, Anita Louise, Alan Mowbray, June Clayworth and Hedda Hopper.  The film was released on July 2, 1935, by Universal Pictures.

General Crack: General Crack is a 1930 American Pre-Code part-talkie historical costume melodrama with Technicolor sequences which was directed by Alan Crosland and produced and distributed by Warner Bros. It was filmed and premiered in 1929, and released early in 1930.  It stars John Barrymore in his first full-length all-talking feature.  The film would prove to be Crosland and Barrymore's last historical epic together.

Carmen Maura: Carmen García Maura (born 15 September 1945) is a Spanish actress.  In a career that has spanned six decades, Maura is best known for her collaborations with noted Spanish film directors Pedro Almodóvar and Álex de la Iglesia.

The Holy Girl: The Holy Girl (Spanish: "La niña santa" ) is a 2004 Argentinian drama film directed by Lucrecia Martel.  The picture was executively produced by Pedro Almodóvar, Agustín Almodóvar, and Esther García.  It was produced by Lita Stantic.  The film features Mercedes Morán, María Alche, Carlos Belloso, Alejandro Urdapilleta, Julieta Zylberberg, among others.

Women on the Verge of a Nervous Breakdown: Women on the Verge of a Nervous Breakdown (Spanish: Mujeres al borde de un ataque de nervios ) is a 1988 Spanish black comedy-drama film written and directed by Pedro Almodóvar, starring Carmen Maura and Antonio Banderas.  The film brought Almodóvar to widespread international attention: it was nominated for the 1988 Academy Award for Best Foreign Language Film, and won five Goya Awards including Best Film and Best Actress in a Leading Role for Maura.

Contraband (1925 film): Contraband is a lost 1925 silent film produced by Famous Players-Lasky and distributed by Paramount Pictures.  Alan Crosland directed and Lois Wilson stars.  The film is taken from a novel, "Contraband", by Charles Buddington Kelland.  The last film directed by Alan Crosland the cooperation with distributor Paramount Pictures.

Question: Which of these two film directors is American, Pedro Almodóvar or Alan Crosland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "american_director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the director who is American."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the American director."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "other_director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other director mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the other director."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean",
      "description": "Indicates if the question about identifying the American director was successfully answered."
    }
  },
  "required": [
    "american_director",
    "other_director",
    "question_answered"
  ],
  "additionalProperties": false
}
