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
Yellow Submarine (sculpture): The Yellow Submarine in Liverpool is a large model representation of the submarine featured in the animated film "Yellow Submarine", inspired by the song of the same name on the Beatles album "Revolver".  It was built by a group of about 80 apprentices from Cammell Laird's shipyard, designed in part by Mr L Pinch, a draughtsman at the yard, for exhibition at the International Garden Festival in Liverpool in 1984.  The Submarine was in a garden themed around the Beatles, one of 60 such themed gardens, and was highly popular.  The garden took the form of an apple-shaped labyrinth, containing symbolic references to the group, and included a bronze statue of John Lennon, which now stands at Liverpool John Lennon Airport.

Ben Margulies: Ben Margulies is a Grammy-nominated songwriter and a RIAA nine-time platinum certified record producer, as well as a drummer, guitarist, piano player and singer.  He is best known for co-writing seven of the 11 songs on Mariah Carey's debut album "Mariah Carey", including the number one hits "Vision of Love", "Love Takes Time", and "Someday".  The album was nominated for multiple Grammys and has sold over 20 million records worldwide.  "Love Takes Time" also won Song of the Year at the 1992 BMI Pop Awards.

Ridiculous (album): Ridiculous is an album by the British new wave group Squeeze.  It was the band's eleventh studio album, and it introduced their latest drummer Kevin Wilkinson (no relation to bassist Keith Wilkinson).  As on the previous album, "Some Fantastic Place," the band recorded one song penned by Keith Wilkinson.  This time, however, Wilkinson did not perform the lead vocals.  That song, "Got to Me", is the last Wilkinson would write with Squeeze.  Chris Difford sang lead on two songs, "Long Face" and "Fingertips".  He had not performed lead on an album cut since "Slaughtered, Gutted and Heartbroken" and "Love Circles" on the 1989 album "Frank".  This record was produced by Glenn Tilbrook and Peter Smith.

Weight of the World (Ringo Starr song): "Weight of the World" is a song performed by Ringo Starr, released on his 1992 album, "Time Takes Time".  Written by Brian O'Doherty and Fred Velez, the song was released as a lead single backed with "After All These Years", and "Don't Be Cruel" (the latter was only on the CD single).  The single reached 74 in the UK charts.  It was released on 28 April 1992 in the US, and on 18 May in the UK.

Brooklyn Dreams (group): The Brooklyn Dreams was a successful singing group of the late 1970s and early 1980s mixing R&B harmonies with contemporary dance/disco music and best known for a number of collaborations with singer Donna Summer.  The band consisted of Joe "Bean" Esposito, Eddie Hokenson and Bruce Sudano.  Esposito provided lead vocals for the band and played guitar, while Sudano played keyboards and Hokenson played drums and occasionally sang lead vocals.

Gail Ann Dorsey: Gail Ann Dorsey (born November 20, 1962) is an American musician.  With a long career as a session musician, she is perhaps best known for her lengthy residency in David Bowie's band, from 1995 to Bowie's death in 2016.  Aside from playing bass, she occasionally sang lead vocals on "Under Pressure" and dueted with Bowie on other songs, including "The London Boys", "Aladdin Sane (1913-1938-197?) ", "I Dig Everything", accompanying Bowie on clarinet, and a cover of Laurie Anderson's "O Superman".

Ringo Starr: Richard Starkey, {'1': ", '2': ", '3': ", '4': "} (born 7 July 1940), known professionally as Ringo Starr, is an English drummer, singer, songwriter and actor who gained worldwide fame as the drummer for the Beatles.  He occasionally sang lead vocals, usually for one song on an album, including "With a Little Help from My Friends", "Yellow Submarine", "Good Night", and their cover of "Act Naturally".  He also wrote the Beatles' songs "Don't Pass Me By" and "Octopus's Garden", and is credited as a co-writer of others, including "What Goes On" and "Flying".

Angel in Disguise (McCartney–Starr song): "Angel in Disguise" is a song co-written by Paul McCartney and Ringo Starr that has never been released.  The song was intended for Ringo's 1992 "Time Takes Time" album; however, it did not make it onto the album, and therefore remains an intriguing, publicly unheard song.  Had it been released in 1992 it would have been the first McCartney-Starkey composition on record, although there were Beatles songs that were credited to Lennon–McCartney–Starkey and Lennon–McCartney–Harrison–Starkey.

Larry Hoppen: Larry Lewis Hoppen (January 12, 1951 – July 24, 2012) was a co-founder, vocalist and guitarist/keyboardist of the pop-rock group Orleans.  Orleans was formed in Woodstock, New York in January 1972 by Hoppen, vocalist/guitarist/songwriter (and future member of Congress) John Hall, and drummer/percussionist Wells Kelly.  In October 1972, Hoppen's younger brother Lance joined the group on bass guitar.  Larry sang lead on Orleans' three biggest hits, "Still the One," "Dance with Me" and "Love Takes Time."

Time Takes Time: Time Takes Time is the tenth studio album by Ringo Starr, released in 1992, his critically acclaimed comeback album.  His first studio album since 1983's "Old Wave", it followed a successful 1989–90 world tour with his All-Starr Band.  "Time Takes Time" features several celebrity guests including Brian Wilson, Harry Nilsson and Electric Light Orchestra frontman Jeff Lynne.

Question: What is the name of the songwriter who created "Time Takes Time" and occasionally sang lead vocals on one song on an album such as, "Yellow Submarine?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "songwriter_name": {
      "type": "string",
      "description": "The name of the songwriter."
    },
    "albums_associated": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of albums the songwriter is associated with, particularly those mentioned in the question."
    },
    "vocal_details": {
      "type": "object",
      "properties": {
        "vocal_role": {
          "type": "string",
          "description": "The type of vocal contribution made by the songwriter."
        },
        "songs_with_lead_vocals_examples": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Examples of songs where the songwriter sang lead vocals."
        },
        "vocal_frequency_description": {
          "type": "string",
          "description": "A description of how frequently the songwriter performed lead vocals."
        }
      },
      "required": [
        "vocal_role",
        "songs_with_lead_vocals_examples",
        "vocal_frequency_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "songwriter_name",
    "albums_associated",
    "vocal_details"
  ],
  "additionalProperties": false
}
