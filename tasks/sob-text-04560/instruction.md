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
Jen Foster: Jennifer Kate Foster is an American singer-songwriter, musician, performer, record producer, and owner of her own record label, "Fosterchild Records."  Her music incorporates elements of rock, pop, r&b, folk, country and dance.  She has released 3 studio albums, 3 EP's and has contributed to various film, television and multi-media soundtracks and exceeded sales of 50, 000 units as an independent artist.  Foster has garnered a number of awards for her songwriting skills and has written with a number Nashville, Tennessee Music Row hit songwriter's including Pam Tillis ("Mi Vida Loca", "Spilled Perfume"),Jeffrey Steele ("What Hurts The Most", "My Wish"), Natalie Hemby ("Only Prettier", "White Liar"), Liz Rose ("Teardrops on My Guitar"), Mike Reid ("I Can't Make You Love Me"), Kristen Hall of Sugarland ("Baby Girl", "Stay"), Greg Barnhill ("Walkaway Joe"), Keith Follese ("Smile",“Lookin For a Good Time",“I Love You"),Rob Giles (The Rescues), Emily West ("I Hate You, I Love You", "Blue Sky")

List of songs written by Jeffrey Steele: This is an alphabetical list of songs written or co-written by the American songwriter Jeffrey Steele.  His credits include several singles mainly recorded by country music artists.  Among his co-writes are the Number One Hot Country Songs hits "Brand New Girlfriend" by Steve Holy, "The Cowboy in Me" by Tim McGraw, "These Days," "What Hurts the Most," "Here" and "My Wish" by Rascal Flatts.

BRIT School: The BRIT School for Performing Arts and Technology is a British performing arts and technology school located in Selhurst, Croydon, in the London Borough of Croydon, England, with a mandate to provide education and vocational training for the performing arts, media, art and design and the technologies that make performance possible.  Selective in its intake, the school is notable for its numerous famous alumni including Marsha Ambrosius, Adele, Tara McDonald, Leo the Lion, Stefan Abingdon, Katy B, The Feeling, Imogen Heap, Jessie J, Cush Jumbo, Rizzle Kicks, the Kooks, King Krule, Loyle Carner, Leona Lewis, Eman Kellam, Raye, Ashley Madekwe, Katie Melua, Kate Nash, Shingai Shoniwa, Amy Winehouse, Ella Eyre, Rainy Milo, Antonio Orozco, and Tom Holland.

Jeffrey Steele: Jeffrey LeVasseur (born August 27, 1961) is an American country music singer and songwriter, more commonly known by the name Jeffrey Steele.  Along with recording his own material, Steele has become a prolific Nashville songwriter, having co-written more than sixty hit songs for such artists as Montgomery Gentry, Tim McGraw, Faith Hill, LeAnn Rimes, Rascal Flatts, Billy Ray Cyrus, and others.

Love Is a Beautiful Thing (Phil Vassar song): "It's a Beautiful Thing", also known as "Love Is a Beautiful Thing", is a country music song co-written by American songwriters Jeffrey Steele and Craig Wiseman.  The first version of this song was released on September 14, 1999 (Morten Harket's 40th birthday) by Canadian singer Paul Brandt from his 1999 album "That's the Truth", from which it was released as a single in both Canada and the United States.  Eight years later, American singer Phil Vassar covered the song under the title "Love Is a Beautiful Thing" on his album "Prayer of a Common Man".  Vassar's version reached its peak of #2 on the "Billboard" Hot Country Songs charts in mid-2008.

These Days (Rascal Flatts song): "These Days" is a song written by Jeffrey Steele, Steve Robson, and Danny Wells, and recorded by American country music group Rascal Flatts on their 2002 album "Melt".  Released in June 2002 as that album's first single, the song became the group's first Number One hit on the "Billboard" Hot Country Singles & Tracks (now Hot Country Songs) charts in November of that year.

Shingai Shoniwa: Shingai Elizabeth Maria Shoniwa ( ; born on 1 September 1981) is an English singer, best known as the vocalist and bassist for the UK indie rock band Noisettes.  Her first name, Shingai, means "be bold/courageous/strong" in the Shona language.

Noisettes: Noisettes are an English indie rock band from London, currently composed of singer and bassist Shingai Shoniwa and guitarist Dan Smith.  The band first achieved commercial success and nationwide recognition with the second single of their second album, "Don't Upset the Rhythm (Go Baby Go)" which reached number two on the UK Singles Chart in Spring 2009.

Boy Howdy: Boy Howdy was an American country music band.  It was founded in 1990 in Los Angeles, California, United States by Jeffrey Steele (lead vocals, bass guitar), Hugh Wright (drums), and brothers Cary (guitar, mandolin, vocals) and Larry Park (guitar, fiddle, vocals).  Between 1992 and 1995, the band recorded two albums (1992's "Welcome to Howdywood" and 1995's "Born That Way") and an extended play (1994's "She'd Give Anything"), all on the Curb Records label.  In that same time span, Boy Howdy charted seven singles on the "Billboard" Hot Country Singles & Tracks (now Hot Country Songs) charts, including the Top Ten hits "She'd Give Anything" and "They Don't Make 'Em Like That Anymore."  After Boy Howdy disbanded in 1996, frontman Jeffrey Steele embarked on a solo career, recording several solo albums, in addition to writing more than sixty hit singles for other country acts.

I Thought I Lost You: "I Thought I Lost You" is a pop rock song performed by both American singer-songwriter and actress Miley Cyrus and actor and singer John Travolta.  The song was co-written by Cyrus with producer Jeffrey Steele.  It was released to Radio Disney as promotion for the 2008 Disney animated film "Bolt", in which Cyrus and Travolta provide the voices of Penny and Bolt.  "I Thought I Lost You" was made after filmmakers requested Cyrus to write a song for the film.  The lyrics speak of getting lost and getting found.

Question: What profession did Shingai Shoniwa and Jeffrey Steele have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the first person."
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the second person."
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    },
    "common_profession": {
      "type": "string",
      "description": "The profession shared by both individuals."
    }
  },
  "required": [
    "person_1",
    "person_2",
    "common_profession"
  ],
  "additionalProperties": false
}
