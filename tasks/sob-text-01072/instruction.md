{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFuturia Fantasia: Futuria Fantasia was an American science fiction fanzine created by Ray Bradbury in 1938, when he was 18 years old.  Though only 4 issues of the fanzine were published, \"Futuria Fantasia\" boasted an impressive list of contributors, including Hannes Bok, Forrest J. Ackerman, Henry Kuttner, Damon Knight, and Robert A. Heinlein.\n\nThe Black Wheel: The Black Wheel is a fantasy novel written by A. Merritt and Hannes Bok.  Merritt had completed the first seven chapters, roughly 20,000 words, before his death in 1943.  Bok wrote the remainder of the novel, twenty chapters of more than 60,000 words, working from \"a sketchy plot outline\" left by Merritt.  The story concerns the discovery of a centuries-old shipwreck, complete with the preserved bodies of its crew, and the consequences for the passengers and crew of the cruise ship that comes across it.\n\nWhee-lo: The Whee-lo or Magnet Space Wheel, is a toy that propels a plastic wheel along both sides of a metal track with magnets built into the wheel.  As the track is tilted up and down, the wheel rolls the length of the track, top and bottom, and then again on the opposite side of the wire.  In this way, the wheel always keeps in contact with the track, and can be continually propelled on its cyclical course.  With proper timing, the wheel can be brought to a great speed.\n\nBeyond the Golden Stair: Beyond the Golden Stair is a fantasy novel written by American writer Hannes Bok.  It was first published as the short story \"The Blue Flamingo\" in the January 1948 issue of the magazine \"Startling Stories\"; later the story was extensively revised and expanded by the author into novel form.  The novel version was first published in book form (posthumously) in paperback by Ballantine Books as the twenty-third volume of the Ballantine Adult Fantasy series in November, 1970.  The Ballantine edition includes an introduction by American author Lin Carter.\n\nKinsmen of the Dragon: Kinsmen of the Dragon is a fantasy novel by author Stanley Mullen.  It was published in 1951 by Shasta Publishers in an edition of 3,500 copies.  The book had originally been announced by Mullen's own Gorgon Press.  The superb jacket art was by Hannes Bok.\n\nA Rose for Ecclesiastes: \"A Rose for Ecclesiastes\" is a science fiction short story by American author Roger Zelazny, first published in the November 1963 issue of \"The Magazine of Fantasy and Science Fiction\" with a special wraparound cover painting by Hannes Bok.  It was nominated for the 1964 Hugo Award for Short Fiction.\n\nHannes Bok: Hannes Bok, pseudonym for Wayne Francis Woodard (July 2, 1914 – April 11, 1964), was an American artist and illustrator, as well as an amateur astrologer and writer of fantasy fiction and poetry.  He painted nearly 150 covers for various science fiction, fantasy, and detective fiction magazines, as well as contributing hundreds of black and white interior illustrations.  Bok's work graced the pages of calendars and early fanzines, as well as dust jackets from specialty book publishers like Arkham House, Llewellyn, Shasta Publishers, and Fantasy Press.  His paintings achieved a luminous quality through the use of an arduous glazing process, which was learned from his mentor, Maxfield Parrish.  Bok shared one of the inaugural 1953 Hugo Awards for science fiction achievement (best Cover Artist).\n\nA. Merritt: Abraham Grace Merritt (January 20, 1884 – August 21, 1943) – known by his byline, A. Merritt – was an American Sunday magazine editor and a writer of fantastic fiction.\n\nThe Sorcerer's Ship: The Sorcerer's Ship is a fantasy novel by Hannes Bok.  It was first published in the December 1942 issue of the magazine \"Unknown\", and was first published in book form in paperback by Ballantine Books as the ninth volume of the Ballantine Adult Fantasy series in December 1969.  The Ballantine edition includes an introduction by Lin Carter.  The novel has also been published in translation in Polish and Russian.  Like much of Bok's fiction, it is the story of a traveler \"from our world who found [himself] in colourful, magic lands that are far more attractive than our own\".\n\nThe Checklist of Fantastic Literature: The Checklist of Fantastic Literature is a bibliography of English science fiction, fantasy and weird books compiled and edited by Everett F. Bleiler with a preface by Melvin Korshak and a cover by Hannes Bok.\n\nQuestion: Which fantasy fiction author wrote The Black Wheel along with co-author Hannes Bok?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"book_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the book in question.\"\n    },\n    \"co_author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-author who wrote the book with Hannes Bok.\"\n    },\n    \"author_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the co-author.\"\n        },\n        \"byline\": {\n          \"type\": \"string\",\n          \"description\": \"The byline or known name of the co-author.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of fiction the co-author is known for.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"byline\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"book_title\",\n    \"co_author_name\",\n    \"author_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "book_title": {
        "type": "string",
        "description": "The title of the book in question."
      },
      "co_author_name": {
        "type": "string",
        "description": "The name of the co-author who wrote the book with Hannes Bok."
      },
      "author_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the co-author."
          },
          "byline": {
            "type": "string",
            "description": "The byline or known name of the co-author."
          },
          "genre": {
            "type": "string",
            "description": "The genre of fiction the co-author is known for."
          }
        },
        "required": [
          "full_name",
          "byline",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "book_title",
      "co_author_name",
      "author_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
