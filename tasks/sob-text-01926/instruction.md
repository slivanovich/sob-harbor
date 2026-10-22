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
A Black Man's Soul: A Black Man's Soul is an instrumental funk and soul album released by Ike Turner & The Kings of Rhythm in 1969 on Pompeii Records.  The album was recorded while Turner was touring with then-wife Tina Turner during his free time.  "A Black Man's Soul" exposed a side of Turner's music not as popular with his audiences of the time.  While Turner's more popular tracks like "Proud Mary" relied heavily on vocal harmonies and popular soul influences, these tracks reflected a more traditional and simple funk popularized by acts such as Charles Wright & the Watts 103rd Street Rhythm Band, Baby Huey, The Bar-Kays and Brother Jack McDuff, among others.

Betty Everett: Betty Everett (November 23, 1939 – August 19, 2001) was an American soul singer and pianist, best known for her biggest hit single, the million-selling "The Shoop Shoop Song (It's in His Kiss)".

Workin' Together: Workin' Together is a 1971 album recorded and released by Ike & Tina Turner on the Liberty Records label.  Their second album with the label, it was also their most successful album to date.  Much like their previous album, "Come Together", the album featured several covers of rock songs and also featured renewed versions of previous Ike & Tina songs, which was a habit for the couple.  The album featured the duo's biggest-selling hit, a funk rock styled cover of "Proud Mary" and also featured another popular Ike & Tina song, the Ike Turner & Alliene Bullock-composed "Funkier Than a Mosquita's Tweeter", later covered by Nina Simone.  Several of the songs were written by Ike (including one by "Eki Renrut", which is Ike Turner's name backwards) and "The Way You Love Me" which was a song the Turners had recorded for their very first studio album together, "The Soul of Ike & Tina Turner", a decade earlier.

A Fool in Love: "A Fool in Love" is the debut single for the team of Ike & Tina Turner.  Originally written by Ike Turner, the song became the first official single featuring Tina Turner and was the duo's first hit single, released on the Sue Records label in 1960.

Acid Queen: Acid Queen is Tina Turner's second solo album, released in 1975 on the EMI label in the UK, and on United Artists in the US.  Although it is a Tina Turner solo album, the very first single, "Baby Get It On", was a duet with Ike Turner, Tina Turner's musical partner and husband at the time.  As it turned out, it was her last solo album to be released before she left Ike Turner and the Ike & Tina Turner Revue.

Kings of Rhythm: The Kings of Rhythm are an American Rhythm and blues and Soul group formed in the late 1940s in Clarksdale, Mississippi and led by Ike Turner through to his death in 2007.  Turner would retain the name of the band throughout his career, although the group has undergone considerable lineup changes over time.  The group was an offshoot of a large big band ensemble called "The Tophatters".  By the late 1940s Turner had renamed this group the "Kings of Rhythm".  Their early stage performances consisted largely of covers of popular jukebox hits of the day.  A 1951 lineup of the group recorded the song "Rocket 88", which was an early example of Rock and roll.  In the 1960s they became the band for the "Ike & Tina Turner Revue".  For a few years in the early 1970s they were renamed "The Family Vibes", and released 2 albums under this name, both produced by, but not featuring Ike Turner.  The band have continued, for a time under the leadership of pianist Ernest Lane (himself a childhood friend of Turner's), and continues to tour with vocalist Earl Thomas.  The group has been running for at least 64 years.

I Idolize You: "I Idolize You" is a soul blues song written and produced by Ike Turner and released as a single by Ike & Tina Turner in 1961.

I'm Blue (The Gong-Gong Song): ""I'm Blue (The Gong-Gong Song)"" is a song written by Ike Turner, produced by Ike & Tina Turner and recorded and released as a single by Ike & Tina's backing trio, The Ikettes.  Recorded in 1961, it became a hit for the Ikettes in 1962.  "Billboard" named the song #63 on their list of 100 Greatest Girl Group Songs of All Time.

Jack Rabbit Blues – The Singles of 1958–1960: Jack Rabbit Blues is a compilation album of songs that Ike Turner performed on between 1958 and 1960 released through Secret Records.  At this time, Turner was involved and performed with various bands and musicians including Kenneth Churchill, Otis Rush, Betty Everett, Buddy Guy and his own Kings of Rhythm as well as his earlier singles with future wife, Tina Turner (she also went under the alias of Little Ann).  Every one of these tracks features Ike Turner on guitar, piano and/or vocals.

Nutbush City Limits: "Nutbush City Limits" is a semi-autobiographical song written and originally performed by Tina Turner in which she commemorates her rural hometown of Nutbush, Tennessee.  Released June 1973, shortly before her separation from then-husband and musical partner Ike Turner, "Nutbush City Limits" was the last hit single the duo would produce together.

Question: Ike Turner performed with this American soul singer and pianist, who went on to produce what million-selling single?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the American soul singer and pianist who performed with Ike Turner."
    },
    "singer_occupation": {
      "type": "string",
      "description": "The occupation of the singer."
    },
    "million_selling_single": {
      "type": "string",
      "description": "The title of the singer's biggest hit, which was a million-selling single."
    },
    "ike_turner_involvement": {
      "type": "string",
      "description": "Description of Ike Turner's performance involvement with the singer."
    }
  },
  "required": [
    "singer_name",
    "singer_occupation",
    "million_selling_single",
    "ike_turner_involvement"
  ],
  "additionalProperties": false
}
