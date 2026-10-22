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
Laura Bush: Laura Lane Welch Bush (born November 4, 1946) is the wife of the 43rd President of the United States, George W. Bush, and was the First Lady from 2001 to 2009.

Carol Judge: Carol Ann Judge (June 7, 1941 – December 7, 2014) was an American healthcare advocate and registered nurse.  She served as the First Lady of the U.S. state of Montana from January 1, 1973, until her divorce from Governor Thomas Lee Judge in the winter of 1980.  Judge, who was 31 years old when she assumed the role of First Lady in 1973, remains the youngest First Lady in Montana's history.

Devin Scillian: Devin Scillian ( ; born January 11, 1963) is an American journalist, country singer, children's author and actor.  His eighteen books include the national bestseller "A Is For America" (2001), "Fibblestax" (2000), and "Memoirs of a Goldfish" (2010) which won the Wanda Gag Award as the nation's best "read aloud" book.  His most recent book is "Missile Toe: A Very Confused Christmas" illustrated by Marty Kelley, published by Sleeping Bear Press in 2017.  He's co-written two books with his wife, Corey.  "One Kansas Farmer," illustrated by Doug Bowles, was released in 2009.  Their previous book, "S Is For Sunflower", won the Bill Martin, Jr.  Picture Book Award in 2007.  Among his fans is former First Lady Laura Bush who invited him to read at the White House for the 2004 Easter Egg Roll.

Charlie Fern: Charlene "Charlie" Fern (born in 1968) is an American speechwriter, business owner, public speaker and journalist who served as First Lady Laura Bush's speechwriter for six years, first in the Texas Governor's Office, then at the White House, through October 2002.  Fern's speeches included the first Presidential radio address delivered by a U.S. First Lady, in November 2001, and a May 2002 Radio Free Afghanistan address, following the September 11 attacks.  She also wrote for President George W. Bush.

Denise Brunkus: Denise Brunkus is an American illustrator of children's picture books.  She has illustrated more than 60 books, including the Junie B. Jones series and "Read All About It!"  by Laura and Jenna Bush.

Vicki Risch: Vicki Risch is the former First Lady of Idaho and the wife of U.S. Sen. Jim Risch, who served as Governor of Idaho in 2006.  She became First Lady on May 26, 2006, when her husband succeeded former Gov. Dirk Kempthorne, who resigned to become United States Secretary of the Interior.  Mrs. Risch succeeded former First Lady Patricia Kempthorne who had held the post for over seven years.  Mrs. Risch served as First Lady until January 2007, as her husband did not seek a full term as governor, but rather was reelected to his old post as lieutenant governor.

Louisa Adams: Louisa Catherine Johnson Adams (February 12, 1775 – May 15, 1852), wife of John Quincy Adams, was First Lady of the United States from 1825 to 1829.  The daughter of the American Consul in London, she was the first First Lady to be born outside the United States, or outside areas that were later to become part of the United States, such as the Thirteen Colonies – a distinction that would not be replicated until 192 years later by Melania Trump.

White House FBI files controversy: The White House FBI files controversy of the Clinton Administration, often referred to as Filegate, arose in June 1996 around improper access in 1993 and 1994 to FBI security-clearance documents.  Craig Livingstone, director of the White House's Office of Personnel Security, improperly requested, and received from the FBI, background reports concerning several hundred individuals without asking permission.  The revelations provoked a strong political and press reaction because many of the files covered White House employees from previous Republican administrations, including top presidential advisors.  Under criticism, Livingstone resigned from his position.  Allegations were made that senior White House figures, including First Lady Hillary Clinton, may have requested and read the files for political purposes, and that the First Lady had authorized the hiring of the underqualified Livingstone.

Lois Rhame West: Lois Rhame West (September 5, 1921 – May 6, 2014) was an American health and physical fitness advocate, activist, and philanthropist.  She served as First Lady of South Carolina from 1971 until 1975 during the administration of her husband, former Governor John C. West.  Rhame West, a former faculty member at the University of South Carolina, made physical education and wellness the focus of her tenure as the state's First Lady.  West later became the first woman serve as president of the Muscular Dystrophy Association, a position she held for two terms.  She served on the Muscular Dystrophy Association's national board of directors for forty years.

Anna Harrison: Anna Tuthill Symmes Harrison (July 25, 1775 – February 25, 1864), wife of President William Henry Harrison and grandmother of President Benjamin Harrison, was nominally First Lady of the United States during her husband's one-month term in 1841, but she never entered the White House.  At the age of 65 years during her husband's presidential term, she is the oldest woman ever to become First Lady, as well as having the distinction of holding the title for the shortest length of time, and the first person to be widowed while holding the title.  She was the last First Lady to have been born in British America.

Question: In what years was one of the co-authors of "Read All About It!" a First Lady?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_lady_name": {
      "type": "string",
      "description": "The name of the co-author who served as a First Lady."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book co-authored by the First Lady."
    },
    "first_lady_tenure": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The year the individual began their term as First Lady."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the individual ended their term as First Lady."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "first_lady_name",
    "book_title",
    "first_lady_tenure"
  ],
  "additionalProperties": false
}
