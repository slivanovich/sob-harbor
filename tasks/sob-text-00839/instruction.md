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
Truck Dogs: Truck Dogs: A Novel in Four Bites is a children's adventure/science fiction novel by Australian author Graeme Base, who is famous for his large picture books such as "Animalia".  It was published in 2003 and nominated for a CBCA 2004 Book of the Year for younger readers.  The novel is supposed to take place in the future, but the setting is ultimately a fantasy world based on a rural desert town (as in the Australian outback or the western United States).  All of the characters are caricaturized, anthropomorphic dogs of various breeds, part biological and part machine.  Their lower bodies are formed by the chassis and wheels of some kind of modern vehicle, often a truck.  Reviewers have referred to the novel as a meeting of "Hell" and the Book of Revelation

Bing West: Francis J. "Bing" West (Boston, Massachusetts, May 2, 1940) is an American author and former Assistant Secretary of Defense for International Security Affairs during the Reagan Administration.  His 2004 book "The March Up: Taking Baghdad with the First Marine Division", written with United States Marine Corps General Ray L. Smith, received the 2004 William E. Colby Award, as well as the 2004 General Wallace M. Greene, Jr.  Award given by the Marine Corps Heritage Foundation for "distinguished non-fiction dealing with U.S. Marines or Marine Corps life."

How to Talk to a Liberal (If You Must): How to Talk to a Liberal (If You Must) is a 2004 book by Ann Coulter.

The Price of Loyalty: The Price of Loyalty: George W. Bush, the White House, and the Education of Paul O'Neill, is a 2004 book by Pulitzer Prize-winning author Ron Suskind.  The book was the first to provide critical insight into the events that led up to the Iraq War.  "The Price of Loyalty" was met with both commercial and critical success, and was the first book by Suskind to be a #1 "New York Times" best-seller.

Michael Leahy (author): Michael Leahy (born 1953) is an American author and award-winning writer for "The Washington Post" and "The Washington Post Magazine".  He is best known for his latest non-fiction book, The Last Innocents, which examines the tumultuous political & social change of the 1960s through the lens of the legendary Los Angeles Dodgers.  Leahy has also earned recognition for his 2004 book, When Nothing Else Matters, which chronicles basketball superstar Michael Jordan's last comeback to the NBA.  Leahy's stories have also been selected for the 2001, 2002, 2003, and 2004 editions of The Best American Sports Writing anthologies.  His first book, Hard Lessons, follows the lives of six Beverly Hills High School students, class of 1986, and deals with the challenges and anxieties of teenage life in modern America.

The Bloke's Guide To Pregnancy: The Bloke's Guide To Pregnancy is a 2004 book by Jon Smith, a father, Internet marketing expert, and author of the Amazon.co.uk Best Seller "Get Into Bed With Google".  The book provides advice, information, and "a helping hand" to expectant fathers and new dads.  Written with the input of 116 dads, the book outlines what dad can expect to see, think, and feel over the nine months of pregnancy.  Since publication, the book has generated heated online debate regarding the role of fathers during pregnancy and extensive press coverage.

Douglas Wood (naturalist): Douglas Wood is an American children's author, author, singer, song writer, speaker, and musician.  One of Wood's children's books, "Old Turtle and the Broken Truth", won one of the 2004 Book Sense Book of the Year Awards.

The Secret Life of Bees (novel): The Secret Life of Bees is a book by author Sue Monk Kidd.  Set in 1964, it is a coming-of-age story about loss and betrayal.  It received critical acclaim and was a "New York Times" bestseller.  It won the 2004 Book Sense Book of the Year Awards (Paperback), and was nominated for the Orange Broadband Prize for Fiction.

Ann Coulter: Ann Hart Coulter ( ; born December 8, 1961) is an American conservative social and political commentator, writer, syndicated columnist, and lawyer.  She frequently appears on television, radio, and as a speaker at public and private events.

Living Under God: Living Under God is a sequel to the 2004 book by dc Talk members Toby Mac and Michael Tait.  The book follows much the same style as the first book, "Under God".  It was published with help from WallBuilders.

Question: The author of the 2004 book How to Talk to a Liberal (If You Must) was born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the book mentioned in the question."
    },
    "book_publication_year": {
      "type": "integer",
      "description": "The publication year of the book."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the book."
    },
    "author_birth_year": {
      "type": "integer",
      "description": "The birth year of the author."
    }
  },
  "required": [
    "book_title",
    "book_publication_year",
    "author_name",
    "author_birth_year"
  ],
  "additionalProperties": false
}
