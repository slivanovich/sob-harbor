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
The Garden of Eden (novel): The Garden of Eden is the second posthumously released novel of Ernest Hemingway, published in 1986.  It was begun in 1946, and Hemingway worked on the manuscript for the next 15 years, during which time he also wrote "The Old Man and the Sea", "The Dangerous Summer", "A Moveable Feast", and "Islands in the Stream".

Reach for the Sun: Reach for the Sun is the debut studo album by American alternative rock band The Dangerous Summer.

A Dangerous Summer: A Dangerous Summer is a 1982 Australian crime film drama film directed by Quentin Masters and starring Tom Skerritt, Ian Gilmour, Guy Doleman and James Mason.

The Dangerous Summer: The Dangerous Summer is a nonfiction book by Ernest Hemingway published posthumously in 1985 and written in 1959 and 1960.  The book describes the rivalry between bullfighters Luis Miguel Dominguín and his brother-in-law, Antonio Ordóñez, during the "dangerous summer" of 1959.  It has been cited as Hemingway's last book.

Count to Four: Count to Four are a progressive pop-punk band from South Jersey/Philadelphia in the vein of The Wonder Years.  Initially founded in 2009, the band didn't release material or push social media sites until 2010 at which point their lineup was solidified.  Since inception, Count to Four recorded and self-released three EPs and a full-length studio album from the beginning of 2010 to the end of 2013.  They've shared the stage with reputable acts such as The Dangerous Summer, Rufio, Man Overboard, and also received a major endorsement from frontman Alex Gaskarth of All Time Low.  Currently the band is unsigned but under Kolossal Management with booking and PR teams.

Golden Record (album): Golden Record is the third studio album by American alternative rock band The Dangerous Summer, scheduled for release on August 6, 2013 through Hopeless Records.

War Paint (The Dangerous Summer album): War Paint is the second album from American alternative rock band The Dangerous Summer, released through Hopeless Records.  The album was released July 19, 2011.

Hello Sleepwalkers: Hello Sleepwalkers (ハロー・スリープウォーカーズ ) is a five member Japanese alternative rock band from Okinawa formed in 2008.  The band is signed to A-Sketch Music Label and have currently released three studio albums, one extended play, four single albums, and ten singles.  They are best known for performing the opening theme song of the anime "Noragami", "Goya no Machiawase" (午夜の待ち合わせ , Midnight's Appointment ) .

Natsu no Yoru wa Danger!: "Natsu no Yoru wa Danger!"  (夏の夜はデインジャー!  , Dangerous Summer Night! )  is the sixth single by Japanese girl group Melon Kinenbi.  It was released on June 19 2002, and its highest position on the Oricon weekly chart was #14.

The Dangerous Summer (band): The Dangerous Summer is a rock band from Ellicott City, Maryland.

Question: Which band, The Dangerous Summer or Hello Sleepwalkers, is based in America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_focus": {
      "type": "string",
      "description": "The main subject or type of information the question is asking about."
    },
    "bands_evaluated": {
      "type": "array",
      "description": "A list of bands that were evaluated for their country of origin.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the band is based."
          }
        },
        "required": [
          "band_name",
          "origin_country"
        ],
        "additionalProperties": false
      }
    },
    "american_band_name": {
      "type": "string",
      "description": "The name of the band identified as being based in America."
    },
    "is_american_band_found": {
      "type": "boolean",
      "description": "True if an American band was found among those evaluated, false otherwise."
    }
  },
  "required": [
    "question_focus",
    "bands_evaluated",
    "american_band_name",
    "is_american_band_found"
  ],
  "additionalProperties": false
}
