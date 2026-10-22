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
Alexandra Sokoloff: Alexandra Sokoloff is an American novelist and screenwriter, and the author of the Thriller award-nominated Huntress/FBI series, following a haunted FBI agent on the hunt for a female serial killer ("Huntress Moon", "Blood Moon", "Cold Moon", published by Thomas & Mercer in 2015).  Her first novel, "The Harrowing", was published by St. Martin's Press in 2006.  Her second novel, "The Price," was published by St. Martin's in 2007, her third, "The Unseen", in 2009, her fourth, "Book of Shadows", in 2010.  She is a Bram Stoker and Anthony award nominee and a Thriller award winner, and the co-author of the paranormal mystery romance series "The Keepers".

Andre Norton Award: The Andre Norton Award for Young Adult Science Fiction and Fantasy is an annual award presented by the Science Fiction and Fantasy Writers of America (SFWA) to the author of the best young adult or middle grade science fiction or fantasy book published in the United States in the preceding year.  It is named to honor prolific science fiction and fantasy author Andre Norton (1912–2005), and it was established by then SFWA president Catherine Asaro and the SFWA Young Adult Fiction committee and announced on February 20, 2005.  Any published young adult or middle grade science fiction or fantasy novel is eligible for the prize, including graphic novels.  There is no limit on word count.  The award is presented along with the Nebula Awards and follows the same rules for nominations and voting; as the awards are separate, works may be simultaneously nominated for both the Andre Norton award and a Nebula Award.

The Vampire Huntress Legend Series: The Vampire Huntress Legend Series (VHL) is a twelve book series written by Leslie Esdaile Banks under the pen name L.A. Banks.  The series centers around a young "twenty-something" woman named Damali Richards who is a spoken word artist but is also the Neteru, a human who is born once every thousand years to fight the Dark Realms.  Her most dangerous and most constant enemy from The Dark Realms are vampires.

Christopher Stasheff: Christopher Stasheff (born 1944) is an American science fiction author and fantasy author whose novels include "The Warlock in Spite of Himself" (1969) and "Her Majesty's Wizard" (1986).  He has a PhD.  in Theatre and taught radio and television at Eastern New Mexico University in Portales, New Mexico; he is now retired and living in Champaign, Illinois.  Stasheff has been noted for his blending of science fiction and fantasy, as seen in his "Warlock" series, which placed an "'epic fantasy' in a science fictional frame".  Stasheff's writing is often seen in the moral and ethical mentor style similar to Terry Goodkind, Terry Brooks or J.R.R. Tolkien.

Fantasy author: The definition of a fantasy author is somewhat diffuse, and a matter of opinion – Jules Verne considered H. G. Wells to be a fantasy author – and there is considerable overlap with science fiction authors and horror fiction authors.  However some notable part of the output of the fantasy writers leans more to the fantasy end of the spectrum.

Elizabeth Haydon: Elizabeth Haydon (born 1965) is an American fantasy author.  She has written two fantasy series set within the same universe, the fantasy/romance/whodunit fusion called The Symphony of Ages and the young adult series The Lost Journals of Ven Polypheme.  Her WebSite is located at ElizabethHaydon.net.

Night Huntress: Night Huntress is a series of "New York Times" bestselling urban fantasy romance novels by author Jeaniene Frost.  The first novel was published in 2007 by Avon and takes place in a world where supernatural creatures exist but are not known to the general public at large.  The series initially focused around the character of half-vampire Catherine "Cat" Crawfield and her full-vampire lover Bones, but eventually shifted focus to other characters such as Vlad Tepesh, a character that Frost had initially not planned to include.

Monarchies of God: The Monarchies of God is an epic fantasy series written by Irish author Paul Kearney.  This series was published between 1995 and 2002 in five volumes.  The series is noteworthy for its ruthlessness in dispatching major characters, its large number of epic battles and its use of gunpowder and cannons.  Kearney also has an extensive knowledge of sailing and uses this to inform his description of naval travel and combat.  The series garnered critical praise and numbers fantasy author Steven Erikson among its fans as he mentions in an interview with Neil Walsh, May 2000.  The series has also been criticised for its pessimism.

The Fortress Series: Fortress is a series of fantasy novels by science fiction and fantasy author C. J. Cherryh, published by HarperCollins.  They are set in a medieval fantasy world with a 15th-century feel and feature magic, sorcery, medieval warfare, politics and other elements common to the high fantasy subgenre.  The first book in the series, "Fortress in the Eye of Time", was published in 1995 and followed by "Fortress of Eagles" in 1998, "Fortress of Owls" in 1999, "Fortress of Dragons" in 2000 and "Fortress of Ice" in 2006.

Jeaniene Frost: Jeaniene Frost is an American fantasy author, known for her work on the "New York Times" and "USA Today" bestselling "Night Huntress" series and the "Night Huntress World" novels.  Foreign rights for her novels have sold to nineteen different countries.

Question: Night Huntress was a series written by the fantasy author of what nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_information": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the book series."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the series."
        }
      },
      "required": [
        "series_name",
        "genre"
      ],
      "additionalProperties": false
    },
    "author_information": {
      "type": "object",
      "properties": {
        "author_name": {
          "type": "string",
          "description": "The name of the author."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the author."
        },
        "other_notable_works": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other notable series or works by the author mentioned in the context."
        }
      },
      "required": [
        "author_name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The nationality of the author of the specified series."
    }
  },
  "required": [
    "series_information",
    "author_information",
    "answer"
  ],
  "additionalProperties": false
}
