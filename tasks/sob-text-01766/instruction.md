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
Richard McGuire: Richard McGuire (born 1957) is an illustrator, graphic designer, comic book artist, animator, children's book author, musician, and toy designer.  His illustrations have been published in the New York Times, The New Yorker, Le Monde, and other publications.  His short story "Here" is likely the most lauded comic book story from recent decades.  He is a founding member and bassist for the band Liquid Liquid.  His bass line from the song ""Cavern"" is considered one of the most sampled bass lines of all time.""

Metropolis Collectibles: Metropolis Collectibles is a famous rare comic book dealer of vintage American comics, primarily known for its large collection of comic books originally published in the 1930s, 1940s, 1950s, 1960s and 1970s.  Metropolis was founded in 1984 by Stephen Fishler, and merged companies in 1999 with Vincent Zurzolo, Jr., of Vincent's Collectibles.; Zurzolo said that as he found he could not compete with Fishler's business, merging the two made sense.  The company is located on Broadway in New York City, and the comic book showroom allows viewings by appointment only.  Over the years, Metropolis Collectibles has grown from being a comic-book mail-order company to maintaining a major online retail presence.  In addition to being comic book buyers and comic book sellers, Metropolis also gives comic book appraisals and provides comic book valuation services of rare, old out-of-print comics.  Metropolis Collectibles has obtained a variety of notable classic comic book collections over the years, or "pedigrees", including the Crowley Collection, the Allentown Pedigree, the D-Copy Collection, and the Northford Collection.  In August 2014, the company was able to purchase a near-mint copy of "Action Comics #1" (CGC 9.0) for $3.2 million in an auction on eBay.

Silent Bob Speaks: Silent Bob Speaks: The Collected Writings of Kevin Smith is a collection of essays written by screenwriter, director, and comic book author Kevin Smith.  The collection comes from sources including "Arena Magazine", "Details", "New Jersey Monthly", and "Film Comment".  Topics range from polemic assaults on pop culture figures to reflections on Spider-Man and his diagnosis with morbid obesity.

Len Strazewski: Len Strazewski (born February 16, 1955) is a comic book author who wrote "Starman" after Roger Stern.  He has also worked on "The Flash", "Justice Society of America", "Phantom Lady", "The Fly", and many other titles for DC comics.  He also worked on a comic version of Speed Racer for NOW Comics.  His "Street Fighter II" comic for Malibu Comics was canceled after three issues by Capcom because of his choice to have Ken Masters murdered in the second issue.  Also on Malibu, he wrote "Prime", "Elven" and "Prototype".  He is a professor of journalism at Columbia College Chicago and a member of the school's Board of Trustees.

The Traffic in Women: "The Traffic in Women" is an essay written by anarchist writer Emma Goldman in 1910.  It has been published in various ways, including within Emma Goldman’s "Anarchism and Other Essays" (1911), published by Mother Earth, and as the named, leading essay of a collection of Emma Goldman essays: "The Traffic in Women, and Other Essays on Feminism" (1970, Times Change Press, 1971 paperback). " Mother Earth" was a monthly anarchist magazine founded by Goldman, Max Baginski, and others in 1906.  The essay is one of more than 20 articles that Goldman wrote during 1906 to 1940.

George Petros: George Petros (born George Lawrence Petros, January 11, 1955, Chicago, Illinois, United States) is an American art designer, author, editor, interviewer and illustrator.  From 1984 through 1992 he published and edited "EXIT", a punk-inspired art and science fiction magazine he founded with Adam Parfrey and Kim Seltzer.  From 1992 through 2000 he edited and art-directed "Seconds", an all-interview music and culture magazine founded by Steven Blush.  From 2000 through 2005 he was a contributing editor of "Juxtapoz", the low-brow art magazine founded by Robert Williams, and the senior editor of "Propaganda", a goth/industrial music and style magazine founded by Fred H. Berger.

Comics artist: A comics artist (also comic book artist or graphic novel artist, comic book producer, comic book illustrator, comic book writer, and comic book author) is a person working within the comics medium on comic strips, comic books, or graphic novels.  The term may refer to any number of artists who contribute to produce a work in the comics form, from those who oversee all aspects of the work to those who contribute only a part.

Comic Book Artist: Comic Book Artist was an American magazine founded by Jon B. Cooke devoted to anecdotal histories of American comic books, with emphasis on comics published since the 1960s.  It was published by TwoMorrows Publishing and later Top Shelf Productions from 1998–2005.  Its sequel is "Comic Book Creator" magazine which started publishing in 2013 and is also published by TwoMorrows.

The Big Moo: The Big Moo: Stop Trying to be Perfect and Start Being Remarkable (2005) is a collection of short essays on marketing.  The essays were written by 32 different well-known authors in the field.  They included Tom Peters, Malcolm Gladwell, Guy Kawasaki, Mark Cuban, and Dan Pink.  The specific author of each essay, however, was not identified.  The book's editor, Seth Godin said that to identify which author wrote what essay would have been a distraction.  The goal of the book was to spark people's imaginations as well as raise money for charity.  Proceeds from the book are donated to the Acumen Fund, the Juvenile Diabetes Research Foundation International, and Room to Read.

Details (magazine): Details was an American monthly men's magazine published by Condé Nast, founded in 1982 by Annie Flanders.  Though primarily a magazine devoted to fashion and lifestyle, "Details" also features reports on relevant social and political issues.  In November 2015 Condé Nast announced that the magazine would cease publication with the issue of December 2015/January 2016.

Question: What comic book author wrote a collection of essays that included a magazine founded by Annie Flanders as a source?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comic_book_author": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the comic book author."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles attributed to the author."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "essay_collection": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the essay collection written by the author."
        },
        "sources_from_magazine": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "magazine_name": {
                "type": "string",
                "description": "The name of the magazine that served as a source."
              },
              "founder_name": {
                "type": "string",
                "description": "The name of the magazine's founder."
              },
              "founding_year": {
                "type": "integer",
                "description": "The year the magazine was founded."
              }
            },
            "required": [
              "magazine_name",
              "founder_name",
              "founding_year"
            ],
            "additionalProperties": false
          },
          "description": "Details about the magazine sources for the essay collection, specifically those founded by Annie Flanders."
        }
      },
      "required": [
        "title",
        "sources_from_magazine"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the comic book author who meets the criteria."
    }
  },
  "required": [
    "comic_book_author",
    "essay_collection",
    "final_answer"
  ],
  "additionalProperties": false
}
