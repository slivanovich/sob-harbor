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
My Big Fat Greek Bob: "My Big Fat Greek Bob" is the fourth episode of the fourth season of the animated comedy series "Bob's Burgers" and the overall 49th episode, and is written by Scott Jacobson and directed by Don MacKinnon.  It aired on Fox in the United States on November 10, 2013.

The Cook, the Steve, the Gayle, &amp; Her Lover: "The Cook, the Steve, the Gayle, & Her Lover" is the sixth episode of the sixth season of the animated comedy series "Bob's Burgers" and the overall 94th episode, written by Nora Smith and directed by Tyree Dillihay.  It aired on Fox in the United States on January 17, 2016.  When Bob throws a dinner party to bond with his new friend, Gayle uses the opportunity to introduce the family to her new love interest.  Little does she know, Louise has a long-standing feud with Gayle’s boyfriend and her niece will stop at nothing to break them apart.  Calamity ensues as Bob attempts to impress his new buddy and the kids take action.

Computer Blue: "Computer Blue" is the fourth track on Prince and the Revolution's soundtrack album, "Purple Rain".  In the film, the song represents Prince's angst at the budding relationship between the characters played by Morris Day and Apollonia.  The song was composed by Prince, with credit to his father, John L. Nelson for the guitar solo based on a piano instrumental written by Nelson and Prince.  Prince titled the piece "Father's Song" and recorded it on piano for the film, though on screen it was portrayed as being played by Prince's on-screen father, actor Clarence Williams III.  On the box-set "Purple Rain Deluxe" (2017) a different and longer recording of "Father's Song" is included.

The Deepening: "The Deepening" is the sixth episode of the third season of the animated comedy series "Bob's Burgers" and the overall 28th episode, and is written by Greg Thompson and directed by Bernard Derriman.  It aired on Fox in the United States on November 25, 2012.

Dr. Yap: "Dr. Yap" is the sixth episode of the second season of the animated comedy series "Bob's Burgers" and the overall 19th episode, and is written by Steven Davis and Kelvin Yu and directed by Anthony Chun.  It aired on Fox in the United States on April 29, 2012.

Father of the Bob: "Father of the Bob" is the sixth episode of the fifth season of the animated comedy series "Bob's Burgers" and the overall 73rd episode, and is written by Steven Davis and Kelvin Yu and directed by Chris Song.  It aired on Fox in the United States on December 7, 2014.

The Quirkducers: "The Quirkducers" is the sixth episode of the seventh season of the animated comedy series "Bob's Burgers" and the overall 113th episode, and is written by Steven Davis and Kelvin Yu and directed by Mauricio Pardo.  It aired on Fox in the United States on November 20, 2016.  In the episode, Gene and Louise decide to sabotage the annual Thanksgiving play to save their long weekend, but Tina provides her fan fiction as the subject matter, leading the kids to work on their own version.  Meanwhile, Linda finds a potato that resembles her deceased grandfather.

Purple Rain Tour: The Purple Rain Tour was the fifth concert tour by American recording artist Prince and The Revolution following up on the success of his sixth studio album "Purple Rain" and his 1984 film "Purple Rain".  According to "Spin", the tour sold over 1.7 million tickets.

Purple Rain (song): "Purple Rain" is a song by Prince and The Revolution.  It is the title track from the 1984 album of the same name, which in turn is the soundtrack album for the 1984 film of the same name, and was released as the third single from that album.  The song is a combination of rock, R&B, gospel, and orchestral music.  It reached number 2 in the United States for two weeks, behind "Wake Me Up Before You Go-Go" by Wham! , and it is considered to be one of Prince's signature songs.

Purple Rain-Union: "Purple Rain-Union" is the sixth episode of the fourth season of the animated comedy series "Bob's Burgers" and the overall 51st episode, and is written by Loren Bouchard and Nora Smith and directed by Tyree Dillihay.  It aired on Fox in the United States on December 1, 2013.  The title of the episode is a reference to the song, film, and album "Purple Rain" by Prince.

Question: "Purple Rain-Union" is the sixth episode of the fourth season of the animated comedy series "Bob's Burgers", it aired on Fox in the United States on which date, the title of the episode is a reference to the song, film, and album "Purple Rain" by Prince?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the episode."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the animated comedy series."
    },
    "air_date": {
      "type": "string",
      "format": "date",
      "description": "The date the episode first aired."
    },
    "episode_identifiers": {
      "type": "object",
      "properties": {
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number_in_season": {
          "type": "integer",
          "description": "The episode number within its season."
        },
        "overall_episode_number": {
          "type": "integer",
          "description": "The overall episode number in the series."
        }
      },
      "required": [
        "season_number",
        "episode_number_in_season",
        "overall_episode_number"
      ],
      "additionalProperties": false
    },
    "title_references": {
      "type": "array",
      "description": "A list of works referenced by the episode's title.",
      "items": {
        "type": "object",
        "properties": {
          "reference_type": {
            "type": "string",
            "description": "The type of work referenced (e.g., song, film, album)."
          },
          "referenced_work_title": {
            "type": "string",
            "description": "The title of the referenced work."
          },
          "referenced_artist": {
            "type": "string",
            "description": "The artist associated with the referenced work."
          }
        },
        "required": [
          "reference_type",
          "referenced_work_title",
          "referenced_artist"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "episode_title",
    "series_name",
    "air_date",
    "episode_identifiers",
    "title_references"
  ],
  "additionalProperties": false
}
