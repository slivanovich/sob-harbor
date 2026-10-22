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
Johnson Publishing Company: Johnson Publishing Company, Inc. is an American publishing company founded in November 1942 by businessman John H. Johnson.  Headquartered at 200 S. Michigan Avenue in Chicago, Illinois, United States.  Led by its flagship publication, "Ebony", Johnson Publishing is the largest African-American-owned publishing firm in the United States.  Johnson Publishing Company also published "Jet" magazine, a weekly magazine from November 1951 until June 2014.  The company operates a book division, which has published books such as "The New Ebony Cookbook" and the more controversial "". The company produced the 1954 film "The Secret of Selling the Negro Market", which was designed to encourage advertisers to promote their products and services in the African American media.  In 2016, Johnson announced the sale of its publications and the creation of a new publisher by the new owner called "Ebony Media Corp." The specialty cosmetics business will be retained by Johnson.

It's OK, I'm Wearing Really Big Knickers: It's OK, I'm Wearing Really Big Knickers is a bestselling young adult novel by Louise Rennison, the second in the Confessions of Georgia Nicolson series.  It was published in the US as On the Bright Side, I'm Now the Girlfriend of a Sex God.  Elements of the book were used in the film "Angus, Thongs and Perfect Snogging".

World Publishing Company: The World Publishing Company was an American publishing company founded by Alfred H. Cahen.  Originally headquartered in Cleveland, the company later added an office in New York City.  The company published genre fiction, trade paperbacks, children's literature, nonfiction books, textbooks, Bibles, and dictionaries, primarily from 1940 to 1980.  Authors published by World Publishing Company include Ruth Nanda Anshen, Michael Crichton, Simone de Beauvoir, Robert Ludlum, Sam Moskowitz, Ayn Rand, Rex Stout, Gay Talese, and Lin Yutang.  The company's Cleveland headquarters were located in the Caxton Building.

March of Comics: March of Comics was a long-running comic book series published by Western Publishing.  488 issues were published from 1946 to 1982.  Comic book writer Mark Evanier has described it as "...one of the most widely-circulated comic books in the history of mankind ... some issues reportedly were issued in quantities of five million and up".  The comic was not in a standard comic format.  All issues were smaller (in page count and eventually in size) than normal and at one point printed in an oblong format.  None were sold.  The series was published as a "giveaway" premium and sold to vendors who would stamp their name on it (or arranged for their logo to be printed on the cover) and given away to children who shopped at their store.  A prominent outlet for the series was through shoe departments at Sears stores.  No publisher logo was on the cover.  It was published under Western's "K.K. Publishing" subsidiary through the mid-1960s, then by just Western.  Many of the characters published by Western for Dell Comics and their own Gold Key Comics, both licensed and original, appeared in the comic.

Rhett Reese: Rhett Reese is an American film producer, television producer and screenwriter.  As a screenwriter, his credits include "Clifford's Really Big Movie", "Cruel Intentions 3".  He has collaborated with Paul Wernick, writing the films "Zombieland", "", and "Deadpool".  Together they also created the reality series "The Joe Schmo Show".

List of The Simpsons comics: The following is a list of comic book series based on the animated TV show The Simpsons and published by Bongo Comics in the United States.  The first comic strips based on "The Simpsons" appeared in 1991 in the magazine "Simpsons Illustrated" (not to be confused with the comic publications from 2012 bearing the same name), which was a companion magazine to the show.  The comic strips were popular and a one-shot comic book entitled "Simpsons Comics and Stories", containing three different stories, was released in 1993 for the fans.  The book was a success and due to this, the creator of "The Simpsons", Matt Groening, and his companions Bill Morrison, Mike Rote, Steve Vance and Cindy Vance created the publishing company Bongo Comics.  By the end of 1993, Bongo was publishing four titles: "Simpsons Comics", "Bartman", "Radioactive Man" and "Itchy & Scratchy Comics".  Since then, many more titles have been published, out of which "Simpsons Comics", "Bart Simpson", "Bart Simpson's Treehouse of Horror", "Simpsons Super Spectacular", Simpsons Summer Shindig, and "Simpsons Winter Wingding".

Clifford's Really Big Movie: Clifford's Really Big Movie is an American animated musical epic adventure comedy-drama family film, loosely based on the book series "Clifford the Big Red Dog" by Norman Bridwell, and more closely based on the classic PBS Kids TV series adapted from it.  This film was directed by Robert Ramirez, produced by Scholastic Entertainment and Big Red Dog Productions, and originally released to theaters by Warner Bros. on February 20, 2004.

Clifford the Big Red Dog: Clifford the Big Red Dog is an eponymously titled American children's book series about a giant red dog named Clifford.  It was first published in 1963 and was written by Norman Bridwell (1928–2014).  The series helped establish Scholastic as a premier publishing company, and Clifford himself is Scholastic's official mascot.

Jamsai: Jamsai is a publishing company located in Bangkok, Thailand.  Publishing since 2002, Jamsai has four brands: Jamsai Publishing Books, Enter Books Publishing, Zion Press Publishing, and Book Wave Publishing.  It is considered one of the largest publishers of teen romantic fiction in Thailand.  This publishing company has published many famous Thai writers.  Jamsai also supports many charities benefitting local communities.

The X-Files Season 11 (comics): The X-Files Season 11 is an 8-issue comic book series published by IDW Publishing.  The title follows "The X-Files Season 10" comic book series and serves as an extension of the television series "The X-Files".  Chris Carter, who created the television series, is the Executive Producer of the comic book series, while the issues are written by Joe Harris and illustrated by Matthew Dow Smith and Jordie Bellaire.

Question: "Clifford's Really Big Movie" is based of a book series published by what publishing company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie in question."
    },
    "book_series_title": {
      "type": "string",
      "description": "The title of the book series the movie is based on."
    },
    "publishing_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the publishing company."
        },
        "role": {
          "type": "string",
          "description": "The role of the company in relation to the book series."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "book_series_title",
    "publishing_company"
  ],
  "additionalProperties": false
}
