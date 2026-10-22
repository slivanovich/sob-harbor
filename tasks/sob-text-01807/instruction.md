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
Cheap Trick (1997 album): Cheap Trick, commonly referred to as Cheap Trick '97, is the second eponymous album, and thirteenth studio album, by the American rock band Cheap Trick, produced by the band and Ian Taylor and released on Red Ant Records and Alliance Entertainment.  The album is referred to as "Cheap Trick II" when it is referenced on the promotional DVD that was released with the band's "Special One" album in 2003.  Ian Taylor had previously engineered the "One On One" LP in 1982 and produced a handful of other tracks from 1983's "Next Position Please" LP, as well as the title track for the 1983 Sean S. Cunningham comedy film "Spring Break".

Triple Fast Action: Triple Fast Action (sometimes stylized as tripl3fastaction) was an indie rock/alternative rock band started by Wes Kidd and Brian St. Clair, both previous members of Chicago band Rights of the Accused, in 1995.  Kidd went on to manage such bands as Cheap Trick, The Damnwells and bandmate Kevin Tihista while working for New York-based Silent Partner Management.  St. Clair joined the band Local H after stints as tour manager for Chicago's Liz Phair and served as drum tech for Bun E. Carlos of Cheap Trick.  Triple Fast Action member Kevin Tihista released several of his own solo albums after the band's breakup.

Need Your Love (Cheap Trick song): Need Your Love is a song written by Rick Nielsen and Tom Petersson that was originally performed by American rock band Cheap Trick.  The song appeared on Cheap Trick's 1979 album "Dream Police".  A live version was included on the 1978 album "Cheap Trick at Budokan", which initially appeared only in Japan but eventually was in the United States in early 1979.  Because Cheap Trick was immensely popular in Japan, the band's Japanese label demanded that "At Budokan" include three new songs.  The three songs were "Ain't That a Shame", "Goodnight Now", and "Need Your Love."

Elo Kiddies: "ELO Kiddies" is a song originally released by Cheap Trick on the 1977 album "Cheap Trick".  It was written by Rick Nielsen, Cheap Trick's lead guitarist and primary songwriter.  It was released as a single twice, in 1977 as an A-side backed by "Speak Now Or Forever Hold Your Peace" and in 1979, as the B-side the live "Ain't That a Shame" from "Cheap Trick at Budokan".

Taylor Hanson: Jordan Taylor Hanson (born March 14, 1983) is an American musician best known as a member of the pop rock band Hanson.  He was born in Jenks, Oklahoma, a suburb of Tulsa.  He sings both lead and back-up vocals, and plays keyboard, percussion (including drums, bongos and the tambourine), guitar, harmonica, and piano.  He is also the lead singer of supergroup Tinted Windows.

Tinted Windows (album): Tinted Windows is the eponymous debut album of the American supergroup, Tinted Windows.  Tinted Windows was formed in New York City and consists of guitarist James Iha, previously of The Smashing Pumpkins and A Perfect Circle, singer Taylor Hanson of Hanson, bassist Adam Schlesinger of Fountains of Wayne and Ivy, and Cheap Trick's Bun E. Carlos.  The album was recorded at Stratosphere Sound Studios in New York, which Schlesinger and Iha co-own with Ivy's Andy Chase.

He's a Whore: "He's a Whore" is a song written by Rick Nielsen that was first released on Cheap Trick's 1977 debut album "Cheap Trick".  It has also appeared on a number of Cheap Trick compilation albums, including "The Essential Cheap Trick".  It has also been covered by many artists including Big Black, Neon and Vince Neil.  Like many of Cheap Trick's songs, it was played in early midwest concerts starting in 1975.

Bun E. Carlos: Brad M. Carlson (born June 12, 1950), better known by the stage name Bun E. Carlos, is the original drummer for American rock band Cheap Trick.  He was the band's chief setlister and archivist, and maintained recordings of all the band's shows, some of which have been released under the title 'Bun E's Bootlegs'.  Carlos has two side bands with former Cheap Trick bassist Jon Brant: The Bun E Carlos Experience, and the Monday Night Band.

Tinted Windows (band): Tinted Windows is an American rock supergroup formed by guitarist James Iha, previously of The Smashing Pumpkins, singer Taylor Hanson of Hanson, bassist Adam Schlesinger of Fountains of Wayne and Ivy, and Bun E. Carlos of Cheap Trick.  Josh Lattanzi also often performs with the band as the second guitarist.  This new project will run alongside all the artists' main bands.  The first performance by the band was on March 18, 2009 at Cain's Ballroom in Tulsa, Oklahoma in a small show at the side-stage.  Tickets sold out quickly and people flew from all over the world to see the debut.  The band made their South by Southwest Festival debut in Austin, Texas on Friday, March 20, 2009 at the Levi/Fader Fort, followed by a set at Pangaea.  The band also played at The Bamboozle music festival in New Jersey on May 3, 2009.

Auf Wiedersehen (song): "Auf Wiedersehen" (German for "Goodbye") is a song co-written by Cheap Trick guitarist Rick Nielsen and bassist Tom Petersson and first released on the band's 1978 album "Heaven Tonight."  It was also released as a single as the B-side of "Surrender".  Since its original release, it has also been released by Cheap Trick on several live and compilation albums, including "Budokan II"; "Sex, America, Cheap Trick"; "The Essential Cheap Trick", and the 30th Anniversary Edition of "Cheap Trick at Budokan", which also includes a DVD with a video performance of the song.  Allmusic critic Stephen Thomas Erlewine described the song as one of the peaks of "Heaven Tonight" and as one of Cheap Trick's "stone-cold classics."  It has often been used by the band to close their concerts.  Since its original release, it has been covered by Anthrax, Cell, John Easdale, and Steel Pole Bath Tub.

Question: Which member of the band Hanson collaborated in a supergroup with Adam Schlesinger of Fountains of Wayne and Bun E. Carlos of Cheap Trick?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "supergroup_name": {
      "type": "string",
      "description": "The name of the supergroup."
    },
    "hanson_member": {
      "type": "string",
      "description": "The member from the band Hanson who was part of the supergroup."
    },
    "collaborators": {
      "type": "array",
      "description": "A list of other key collaborators in the supergroup.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the collaborator."
          },
          "original_band": {
            "type": "string",
            "description": "The original band of the collaborator."
          }
        },
        "required": [
          "name",
          "original_band"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "supergroup_name",
    "hanson_member",
    "collaborators"
  ],
  "additionalProperties": false
}
