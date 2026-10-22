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
Alain Tanner: Alain Tanner (born 6 December 1929) is a Swiss film director.

Princess Yang Kwei-Fei: Princess Yang Kwei-Fei (楊貴妃 , "Yōkihi" , a.k.a. "The Consort Yáng Guìfēi") is a 1955 Japanese film directed by Kenji Mizoguchi.  It was a co-production between Daiei Film and Hong Kong's Shaw & Sons, a predecessor of Shaw Brothers Studio .  It is one of Mizoguchi's two color films, the other being "Tales of the Taira Clan", made the same year.

Tokyo March: Tokyo March (東京行進曲 , Tōkyō kōshinkyoku ) is a 1929 black and white Japanese silent film, originally presented with benshi accompaniment, directed by Kenji Mizoguchi.  It is a classic melodramatic love tragedy addressing social inequality in modern Japan, depicted in Mizoguchi's typical style.  The theme song "Tokyo March" was originally sung by Chiyako Sato.

Osaka Elegy: Osaka Elegy (浪華悲歌 , "Naniwa erejii" ) (originally Naniwa Elegy) is a 1936 Japanese film directed by Kenji Mizoguchi.  Mizoguchi considered the film his first serious effort as a director, and it was also his first commercial and critical success in Japan.  "Osaka Elegy" is often considered a companion piece to Mizoguchi's next film, "Sisters of the Gion", which was released the same year and featured much the same cast and crew.

Kenji Mizoguchi: The Life of a Film Director: Kenji Mizoguchi: The Life of a Film Director (ある映画監督の生涯 溝口健二の記録 , Aru eiga-kantoku no shōgai ) is a 1975 Japanese documentary film on the life and works of director Kenji Mizoguchi, directed by Kaneto Shindo.

Kenji Mizoguchi: Kenji Mizoguchi (溝口 健二 , Mizoguchi Kenji , May 16, 1898 – August 24, 1956) was a Japanese film director and screenwriter.

The Lady of Musashino: The Lady of Musashino (武蔵野夫人 , Musashino-Fujin ) is a 1951 Japanese film directed by Kenji Mizoguchi.  The script for the film was adapted by Mizoguchi from the best-selling serial novel by Shōhei Ōoka.

Street of Shame: Street of Shame (赤線地帯 , "Akasen chitai" ) is a 1956 black-and-white Japanese film directed by Kenji Mizoguchi.  It is the personal tales of several Japanese women of different backgrounds who work together in a brothel.  It was Mizoguchi's last film.

Sisters of the Gion: Sisters of the Gion (祇園の姉妹 , Gion no kyōdai ) or Sisters of Gion is a 1936 black and white Japanese film drama directed by Kenji Mizoguchi about two sisters living in the Gion District.  The film is seen as a companion piece to Mizoguchi's "Osaka Elegy" which shares much of the same cast and production team.

Utamaro and His Five Women: Utamaro and His Five Women or Five Women Around Utamaro (Japanese: 歌麿をめぐる五人の女 , Hepburn: Utamaro o meguru gonin no onna ) is a 1946 Japanese film directed by Kenji Mizoguchi.  It is based on the novel of the same title by Kanji Kunieda, itself a fictionalized account of the life of printmaker Kitagawa Utamaro.  It was Mizoguchi's first film made under the American occupation.

Question: Who was born first Kenji Mizoguchi or Alain Tanner?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "directors_involved": {
      "type": "array",
      "description": "List of directors involved in the comparison with their birth years.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the director."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "comparison_summary": {
      "type": "object",
      "description": "Summary of the birth year comparison.",
      "properties": {
        "director_born_first": {
          "type": "string",
          "description": "The name of the director who was born first."
        },
        "year_born_first": {
          "type": "integer",
          "description": "The birth year of the director who was born first."
        },
        "director_born_second": {
          "type": "string",
          "description": "The name of the director who was born second."
        },
        "year_born_second": {
          "type": "integer",
          "description": "The birth year of the director who was born second."
        }
      },
      "required": [
        "director_born_first",
        "year_born_first",
        "director_born_second",
        "year_born_second"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The name of the director who was born first."
    }
  },
  "required": [
    "directors_involved",
    "comparison_summary",
    "answer"
  ],
  "additionalProperties": false
}
