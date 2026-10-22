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
War of the Wizards (gamebook): War of the Wizards is the fourth and final book in the World of Lone Wolf book series created by Joe Dever and written by Ian Page.  It is one of four books in the mini-series and features Grey Star, for whom the first book is named, a young Wizard trained by the enigmatic Shianti to stop the Wytch-King and his Shadakine Empire.  All four of the Grey Star books were released by Project Aon along with many of the other installments of the Lone Wolf series.

The Captives of Kaag: The Captives of Kaag is the fourteenth book in the Lone Wolf book series created by Joe Dever.  As with most of the later books in the series, this one is illustrated by Brian Williams.

List of Lone Wolf media: The following is a list of media published in the "Lone Wolf" series of gamebooks, and other derivative media based on the gamebooks.  The original gamebook series, and the bulk of subsequent Lone Wolf media, was written by Joe Dever.  The success and cult status of the original gamebooks helped in the creation of a spin-off called The World of Lone Wolf, written by Ian Page, a series of novelizations, a collection of role-playing games, and a number of video games and other derivative works.

Lone Wolf (gamebooks): Lone Wolf is a series of 29 gamebooks, created by Joe Dever and initially illustrated (books 1-8) by Gary Chalk.  The series was first published in July 1984 and sold more than 9 million copies worldwide.  The story focuses on the fictional world of Magnamund, where the forces of good and evil fight for control of the planet.  The protagonist is Lone Wolf, last of his caste of warrior monks known as Kai Lords.  The book series is written in the second person and recounts Lone Wolf's adventures as if the reader is the main character.  As Lone Wolf, the reader makes choices at regular intervals throughout the story which then change the course, and the final outcome, of the book.

Joe Dever: Joseph Robert Dever, also known as Joe Dever (12 February 1956 – 29 November 2016) was a British fantasy author and game designer.  Originally a musician, Dever became the first British winner of the "Advanced Dungeons & Dragons" Championship of America in 1982.

Joe Dever's Lone Wolf: Joe Dever's Lone Wolf, is a role-playing game video game developed by Bulkypix and released for iOS on October 29, 2013, and now also available on Android.  It is based on the series of gamebooks by author Joe Dever entitled "Lone Wolf".  The story involves Lone Wolf adventuring to uncover the secret of the Shianti Cube.

The Chasm of Doom: The Chasm of Doom is the fourth book in the award-winning Lone Wolf book series created by Joe Dever and illustrated by Gary Chalk.

Freeway Warrior: Freeway Warrior is a series of 4 gamebooks, created by Joe Dever.  The books were published between 1988 and 1989, detailing the complete story of a band of nuclear holocaust survivors as they flee Texas to the relative safety of California.

The Cauldron of Fear: The Cauldron of Fear is the ninth book in the Lone Wolf book series created by Joe Dever.  Starting with this book, long-time illustrator Gary Chalk was replaced with Brian Williams.

Legends of Skyfall: The Legends of Skyfall was a series of four adventure gamebooks written by David Tant and published by Armada in 1985.  They were written to cash in on the explosive popularity of such books, spawned by Steve Jackson and Ian Livingstone's Fighting Fantasy and later Joe Dever's Lone Wolf series.

Question: The Chasm of Doom is the fourth book of which series of 29 gamebooks, created by Joe Dever and initially illustrated (books 1-8) by Gary Chalk?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the gamebook series."
    },
    "series_details": {
      "type": "object",
      "properties": {
        "number_of_books": {
          "type": "integer",
          "description": "The total number of books in the series."
        },
        "creator": {
          "type": "string",
          "description": "The creator of the series."
        },
        "initial_illustrator": {
          "type": "string",
          "description": "The illustrator for the initial books in the series."
        }
      },
      "required": [
        "number_of_books",
        "creator",
        "initial_illustrator"
      ],
      "additionalProperties": false
    },
    "book_in_question": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the specific book mentioned in the question."
        },
        "series_position": {
          "type": "integer",
          "description": "The position of the book within its series."
        }
      },
      "required": [
        "title",
        "series_position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_name",
    "series_details",
    "book_in_question"
  ],
  "additionalProperties": false
}
