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
The Tall Grass and Other Stories: The Tall Grass and other Stories is a short story collection written by American author Joe R. Lansdale.  It was published by Gere Donovan Press.  This collection is currently only available as an Amazon Kindle e-book.  According to the author, it may be available as a printed book at a later date.

Neil Gaiman: Neil Richard MacKinnon Gaiman ( ; born Neil Richard Gaiman, 10 November 1960) is an English author of short fiction, novels, comic books, graphic novels, audio theatre, and films.  His notable works include the comic book series "The Sandman" and novels "Stardust", "American Gods", "Coraline", and "The Graveyard Book".  He has won numerous awards, including the Hugo, Nebula, and Bram Stoker awards, as well as the Newbery and Carnegie medals.  He is the first author to win both the Newbery and the Carnegie medals for the same work, "The Graveyard Book" (2008).  In 2013, "The Ocean at the End of the Lane" was voted Book of the Year in the British National Book Awards.

M Is for Magic: M Is for Magic is a collection of child-friendly short fiction by Neil Gaiman.

Sharon Creech: Sharon Creech (born July 29, 1945) is an American writer of children's novels.  She was the first American winner of the Carnegie Medal for British children's books and the first person to win both the American Newbery Medal and the British Carnegie.

Jan Mark: Jan Mark (22 June 1943 – 16 January 2006) was a British writer best known for children's books.  In all she wrote over fifty novels and plays and many anthologised short stories.  She won the annual Carnegie Medal from the Library Association, recognising the year's best children's book by a British subject, both for "Thunder and Lightnings" (1976) and for "Handles" (1983).  She was also a "Highly Commended" runner up for "Nothing To Be Afraid Of" (1980).  She has won the Carnegie Medal twice, and no one has won three Carnegies.

Carnegie Medal for Excellence in Children's Video: The Andrew Carnegie Medal for Excellence in Children's Video was named in honor of nineteenth-century American philanthropist Andrew Carnegie.  It honors the producer of the most outstanding video production for children.  The Medal is supported by the Carnegie Corporation of New York and administered by the Association for Library Service to Children (ALSC), a division of the American Library Association (ALA), through a Carnegie endowment.  In the past 19 years (1991-2009), 19 titles have been honored with the award.

Tulku (novel): Tulku is a children's historical novel by Peter Dickinson, published by Gollancz in 1979.  Set in China and Tibet at the time of the Boxer Rebellion, it features a young teenage boy orphaned by the violence, who flees with others to a Buddhist monastery.  Dickinson and "Tulku" won two major awards for British children's books, the Whitbread Children's Book Award and the Carnegie Medal.  The Carnegie Medal from the Library Association then recognised the year's outstanding children's book by a British subject.

Bernard Ashley (author): Bernard John Ashley (born April 1935) is a British author of books for children and young adults.  His debut novel, "The Trouble with Donovan Croft", published in 1974, won "The Other Award", an alternative to the Carnegie Medal.  "A Kind of Wild Justice" (1978), "Running Scared" (1986), and "Little Soldier" (1999) were commended runners up for the Carnegie Medal from the Library Association, recognising the year's best children's book.  The first two have been reissued by OUP in their Children's Modern Classics series, the third re-issued in a 15th anniversary edition.  Ashley's TV drama "Dodgem" (based on his own novel) won the Royal Television Society Award for Best Entertainment programme (BBC) in 1993.

Set in Stone (novel): Set in Stone is a children's fantasy novel written by Linda Newbery.  It won the Costa Children's Book of the Year Prize for 2006, and was nominated for the 2007 Carnegie Medal.

The Wanderer (Creech novel): The Wanderer is a children's novel by Sharon Creech, published in 2000.  It was shortlisted for the Carnegie Medal and named a Newbery Honor book.

Question: M Is for Magic is a collection written by an author who won both a Newbery and Carnegie medal for what book?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "collection_title": {
      "type": "string",
      "description": "The title of the short story collection mentioned in the question."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author who wrote the collection."
    },
    "awards_received_by_author": {
      "type": "array",
      "description": "A list of notable awards won by the author.",
      "items": {
        "type": "string"
      }
    },
    "book_awarded_both_medals": {
      "type": "object",
      "description": "Details about the specific book that won both the Newbery and Carnegie medals for the author.",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the book."
        },
        "medals_won": {
          "type": "array",
          "description": "The specific medals won by this book.",
          "items": {
            "type": "string"
          }
        },
        "award_year": {
          "type": "integer",
          "description": "The year the book won the specified medals."
        }
      },
      "required": [
        "title",
        "medals_won",
        "award_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "collection_title",
    "author_name",
    "awards_received_by_author",
    "book_awarded_both_medals"
  ],
  "additionalProperties": false
}
