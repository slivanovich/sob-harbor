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
C. J. Cherryh: Carolyn Janice Cherry (born September 1, 1942), better known by the pen name C. J. Cherryh, is an American writer of speculative fiction.  She has written more than 60 books since the mid-1970s, including the Hugo Award-winning novels "Downbelow Station" (1981) and "Cyteen" (1988), both set in her Alliance-Union universe.  She is known for "world building," depicting fictional realms with great realism supported by vast research in history, language, psychology, and archeology.  Her series of fantasy novels set in the Alliance-Union universe, the Morgaine Stories, have sold in excess of 3 million copies.

Brothers of Earth: Brothers of Earth is a 1976 science fiction novel by American writer C. J. Cherryh.  It was the second of Cherryh's novels to be published, appearing after "Gate of Ivrel", although she had completed and submitted "Brothers of Earth" first.  Donald A. Wollheim, the editor of DAW Books, decided that publishing "Gate of Ivrel" first would be more commercially desirable, so "Brothers of Earth" was delayed until the former was released.

Women in speculative fiction: In 1948, 10–15% of science fiction writers were female.  Women's role in speculative fiction (including science fiction) has grown since then, and in 1999, women comprised 36% of the Science Fiction and Fantasy Writers of America's professional members. " Frankenstein" (1818) by Mary Shelley has been called the first science fiction novel, although women wrote utopian novels even before that, with Margaret Cavendish publishing the first ("The Blazing World") in the seventeenth century.  Early published fantasy was written by and for both genders.  However, speculative fiction, with science fiction in particular, has traditionally been viewed as a male-oriented genre.

Gate of Ivrel: Gate of Ivrel is a 1976 science fiction novel written by C. J. Cherryh and was her first published work.  It is the first of four books composing the Morgaine Stories, chronicling the deeds of Morgaine, a woman consumed by a mission of the utmost importance, and her chance-met companion, Nhi Vanye i Chya.

Keith Stevenson (writer): Keith Stevenson is an Australian speculative fiction writer, editor, reviewer, publisher and podcaster.  Born in Scotland, he emigrated to Australia in 1990.  From 1999 he was submissions manager for Aurealis Magazine – Australian Fantasy and Science Fiction and later became editor of the magazine from 2001 to the end of 2004.  During that time he was also organising convenor of the Aurealis Awards for several years and has since served as a judge on a number of occasions.  In 2005 he formed coeur de lion publishing with fellow Melbourne-based writer Andrew Macrae.  In 2007 he became science fiction and horror reviewer for Aurealis Magazine.  In 2008 he commenced the Terra Incognita Australian Speculative Fiction Podcast.  In 2014 he launched Dimension6 magazine and became a speculative fiction reviewer for the Newtown Review of Books.  His debut novel "Horizon" an SF thriller was published by Voyager Impulse (an imprint of HarperCollins Publishers).  He lives in Sydney with his partner.

Hugo Award for Best Related Work: The Hugo Awards are given every year by the World Science Fiction Society for the best science fiction or fantasy works and achievements of the previous year.  The award is named after Hugo Gernsback, the founder of the pioneering science fiction magazine "Amazing Stories", and was once officially known as the Science Fiction Achievement Award.  The award has been described as "a fine showcase for speculative fiction" and "the best known literary award for science fiction writing".  The Hugo Award for Best Related Work is given each year for primarily non-fiction works related to science fiction or fantasy, published in English or translated into English during the previous calendar year.  Awards are also given out for works of fiction in the novel, novella, novelette, and short story categories.

Man Plus: Man Plus is a 1976 science fiction novel by American writer Frederik Pohl.  It won the Nebula Award for Best Novel in 1976, was nominated for the Hugo and Campbell Awards, and placed third in the annual Locus Poll in 1977.  Pohl teamed up with Thomas T. Thomas to write a sequel, "Mars Plus", published in 1994.

All the Birds in the Sky: All the Birds in the Sky is a 2016 science fantasy novel by American writer and editor Charlie Jane Anders.  It is her debut speculative fiction novel and was first published in January 2016 in the United States by Tor Books.  The book is about a witch and a techno-geek, their troubled relationship, and their attempts to save the world from disaster.  The publisher described the work as "blending literary fantasy and science fiction".

Children of Dune: Children of Dune is a 1976 science fiction novel by Frank Herbert, the third in his "Dune" series of six novels.  Initially selling over 75,000 copies, it became the first hardcover best-seller ever in the science fiction field.  The novel was critically well-received for its gripping plot, action, and atmosphere, and was nominated for the Hugo Award for Best Novel in 1977.  It was originally serialized in "Analog Science Fiction and Fact" in 1976, and was the last "Dune" novel to be serialized before book publication.  The novels "Dune Messiah" and "Children of Dune" were published in one volume by the Science Fiction Book Club in 2002 and the two were adapted into a well-received television miniseries entitled "Frank Herbert's Children of Dune" by the Sci-Fi Channel in 2003.

World SF: World SF is a loose term for international, or global, speculative fiction, predominantly from the non-Anglophone world.  An early use of the term came with the establishment of "World SF", an association of SF professionals in 1976.  According to the third edition of the Encyclopedia of Science Fiction, the term was partly revived by the author Lavie Tidhar, leading to the establishment of the "World SF Blog", which ran 2009-2013.  Early on, the Filipino blogger Charles A. Tan became involved with the blog, contributing much of the original material - including interviews with authors, reviews and the occasional editorial, including the important "World SF: Our Possible Future" in 2012.  Tan was himself twice nominated for the World Fantasy Award, for his own blog, "Bibliophile Stalker", and has edited several anthologies of Filipino speculative fiction.

Question: Gate of Ivrel is a 1976 science fiction novel written by which American writer of speculative fiction, Carolyn Janice Cherry is better know as who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the book."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the book was published."
    },
    "author_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the author."
        },
        "pen_name": {
          "type": "string",
          "description": "The pen name the author is better known by."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the author."
        },
        "genre": {
          "type": "string",
          "description": "The primary genre of fiction the author writes."
        }
      },
      "required": [
        "full_name",
        "pen_name",
        "nationality",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "book_title",
    "publication_year",
    "author_details"
  ],
  "additionalProperties": false
}
