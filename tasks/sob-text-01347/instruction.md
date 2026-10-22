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
Ben Folds Five (album): Ben Folds Five is the self-titled debut studio album by American alternative rock band Ben Folds Five, released in 1995.  A non-traditional rock album, it featured an innovative indie-pop sound, and excluded lead guitars completely.  The album was released on the small independent label Passenger Records, owned by Caroline Records, a subsidiary of Virgin/EMI.  "Ben Folds Five" received positive reviews, and spawned five singles.  The record failed to chart, but sparked an intense bidding war eventually won by Sony Music.  Several live versions of songs originally released on "Ben Folds Five" reappeared later as b-sides or on compilations.

Nick Carter, Master Detective: Nick Carter, Master Detective was a Mutual radio crime drama based on tales of the fictional private detective Nick Carter from Street & Smith's dime novels and pulp magazines.  Nick Carter first came to radio as The Return of Nick Carter, a reference to the character's pulp origins, but the title was soon changed to Nick Carter, Master Detective.  A veteran radio dramatist, Ferrin Fraser, wrote many of the scripts.

Where's Summer B.?: "Where's Summer B.?"  is a song from Ben Folds Five's 1995 first album, "Ben Folds Five".  It was written by Ben Folds and Darren Jessee.  The song, though up-tempo, deals with the disappointment of returning to a hometown after being away and seeing things much the same as before.

Boxing (song): "Boxing" is a song from Ben Folds Five's 1995 self-titled debut album.  It was written by Ben Folds.  A live version appears on the 1998 album "Naked Baby Photos".  The song also appears in a solo version by Folds on the 2005 download-only album "iTunes Originals - Ben Folds" and in a symphonic version with the West Australian Symphony Orchestra on the 2005 DVD "Ben Folds and WASO Live in Perth", and in an a cappella version on "".

Ben Folds: Benjamin Scott Folds (born September 12, 1966) is an American singer-songwriter and record producer.  From 1995 to 2000, Folds was the frontman and pianist of the alternative rock band Ben Folds Five.  After the group temporarily disbanded, Folds performed as a solo artist and has toured all over the world.  The group reunited in 2011.  He has also collaborated with musicians such as William Shatner, Regina Spektor and "Weird Al" Yankovic and undertaken experimental songwriting projects with authors such as Nick Hornby and Neil Gaiman.  In addition to contributing music to the soundtracks of the animated films "Over the Hedge," and "Hoodwinked! ", Folds produced Amanda Palmer's first solo album and was a judge on the NBC a cappella singing contest "The Sing-Off" from 2009 to 2013.

Shut Up and Listen to Majosha: Shut Up and Listen to Majosha is Majosha's first and only album.  This album never made it to CD, and was only ever available on vinyl and cassette.  All songs were written by Ben Folds and Millard Powers except "Emaline", written by both Ben Folds and Evan Olson.  Songs "Emaline" and "Video" later appeared on Ben Folds Five albums, and "Kalamazoo" was released on the Folds solo EP "Super D".

Ben Folds and WASO Live in Perth: Ben Folds and WASO Live in Perth is a DVD featuring performances by singer-songwriter and pianist Ben Folds, backed by the West Australian Symphony Orchestra.  Filmed over two nights on March 12 & 13, 2005 at Kings Park and Botanical Gardens in Perth, Australia - a venue Folds jokingly refers to as a "luminous green petri dish" - the DVD offers 14 songs from the three major Ben Folds Five albums and Folds' debut solo album "Rockin' the Suburbs".

Brick (song): "Brick" is a song by American alternative rock group Ben Folds Five.  It was released in November 1997 as a single from their album "Whatever and Ever Amen" and later on "Ben Folds Live".  The verses were written by Ben Folds about his high school girlfriend undergoing an abortion, and the chorus was written by the band's drummer, Darren Jessee.  "Brick" was one of Ben Folds Five's biggest hits, gaining much mainstream radio play in the USA, the UK, and Australia in 1998.

Nick Carter (musician): Nickolas Gene "Nick" Carter (born January 28, 1980) is an American singer, songwriter, actor, and dancer.  He is best known as a member of the pop group the Backstreet Boys.  As of 2015, Carter has released three solo albums, "Now or Never", "I'm Taking Off" and "All American" during breaks between Backstreet Boys schedules, and a collaboration with Jordan Knight titled "Nick & Knight".  He has made occasional television appearances and starred in his own reality shows, "House of Carters" and "I (Heart) Nick Carter".  He gained fame in the mid 1990s and early 2000s as a teen idol.  He is also the older brother of singer Aaron Carter and the late Leslie Carter.

Speed Graphic (EP): Speed Graphic is the first of a three-EP series released by Ben Folds.  It included a cover of "In Between Days" (originally by The Cure, from their 1985 album "The Head on the Door").  It also included a piano and vocal arrangement of "Give Judy My Notice", which would later appear on "Songs for Silverman" in a rearranged full-band version.  The final three tracks were written a long time before this release.  Two of those songs, "Protection" (co-written by Ben's former wife, Anna Goodman) and "Dog" have floated around as bootlegged early demos for years, and the other one, "Wandering", was never available in any format previously, and was written by Ben Folds and his fellow Ben Folds Five bandmate, Darren Jessee.

Question: Are Nick Carter and Ben Folds from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the first person."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "person_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the second person."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "are_from_same_country": {
      "type": "boolean",
      "description": "True if both persons are from the same country, false otherwise."
    }
  },
  "required": [
    "person_one",
    "person_two",
    "are_from_same_country"
  ],
  "additionalProperties": false
}
