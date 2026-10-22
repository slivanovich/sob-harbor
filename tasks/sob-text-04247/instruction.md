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
Bacon Popper: Bacon Popper was an electronic music duo best known for their 1998 dance single "Free," which was memorable in part for its lyrical refrain "you're just a bunch of freaks," and for its sample of U2's song "New Year's Day."

The Walls: The Walls are an Irish rock band.  They were formed in 1998 by two ex-members of The Stunning – brothers Steve and Joe Wall.  Their debut album "Hi-Lo" was released in 2000 and included the singles "Bone Deep", "Something's Wrong" and "Some kind of a Girl".  U2 invited The Walls to support them at their second show in Slane Castle in 2002 after the band sent them copies of their debut.  A number of songs from "Hi-Lo" featured in movies: Goldfish Memory, On the Edge, and Dead Bodies.  In 2002 they released the single "To the Bright and Shining Sun".  It was used on an Irish TV commercial and became a hit in Ireland.  The subsequent album "New Dawn Breaking" (2005) included "To the Bright and Shining Sun" and three other singles: "Drowning Pool", "Passing Through" and "Black and Blue".  The 2013 movie Begin Again starring Keira Knightley and Mark Ruffalo features "Drowning Pool" over the opening credits.  The first track on the album "Open Road" proved a favourite with Nic Harcourt on his KCRW show "Morning Becomes Eclectic" and he invited the band to play a session on the show in 2006.  They played SXSW in Austin, Texas, a few days beforehand.  The following year the band travelled to Australia and played their first shows there, opening up for Crowded House on the latter's first reunion gigs.  The Walls opened the shows in Sydney and Melbourne and also performed their own gigs in both of those cities.  The band's third album "Stop the Lights" was released in 2012.  The first single "Bird in a Cage" became a firm favourite with Irish radio, in particular with Irish DJ Tony Fenton who championed them.  The second single was the title track "Stop the Lights", an autobiographical story of a motorbike crash.  A video was shot for the song in the brother's hometown, Ennistymon, and in the Dublin mountains.  In March 2013 the band played their first shows in Russia and performed live on the Evening Urgant show.  They returned the following year.

Batman Forever (score): Batman Forever: Original Motion Picture Score Album is a 1995 Grammy nominated film score album for "Batman Forever", composed by Elliot Goldenthal.  It was released in conjunction with its soundtrack counterpart.  Despite Goldenthal having recorded over 2 hours of music, the soundtrack only had 45 minutes before La-La Land Records released an expanded version in 2012.  The score features big brass, strings and discordant noises while maintaining an anthemic sound.  Regarding the villainous leitmotifs, Goldenthal said Two-Face focuses on paired notes and doubled beats while being inspired by Russian composers such as Sergei Prokofiev and Dmitri Shostakovich, and Riddler has a sound reminiscent of old science fiction B-movies with a theremin.  On the U2 single "Hold Me, Thrill Me, Kiss Me, Kill Me", there is a track titled "Theme from "Batman Forever"" composed by Goldenthal; this can also be found on the expanded release issued in 2012.

New Year's Day (song): "New Year's Day" is a song by Irish rock band U2.  It is on their 1983 album "War" and it was released as the album's lead single in January 1983.  Written about the Polish Solidarity movement, "New Year's Day" is driven by Adam Clayton's distinctive bassline and the Edge's piano and guitar playing.  It was the band's first UK hit single, peaking at no. 10, also becoming the band's first international hit, reaching for example no. 9 in Norway, no. 11 on the Dutch Top 40, no. 17 in Sweden and charting on the "Billboard" Hot 100 in the United States (just missing the Top 50) for the first time in their career.

Sunday Bloody Sunday: "Sunday Bloody Sunday" is a song by Irish rock band U2.  It is the opening track from their 1983 album "War" and was released as the album's third single on 11 March 1983 in Germany and the Netherlands.  "Sunday Bloody Sunday" is noted for its militaristic drumbeat, harsh guitar, and melodic harmonies.  One of U2's most overtly political songs, its lyrics describe the horror felt by an observer of the Troubles in Northern Ireland, mainly focusing on the Bloody Sunday incident in Derry where British troops shot and killed unarmed civil rights protesters and bystanders.  At the same time, the lyrics reject hate and revenge as a response, as noted in the line "There's many lost, but tell me who has won."  Along with "New Year's Day," the song helped U2 reach a wider listening audience.  It was generally well received by critics on the album's release.

1990s in jazz: In the 1990s in jazz, jazz rap continued progressing from the late 1980s and early 1990s, and incorporated jazz influence into hip hop.  In 1988, Gang Starr released the debut single "Words I Manifest", sampling Dizzy Gillespie's 1962 "Night in Tunisia", and Stetsasonic released "Talkin' All That Jazz", sampling Lonnie Liston Smith.  Gang Starr's debut LP, "No More Mr. Nice Guy" (Wild Pitch, 1989), and their track "Jazz Thing" (CBS, 1990) for the soundtrack of "Mo' Better Blues", sampling Charlie Parker and Ramsey Lewis.  Gang Starr also collaborated with Branford Marsalis and Terence Blanchard. Groups making up the collective known as the Native Tongues Posse tended towards jazzy releases; these include the Jungle Brothers' debut "Straight Out the Jungle" (Warlock, 1988) and A Tribe Called Quest's "People's Instinctive Travels and the Paths of Rhythm" (Jive, 1990) and "The Low End Theory" (Jive, 1991).

List of songs recorded by U2: U2 are an Irish rock band from Dublin.  The band formed in 1976 and released their debut EP "Three" in 1979 exclusively in Ireland.  Following the release of their single "Another Day" in 1980, U2 signed a recording contract with Island Records, which lead to the release of their first album, "Boy", later that year.  The band has since released 13 studio albums, with the most recent release being "Songs of Innocence" in 2014.

Pump Up the Volume (song): "Pump Up the Volume" is the only single by British recording act M| A| R| R|S.  Recorded and released in 1987, it was a number-one hit in many countries and is regarded as a significant milestone in the development of British acid house music and music sampling.  The song derives its title directly from a lyrical sample from "I Know You Got Soul", a hit single by labelmates Eric B. & Rakim, released months prior in that same year.

Bacon (song): "Bacon" is a song recorded by American singer Nick Jonas, featuring guest vocals from singer Ty Dolla $ign.  It was released on July 12, 2016, as the second single from Jonas' third studio album, "Last Year Was Complicated".  The song was written by Jonas, Priscilla Renea, Tyrone Griffin, Jr. and Nolan Lambroza.  "Bacon" was nominated for the 2016 MTV Video Music Awards for the category "Song of the Summer".  It was the second consecutive year that Jonas was nominated for that award.

Stripped (song): "Stripped" is Depeche Mode's fifteenth UK single, released on 10 February 1986.  It was the first single from the album "Black Celebration", and the band's thirteenth overall and sixth consecutive single to hit the UK Top 20, peaking at number 15.  "Stripped" is well known for its innovative use of sampling.  The underlying beat is a distorted and slowed-down sound of a motorcycle engine running, while the main melody begins with a car's ignition starting, and the end uses sounds of fireworks.

Question: In what year was the U2 single that Bacon Popper is known for sampling released?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sampling_artist": {
      "type": "string",
      "description": "The artist known for sampling the U2 song."
    },
    "sampling_song_title": {
      "type": "string",
      "description": "The title of the song that contains the sample."
    },
    "sampled_u2_song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the U2 song that was sampled."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the U2 song was released as a single."
        },
        "album_title": {
          "type": "string",
          "description": "The album from which the U2 song originated."
        }
      },
      "required": [
        "title",
        "release_year",
        "album_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "sampling_artist",
    "sampling_song_title",
    "sampled_u2_song"
  ],
  "additionalProperties": false
}
