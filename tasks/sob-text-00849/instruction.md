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
You Gotta Be My Baby: "You Gotta Be My Baby" is a song written and recorded by George Jones.  It was his second Top 10 hit on Starday Records, peaking at #7 on the country singles chart.  That same year, he sang "You Gotta Be My baby" at his first appearance on "The Grand Ole Opry".  According to Bob Allen's book "George Jones: The Life and Times of a Honky Tonk Legend", Jones nearly walked off the "Opry" show when one of the WSM officials told him he could not take his guitar with him onstage but relented after Opry regular George Morgan handed him a guitar owned by Little Jimmy Dickens and promised he would take responsibility.  In the video biography "Same Ole Me", George recalled, "I was just so nervous.  This was the biggest thing that could ever happen to anybody in the world and I was just shakin'.  I mean just "truly" shakin' all over."

Bradley Gaskin: Bradley Gaskin (born in Gadsden, Alabama) is an American country music singer-songwriter.  He signed with Columbia Nashville in 2011 and has released his debut single, "Mr. Bartender" after being discovered through a talent contest sponsored by John Rich.  At the time, Gaskin had been working for his father hanging sheetrock.  The song entered the Hot Country Songs charts at number 51 on the chart dated for the week ending April 2, 2011.  He made his Grand Ole Opry debut on August 20th, 2011.  After a corporate restructuring, Gaskin moved to Columbia Records to release his second single, "Diamonds Make Babies".  On June 4, 2012, it was announced that Sony Nashville was retiring the BNA label and moving its roster to Columbia Nashville.  Gaskin was dropped from the label following this move.  Gaskin spent much of 2012 touring with Big & Rich, typically performing "Mr. Bartender" as well as a cover of Keith Whitley's "Don't Close Your Eyes".  Gaskin had plans for releasing a version of the Keith Whitley song prior to the problems that arose with his label.  Gaskin wrote a Tate Stevens "Power of a Love Song" in 2013.  Bradley performed "Don't Close Your Eyes" during a Grand Ole Opry performance on October 30, 2015.

The Bailey Brothers and the Happy Valley Boys: The Bailey Brothers and the Happy Valley Boys were an American bluegrass act widely considered to be among the first to cultivate the duo harmony vocal technique widely used in modern bluegrass music today.  Charlie Bailey (February 11, 1916 in Happy Valley, Tennessee, near Rogersville – March 12, 2004 in Bear, Delaware) began his musical career in 1936.  His brother, Danny Bailey (December 1, 1919, Happy Valley, Tennessee – March 22, 2004, Knoxville, Tennessee), teamed up with him in 1940, and the brothers began making frequent appearances on Tennessee radio stations in the Knoxville area.  Danny formed the Happy Valley Boys after Charlie joined the military in 1941.  In 1944 the Happy Valley Boys relocated to Nashville, where they became members of the Grand Ole Opry, and also made regular appearances on WSM radio in Nashville.  At that time, Danny was the youngest person to ever perform on the Grand Ole Opry.  When Charlie returned from his military service in 1946 the brothers were reunited as a duo but only stayed in Nashville briefly before returning to radio work in Knoxville.

Keith Bilbrey: Keith Bilbrey (born August 14, 1952) is an American country music disc jockey and television host in Nashville, Tennessee.  He served as a disc jockey at Nashville's WSM, as an announcer on the Grand Ole Opry, and as the host of TNN’s Grand Ole Opry Live.

McGee Brothers: The McGee Brothers were an American old-time performing duo of brothers Sam McGee (b. Samuel Fleming McGee, May 1, 1894, d. August 21, 1975) and Kirk McGee (b. David Kirkland McGee, November 4, 1899, d. October 24, 1983).  Sam typically played guitar and Kirk usually played banjo or fiddle, although they were both proficient in multiple string instruments.  The McGee Brothers were one of the most enduring acts on the Grand Ole Opry during the show's first fifty years.  They made their initial appearance on the Opry in 1926 and the following year joined Uncle Dave Macon's band, the Fruit Jar Drinkers.  In the 1930s, the McGees teamed up with early Opry fiddler Arthur Smith to form a string band known as the "Dixieliners," and in the 1940s they played and toured with Bill Monroe and His Bluegrass Boys and several other notable acts.

May the Bird of Paradise Fly Up Your Nose: "May the Bird of Paradise Fly Up Your Nose" is a 1965 novelty song performed by Little Jimmy Dickens.  It was Dickens' most successful single on the U.S. country music chart.  It spent two weeks at No. 1 that November, and stayed on the chart for a total of 18 weeks.  On the overall "Billboard" Hot 100 the song peaked at No. 15.

Ryman Auditorium: Ryman Auditorium (formerly Grand Ole Opry House and Union Gospel Tabernacle) is a 2,362-seat live performance venue, located at 116 5th Avenue North, in Nashville, Tennessee and is best known as the home of the "Grand Ole Opry" from 1943 to 1974.  It is owned and operated by Ryman Hospitality Properties, Inc.

Little Jimmy Dickens: James Cecil Dickens (December 19, 1920 – January 2, 2015), better known by his stage name, Little Jimmy Dickens, was an American country music singer and songwriter famous for his humorous novelty songs, his small size (4'11" [150 cm]), and his rhinestone-studded outfits (which he is given credit for introducing into country music live performances).  He started as a member of the Grand Ole Opry in 1948 and was inducted into the Country Music Hall of Fame in 1983.  Before his death he was the oldest living member of the Grand Ole Opry.

Grand Ole Opry: The Grand Ole Opry is a weekly country-music stage concert in Nashville, Tennessee, which was founded on November 28, 1925, by George D. Hay as a one-hour radio "barn dance" on WSM.  Currently owned and operated by Opry Entertainment (a division of Ryman Hospitality Properties, Inc.), it is the longest-running radio broadcast in US history, albeit not the longest-running one on a radio network.  Dedicated to honoring country music and its history, the Opry showcases a mix of famous singers and contemporary chart-toppers performing country, bluegrass, Americana, folk, gospel, and comedic performances and skits.  It attracts hundreds of thousands of visitors from around the world and millions of radio and Internet listeners.

Theron Hale: Theron Evan Hale (May 21, 1883 – January 29, 1954) was an American old-time fiddle and banjo player.  He was a member of the Grand Ole Opry in the late 1920s and 1930s, and is often remembered as a more laid back and sedate alternative to the raucous dance and "hoedown" music that dominated the Opry in its early days.  Hale continued playing and recording until the late 1940s, often accompanied by Opry guitarist Sam McGee.

Question: When did the singer of "May the Bird of Paradise Fly Up Your Nose" become a member of the Grand Ole Opry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the singer who performed the specified song."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song mentioned in the question."
    },
    "grand_ole_opry_membership": {
      "type": "object",
      "properties": {
        "is_member": {
          "type": "boolean",
          "description": "Indicates if the singer became a member of the Grand Ole Opry."
        },
        "membership_year": {
          "type": "integer",
          "description": "The year the singer became a member of the Grand Ole Opry."
        }
      },
      "required": [
        "is_member",
        "membership_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "singer_name",
    "song_title",
    "grand_ole_opry_membership"
  ],
  "additionalProperties": false
}
