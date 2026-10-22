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
Just Give Me a Reason: "Just Give Me a Reason" is a song recorded by American singer and songwriter Pink, featuring fun. 's lead singer Nate Ruess.  The song was chosen as the third single from Pink's sixth studio album, "The Truth About Love" (2012).  Jeff Bhasker assisted the artists in writing the song and is also the producer.  "Just Give Me a Reason" is a pop ballad about the desire to hold on to a relationship even when it appears to be breaking down.  It starts off with a simple melody played on the piano, as Pink starts to sing the first verse and chorus, the latter of which introduces drum machines and bass.  Ruess then sings the second verse, and the rest of the song is sung as a duet.  The song ends with a piano solo, similar to the intro.  It has a duration of four minutes and two seconds.

Modern (album): Modern is the sixth studio album by English pop punk band Buzzcocks.  After the critical success of the band's previous album "All Set" (1996), the band became disillusioned with trying to be a rock band and set out to become more "modern," thus birthing the project.  Recording the album in Chipping Barnet with the band's bassist Tony Bassist producing, "Modern" sees a strong electronic music influence, with electronic instruments and drum machines featuring on the songs, especially those written by Steve Diggle, who wrote five of the album's songs whilst Pete Shelley wrote the other eight songs.

Go to Sleep: "Go to Sleep.  (Little Man being Erased.)" , commonly referred to as "Go to Sleep", is a song by the English rock band Radiohead, released as the second single from their sixth studio album "Hail to the Thief" (2003) on 18 August 2003.  The song reached #12 on the UK Singles Chart and reached #39 on the Australian ARIA Charts.

Hail to the Thief: Hail to the Thief is the sixth studio album by the English rock band Radiohead.  It was released on 9 June 2003, by Parlophone Records in the United Kingdom, and a day later by Capitol Records in the United States.  Following "Kid A" (2000) and "Amnesiac" (2001), which incorporated jazz, classical and electronic music influences, "Hail to the Thief" combines alternative rock instrumentation with drum machines, synthesisers, and digital manipulation.

Into the Groove: "Into the Groove" is a song by American singer Madonna from the 1985 film "Desperately Seeking Susan".  It was featured on the re-issue of her second studio album, "Like a Virgin" (1984), outside North America.  Sire Records released it on July 23, 1985, as the album's fourth single.  Madonna's inspiration behind the song was the dance floor, and she wrote it while watching a handsome Puerto Rican man, across her balcony.  Initially written for her friend Mark Kamins, Madonna later decided to use it as the soundtrack of her film "Desperately Seeking Susan".  "Into the Groove" consists of instrumentation from synthesizers and drum machines. Madonna's voice is double tracked in the chorus; the song also consists of musical contrasts, overdubs, and Madonna's voice in lower register during the bridge.  The lyrics of the song are simple, written as an invitation to dance with the singer.  However, it carries sexual innuendos and undertones in the meaning.

Beck discography: The discography of Beck, an American rock musician, singer-songwriter, record producer and multi-instrumentalist, consists of twelve studio albums, one compilation album, one remix album, three extended plays (EPs) and forty singles. With a pop art collage of musical styles, oblique and ironic lyrics, and postmodern arrangements incorporating samples, drum machines, live instrumentation and sound effects, Beck has been hailed by critics and the public throughout his musical career as being amongst the most creative and idiosyncratic musicians of 1990s and 2000s alternative rock.

Rux Revue: Rux Revue is the debut album by Carl Hancock Rux, released by Sony 550 Music which operated through Sony Music's Epic Records division.  The album was produced in Los Angeles by the Dust Brothers;Tom Rothrock and Rob Schnapf; featuring drummers Joey Waronker (formerly of R.E.M.) and James Gadson; bassists Atom Ellis (of Link Wray/The New Cars) and Carol Kaye; keyboardist James Hall, bass guitarist Wah-Wah Watson and additional keyboard, Keyboard, Piano and Melodica by Money Mark The album mixes soul, gospel, blues, rock, classical and hip-hop into a collage of machine samples, drum machines, live instrumentation and sound effects, incorporating a gospel influenced Sprechgesang and Vocalese style reliant upon African American alliteration, consonance and assonance while abstaining from the common techniques of poetic monologue popular in spoken word and slam poetry.

Kid A: Kid A is the fourth studio album by the English rock band Radiohead, released on 2 October 2000 by Parlophone.  On the verge of a breakdown after promoting Radiohead's 1997 album "OK Computer", songwriter Thom Yorke envisioned a radical change in direction.  Radiohead replaced their rock sound with synthesisers, drum machines, the ondes Martenot, string orchestras and brass instruments.  They incorporated influences from genres such as electronic music, krautrock, jazz, and 20th-century classical music.  They recorded "Kid A" with "OK Computer" producer Nigel Godrich in Paris, Copenhagen, Gloucestershire and their hometown Oxford, England.  The sessions produced over 20 tracks, and Radiohead split the work in two albums: "Kid A" and "Amnesiac".  The latter was released the following year.

Daft Punk: Bangalter and Homem-Christo were originally briefly in an indie rock band named Darlin'.  When the group disbanded, it left the two to experiment musically with drum machines and synthesisers.  The duo released their debut studio album "Homework" through Virgin Records in 1997 to highly positive reviews.  The duo's next album "Discovery" (2001) was even more successful, driven by the release of the hit singles "One More Time", "Digital Love" and "Harder, Better, Faster, Stronger".  In March 2005, the duo released their third album "Human After All" to mixed reviews.  However, the singles "Robot Rock" and "Technologic" achieved considerable success in the United Kingdom.

No-One Driving: "No-One Driving" is a 1980 song by UK artist John Foxx, and was released as a single in March 1980.  It was the second single release from the "Metamatic" album, after "Underpass".  The song is typical of Foxx's musical output of the time, featuring a Ballardian dystopian scenario involving an automobile in the lyrics, with music produced using electronic instruments (synthesisers, drum machines, electronic percussion) only.

Question: What was Radiohead's sixth studio album that was influenced by alternative rock instrumentation with drum machines, synthesisers, and digital manipulation and featured the single "Go to Sleep"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the artist or band who released the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'studio album'."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the album in the artist's discography."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "musical_elements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key musical instruments or styles incorporated into the album."
    },
    "featured_singles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the single."
          },
          "release_date": {
            "type": "string",
            "description": "The release date of the single."
          }
        },
        "required": [
          "title",
          "release_date"
        ],
        "additionalProperties": false
      },
      "description": "A list of singles featured on the album."
    }
  },
  "required": [
    "album_name",
    "artist_name",
    "album_type",
    "album_number",
    "release_year",
    "musical_elements",
    "featured_singles"
  ],
  "additionalProperties": false
}
