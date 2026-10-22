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
Larklight: Larklight, or the Revenge of the White Spiders!  or to Saturn's Rings and Back!  is a young adult novel by author Philip Reeve.  Illustrated by David Wyatt, it is the first book in the Larklight Trilogy.

Here Lies Arthur: Here Lies Arthur is a young-adult novel by Philip Reeve, published by Scholastic in 2007.  Set in fifth or sixth century Britain and the Anglo-Saxon invasion, it features a girl who participates in the deliberate construction of legendary King Arthur during the man's lifetime, orchestrated by a bard.  Reeve calls it a back-creation: not a genuine historical novel as it is not based on actual specific events; rather it is "back-created" from the legends, giving them a "realistic" origin.

Mortal Engines Quartet: The Mortal Engines Quartet is a tetralogy consisting of four novels written by the British author Philip Reeve: "Mortal Engines" (2001), "Predator's Gold" (2003), "Infernal Devices" (2005), and "A Darkling Plain" (2006).  It has also been referred to as the Predator Cities Quartet or the Hungry City Chronicles, although the author has objected to those names.

Starcross (novel): Starcross, or the Coming of the Moobs!  or Our Adventures in the Fourth Dimension!  is a young adult novel by Philip Reeve, released in October 2007.  Illustrated by David Wyatt, it is the second book in the "Larklight" trilogy, sequel to the 2006 novel "Larklight".

A Web of Air: A Web of Air is a young adult post-apocalyptic science fiction novel by Philip Reeve.  The sequel to "Fever Crumb", it is the second book in the Mortal Engines Quartet prequel series.  It was published in April 2010.

Traction City (novella): Traction City is a novella by Philip Reeve and is a prequel to the Mortal Engines Quartet it was released as a flip book alongside Chris Priestlys' teachers tales of terror for World Book Day.

Fever Crumb Series: The Fever Crumb Series is the title of a series of novels written by British author, Philip Reeve, and is the prequel series to his critically acclaimed "Mortal Engines Quartet".  As of 2015 the series consists of three books: "Fever Crumb" (2009), "A Web of Air" (2010), and "Scrivener's Moon" (2011).  The books follow a young woman known as Fever Crumb, and her adventures set around the time of the creation of the first traction cities that become so prevalent in the Mortal Engines series.  Reeve stated in 2011 that he had always envisaged a quartet for the series, assuring readers of a fourth installment.

Mortal Engines: Mortal Engines is the first of four novels in Philip Reeve's quartet of the same name.  The book focuses on a futuristic, steampunk version of London, now a giant machine striving to survive on a world running out of resources.  The book has won a Nestlé Smarties Book Prize and was shortlisted for the 2002 Whitbread Award.

Infernal Devices (Philip Reeve novel): Infernal Devices is the third of four novels in Philip Reeve's children's series, the "Mortal Engines Quartet".

Mothstorm: Mothstorm, or the Horror from Beyond Uranus Georgium Sidus!  or a Tale of Two Shapers is a young adult novel by Philip Reeve, released in October 2008.  Illustrated by David Wyatt, it is the third book in the Larklight Trilogy, sequel to the 2007 novel "Starcross".

Question: Traction city is a prequel to a novella by Philip Reeve, what is the third book including the prequel?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "prequel_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the prequel novella."
        },
        "is_novella": {
          "type": "boolean",
          "description": "Indicates if the prequel is a novella."
        },
        "prequel_to_series": {
          "type": "string",
          "description": "The name of the series the novella is a prequel to."
        }
      },
      "required": [
        "title",
        "is_novella",
        "prequel_to_series"
      ],
      "additionalProperties": false
    },
    "main_series_books": {
      "type": "array",
      "description": "A list of books in the main series, in order.",
      "items": {
        "type": "object",
        "properties": {
          "order_in_series": {
            "type": "integer",
            "description": "The sequential order of the book within its main series."
          },
          "title": {
            "type": "string",
            "description": "The title of the book."
          },
          "publication_year": {
            "type": "integer",
            "description": "The year the book was published."
          }
        },
        "required": [
          "order_in_series",
          "title",
          "publication_year"
        ],
        "additionalProperties": false
      }
    },
    "combined_sequence_position": {
      "type": "integer",
      "description": "The position of the requested book in the combined sequence (prequel + main series)."
    },
    "answer_book_title": {
      "type": "string",
      "description": "The title of the book at the specified position in the combined sequence."
    }
  },
  "required": [
    "prequel_details",
    "main_series_books",
    "combined_sequence_position",
    "answer_book_title"
  ],
  "additionalProperties": false
}
