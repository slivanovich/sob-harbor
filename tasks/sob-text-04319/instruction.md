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
Michael Vey: The Prisoner of Cell 25: Michael Vey: The Prisoner of Cell 25 is a 2011 young adult/science fiction novel by Richard Paul Evans, and published by Glenn Beck's owned Mercury Ink.  The story follows Michael Vey, a teenager who is diagnosed with Tourette's syndrome and has the ability to pulse or surge electricity out of the palms of his hands.  It is the first book in what is to be a heptalogy.

Soldiers' Pay: Soldiers' Pay is the first novel published by the American author William Faulkner.  It was originally published by Boni & Liveright on February 25, 1926.  It is unclear if Soldiers' Pay is the first novel written by Faulkner.  It is however the first novel published by the author.  Faulkner was working on two manuscripts while finishing Soldiers' Pay.

The Locket (2002 film): The Locket is a 2002 Hallmark Hall of Fame psychological drama film starring Vanessa Redgrave.  The film is a screen adaptation of Richard Paul Evans' novel of the same name, adapted by Karen Arthur, and premiered on December 8, 2002 on CBS Television.

Michael Vey: Hunt for Jade Dragon: Michael Vey: Hunt for Jade Dragon is the fourth book of the seven book Michael Vey series, written by Richard Paul Evans.  The first book in the series, "", was #1 on the New York Times Best Seller list.

Adam Bede: Adam Bede, the first novel written by George Eliot (the pen name of Mary Ann Evans), was published in 1859.  It was published pseudonymously, even though Evans was a well-published and highly respected scholar of her time.  The novel has remained in print ever since and is used in university studies of 19th-century English literature.

Michael Vey: Storm of Lightning: Michael Vey: Storm of Lightning is the fifth book in Richard Paul Evans "Michael Vey" heptalogy.  It was released in September 2015.

Richard Paul Evans: Richard Paul Evans (born October 11, 1962) is an American author, best known for writing "The Christmas Box" and, more recently, the Michael Vey series.

Michael Vey: Battle of the Ampere: Michael Vey: Battle of the Ampere is the third book of the seven book Michael Vey series, written by Richard Paul Evans.  It was published September 17, 2013 by Simon Pulse/Mercury Ink.  The first book in the series, "", was #1 on the "New York Times" Best Seller list.

Michael Vey: Rise of the Elgen: Michael Vey: Rise of the Elgen is the second book by Richard Paul Evans in the Michael Vey series.  It carries on where the first book ("Michael Vey: Prisoner of Cell 25") left off in search for Michael's mother.

The Christmas Box: The Christmas Box (ISBN  ) is an American novel written by Richard Paul Evans and self-published in 1993.

Question: In what year was the first novel written by Richard Paul Evans published?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "first_novel_title": {
      "type": "string",
      "description": "The title of the author's first published novel."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the first novel was published."
    },
    "is_self_published": {
      "type": "boolean",
      "description": "Indicates if the novel was self-published."
    }
  },
  "required": [
    "author_name",
    "first_novel_title",
    "publication_year",
    "is_self_published"
  ],
  "additionalProperties": false
}
