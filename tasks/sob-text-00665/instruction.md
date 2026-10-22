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
Sonnet 8: Sonnet 8 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.  As with the other procreation sonnets, it urges a young man to settle down with a wife and to have children.  It insists a family is the key to living a harmonious, peaceful life.

Sonnet 14: Sonnet 14 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.

Sonnet 3: Sonnet 3 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.

Sonnet 1: Sonnet 1 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.

Sonnet 12: Sonnet 12 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.

Sonnet 2: Sonnet 2 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.

Sonnet 6: Sonnet 6 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.  The sonnet continues Sonnet 5, thus forming a diptych.  It also contains the same distillatory trope featured in Sonnet 54, Sonnet 74 and Sonnet 119.

Early texts of Shakespeare's works: The earliest texts of William Shakespeare's works were published during the 16th and 17th centuries in quarto or folio format.  Folios are large, tall volumes; quartos are smaller, roughly half the size (see Book size).  The publications of the latter are usually abbreviated to Q1, Q2, etc., where the letter stands for "quarto" and the number for the first, second, or third edition published.

Sonnet 11: Sonnet 11 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the 126 sonnets of the Fair Youth sequence, a grouping of Shakespeare's sonnets addressed to an unknown young man.  While the order in which the sonnets were composed is undetermined (though it is mostly agreed that they were not written in the order in which modern readers know them), Sonnet 11 was first published in a collection, the Quarto, alongside Shakespeare's other sonnets in 1609.

Sonnet 5: Sonnet 5 is one of 154 sonnets written by the English playwright and poet William Shakespeare.  It is a procreation sonnet within the Fair Youth sequence.  It forms a diptych with Sonnet 6, which continues it.

Question: What procreation sonnet within the 126 sonnets of the Fair Youth sequence was published in smaller volumes roughly half the size of Folios?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sonnet_number": {
      "type": "integer",
      "description": "The numerical identifier of the sonnet."
    },
    "sonnet_type": {
      "type": "string",
      "description": "The thematic classification of the sonnet."
    },
    "sequence": {
      "type": "string",
      "description": "The sequence of sonnets to which this sonnet belongs."
    },
    "sequence_total_sonnets": {
      "type": "integer",
      "description": "The total number of sonnets in the specified sequence."
    },
    "publication_details": {
      "type": "object",
      "properties": {
        "format": {
          "type": "string",
          "description": "The publication format of the sonnet."
        },
        "size_description": {
          "type": "string",
          "description": "A description of the publication format's size relative to other formats."
        },
        "first_publication_year": {
          "type": "integer",
          "description": "The year the sonnet was first published in this format."
        }
      },
      "required": [
        "format",
        "size_description",
        "first_publication_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "sonnet_number",
    "sonnet_type",
    "sequence",
    "sequence_total_sonnets",
    "publication_details"
  ],
  "additionalProperties": false
}
