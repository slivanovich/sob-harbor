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
Ajita Wilson: Ajita Wilson (January 12, 1950 – May 26, 1987) was an American actress who starred in European exploitation and hardcore films in the 1970s and 1980s.  Born in Brooklyn, Wilson was according to most accounts, transsexual, born male name George Wilson.  Wilson died from a brain hemorrhage on May 26, 1987, at age 37.

Gamecock Media Group: Gamecock Media Group was an American video game publisher based in Austin, Texas.  It was founded in February 2007 by video game industry veterans Mike Wilson, Harry A. Miller IV, and Rick Stults, original founders of Gathering of Developers.  They used a more hands-off approach and allowed developers creative freedom with their work, as well as letting them keep their own intellectual property.  On October 14, 2008, SouthPeak Games acquired Gamecock Media Group, and dissolved them shortly after.

George Wilson Homestead: George Wilson Homestead is a historic home located at Halfmoon Township, Centre County, Pennsylvania.  It was built in 1810, and is a 2 1/2-story, five bay, limestone and sandstone dwelling with a medium pitch gable roof.  The house measures 40 feet by 25 feet, and is in the Georgian style.  A 1 1/2-story, 16 feet square addition was built about 1870.  Also on the property are a number of contributing outbuildings including the barn (c. 1820), carriage shed, storage garage (1930s), saltbox shed, gable shed, two corn cribs, and an ice house.  George Wilson was the pioneer Quaker settler in the Halfmoon Valley.

Dennis the Menace (1959 TV series): Dennis the Menace is an American sitcom based on the Hank Ketcham comic strip of the same name and preceded "The Ed Sullivan Show" on Sunday evenings on CBS from October 1959 to July 1963.  The series stars Jay North as Dennis Mitchell; Herbert Anderson as his father, Henry; Gloria Henry as his mother, Alice; Joseph Kearns as George Wilson, Gale Gordon as George's brother, John Wilson, Sylvia Field as George's wife, Martha Wilson, and Sara Seegar as John's wife, Eloise Wilson.

George Wilson (quarterback): George William Wilson, Jr. (May 29, 1943 – August 6, 2011) was an American football player.  He played college football at Xavier University and professionally for the American Football League's (AFL) 1966 expansion team, the Miami Dolphins.  In 1965, Wilson was selected in the 20th round of the National Football League draft by the Detroit Lions, with the overall 277th pick.  However, he eventually signed with the AFL's Buffalo Bills, who drafted him as the 96th pick in the 12th round of the Red Shirt draft.  In 1966, Wilson was traded to the Miami Dolphins in exchange for a 13th round 1967 draft pick.  At the time, the Dolphins' head coach was his father, George Wilson, Sr.

Cocky (mascot): Cocky is the costumed mascot of the University of South Carolina athletics teams.  He represents a cartoon version of a gamecock (a fighting rooster).

Cockfight: A cockfight is a blood sport between two cocks, or gamecocks, held in a ring called a cockpit.  The history of raising fowl for fighting goes back 6,000 years.  The first documented use of the "word" gamecock, denoting use of the cock as to a "game", a sport, pastime or entertainment, was recorded in 1634, after the term "cock of the game" used by George Wilson, in the earliest known book on the sport of cockfighting in "The Commendation of Cocks and Cock Fighting" in 1607.  But it was during Magellan's voyage of discovery of the Philippines in 1521 when modern cockfighting was first witnessed and documented by Antonio Pigafetta, Magellan's chronicler, in the kingdom of Taytay.

Fanthomas: Fanthomas is a Norwegian 2D cartoon comedy series, written by the Norwegian comedian Anders Bye.  It centers around a cartoon version of the Norwegian Hollywood makeup artist Jan Thomas Mørch Husby, and his boyfriend Christoffer.  The two have secret identities, as crime-fighting superstars.  In each episode, the pair fight a Norwegian celebrity, such as Anne Kat Hæland, Alexander Rybak, Eyvind Hellstrøm, Mira Craig and Petter Stordalen.  Plots include Fanthomas being fed up with Alexander Rybak's song "Fairytale" and going as far as Siberia to get away from it; fighting Norwegian actor Aksel Hennie; and trying to save Barack Obama's ears from a very clumsy hair stylist right before the handing out of the Nobel Peace Prize.

United States v. Wilson: United States v. Wilson, 32 U.S. 150 (1833), was a case in the United States in which the defendant, George Wilson, was convicted of robbing the US Mail in Pennsylvania and sentenced to death.  Due to his friends' influence, Wilson was pardoned by Andrew Jackson.  Wilson, however, refused the pardon.  The Supreme Court was thus asked to rule on the case.

Lifestyles of the Ramones: Lifestyles of the Ramones is a VHS video made by the Ramones featuring interviews and music videos.  Later, it was released again on DVD includes extras such as "Photo Gallery" & "Discography" - with Portuguese Brazilian subtitle, plus English lyrics for each song, and in 2005, it was re-released and included as a bonus disc of the 4 Disc Box-Set "Weird Tales Of The Ramones", and plus some music videos from 1992 to 1996, especially the unseen video 'Blitzkrieg Bop (Fast Live Version 1991)', 'Substitute' (1993 MTV Banned Version) and 'Spiderman' (1992 Cartoon Version).

Question: Cocky represents a cartoon version of a gamecock after what term was used by George Wilson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mascot_name": {
      "type": "string",
      "description": "The name of the mascot."
    },
    "mascot_representation": {
      "type": "string",
      "description": "What the mascot represents."
    },
    "george_wilson_term": {
      "type": "string",
      "description": "The term used by George Wilson related to gamecocks."
    },
    "book_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the book where George Wilson's term appeared."
        },
        "publication_year": {
          "type": "integer",
          "description": "The publication year of the book."
        }
      },
      "required": [
        "title",
        "publication_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mascot_name",
    "mascot_representation",
    "george_wilson_term",
    "book_details"
  ],
  "additionalProperties": false
}
