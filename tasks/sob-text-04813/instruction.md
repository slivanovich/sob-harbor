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
Primitive Man (album): Primitive Man is an album by the Australian synthpop band Icehouse, released in September 1982.  In January 1982, Icehouse founder Iva Davies started recording "Primitive Man" essentially as a solo project, it was co-produced with Keith Forsey who later worked with Simple Minds and Billy Idol.  Forsey supplied additional percussion; Davies supplied vocals, lead guitar, keyboards (Sequential Circuits Prophet-5), bass guitar and programmed the Linn drum machine.  Released as an Icehouse album, "Primitive Man" reached #3 on the National album charts and provided their international breakthrough single, "Hey Little Girl" which peaked at #7 in Australia, #2 in Switzerland, #5 in Germany, Top 20 in UK, Sweden and Netherlands, and #31 on the U.S. "Billboard" Mainstream Rock chart.  Another single "Great Southern Land" made the Australian Top 5, it was later featured in the 1988 Yahoo Serious film "Young Einstein", and remains their most popular song according to listeners of Triple M in 2007.  To promote "Primitive Man" on tour, Davies re-assembled Icehouse with Michael Hoste (keyboards) and John Lloyd (drums), and new members: Bob Kretschmer (guitar, backing vocals), Guy Pratt (bass guitar, backing vocals) and Andy Qunta (keyboards, backing vocals).

The Seabellies: Seabellies were an Australian alternative rock band formed in Newcastle in 2006.  The line-up included Eddie Garven on bass guitar; Kyle Grenell on guitars, percussion, bass guitar and keyboards; his brother, Trent Grenell on lead vocals, guitar, percussion and keyboards; Sean Kelleher on drums, horns and backing vocals; Antony Martin on keyboards, guitars and bass guitar; and Stephanie Setz on melodica, metalaphone, keyboards, bass guitar and backing vocals.  Their live performances display a variety of instrumentation and multi-percussive layering.

MGMT: MGMT is an American psychedelic rock band formed in 2002 at Wesleyan University.  It currently consists of Andrew VanWyngarden (lead vocals, guitar, keyboards, bass guitar, drums, percussion) and Ben Goldwasser (vocals, keyboards, guitar, percussion).  In the live lineup it consists of VanWyngarden, Goldwasser, Will Berman (drums, percussion, harmonica, backing vocals), Matt Asti (bass guitar, backing vocals), James Richardson (lead guitar, keyboards, backing vocals) and Hank Sullivant (guitar, keyboards).

Andrus, Blackwood and Company: Andrus, Blackwood & Company was a racially integrated Contemporary Christian Music group, releasing six albums between 1977 and 1984.  The group was composed of two former members of The Imperials, Sherman Andrus and Terry Blackwood as co-lead vocalists.  Rounding out the group's first touring band in 1977 were Rocky Laughlin on bass, Tim Marsh on drums, Bob Villareal on guitar and backing vocals, and Karen Voegtlin on keyboards and backing vocals.  Other alternating band members between 1978 and 1986 included Billy Blackwood (cousin of Terry Blackwood) on drums, John Mays on bass, Mark Hughes on bass (later with Dobie Gray and owner the world's largest used music store, Mr Mark's Music in Nashville (1980–90, 2000-2016-current), Jeff Chambers on guitars, Randy Dennis on keyboards, David Ennis (later with country group Restless Heart) on keyboards, Gerritt Wilson on Synths, David Hassell on keyboards and vocals, Mark Burchfield on bass.  David Hassell also worked as office manager and tour manager for the group.  The group's final performance came in June 1986 at Six Flags theme park in Chicago, IL.

King Charles (musician): King Charles (born Charles Costa, 6 May 1985) is a singer-songwriter from West London.

List of songs recorded by Brand New: The American rock band Brand New has recorded songs for five studio albums, as well as numerous extended plays and demos.  This list comprises the band's song catalog, as well as live renditions, early demo tracks, recorded appearances on other albums, and unreleased tracks that have been discussed by the band.  Brand New formed in Long Island, a suburb of New York City in 2000.  The group consists of vocalist and guitarist Jesse Lacey, guitarist Vincent Accardi, drummer Brian Lane, and bassist Garrett Tierney.  Previous member Derrick Sherman also contributed guitar to a number of the bands releases, whilst producer Mike Sapone has worked with the band throughout their career, and is considered by the band to be a fifth or sixth member.

Incredible Kidda Band: The Incredible Kidda Band (aka The Kidda Band) were a British power pop band formed in Nuneaton on 10 February 1976, and composed of Alan Hammonds (guitar/Vocals), Graham "Kidder" Hammonds (percussion/ backing vocals), Dave 'Legs' Lister, [lead guitar backing vocals], John Rollason (guitar/ backing vocals), Les Rollason (bass), Graham "Dick" Millington (drums).  Later members of the band were Mark "Tarky" Bates (drums/ backing vocals), Keith Taylor (bass), Mick Rollason (guitar/ backing vocals) and Paul Gardner (drums).

Brand New (band): Brand New is an American rock band from Long Island, New York.  Formed in 2000, the band consists of Jesse Lacey (vocals, guitar), Vincent Accardi (guitar, vocals), Garrett Tierney (bass guitar, vocals), and Brian Lane (drums, percussion); they are joined by Benjamin Homola (percussion) and Kevin Devine (guitar, vocals) for their live performances.  From 2005 until 2013 the band also included Derrick Sherman (guitar, backing vocals, keyboards).

Cold War Kids: Cold War Kids is an American indie rock band from Long Beach, California.  Band members are Nathan Willett (vocals, piano, guitar), Matt Maust (bass guitar), David Quon (guitar, backing vocals), Matthew Schwartz (backing vocals, keyboards and piano, percussion, guitar), and Joe Plummer (drums, percussion).  Dann Gallucci (guitar, keyboards, percussion), Matt Aveiro (drums, percussion), and Jonnie Russell (guitar, vocals, piano, keyboards, percussion) are all former members of the band.

O'Brother: O'Brother is an American rock band from Atlanta, Georgia.  After releasing their debut EP, "In Comparison to Me", in 2006, Aaron Wamack and Tanner Merritt joined the band in 2008.  A second EP, "The Death of Day" was released on May 5, 2009 by Favorite Gentlemen Recordings, to positive reviews.  The band also released a vinyl split of their song, "Lay Down", in collaboration with Sainthood Reps (a side-project of Brand New's Derrick Sherman), under the vinyl label, The Ambitious Guest.  After the release of "The Death of Day", the band toured with Manchester Orchestra and The Features in February – March 2010.  O'Brother joined Thrice's "Major/Minor" tour in September – November 2011, alongside Moving Mountains and La Dispute.  Their first LP, "Garden Window", was released on November 15, 2011, and was well-received critically.  The record was released by Triple Crown and was co-produced by Andy Hull and Robert McDowell from Manchester Orchestra.  The band recorded a session at Daytrotter in Nov 2011.  In February 2012, O'Brother went on a co-headlining tour with Junius.  Aaron Wamack left the band prior to the tour's start.

Question: In between Brand New and King Charles which included Derrick Sherman (guitar, backing vocals, keyboards)?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that included the specified member."
    },
    "member_name": {
      "type": "string",
      "description": "The name of the band member in question."
    },
    "instruments_played": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of instruments played by the member in the band."
    },
    "membership_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The year the member joined the band."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the member left the band."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false,
      "description": "The period during which the member was part of the band."
    }
  },
  "required": [
    "band_name",
    "member_name",
    "instruments_played",
    "membership_period"
  ],
  "additionalProperties": false
}
