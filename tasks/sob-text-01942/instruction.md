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
Bloomsbury 21: Bloomsbury 21 is a series of 21 books published in 2007 by Bloomsbury to celebrate their 21st anniversary.  The books are limited editions of 21 of Bloomsbury's most famous published works.  The books have covers featuring a white background with a picture of the original cover of the particular book, tilted in such a way that part of the picture is cut off and appears on the next book in the series.  When the books are placed side by side in numerical order, their covers form a panorama of the 21 original book covers.  Each book features an introduction by a fellow author and reading group guides.  On the spine of each book is its number in the series above the number 21 to indicate the book's place within the series.  Authors whose works have been included in the series include Margaret Atwood and J.K. Rowling.

Throne of Glass: Throne of Glass is a young adult high fantasy novel series by American author Sarah J. Maas, beginning with the inaugural entry of the same name.  The story follows the journey of Celaena Sardothien, a teenage assassin in a corrupted kingdom with a tyrannical ruler.  As the tale progresses, Celaena forms unexpected bonds and uncovers a conspiracy amidst her adventures.

Christadelphian hymnals: The earliest Christadelphian hymn book published was the "Sacred Melodist" which was published by Benjamin Wilson in Geneva, Illinois in 1860.  The next was the hymn book published for the use of "Baptised Believers in the Kingdom of God" (an early name for Christadelphians) by George Dowie in Edinburgh in 1864. " "The Golden Harp"" was put together in 1864 by Scotsman Robert Roberts.  This was then followed a year later by first 'official' (as the Christadelphians had not been named as such until then) book, compiled also by Roberts, and was called simply ""The Christadelphian Hymn Book.""  It contained 223 psalms/hymns and 50 anthems but no music.  In 1869 Robert's produced a version of this book with music included.

The Good Book (book): The Good Book is a book by A. C. Grayling.  It was published in March 2011 by Walker & Company (a US imprint of Bloomsbury) with the subtitle "A Humanist Bible," and in April 2011 by Bloomsbury with the subtitle "A Secular Bible."

Sarah J. Maas: Sarah Janet Maas (born 5 March 1986) is a "New York Times" and "USA Today" bestselling American fantasy author.  Her debut novel, "Throne of Glass", was published in 2012 by Bloomsbury.

The Revengers (novel): The Revengers, published in 1982, is a novel in the long-running secret agent series Matt Helm by Donald Hamilton.  It was the first Helm book published since 1977 and the nineteenth book published overall since 1960.

Continuum International Publishing Group: Continuum International Publishing Group was an academic publisher of books with editorial offices in London and New York City.  It was purchased by Nova Capital Management in 2005.  In July 2011 it was taken over by Bloomsbury Publishing.  As of September 2012, all new Continuum titles are published under the Bloomsbury name (under the imprint Bloomsbury Academic).

Unique World Records: Unique World Records is a world record book published in India.  The reference book published annually, listing all world records in the categories of amazing facts, biggest, business, collections, creativity, education, extraordinary talent, inventions, marathon, memory and mental world, most and mass, people and places, smallest, strength and stamina, and youngest achievers.

Assassin's Creed III: Liberation: Assassin's Creed III: Liberation is a 2012 action-adventure video game developed and published by Ubisoft, initially as an exclusive title for PlayStation Vita.  Sony announced the game at its press conference during the Electronic Entertainment Expo 2012, few days after first leaks about the game presented in "Game Informer".  It was released on October 30, 2012 alongside "Assassin's Creed III", with which it can be linked.  The game was re-released as Assassin's Creed: Liberation HD for the PlayStation 3, Xbox 360 and Microsoft Windows via the PlayStation Network, Xbox Live Arcade and Steam, respectively.  It was later packed as part of "Assassin's Creed The Americas Collection" for the PlayStation 3 and Xbox 360, along with "Assassin's Creed III" and "".

Assassin's Creed Rogue: Assassin's Creed Rogue is an action-adventure video game developed by Ubisoft Sofia and published by Ubisoft.  It is the seventh major installment in the "Assassin's Creed" series, and acts as a sequel to 2013's "" and a prequel to 2012's "Assassin's Creed III" with its final mission being the prologue to 2014's "Assassin's Creed Unity".  It is the last of the "Assassin's Creed" games to be released for PlayStation 3 and Xbox 360, Ubisoft announcing that the company will no longer release games for them, except for its casual rhythm series "Just Dance".  The game was first released for PlayStation 3 and Xbox 360 in November and December 2014, and released for Microsoft Windows on March 10, 2015.

Question: Who is the teenage assassin in the book published in 2012 by Bloomsbury?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "assassin_name": {
      "type": "string",
      "description": "The name of the teenage assassin character."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book featuring the assassin."
    },
    "author_name": {
      "type": "string",
      "description": "The author of the book."
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the book."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the book was published."
    },
    "character_role": {
      "type": "string",
      "description": "The role of the character in the story."
    }
  },
  "required": [
    "assassin_name",
    "book_title",
    "author_name",
    "publisher",
    "publication_year",
    "character_role"
  ],
  "additionalProperties": false
}
