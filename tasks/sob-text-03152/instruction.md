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
+ (Ed Sheeran album): + (pronounced "plus") is the debut studio album by English singer-songwriter, Ed Sheeran, released on 9 September 2011 by Asylum Records and Atlantic Records.  The album marks Sheeran's commercial breakthrough, having previously released five EPs independently.  Jake Gosling and Sheeran produced the majority of the album, with additional production by American hip hop producer, No I.D..

Austin Mahone discography: The discography of Austin Mahone, an American singer-songwriter, consists of two extended play album, six singles, twenty promotional singles, and sixteen music videos. Mahone independently released his debut single, "11:11" to iTunes on February 14, 2011.  On June 4, 2012, he released his debut EP, "Extended Play", in Japan only.  On June 5, 2012, Mahone independently released his second single, "Say Somethin", his first release under the management of Chase Entertainment.  On August 28, 2012, Mahone announced that he had been signed to Chase/Universal Republic Records.

Attalus (band): Attalus is an American Christian rock band from Raleigh, North Carolina.  The band started making music in 2010, with members, lead vocalist and keyboardist, Seth Davey, guitarist and background vocalist, Evan King, drummer, Adam King, bassist and background vocalist, Chris Sierra, and guitarist, John Sierra.  The band released one extended play, "The Greater Tide", independently, in 2010.  Their next release, an album, "Post Tenebras Lux", was released independently, in 2011.  They released, another extended play, "Brighter Side", in 2012.  The subsequent album, also released independently, "Gospel Hymns, Vol.  1", came out in 2013.  They signed with Facedown Records, where they released, "Into the Sea", a studio album, in 2015.  This album was their breakthrough release upon the "Billboard" charts, where it placed on the Christian Albums chart.

Ed Sheeran: Edward Christopher Sheeran, {'1': ", '2': ", '3': ", '4': "} (born 17 February 1991) is an English singer-songwriter, guitarist, and record producer.  He was born in Halifax, West Yorkshire, and raised in Framlingham, Suffolk.  He attended the Academy of Contemporary Music in Guildford, Surrey, as an undergraduate from the age of 18 in 2009.  In early 2011, Sheeran independently released the extended play, "No. 5 Collaborations Project".  After signing with Asylum Records, his debut album, "+" (read as "plus"), was released on 9 September 2011 and has since been certified seven-times platinum in the UK.  The album contains the single "The A Team", which earned him the Ivor Novello Award for Best Song Musically and Lyrically.  In 2012, Sheeran won the Brit Awards for Best British Male Solo Artist and British Breakthrough Act.

Sam Sparro discography: Sam Sparro, the Australian born pop, dance, house, and soul singer-songwriter, producer, and remix engineer, has released two studio albums. His eponymous debut album, "Sam Sparro", released through both Modus Vivendi and Island Records, has been certified Gold.  His second album, "Return to Paradise" was released with EMI.  He has released two mixtapes. On August 5, 2013 Sparro released the mixtape "Mechanical."  to his SoundCloud account to promote his upcoming extended play, "Quantum Physical, Vol.  1". "Love Made Me Do It" was released via his SoundCloud account on February 13, 2015.  Sparro has released five extended plays. His first extended play "Black + Gold" was released by Modus Vivendi Music in January 2007.  "London Festival '08" was first released on January 1, 2008 with Island Records.  Sparro released his third extended play, "Pink Cloud", as a free download to promote his then upcoming second album before a number of release push-backs.  He released "Quantum Physical, Vol.  1" independently on October 1, 2014.  On October 16, 2015 Sparro released the second volume of "Quantum Physical" with Intuit Records.

Pacific Gold: Pacific Gold, (formerly, Wayfarer), is an American Christian music band.  They come from Seattle, Washington.  The band started making music in 2012.  Their membership is Torry Anderson, Brian Hibbard, Dan Koch, John Raines, and David Stuart.  The band released, an extended play, "The River", independently, in 2012, also the same year, another extended play released independently, "The Holly & the Ivy".  They released, a third extended play, "Pacific Gold", in 2013, independently.  Their first studio album, "Sing My Welcome Home", was released by BC Music, standing for Bad Christian Music, in 2015.

Alexz Johnson: Alexzandra Spencer "Alexz" Johnson (born November 4, 1986) is a Canadian singer-songwriter, record producer, actress and philanthropist.  Her debut album "Voodoo" was independently released in 2010, followed by the demo release of "The Basement Recordings" in 2011, with its sequel, "The Basement Recordings II", and EP "Skipping Stone" in 2012. " The Basement Recordings III" was released in 2013.  A follow-up extended play "Heart" followed in 2014; with her sophomore effort "Let 'Em Eat Cake" being released October of that year.  Johnson's third studio album "A Stranger Time" was released in 2017.

Songs I Wrote with Amy: Songs I Wrote with Amy is an extended play, independently released by Ed Sheeran on April 4, 2010.  After the success of +, Sheeran re-released five of his EPs, including "Songs I Wrote with Amy", which was released a second time on December 9, 2011.  All of the songs were written collaboratively by Ed Sheeran and Amy Wadge.

Jumpers for Goalposts: Live at Wembley Stadium: Jumpers for Goalposts: Live at Wembley Stadium is a home video by English singer-songwriter Ed Sheeran, released on Blu-ray on 13 November 2015.  It features the footage taken from Sheeran's x Tour, when he became the first solo artist to take the stage at Wembley Stadium in London and played across three sold out nights to a crowd of 240,000 people.  "Jumpers for Goalposts: Live at Wembley Stadium" features performances of hits like "The A Team", "Sing" or "Thinking Out Loud".  Sir Elton John duets with Sheeran on two songs.  Aside from the live performances, "Jumpers for Goalposts: Live at Wembley Stadium" gives viewers an insight into life backstage on the road with Sheeran.  Simultaneously, "Jumpers for Goalposts: Live at Wembley Stadium" was released on DVD as part of the re-release of Sheeran's 2014 "x" album.  This CD/DVD combo titled "x (Wembley Edition)" also includes five new tracks on the CD portion.

Natalia Keery-Fisher discography: The English singer-songwriter Natalia Keery-Fisher has released two studio albums, two extended play (EP), and seven singles as an artist, as well as four as a featured artist, and thirteen music videos.  She began her musical career by releasing a standalone single, entitled "Don't Play Nice", under the alias of Verbalicious, with label All Around the World.  Although the song reached number eleven in the United Kingdom, the label went bankrupt shortly after the song's release.  In 2008, Sinclair collaborated with French recording artist M. Pokora in the song "They Talk Shit About Me", as Verse.  Sinclair later changed her stage name to Natalia Cappuccini and released the extended play "Wommanequin" independently.

Question: Songs I Wrote with Amy is an extended play, independently released on which date, by Edward Christopher Sheeran, an English singer-songwriter, guitarist, and record producer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ep_title": {
      "type": "string",
      "description": "The title of the extended play."
    },
    "artist_name": {
      "type": "string",
      "description": "The full name of the artist who released the EP."
    },
    "artist_nationality": {
      "type": "string",
      "description": "The nationality of the artist."
    },
    "artist_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations of the artist."
    },
    "release_date": {
      "type": "string",
      "description": "The date the extended play was independently released."
    },
    "release_type": {
      "type": "string",
      "description": "The type of musical release (e.g., extended play)."
    },
    "release_method": {
      "type": "string",
      "description": "The method of release (e.g., independently released)."
    }
  },
  "required": [
    "ep_title",
    "artist_name",
    "artist_nationality",
    "artist_occupations",
    "release_date",
    "release_type",
    "release_method"
  ],
  "additionalProperties": false
}
