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
Showboat (Kenny Dorham album): Showboat is an album by American jazz trumpeter Kenny Dorham featuring performances of tunes from the Jerome Kern-Oscar Hammerstein II musical "Show Boat" recorded in 1960 and released on the Time label.

This Is the Moment!: This Is the Moment!  (subtitled "Kenny Dorham Sings and Plays") is an album by American jazz trumpeter Kenny Dorham featuring performances recorded in 1958 and released on the Riverside label.  The album marks the recording debut of pianist Cedar Walton.

List of songs composed by Jerome Kern: This is an alphabetical list of Jerome Kern songs.  Jerome Kern (January 27, 1885 – November 11, 1945) was an American composer of popular music and, according to a joint resolution passed by Congress, "the father of American musical theater".  He wrote around 700 songs, including such classics as "Ol' Man River", "Can't Help Lovin' Dat Man", "A Fine Romance", "Smoke Gets in Your Eyes", "All the Things You Are", "The Way You Look Tonight", and "Who? ".  His career spanned dozens of Broadway musicals and Hollywood films from 1902 until his death.

Quiet Kenny: Quiet Kenny is an album by the American jazz trumpeter Kenny Dorham of performances recorded in 1959 and released on the New Jazz label.

Show Boat: Show Boat is a musical in two acts, with music by Jerome Kern and book and lyrics by Oscar Hammerstein II, based on Edna Ferber's best-selling novel of the same name.  The musical follows the lives of the performers, stagehands and dock workers on the "Cotton Blossom", a Mississippi River show boat, over 40 years from 1887 to 1927.  Its themes include racial prejudice and tragic, enduring love.  The musical contributed such classic songs as "Ol' Man River", "Make Believe", and "Can't Help Lovin' Dat Man".

Trompeta Toccata: Trompeta Toccata is a 1964 jazz album by trumpeter Kenny Dorham.  It was released on Blue Note label in 1965 as BST 84181.  It was remastered by Rudy Van Gelder in 2006.  "Trompeta Toccata", as the previous "Una Mas", features only four pieces, three of which were written by Dorham himself.  They are mostly fast bop pieces featuring long trumpet and saxophones solos.  Like many Dorham compositions, they incorporate elements of Latin music and blues.  "Trompeta Toccata" is recognized by some critics as one of Dorham's most enduring works, recorded in his most prolific and inspired period.  Although many expected an even greater followup, "Trompeta Toccata" would be his last appearance as a leader; Bob Blumenthal wrote in his 2006 liner notes for the album that "the remainder of Dorhams' recorded career was confined to sideman appearances that can be counted on the fingers of one hand".

Jerome Kern: Jerome David Kern (January 27, 1885 – November 11, 1945) was an American composer of musical theatre and popular music.  One of the most important American theatre composers of the early 20th century, he wrote more than 700 songs, used in over 100 stage works, including such classics as "Ol' Man River", "Can't Help Lovin' Dat Man", "A Fine Romance", "Smoke Gets in Your Eyes", "All the Things You Are", "The Way You Look Tonight", "Long Ago (and Far Away)" and "Who? ".  He collaborated with many of the leading librettists and lyricists of his era, including George Grossmith Jr., Guy Bolton, P. G. Wodehouse, Otto Harbach, Oscar Hammerstein II, Dorothy Fields, Johnny Mercer, Ira Gershwin and E. Y. Harburg.

Una Mas: Una Mas, on the front cover titled "Una Mas (One More Time)", is a jazz album by trumpeter Kenny Dorham and his quintet, released in 1963 on Blue Note as BLP 4127 and BST 84127.  The album would be the next-to-last studio session led by the trumpeter, since after 1964, he began to fade and disappear from the jazz scenes.  "Una Mas" features three compositions by Dorham himself and the jazz ballad "If Ever I Would Leave You", originally composed by Loewe/Lerner for the musical "Camelot".

Kenny Dorham Quintet (album): Kenny Dorham Quintet is a jazz studio album by trumpeter Kenny Dorham.  It was his debut album as a leader and was released in 1953, on the Debut label as DLP-9 and originally included only tracks 1 to 3 and 5 to 7.  Tracks 4 and 8 were released as bonus tracks on 12-inch LP OJC-113, whilst the CD release featured the previously unreleased tracks 9, 10 and 11.  According to the liner notes on the CD back cover "Label head Charles Mingus decided not to release them at the time and they languished in the tape vault for almost 40 years, until their fortuitous discovery in late 1992".

Jazz Contemporary: Jazz Contemporary is an album by American jazz trumpeter Kenny Dorham featuring performances recorded in 1960 and released on the Time label.  The album features the recording debut of pianist Steve Kuhn.

Question: Which album by American jazz trumpeter Kenny Dorham, features songs from the musical that includes "Ol' Man River", "Make Believe", and "Can't Help Lovin' Dat Man"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the Kenny Dorham album."
    },
    "artist": {
      "type": "string",
      "description": "The artist of the album."
    },
    "musical_source": {
      "type": "string",
      "description": "The name of the musical from which the album features songs."
    },
    "musical_composer": {
      "type": "string",
      "description": "The composer of the musical."
    },
    "featured_songs": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of classic songs from the musical mentioned in the context."
    }
  },
  "required": [
    "album_title",
    "artist",
    "musical_source",
    "musical_composer",
    "featured_songs"
  ],
  "additionalProperties": false
}
