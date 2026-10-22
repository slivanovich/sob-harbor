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
800 Two Lap Runners: 800 Two Lap Runners is a 1994 Japanese film directed by Ryūichi Hiroki starring Shunsuke Matsuoka and Eugene Nomura.  For director Hiroki, the film marks a transition from his early work in "pink film" to mainstream cinema.

Otoko no Isshō: Otoko no Isshō (娚の一生 ) is a slice of life romance "josei" manga series written and illustrated by Keiko Nishi.  It was published by Shogakukan on "Flowers" magazine and in four volumes compiling the chapters.  A live action romantic drama film adaptation was released on February 14, 2015.  It's directed by Ryūichi Hiroki and written by Hiroshi Saitō.  It stars Nana Eikura and Etsushi Toyokawa.

J. Lee Thompson: John Lee Thompson (1 August 1914 – 30 August 2002) was a British film director, active in London and Hollywood, best known for such movies as "Ice Cold in Alex" and "The Guns of Navarone".

It's Only Talk: It's Only Talk is a Japanese film, released in 2005 and is based on the prizewinning novel of the same title written by Akiko Itoyama and directed by Ryūichi Hiroki.

Kiiroi Zou: Kiiroi Zou (きいろいゾウ ) is a 2013 Japanese film directed by Ryūichi Hiroki.

Murder Without Crime: Murder Without Crime is a 1950 British crime film directed by J. Lee Thompson (his first film) and starring Dennis Price, Derek Farr and Patricia Plunkett.  J. Lee Thompson also wrote the screenplay adapted from "Double Error", his own successful West End play.

North West Frontier (film): North West Frontier (USA: Flame Over India; Australia: Empress of India) is a 1959 British adventure film starring Kenneth More, Lauren Bacall, Herbert Lom, Wilfrid Hyde-White and I. S. Johar.  The Cinemascope film, which was produced by Marcel Hellman, was directed by J. Lee Thompson.  It was a commercial success at the British box office in 1959.  The film's achievement led to J. Lee Thompson beginning his American career as a director.  In 1961, he made "The Guns of Navarone", which was also noted for the cinematography of Geoffrey Unsworth. .

River (2011 film): River is a 2011 Japanese drama film based on the 2008 Akihabara massacre incident.  The film is written and directed by Ryūichi Hiroki.  The film stars actress Misako Renbutsu, who will play the role of a person who lost her love interest in the attacks.

Vibrator (film): Vibrator (ヴァイブレータ ) is a 2003 Japanese film directed by Ryūichi Hiroki.

Ryūichi Hiroki: Ryūichi Hiroki (廣木 隆一 , Hiroki Ryūichi , born January 1, 1954) is a Japanese film director.  He won critical acclaim for "800 Two Lap Runners".  Film critic and researcher Alexander Jacoby has described Hiroki as "one of the modern Japanese cinema's most intelligent students of character".

Question: Were J. Lee Thompson and Ryūichi Hiroki both film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "is_director": {
          "type": "boolean",
          "description": "Indicates if the first person is a film director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the first person."
        }
      },
      "required": [
        "name",
        "is_director",
        "nationality"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "is_director": {
          "type": "boolean",
          "description": "Indicates if the second person is a film director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the second person."
        }
      },
      "required": [
        "name",
        "is_director",
        "nationality"
      ],
      "additionalProperties": false
    },
    "both_are_directors": {
      "type": "boolean",
      "description": "True if both individuals are film directors, false otherwise."
    }
  },
  "required": [
    "person_1",
    "person_2",
    "both_are_directors"
  ],
  "additionalProperties": false
}
