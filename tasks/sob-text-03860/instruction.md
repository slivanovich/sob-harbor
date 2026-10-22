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
Ska punk: Ska punk (also spelled ska-punk) is a fusion genre that combines ska music and punk rock music.  Ska-core (sometimes spelled skacore) is a subgenre of ska punk that blends ska with hardcore punk.  Early ska punk combined both 2 Tone and ska with hardcore punk.  Ska punk often features wind instruments and especially horns such as saxophones, trombones and trumpets, making the genre distinct from other forms of punk rock.  It is similar to traditional Jamaican ska, but faster and heavier.

Metalcore: Metalcore is a fusion genre combining elements of heavy metal and hardcore punk.  The word is a portmanteau of the names of the two genres.  Among other styles blending metal and hardcore, such as crust punk and grindcore, metalcore is noted for its use of breakdowns, which are slow, intense passages conducive to moshing.  Pioneering metalcore bands—such as Integrity, Earth Crisis and Converge, all of which had formed by 1990—are described as leaning more toward hardcore, with their style sometimes being called metallic hardcore, whereas later bands—such as Killswitch Engage, All That Remains, Trivium, As I Lay Dying, Bullet for My Valentine, and Parkway Drive—are described as leaning more towards metal.  Pantera and Sepultura (who influenced Trivium, Atreyu, Bleeding Through and Unearth) have been particularly influential to the development of metalcore in the 2000s, which saw many bands in the genre achieve commercial success.

Victims Family: Victims Family is a hardcore punk band formed in 1984 in Santa Rosa, California, by the bass guitarist Larry Boothroyd and the guitarist and vocalist Ralph Spight.  Devon VrMeer completed the trio as drummer.  Their sound blended punk, heavy metal and jazz, making them difficult to categorize into a single genre.  Allmusic says, "Since its inception, the trio has refused to be pigeonholed to any single musical style — incorporating elements of hardcore punk, jazz, funk, hard rock, and noise into its challenging sound".  They were known as one of the most musically diverse bands in the San Francisco underground music scene.  Over the years, Victims Family went through four drummers and two break-ups.  Their name was taken from a piece by the cartoonist B. Kliban.

Nu metal: Nu metal (also known as nü-metal and aggro-metal ) is a form of alternative metal that combines elements of heavy metal music with elements of other music genres such as hip hop, alternative rock, funk and grunge.  Nu metal bands have drawn elements and influences from a variety of musical styles, including multiple genres of heavy metal.  Nu metal rarely features guitar solos; the genre is heavily syncopated and based on guitar riffs.  Many nu metal guitarists use seven-string guitars that are down-tuned to play a heavier sound.  DJs are occasionally featured in nu metal to provide instrumentation such as sampling, turntable scratching and electronic backgrounds.  Vocal styles in nu metal include singing, rapping, screaming and growling.  Nu metal is one of the key genres of the new wave of American heavy metal.

Serianna: Serianna was a metalcore band from Madison, Wisconsin.  The band formed in 2006, but disbanded in 2013 due to losing two key members.  Chris Nutting started a new project called Steady/Steady which, instead of Metalcore/Post-hardcore, this new band plays Indie Rock .  Guitarist Kris Meyer-Ruef later started playing in a new band called Deadset.

Canadian hardcore punk: Canadian hardcore punk originated in the early 1980s.  It was harder, faster, and heavier than the Canadian punk rock that preceded it.  Hardcore punk (usually referred to simply as hardcore) is a punk rock music genre and subculture that originated in the late 1970s.  The origin of the term "hardcore punk" is uncertain.  The Vancouver-based band D.O.A. may have helped to popularize the term with the title of their 1981 album, "Hardcore '81".  Hardcore historian Steven Blush said that the term "hardcore" is also a reference to the sense of being "fed up" with the existing punk and new wave music.  Blush also states that the term refers to "an extreme: the absolute most Punk."  One definition of the genre is "a form of exceptionally harsh punk rock."

Sheer Terror: Sheer Terror are an American hardcore punk band from New York City.  The band was one of the first to combine elements of heavy metal with a hardcore punk base, pioneering a heavier style of hardcore that would become popular in the following decades.  Formed in late 1984, the band, stayed together until 1998, surviving numerous lineup changes and shifts in musical style.  In October 2004, the band reunited and gave two shows at New York City's CBGB Club.

Zoetrope (band): Zoetrope was an American heavy metal band from Chicago, Illinois.  Although their sound was akin to thrash metal, the group described themselves as "Street Metal".  The group was formed in 1976 by teenage friends Barry Stern (drums/vocals), Kevin Michael Rasofsky, aka Kevin Michael, (guitar), and Calvin "Willis" Humphrey (bass), soon to be joined by second guitarist Ken Black.  Initially playing covers, the band soon ventured into writing their own material and released a single in 1980.  Although undeniably a metal band, Zoetrope was also active in Chicago's hardcore punk scene, sharing bills with locals hardcore bands and hanging out at O'Banions, a Chicago punk bar (Ken Black and Barry Stern also produced the self-titled LP by Chicago-based hardcore band Life Sentence in 1986).  Following the release of a couple of demo tapes, the group was signed to Combat Records and issued their first LP, "Amnesty", in 1985.  In 1987, the band traveled to Los Angeles to record their follow up, "A Life of Crime", with producer Randy Burns (Megadeth, Nuclear Assault).  During the recording sessions, Ken Black left the band and returned to Chicago to sort out substance abuse issues.  He was replaced by Louis Svitek.  Although Svitek appears on the album's cover, Kevin Michael later confirmed that Ken Black had finished his guitar parts before leaving Los Angeles.  During the tour supporting "A Life of Crime", Svitek was recruited for M.O.D. by Billy Milano.  After the tour, Barry Stern jumped ship to fellow Chicagoans Trouble.  Kevin Michael eventually returned with a new line up for 1993's "Mind Over Splatter" but the band folded for good soon after.

Bad Brains: Bad Brains are an American hardcore punk band formed in Washington, D.C., in 1977.  They are widely regarded as among the pioneers of hardcore punk, though the band's members have objected to this term to describe their music.  They are also an adept reggae band, while later recordings featured elements of other genres like funk, heavy metal, hip hop and soul.  Bad Brains are followers of the Rastafari movement.

The Number Twelve Looks Like You: The Number Twelve Looks Like You are an American hardcore punk band formed in Bergen County, New Jersey in 2002.  According to AllMusic, their music combines hardcore punk, heavy metal, post-hardcore, grindcore, "Japanese-style noise rock à la the Boredoms and the show-offy tempo, time signature, and dynamic shifts of Frank Zappa."  The band went on a six-year hiatus in 2010.  In May 2016, they performed a secret show and then announced their reunion.

Question: Serianna is a band of what genre that combines elements of heavy metal and hardcore punk?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the band."
    },
    "genre_components": {
      "type": "array",
      "description": "The genres that combine to form the band's primary genre.",
      "items": {
        "type": "string"
      }
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    },
    "band_status": {
      "type": "string",
      "description": "The current status of the band (e.g., active, disbanded)."
    }
  },
  "required": [
    "band_name",
    "genre",
    "genre_components",
    "formation_year",
    "band_status"
  ],
  "additionalProperties": false
}
