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
Today I Started Loving You Again: "Today I Started Loving You Again" is a song written by Merle Haggard and Bonnie Owens.  Haggard first recorded it as a B-side to his number 1 hit "The Legend of Bonnie and Clyde", but it failed to chart.  The song was later recorded by Al Martino, followed by many other artists, including Martina McBride, Charlie McCoy, David Peters, Kenny Rogers and the First Edition, Bettye Swann, Connie Smith, Sammi Smith, Bobby Bland, Emmylou Harris and Dolly Parton.  More recently it was recorded by Jeff Carson and Merle Haggard for Carson's 1997 Album Butterfly Kisses.

Barton Hollow (song): "Barton Hollow" is a country and indie folk song co-written and recorded by The Civil Wars.  It was released on January 10, 2011 as the second single and title-track to their debut album "Barton Hollow".  The single did not enter the U.S. Hot 100 but charted on the top spot of the Bubbling Under Hot 100 Singles.  The single's vinyl release had "You Are My Sunshine" as its B-side.

Appropriation (By Any Other Name): "Appropriation (By Any Other Name)" was a 7" and CD release by Sheffield band The Long Blondes.  It was released on June 13, 2005 on Angular Records.  The song is a homage to Hitchcock's 1958 film Vertigo.  it has been said that this song is told from the point of view of Judy, due to lines such as "When I met you, I never wore dresses like that" and "You can't have me, make me act the same".  Lead singer Kate Jackson painted two different portraits for the CD single and 7" Vinyl.  They both depicted Kim Novak's characters Madeleine Elster and Judy Barton.  The song was not featured on their debut album Someone to Drive You Home, but the b-side, "Lust In The Movies" was.  Both were featured on the compilation album "Singles".  The song was well received by critics.

Indian Giver (song): "Indian Giver" is a song written by Bobby Bloom, Ritchie Cordell, and Bo Gentry.  It was first recorded by 1910 Fruitgum Company for their 1969 album, "Indian Giver".  The song went to #5 on The Billboard Hot 100 in 1969 and was on the charts for 13 weeks.  Its B-Side, "Pow Wow", was actually a song called "Bring Back Howdy Doody" deliberately pressed backwards as a way of deterring radio stations from playing the B-Side, which was later recorded by another Buddah bubblegum music group produced by Jerry Kasenetz and Jeffrey Katz called Flying Giraffe.

Are You Gonna Kiss Me or Not: "Are You Gonna Kiss Me or Not" is a song written by Jim Collins and David Lee Murphy, and recorded by American country music duo Thompson Square.  It was released in July 2010 as the second single from their self-titled debut album, which was released on February 8, 2011.  The song has been certified 2× Platinum by the RIAA.  On November 30, the band received two nominations in 54th Grammy Awards for the song in Best Country Duo/Group Performance and Best Country Song but lost to "Barton Hollow" by The Civil Wars and "Mean" by Taylor Swift, respectively.

You've Got the Power (James Brown song): "You've Got the Power" is a song written by James Brown and Famous Flames member Johnny Terry and recorded by Brown with Bea Ford as a duet in 1960.  Released as the B-side of Brown and the Famous Flames' hit recording of "Think", it also charted, reaching #14 R&B and #86 Pop.  It was Brown's first recorded duet and his first hit B-side.  Brown briefly performs the song in a medley on his 1963 album "Live at the Apollo".

You Are My Sunshine: "You Are My Sunshine" is a popular song recorded by Jimmie Davis and Charles Mitchell and first recorded in 1939.  It has been declared one of the state songs of Louisiana because of its association with Davis, a country music singer and governor of the state in the years 1944–1948 and 1960–1964.

The Prize Fighter Inferno: The Prize Fighter Inferno is an acoustic/electronica solo project of Claudio Sanchez, the lead singer and lead/rhythm guitarist for the band Coheed and Cambria.  The first album, called "My Brother's Blood Machine" was released on October 31, 2006 through indie label Equal Vision Records.  According to "My Brother's Blood Machine" liner notes, Claudio recorded the album over a period of seven years with "...random recording devices...".  As of August 2009, Sanchez has been reportedly working on a follow up album to 2006's "My Brother's Blood Machine" releasing updates of the album's status on his Twitter account every few months.  On September 25, 2009, A new song called "Gears" was introduced in the trailer of Claudio's comic series Kill Audio.  The song was released on 7" vinyl along with another song called "Erizo Schultz" in February 2010.  The vinyl credits both Claudio Sanchez and his wife Chondra Echert as "The Prize Fighter Inferno".  An EP was release for New York Comic Con 2012 titled "Half Measures" with tracks, Elm Street Lover Boy, Simple Fix, Pistol Pete Matty, and Half Measures.  On Record Store Day, the EP is set to release as a Glow in the Dark vinyl, along with Big Beige Demos in a coke-bottle clear vinyl, and Davenport Cabinet's EP in a blue vinyl.

Blue Collar Man (Long Nights): "Blue Collar Man (Long Nights)" is the first single that Styx released from the "Pieces of Eight" (1978) album.  Released in 1978, the single came in two 7" vinyl formats: one with the b-side "Superstars" (a track from "The Grand Illusion") and a second single with the instrumental album track "Aku-Aku" as the b-side.  Some printings of the single were also issued in a translucent blue vinyl, which are now highly sought after collectors items.  As read in a "Circus" magazine (or the like) of the time, the song was composed by Tommy Shaw after hearing the sound of his motor boat engine when it failed to start.  He said it sounded like a good riff to a song.  The song reached No. 21 in the United States, and spent two weeks at No. 9 on the Canada RPM Top 100 Singles chart.

Barton Hollow: Barton Hollow is the first full-length studio album from The Civil Wars.  Produced by Charlie Peacock, it was released on February 1, 2011.  It peaked at No. 1 on the "Billboard" Digital Albums chart, No. 10 on the "Billboard" 200, No. 1 on the "Billboard" Folk Albums chart, and No. 2 on the "Billboard" Rock Albums chart, selling 25,000 copies in its first week.  s of August 2013 , the album has sold 623,000 copies in the US.

Question: Barton Hollow was recorded on vinyl with which song, first recorded in 1939, as its B-side?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "main_song_title": {
      "type": "string",
      "description": "The title of the main song."
    },
    "release_medium": {
      "type": "string",
      "description": "The physical medium on which the song was released with its B-side."
    },
    "b_side_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the B-side song."
        },
        "first_recorded_year": {
          "type": "integer",
          "description": "The year the B-side song was first recorded."
        }
      },
      "required": [
        "title",
        "first_recorded_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "main_song_title",
    "release_medium",
    "b_side_details"
  ],
  "additionalProperties": false
}
