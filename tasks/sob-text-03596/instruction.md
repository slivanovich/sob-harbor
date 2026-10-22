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
Bad News (band): Bad News were an English spoof heavy metal band, created for the Channel 4 television series "The Comic Strip Presents...".  Its members were Vim Fuego (aka Alan Metcalfe), vocals and lead guitar (played by Ade Edmondson); Den Dennis, rhythm guitar (Nigel Planer); Colin Grigson, bass (Rik Mayall); and Spider "Eight-Legs" Webb, drums (Peter Richardson).

Bootleg (Bad News album): Bootleg is the second album release by UK parody heavy metal group Bad News.  It is a comedy album, apparently a bootleg of outtakes from the sessions for the group's debut album "Bad News".  The first album features music and some arguing between the band members; this album is almost entirely arguing.

Chris Barnes (actor): Christopher J. "Chris" Barnes (born June 24, 1965) is an American former child actor.  Beginning his professional film career at the age of ten, Barnes is perhaps best known for his role as the short-tempered shortstop, Tanner Boyle in the 1976 feature film, "The Bad News Bears" and its sequel "The Bad News Bears in Breaking Training", as well as for appearing in several "After School Specials" during the late 1970s and early 1980s.

Heavy metal bass: Heavy metal bass is the use of the bass guitar (also called "electric bass") in the rock music genres of heavy metal and hard rock.  The bassist is part of the rhythm section in a heavy metal band, along with the drummer, rhythm guitarist and, in some bands, a keyboard player.  The prominent role of the bass is key to the metal sound, and the interplay of bass and distorted electric guitar is a central element of metal.  The bass guitar provides the low-end sound crucial to making the music "heavy".  The bass plays a "...more important role in heavy metal than in any other genre of rock."

Ade Edmondson: Adrian Charles "Ade" Edmondson (born 24 January 1957) is an English comedian, actor, writer, musician, television presenter and director.  He came to prominence in the early 1980s and was part of the alternative comedy boom.  He is probably best known for his comedic roles in the television series "The Young Ones" (1982–84) and "Bottom" (1991–95), which he wrote together with his long-time collaborative partner Rik Mayall.  Edmondson also appeared in "The Comic Strip Presents..." series of films throughout the 1980s and 1990s.  For one episode of this he created the spoof heavy metal band Bad News, and for another he played his nihilistic alter-ego Eddie Monsoon, an offensive South African television star.

Interlude in Prague: Interlude in Prague is a 2017 film about Wolfgang Amadeus Mozart starring Aneurin Barnard, James Purefoy, Samantha Barks, Morfydd Clark, Adrian Edmondson and Anna Rust.  It was directed by John Stephenson, written by Brian Ashby, and screenplay by Brian Ashby, Helen Clare Cromarty, and John Stephenson.

Bad News (Bad News album): Bad News is the self-titled debut album from British heavy metal group Bad News released in October 1987 by EMI.  The album features a cover of the famous Queen song "Bohemian Rhapsody" and was produced by Queen's guitarist Brian May.  "Bohemian Rhapsody" was released as a single along with music video created for it, written and directed by Adrian Edmondson, who portrays Vim Fuego in the group.  The video was released as a video single by Picture Music International.  In 2004, EMI re-released the album with a re-ordered track listing and with additions of tracks derived from the group's follow-up album "The Cash In Compilation".

Obús: Obús is a Spanish heavy metal band created in Madrid in the early 80s.  They stood out because they took the risk of making a big spectacle in their concerts in order to reach to the level of other international heavy metal bands.  In addition, the lyrics they write and the feelings they transmit connect with the people that follow them.  As they said in an interview: "All our songs , some more and some less, have a meaning".  Far away from renouncing to their genre, they have always claimed that they were a heavy metal band and they even wrote a song about this genre in their first LP called"Dosis de Heavy Metal". In 2012, because of their 30th anniversary, they did a Tour around Spain.

Jackie Earle Haley: Jack "Jackie" Earle Haley (born July 14, 1961) is an American film and television actor.  His earliest roles included Moocher in "Breaking Away" (1979) and Kelly Leak in "The Bad News Bears" (1976), "The Bad News Bears in Breaking Training" (1977) and "The Bad News Bears Go to Japan" (1978).  After spending many years as a producer and director of television commercials, he revived his acting career with a supporting role in "All the King's Men" (2006).  This was followed by his performance as pedophile Ronald James McGorvey in "Little Children" (2006), for which he was nominated for the Academy Award for Best Supporting Actor.  Subsequent notable roles include the vigilante Rorschach in "Watchmen" (2009), horror icon Freddy Krueger in the remake of "A Nightmare on Elm Street" (2010) and Odin Quincannon in "Preacher" (2016–).

BumRush: BumRush is a 2011 Canadian film directed by Michel Jetté.  "BumRush" is an independent film that was shot in Montreal in French and English and features Emmanuel Auger in the lead role of L'Kid and Bad News Brown in the role of gang leader Loosecanon.  Musician and actor Bad News Brown was murdered soon after the film was shot.  The film features some of his musical works.  "BumRush" premiered on Canadian theaters on April 1, 2011.

Question: What 2017 film about Mozart starred the actor who created the spoof heavy metal band Bad News?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_subject": {
      "type": "string",
      "description": "The main subject or person the film is about."
    },
    "actor_who_created_band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who created the band."
        },
        "band_created": {
          "type": "string",
          "description": "The name of the spoof heavy metal band created by the actor."
        }
      },
      "required": [
        "name",
        "band_created"
      ],
      "additionalProperties": false
    },
    "other_starring_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other actors who starred in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_subject",
    "actor_who_created_band",
    "other_starring_actors"
  ],
  "additionalProperties": false
}
