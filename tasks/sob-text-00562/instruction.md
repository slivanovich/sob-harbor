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
Dark Side of the Moon Tour: The Dark Side of the Moon Tour was a concert tour by British rock band Pink Floyd in 1972 and 1973 in support of their album "The Dark Side of the Moon".  There were two separate legs promoting "Dark Side of the Moon", one in 1972 before the album's release and another in 1973 after its release.

The Dark Side (DarkSun album): The Dark Side is the third studio album by power metal band DarkSun, which is the English version of "El Lado Oscuro", the album was released in September 2007.  "The Dark Side" and was released in September 2007 through FC Metal Recordings.  The critics were as good as the Spanish version, like "the album can be defined with one word: brilliant!" .  The band collaborated on Rage's album "Speak of the Dead", with a Spanish version of the song "Full Moon" entitled "La Luna Reine," which appeared as a bonus track.  Just after the release of "The Dark Side" drummer Rafael Yugueros left DarkSun to form part of power metal band WarCry replacing former drummer Alberto Ardines.  Yugueros had already worked with WarCry on their 1997's demo "Demon 97".  The band re-recruited Daniel Cabal who worked on what would become the band's new album "Libera Me".  On the summer of 2008 DarkSun announced that Cabalwas leaving the band, all these occurred in a professional and friendly way from both parties.  On the same announcement the band presented new drummer Jose Ojeda, who had performed drums on Spanish bands like Rivendel Lords, Killian, among others.

Back Against the Wall: Back Against the Wall is an album released in 2005 by Billy Sherwood in collaboration with a number of (mostly) progressive rock artists as a tribute to Pink Floyd's album "The Wall".  A sequel, also organised by Sherwood, was released the next year: "Return to the Dark Side of the Moon" was a tribute to Pink Floyd's "The Dark Side of the Moon".

Dark Side of the Rainbow: Dark Side of the Rainbow – also known as Dark Side of Oz or The Wizard of Floyd – refers to the pairing of the 1973 Pink Floyd album "The Dark Side of the Moon" with the visual portion of the 1939 film "The Wizard of Oz."

Far side of the Moon: The far side of the Moon is the hemisphere of the Moon that always faces away from Earth.  The far side's terrain is rugged, with a multitude of impact craters and relatively few flat lunar maria.  It has one of the largest craters in the Solar System, the South Pole–Aitken basin.  Although both sides of the moon experience two weeks of sunlight followed by two weeks of night, the far side is sometimes called the "dark side of the Moon," with "dark" meaning "unknown" rather than lack of light.

Donald Rumsfeld: Donald Henry "Don" Rumsfeld (born July 9, 1932) is an American retired politician and businessman.  Rumsfeld served as the 13th Secretary of Defense from 1975 to 1977 under President Gerald Ford, and as the 21st Secretary of Defense from 2001 to 2006 under President George W. Bush.  He is both the youngest and the second oldest person to have served as Secretary of Defense.  Additionally, Rumsfeld was a three-term U.S. Congressman from Illinois (1963–1969), Director of the Office of Economic Opportunity (1969–1970), Counsellor to the President (1969–1973), the United States Permanent Representative to NATO (1973–1974), and White House Chief of Staff (1974–1975).

Dark Side of the Moon (film): Dark Side of the Moon is a French mockumentary by director William Karel which originally aired on Arte in 2002 with the title Opération Lune.  The basic premise for the film is the theory that the television footage from the Apollo 11 Moon landing was faked and recorded in a studio by the CIA with help from director Stanley Kubrick.  It features some surprising guest appearances, most notably by Donald Rumsfeld, Dr. Henry Kissinger, Alexander Haig, Vernon Walters, Buzz Aldrin and Stanley Kubrick's widow, Christiane Kubrick.

From the Dark Side of the Moon: From the Dark Side of the Moon is a 2011 album released by singer/songwriter Mary Fahl.  The album is a song-by-song "re-imagining" of Pink Floyd's classic 1973 album "The Dark Side of the Moon".

Wish You Were Here (Pink Floyd album): Wish You Were Here is the ninth studio album by English rock band Pink Floyd.  It was released on 12 September 1975 by Harvest Records in the United Kingdom and a day later by Columbia Records in the United States.  Inspired by material the group composed while performing around Europe, "Wish You Were Here" was recorded during numerous recording sessions at Abbey Road Studios in London, England.  Two of the album's four songs criticise the music business, another expresses alienation and the multi-part track "Shine On You Crazy Diamond" is a tribute to Syd Barrett.  Barrett's mental breakdown had forced him to leave the group seven years earlier, prior to the release of the group's second studio album "A Saucerful of Secrets" (on which he only appeared on three tracks).  It was lead writer Roger Waters' idea to split "Shine On You Crazy Diamond" into two parts that would bookend the album around three new compositions and to introduce a concept linking them all.  The band had used a linking concept for their previous album, "The Dark Side of the Moon", to great success.  As with "The Dark Side of the Moon", the band used studio effects and synthesizers and brought in guest singers to supply vocals on some tracks of the album.  These singers were Roy Harper, who provided the lead vocals on "Have a Cigar", and the Blackberries, who added backing vocals to "Shine On You Crazy Diamond".

Lunar phase: The lunar phase or phase of the moon is the shape of the illuminated (sunlit) portion of the Moon as seen by an observer on Earth.  The lunar phases change cyclically as the Moon orbits the Earth, according to the changing positions of the Moon and Sun relative to the Earth.  The Moon's rotation is tidally locked by the Earth's gravity, therefore the same lunar surface always faces Earth.  This face is variously sunlit depending on the position of the Moon in its orbit.  Therefore, the portion of this hemisphere that is visible to an observer on Earth can vary from about 100% (full moon) to 0% (new moon).  The lunar terminator is the boundary between the illuminated and darkened hemispheres.  Each of the four "intermediate" lunar phases (see below) is roughly seven days (~7.4 days) but this varies slightly due to the elliptical shape of the Moon's orbit.  Aside from some craters near the lunar poles such as Shoemaker, all parts of the Moon see around 14.77 days of sunlight, followed by 14.77 days of "night".  (The side of the Moon facing away from the Earth is sometimes called the "dark side of the Moon", although that is a misnomer.)

Question: Dark Side of the Moon is a French mockumentary featuring a guest appearance by  an American retired politician and businessman who served as the 21st Secretary of Defense under who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the mockumentary film."
    },
    "film_director": {
      "type": "string",
      "description": "The director of the mockumentary film."
    },
    "guest_appearance_details": {
      "type": "object",
      "properties": {
        "guest_name": {
          "type": "string",
          "description": "The name of the guest who appeared in the film."
        },
        "guest_profession": {
          "type": "string",
          "description": "The profession of the guest."
        },
        "secretary_of_defense_term": {
          "type": "object",
          "properties": {
            "term_number": {
              "type": "string",
              "description": "The specific term number as Secretary of Defense (e.g., '21st')."
            },
            "president_served_under": {
              "type": "string",
              "description": "The name of the President under whom the guest served as Secretary of Defense for the specified term."
            }
          },
          "required": [
            "term_number",
            "president_served_under"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "guest_name",
        "guest_profession",
        "secretary_of_defense_term"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_director",
    "guest_appearance_details"
  ],
  "additionalProperties": false
}
