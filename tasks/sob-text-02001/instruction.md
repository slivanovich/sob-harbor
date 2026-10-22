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
The Voice Kids (Russia, season 2): The second season of the Russian reality talent show "The Voice Kids" premiered on 13 February 2015 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Dima Bilan, Pelageya and Maxim Fadeev return as coaches.  Sabina Mustaeva won the competition and Maxim Fadeev became the winning coach for the second time.

The Voice (Russia, season 4): The fourth season of the Russian reality talent show "The Voice" premiered on 4 September 2015 on Channel One.

The Voice (Russia season 5): The fifth season of the Russian reality talent show "The Voice" premiered on 2 September 2016 on Channel One with Dima Bilan and Leonid Agutin returning as coaches alongside Polina Gagarina and Grigory Leps.  Dmitry Nagiev returns as the show's presenter.  Darya Antonyuk was announced the winner on 30 December 2016 marking Leonid Agutin's first win as a coach.

Leonid Agutin: Leonid Nikolayevich Agutin (Russian: Леонид Николаевич Агутин ; born July 16, 1968) is a Russian pop musician and songwriter, Meritorious Artist of Russia (2008).  He has been active since the 1990s.  He has released ten albums and three compilation albums.

The Voice Kids (Russia, season 3): The third season of the Russian reality talent show "The Voice Kids" premiered on 20 February 2016 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Dima Bilan and Pelageya return as coaches.  Leonid Agutin replaced Maxim Fadeev as coach.  Danil Pluzhnikov was announced the winner on 29 April 2016 marking Dima Bilan's first win as a coach.

The Voice Kids (Russia, season 5): The fifth season of the Russian reality talent show "The Voice Kids" will premiere in early 2018 on Channel One.  On August 21, 2017, it was announced about casting.

The Voice (Russia, season 2): The second season of the Russian reality talent show "The Voice" premiered on 6 September 2013 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Dima Bilan, Pelageya, Alexander Gradsky, and Leonid Agutin return as coaches.  Sergey Volchkov won the competition and Alexander Gradsky became the winning coach for the second time.

The Voice (Russia, season 6): The sixth season of the Russian reality talent show "The Voice" premiered on September 1, 2017 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Dima Bilan and Leonid Agutin returned as coaches, while Pelageya returned after two season hiatus alongside Alexander Gradsky who returned after a one-season break.

The Voice (Russia, season 3): The third season of the Russian reality talent show "The Voice" premiered on 5 September 2014 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Leonid Agutin, Pelageya, Alexander Gradsky, and Dima Bilan return as coaches.

The Voice Kids (Russia, season 4): The fourth season of the Russian reality talent show "The Voice Kids" premiered on 17 February 2017 on Channel One.  Dmitry Nagiev returns as the show's presenter.  Dima Bilan returns as coach.  Nyusha and Valery Meladze replaced Pelageya and Leonid Agutin as coaches.

Question: Who  has released ten albums and three compilation albums and was a coach on the sixth season of the Russian reality talent show on Channel One?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The full name of the artist."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "studio_albums_count": {
          "type": "integer",
          "description": "The number of studio albums released by the artist."
        },
        "compilation_albums_count": {
          "type": "integer",
          "description": "The number of compilation albums released by the artist."
        }
      },
      "required": [
        "studio_albums_count",
        "compilation_albums_count"
      ],
      "additionalProperties": false
    },
    "coaching_role": {
      "type": "object",
      "properties": {
        "show_title": {
          "type": "string",
          "description": "The title of the reality talent show."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the show where the artist was a coach."
        },
        "channel": {
          "type": "string",
          "description": "The channel on which the show premiered."
        }
      },
      "required": [
        "show_title",
        "season_number",
        "channel"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "album_details",
    "coaching_role"
  ],
  "additionalProperties": false
}
