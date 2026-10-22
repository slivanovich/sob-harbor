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
Steven Bernstein (musician): Steven Bernstein (born October 8, 1961) is an American trumpeter, slide trumpeter, arranger/composer and bandleader from New York City.  He is best known for his work in The Lounge Lizards, Sex Mob, Spanish Fly and the Millennial Territory Orchestra.  Sex Mob's 2006 CD "Sexotica" was nominated for a Grammy.

Talk to the Hand: Live in Michigan: Talk to the Hand: Live in Michigan is a live album and DVD concert video release from Canadian band Barenaked Ladies, produced by Morningstar Entertainment, Groovepix, and Desperation Records.  The DVD is their third DVD-video release, and their first feature-length concert video offered for sale.  The CD is their second widely released live album after "Rock Spectacle" (1996), not including their management company's sale of most of their live concert recordings via online download or shipped CD-R, several of which saw limited in-store release in certain localities.  The concert was recorded at the DTE Energy Music Theatre in Clarkston, Michigan on June 15, 2007.  The video was allegedly shot in conjunction with the local Detroit PBS affiliate, WTVS, with plans to air the special on their station.  The special has aired on the Toronto-based Canadian station SUN TV on October 12, 2007.

Live (Blood, Sweat &amp; Tears album): Live is a live album by the band Blood, Sweat & Tears, that was recorded in 1980 and released on compact disc in 1995 by Avenue Records through Rhino Records.  This album was recorded at the Street Scene in Downtown Los Angeles on October 12, 1980.  This set was recorded five years after the "Live In Concert/Live And Improvised" album.  The band's hit songs included in this collection were compressed into a 15-minute medley instead of the full-length versions that were included on their previous live album.  The rest of the songs here are from the "Nuclear Blues" album they were touring to support at the time of this recording.  One exception was an 11 ⁄ -minute version of "Gimme That Wine" that was originally released on the "Brand New Day" album in 1977.

Caught in the Act (Michael Bublé album): Caught in the Act is the second live album released by Canadian jazz crooner Michael Bublé.  It was filmed and recorded at the Wiltern Theater in Los Angeles.  The filmed concert was aired on PBS as an episode of "Great Performances", and the show was subsequently released on DVD along with the audio CD to create the album package, although the audio disc only featured eight of the songs from the concert.  The concert featured a few guest artists, including Laura Pausini, Chris Botti, and with an unexpected comedic banter with Bublé, Josh Groban.

Casiopea World Live '88: Casiopea World Live '88 is the fifth live album released by the jazz fusion group Casiopea in 1988.  It is a Compilation Album consisting of Recordings of some of their Songs played live and in Concert during Casiopea's World Tour in 1988 that promoted their Previous Album "Euphony".  It is also a Collaboration Album with 2 Japanese Horn Sections from 2 other bands.  The Brass Section of "Spectrum" and the Brass Section of "The Tops".  It is, additionally, the First Album Spectrum has recorded together since their Break-Up in 1981, And is also their Penultimate Album (Their last Album after they Officially broke up was released in 1991 and was a Remix Compilation Album of songs of theirs that were hits in Japan from the late 1970s).  Lead Trumpeter/Vocalist of Spectrum, Ichiro Nitta was also the Producer of "The Tops" at the time this album was released.  TOPS would release one more album, "SOUL CHILDREN", the following year, before they disbanded in 1991.

Free Touching: Live in Beijing at Keep in Touch: Free Touching: Live at Keep in Touch is a live recording of improvisational performances by Chinese guzheng virtuoso Wang Yong and six international musicians: Dutch jazz drummer Han Bennink, Austrian violinist Andreas Schreiber, American guitarist Dennis Rea, American trumpeter Lesli Dalaba, and horn players Claudio Puntin and Steffen Schorn.  The jam session from which the album is drawn was recorded during the Beijing International Jazz Festival on November 12, 1996 at Keep In Touch, reportedly China's first internet cafe.

Chris Botti: Christopher Stephen "Chris" Botti ( ; born October 12, 1962), is an American trumpeter and composer.

At the Half Note Cafe: At the Half Note Cafe is a live album by American trumpeter Donald Byrd recorded in 1960 at the Half Note in Manhattan and released on the Blue Note label originally as two single LP issues (BLP 4060 and BLP 4061) and reissued as a double CD set.

Copenhagen Concert: Copenhagen Concert is a live album by American trumpeter Buck Clayton recorded in Copenhagen, Denmark in 1959 and released on the SteepleChase label as a double LP in 1979.

Cattin' Curson: Cattin' Curson is a live album by American trumpeter Ted Curson which was recorded in Paris in 1973 and first released on the French Marge label and the on Trident in the US as (Typical Ted).

Question: Who released the live album that recorded a concert having an American trumpeter and composer who was born October 12, 1962 in it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_release_artist": {
      "type": "string",
      "description": "The artist who released the live album."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the live album."
    },
    "featured_musician": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the featured musician."
        },
        "instrument": {
          "type": "string",
          "description": "The primary instrument played by the musician."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the musician."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the musician."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the musician in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "instrument",
        "profession",
        "nationality",
        "birth_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_release_artist",
    "album_title",
    "featured_musician"
  ],
  "additionalProperties": false
}
