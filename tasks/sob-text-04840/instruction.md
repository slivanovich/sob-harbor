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
Backstreet Boys discography: The discography of American pop vocal group Backstreet Boys consists of eight studio albums, 28 singles, one live album, three compilation albums and 25 music videos. Formed in Orlando, Florida in 1993, the group consists of Nick Carter, Brian Littrell, Kevin Richardson, A. J. McLean and Howie Dorough.  Richardson left the group in 2006 to pursue other interests, but rejoined in 2012.  The Backstreet Boys released their debut single "We've Got It Goin' On" in 1995, which peaked at number sixty-nine on the "Billboard" Hot 100.  The single, however, entered the top ten in many European countries.  Their debut album, "Backstreet Boys", was released internationally in 1996, and was certified three times platinum in Europe, and diamond in Canada.  In 1997, they released their second international album, "Backstreet's Back", which continued their international success.  At the same time, they released their second self-titled album in the United States.  It peaked at number four and eventually became the tenth best-selling album of the 1990s.

Backstreet Boys (1997 album): Backstreet Boys is the self-titled debut U.S. studio album by the vocal-pop group Backstreet Boys.  The release of this album coincided with the release of their second international album "Backstreet's Back".  Their international debut album released in 1996 was also titled "Backstreet Boys", but it was not released in the United States.  This second self-titled album was released only in the United States in 1997, making it their debut album in the country.  It became one of the most successful debut albums of all time.  The album peaked at number four on the "Billboard" 200 albums chart and has been certified 14× Platinum (Diamond) by the RIAA for sales to retailers, having sold over 14 million copies to date in the United States.  This was also reported as the second highest seller in the past 14 years for Music Club sales back in 2003, selling 1.72 million units.

Playlist: The Very Best of Backstreet Boys: Playlist: The Very Best of the Backstreet Boys is the second greatest hits album by American vocal group Backstreet Boys, released by Legacy Recordings as part of their "Playlist" series.  This compilation includes songs from the group's first six studio albums, "Backstreet Boys" (1996), "Backstreet's Back" (1997), "Millennium" (1999), "Black & Blue" (2000), "Never Gone" (2005) and "Unbreakable" (2007), and the single "Drowning" from "The Hits – Chapter One" (2001).

Back to Me (Howie Dorough album): Back to Me is the debut solo album by American singer-songwriter Howie Dorough, who is known for being a member of the Backstreet Boys.  The album was released on November 9, 2011 in Japan and November 15, 2011 in the United States.  The album was recorded with a multitude of songwriters and producers.  Production on the album began in 2002 following the Backstreet Boys' initial hiatus, but when the group later re-united in 2004, the project was shelved.  Following the band's revival, Dorough continued working on the album in his spare time, and in 2008, made an official announcement regarding the album.  Dorough initially started off with a Latin sound in mind, exploring his heritage and routes.  Following the band's sixth album, "This is Us", Dorough returned to the studio and completed the project, finally changing the direction of the genre to pop-dance.

Christmas Time (Backstreet Boys song): "Christmas Time" is a Christmas song by American vocal group Backstreet Boys.  The song was written by Veit Renn, Joe Smith, and Johnny Wright.  "Christmas Time" was included on the Christmas edition of "Quit Playing Games (With My Heart)" single and on a bonus disc included in some editions of "Backstreet's Back" album.  The song was also featured on "Platinum Christmas", a compilation album released by Jive Records in 2000, as well as many other Christmas compilation albums through the years.

The Essential Backstreet Boys: The Essential Backstreet Boys is the third compilation album by American pop group Backstreet Boys, released by RCA Records and Legacy Recordings as part of their "Essential" series.  It was released on September 26, 2013 in the United Kingdom, and on October 22, 2013 in the United States.  The album includes songs from the group's first seven studio albums, "Backstreet Boys" (1996), "Backstreet's Back" (1997), "Millennium" (1999), "Black & Blue" (2000), "Never Gone" (2005), "Unbreakable" (2007), and "This Is Us" (2009).  It also includes the song "If You Stay" recorded for the 1997 film "Booty Call", and "Drowning" from their first greatest hits compilation, "The Hits – Chapter One" (2001).

Black &amp; Blue (Backstreet Boys album): Black & Blue is the fourth (third in the U.S.) album of the American vocal-pop group Backstreet Boys.  It was released on November 21, 2000 by Jive Records.  It is their follow-up album from their 1999 studio release "Millennium".  The album recorded the best international sales in a week for an album in history by selling over 5 million copies in its first week of sales globally.  In the United States, "Black & Blue" sold 1.6 million copies in its first week of release, making the Backstreet Boys the first group in Soundscan history to have million-plus first-week sales with back-to-back albums.  As of 2007, the album has sold 24 million copies worldwide.

Backstreet's Back: Backstreet's Back is the second studio album by the Backstreet Boys released internationally August 11, 1997 by Jive Records and Trans Continental Records, with the exception of United States.  It was a follow-up to their successful self-titled international debut.  Some songs from this album and the debut album were compiled into a second self-titled album released only in the US.

All I Have to Give: "All I Have to Give" is a song by American pop group the Backstreet Boys, produced and written by Full Force, and released as the third and final single from their second album "Backstreet's Back" and the sixth and final single from their U.S. debut album.  The single debuted at number 2 on the UK Singles Chart and peaked at number 5 on the US "Billboard" Hot 100, this song became 1999 US "Billboard" 's 29th hottest single.  At the 1999 Teen Choice Awards, the song won Choice Music: Video of the Year.  The song was also featured on the 1999 compilation album "Now That's What I Call Music!  3"

Backstreet Boys: The Backstreet Boys (often abbreviated as BSB) are an American vocal group, formed in Orlando, Florida in 1993.  The group consists of AJ McLean, Howie D., Nick Carter, Kevin Richardson, and Brian Littrell.

Question: In what city was the group that recorded "Backstreet's Back" formed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "group_name": {
      "type": "string",
      "description": "The name of the musical group."
    },
    "formation_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the group was formed."
        },
        "state": {
          "type": "string",
          "description": "The state where the group was formed."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "album_recorded": {
      "type": "string",
      "description": "The album mentioned in the question."
    }
  },
  "required": [
    "group_name",
    "formation_location",
    "album_recorded"
  ],
  "additionalProperties": false
}
