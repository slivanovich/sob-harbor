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
Jyväskylä Sinfonia: Jyväskylä Sinfonia is an orchestra in Finland.  Its current music director is Ville Matvejeff.  Jyväskylä Sinfonia was the first to record Einojuhani Rautavaara's "Aleksis Kivi".  Their first recording for Naxos Records was the first-five numbered symphonies by Joseph Haydn.  The orchestra accompanied baritone Waltteri Torikka on his platinum-selling debyt album "Sydän".

Just Bummin' Around: "Just Bummin' Around" was a song performed by American singer Dean Martin, in the 1967 television special, "Movin' With Nancy", starring Nancy Sinatra.  It was released to home video in 2000.

Ella Fitzgerald: Ella Jane Fitzgerald (April 25, 1917 – June 15, 1996) was an African - American jazz singer often referred to as the First Lady of Song, Queen of Jazz and Lady Ella.  She was noted for her purity of tone, impeccable diction, phrasing and intonation, and a "horn-like" improvisational ability, particularly in her scat singing.

Classic Diamonds – The DVD: Classic Diamonds – The DVD is a DVD video album by hard rock singer Doro Pesch, released in 2004 by AFM Records.  The DVD contains footage from two concerts held during the European tour which followed the release of the studio album "Classic Diamonds".  The album was a special project for Doro Pesch, who revised and re-arranged some of her songs for the Classic Night Orchestra, a 30-elements symphonic orchestra.  A smaller ensemble of the orchestra accompanied Doro and her usual touring musicians on tour, but the full orchestra was on stage in August 2004 at Wacken Open Air for a strictly acoustic set, an unusual performance for the largest European heavy metal festival.  Special guests of the night were former-Iron Maiden singer Blaze Bayley and guitarist Chris Caffery (Savatage, Trans-Siberian Orchestra).

Cartoon All-Stars to the Rescue: Cartoon All-Stars to the Rescue is a 1990 American animated drug-abuse prevention television special starring many of the popular cartoon characters from American weekday, Sunday morning, and Saturday morning television at the time of the film's release.  Financed by McDonald's and Ronald McDonald Children's Charities, the special was originally simulcast on April 21, 1990 on all four major American television networks (by supporting their Saturday morning characters): ABC, NBC, Fox and CBS, and most independent stations, as well as various cable networks.  McDonald's also distributed a VHS home video edition of the special, produced by Buena Vista Home Video, which opened with an introduction from President George H. W. Bush, and First Lady Barbara Bush.  The show was produced by the Academy of Television Arts & Sciences Foundation and Southern Star Productions, and was animated overseas by Wang Film Productions Co., Ltd..  The musical number "Wonderful Ways to Say No" was written by Academy-Award winning composer, Alan Menken and the late Howard Ashman, who also wrote the songs for Disney's "The Little Mermaid", "Beauty and the Beast", and "Aladdin".

Movin' with Nancy (album): Movin' with Nancy is the soundtrack to Nancy Sinatra's 1967 television special of the same name.  It is notable for the inclusion of the hit single "Some Velvet Morning", a song composed by and performed with Lee Hazlewood.  The album was arranged and conducted by Billy Strange.

A Man and His Music + Ella + Jobim: A Man and His Music + Ella + Jobim was a 1967 television special starring Frank Sinatra, Ella Fitzgerald, and Antonio Carlos Jobim, accompanied by Nelson Riddle and his orchestra.  The medley that Jobim & Sinatra sing together was arranged by Claus Ogerman.

Kelly Clarkson's Cautionary Christmas Music Tale: Kelly Clarkson's Cautionary Christmas Music Tale is a Christmas television special produced by Done and Dusted for NBC.  Directed by Hamish Hamilton, it stars Kelly Clarkson, Blake Shelton, Reba McEntire, Trisha Yearwood, Robin Williams, Whoopi Goldberg, William Shatner, Jay Leno, Matt Lauer, Danica Patrick, Heidi Klum, Ken Jeong, Jai Rodriguez and Morgan Bastin.  It is a musical comedy pastiche loosely based on Charles Dickens's "A Christmas Carol" where Clarkson's character learns the true meaning of Christmas, accompanied by the music of her sixth studio album "Wrapped in Red".  With its musical performances filmed live at The Venetian Las Vegas on October 30, 2013, the television special itself was broadcast on December 11, 2013 on NBC in the United States.  The special won a Gold World Medal for best Variety Special in the New York Festival’s International Television & Film Awards.  The special was aired on December 23, 2014 and December 17, 2015.

Some Velvet Morning: "Some Velvet Morning" is a song written by Lee Hazlewood and originally recorded by Hazlewood and Nancy Sinatra in late 1967.  It first appeared on Sinatra's album "Movin' with Nancy," the soundtrack to her 1967 television special of the same name, which also featured a performance of the song.

Hang 'Em High (composition): "Hang 'Em High" is a musical theme composed by Dominic Frontiere for the soundtrack of the 1968 film of the same name.  Though it was first covered by Hugo Montenegro, whose orchestra recorded a full album of music from the film, the tune became a hit in an R&B instrumental version by Booker T. & the M.G.'s that charted #9 Pop and #35 R&B.

Question: Whose orchestra accompanied the First Lady of Song and other singers in a 1967 television special?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "television_special": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the television special."
        },
        "year": {
          "type": "integer",
          "description": "The year the television special was broadcast."
        }
      },
      "required": [
        "title",
        "year"
      ],
      "additionalProperties": false
    },
    "featured_performers": {
      "type": "object",
      "properties": {
        "singers": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the main singers featured in the special."
        },
        "orchestra_leader": {
          "type": "string",
          "description": "The name of the person who led the accompanying orchestra."
        }
      },
      "required": [
        "singers",
        "orchestra_leader"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The name of the orchestra leader who accompanied the singers."
    }
  },
  "required": [
    "television_special",
    "featured_performers",
    "answer"
  ],
  "additionalProperties": false
}
