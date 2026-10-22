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
Killing Yourself to Live: 85% of a True Story: Killing Yourself to Live: 85% of a True Story is a work of non-fiction written by Chuck Klosterman, first published by Scribner in 2005.  The title is a reference to the 1973 song Killing Yourself To Live, by the heavy metal band Black Sabbath.  It is the third book released by Klosterman.  Klosterman constructed the book around the premise of writing magazine feature about death, particularly deaths involving rock 'n roll stars.  The actual feature, published in "Spin" in 2003, shares some ideas and language with the book.

The Hat (book): The Hat is a children's book written and illustrated by French artist and author Tomi Ungerer.  Published in 1970 by Parents' Magazine Press, the book tells the story of a poor veteran, Benito Badoglio, who becomes rich after he unwittingly gains possession of a magic hat.  The book is richly illustrated and the text contains numerous vivid and mellifluous descriptions and dialog.  For example, upon meeting the hat, the protagonist cries, "Thunder of Sebastopole!" ; in another scene, he shouts, "A thousand Potemkins!"  Other characters in the book are "cutthroats", "brigands", a "fainting contessa", and a "dashing cadet".  The author's interest in such colorful prose was explained by Selma G. Lanes in the Atlantic Monthly: "Ungerer feels strongly that children enjoy unfamiliar words and euphonious, mystifying phrases."  The setting for "The Hat" is nineteenth century Italy, and was described by Sydney D. Long in the Horn Book Magazine as "a never-never land ..., the comic-opera pictures [of "The Hat"] are full of mandolin-playing musicians, splashing fountains, and apple-cheeked peasant lasses."

I Wear the Black Hat: I Wear the Black Hat: Grappling with Villains (Real and Imagined) is a book written by Chuck Klosterman, first published by Scribner in 2013.  It is a collection of twelve essays examining the nature of villainy through the lens of popular culture, rock music, and sports.  It is the eighth book released by Klosterman.  The book debuted at number 5 on the "New York Times" bestseller list.

Chuck Klosterman: Charles John "Chuck" Klosterman (born June 5, 1972) is an American author and essayist who has written books and essays focused on American popular culture.  He has been a columnist for "Esquire" and ESPN.com and wrote "The Ethicist" column for "The New York Times Magazine".  Klosterman is the author of nine books, including two novels and the essay collection "".

Fear of a Black Hat: Fear of a Black Hat is a 1993 American mockumentary film on the evolution and state of American hip hop music.  The film's title is derived from the 1990 Public Enemy album "Fear of a Black Planet".  First screened at Sundance Film Festival on January 24, 1993, and later released on June 3, 1994, "Fear of a Black Hat" was written, produced and directed by, and co-stars Rusty Cundieff.

Downtown Owl: Downtown Owl: A Novel is a novel written by Chuck Klosterman, first published by Scribner in 2008.  It is the author's first all-fictional publication.

Eating the Dinosaur: Eating the Dinosaur is the sixth book written by Chuck Klosterman, first published by Scribner in 2009.  In the mold of Klosterman's earlier "", the book is a collection of previously unpublished essays concerning an array of pop culture topics.  The book cover was designed by Paul Sahre.

Sex, Drugs, and Cocoa Puffs: Sex, Drugs, and Cocoa Puffs: A Low Culture Manifesto is a book written by Chuck Klosterman, first published by Scribner in 2003.  It is a collection of eighteen comedic essays on popular culture.

The Visible Man (novel): The Visible Man: A Novel is a novel written by Chuck Klosterman, first published by Scribner in 2011.  It is the seventh book and second novel released by Klosterman.  Thematically, "The Visible Man" touches on the way media transforms reality, the meaning of culture, and the dissonance of self-perception.  It became a "New York Times" bestseller the month of its release.

Fargo Rock City: Fargo Rock City: A Heavy Metal Odyssey in Rural Nörth Daköta is a book written by Chuck Klosterman, first published by Scribner in 2001.  It is a history of heavy metal music, with a particular emphasis on the glam metal that flourished during Klosterman's formative years in the mid-to-late 1980s, through its demise in the early 1990s, and potential rebirth in the late 1990s.

Question: I Wear the Black Hat: Grappling with Villains (Real and Imagined) is a book written by Chuck Klosterman, first published by Scribner, in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The full title of the book."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the book."
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the book."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the book was first published."
    }
  },
  "required": [
    "book_title",
    "author_name",
    "publisher",
    "publication_year"
  ],
  "additionalProperties": false
}
