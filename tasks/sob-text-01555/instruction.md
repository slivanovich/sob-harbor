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
The Edge of Evolution: The Edge of Evolution: The Search for the Limits of Darwinism is an intelligent design book by Discovery Institute fellow Michael Behe, published by the Free Press in 2007.  Behe argues that while evolution can produce changes within species, there is a limit to the ability of evolution to generate diversity, and this limit (the "edge of evolution") is somewhere between species and orders.  On this basis, he says that known evolutionary mechanisms cannot be responsible for all the observed diversification from the last universal ancestor and the intervention of an intelligent designer can adequately account for much of the diversity of life.  It is Behe's second intelligent design book, his first being "Darwin's Black Box".

Philadelphia Free Press: Philadelphia Free Press was a 1960s era underground newspaper published biweekly in Philadelphia, Pennsylvania from 1968 to 1972.  Originally launched at Temple University in May 1968 as the monthly "Temple Free Press", it separated from Temple and became the "Philadelphia Free Press" in September 1968.

Free Press (magazine): Free Press was a short-lived but well-attempted and widely circulated, monthly magazine in Malayalam language published from Dehli between 2003 and 2006.  At 23, Vinod K. Jose became one of the youngest editor-in-chiefs of any current affairs registered magazine in India when he started "Free Press".  "Free Press" was the first publication to have initiated the concept of citizen journalism in Kerala.

Kitzmiller v. Dover Area School District: Tammy Kitzmiller, et al. v. Dover Area School District, et al. (400 F. Supp.  2d 707, Docket No. 4cv2688) was the first direct challenge brought in the United States federal courts testing a public school district policy that required the teaching of intelligent design.  In October 2004, the Dover Area School District of York County, Pennsylvania, changed its biology teaching curriculum to require that intelligent design be presented as an alternative to evolution theory, and that "Of Pandas and People", a textbook advocating intelligent design, was to be used as a reference book.  The prominence of this textbook during the trial was such that the case is sometimes referred to as the Dover Panda Trial, a name which recalls the popular name of the Scopes Monkey Trial in Tennessee, 80 years earlier.  The plaintiffs successfully argued that intelligent design is a form of creationism, and that the school board policy violated the Establishment Clause of the First Amendment to the United States Constitution.  The judge's decision sparked considerable response from both supporters and critics.

Elisa Albert: Elisa Albert (born July 2, 1978) is the author of the short story collection "How this Night is Different (Free Press, 2006)", the novels "The Book of Dahlia (Free Press, 2008)" and "After Birth (Houghton Mifflin Harcourt, 2015)", and an anthology, "Freud's Blind Spot: Writers on Siblings (Free Press, 2010)".

Los Angeles Staff: The Los Angeles Staff was an underground newspaper published in Los Angeles in the 1970s.  It came into existence as a result of the temporary demise of the Los Angeles Free Press, which had been founded and published by Art Kunkin.  Around 1970, the L.A. Free Press failed to make an employee tax payment and the paper was seized by the Internal Revenue Service.  Kunkin managed to sell the "logo" of the paper, the phrase "The Los Angeles Free Press" to publisher Marvin Miller, who then resold it to some other parties in San Diego, California.  The staff of the Free Press, led by editor Brian Kirby and art director Phil Wilson, left to and form their own newspaper, calling it "The Staff".  They first moved into quarters on Santa Monica Blvd near Cahuenga Blvd., in Hollywood, California.  They later relocated to Hollywood Blvd., just west of Western Ave. in offices above a movie theater that was at that time showing soft-core porn.

Bard Free Press: The" Bard Free Press (the Free Press) is a monthly college newspaper published by students of Bard College, a private liberal arts college in Annandale-on-Hudson, New York.  The paper has a circulation of about 2,000 and is the only printed student newspaper at Bard.  The paper was founded in 2000, by former student editors of The Observer", Bard's newspaper at the time.  The" Free Press" and the "Bard Observer" merged in 2008.

Signature in the Cell: Signature in the Cell: DNA and the Evidence for Intelligent Design is a 2009 book about intelligent design by philosopher and intelligent design advocate Stephen C. Meyer.  The book was well received by some within the conservative, intelligent design and evangelical communities, but several other reviewers were critical and wrote that Meyer's claims are incorrect.

Creationism's Trojan Horse: Creationism's Trojan Horse: The Wedge of Intelligent Design is a 2004 book by Barbara Forrest and Paul R. Gross on the origins of intelligent design, specifically the Discovery Institute's Center for the Renewal of Science and Culture and its wedge strategy.  The authors are highly critical of what they refer to as intelligent design creationism, and document the intelligent design movement's fundamentalist Christian origins and funding.

Gert Korthof: Gert Korthof is a Dutch biologist who is trained in Utrecht University.  He has reviewed various books of evolution, creationism, and intelligent design, including Michael Behe's "The Edge of Evolution".  He contributed to "Why Intelligent Design Fails: A Scientific Critique of the New Creationism".

Question: Gert Korthof reviewed the intelligent design book published by Free Press in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the intelligent design book reviewed."
    },
    "author": {
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
    "reviewer": {
      "type": "string",
      "description": "The person who reviewed the book."
    },
    "book_genre": {
      "type": "string",
      "description": "The genre or category of the book."
    }
  },
  "required": [
    "book_title",
    "author",
    "publisher",
    "publication_year",
    "reviewer",
    "book_genre"
  ],
  "additionalProperties": false
}
