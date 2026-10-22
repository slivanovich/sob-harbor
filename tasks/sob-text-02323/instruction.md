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
This Is My Town: Songs of New York: This Is My Town: Songs of New York is a studio album by American singer-songwriter Barry Manilow, released on April 21, 2017 by Decca Records and Stiletto Entertainment.  The album celebrates Barry Manilow's hometown New York City by "saying thanks to the city for giving me my ambition, my sense of humor and my decency", according to Manilow.  It consists both of new original Manilow compositions and standards "evoking the spirit and energy of New York City".

The Greatest Love Songs of All Time: The Greatest Love Songs of All Time is an album by Barry Manilow released on January 26, 2010.  The release came not too long before the start of his new show at the Paris Las Vegas hotel.

Barry Manilow (1973 album): Barry Manilow is the debut album by Barry Manilow.  It was released as Barry Manilow in 1973, then re-mixed and re-released as Barry Manilow I in 1975.

The Greatest Songs of the Sixties: The Greatest Songs of the Sixties is Barry Manilow's sequel album for "The Greatest Songs of the Fifties".  The album was another major hit for Manilow in the United States, selling nearly 50% more than his previous album in its opening week.  As with its predecessor, this album was produced by Clive Davis, along with Manilow and David Benson.  The classics performed in this album includes Frankie Valli's "Can't Take My Eyes Off You", Elvis Presley's #1 hit "Can't Help Falling in Love", Beatles' "And I Love Her" and Frank Sinatra's "Strangers in the Night" (the latter first appeared on Manilow's Sinatra-tribute album "Manilow Sings Sinatra" in 1998).

The Greatest Songs of the Fifties: The Greatest Songs of the Fifties is an album by veteran American singer Barry Manilow, released in the United States on January 31, 2006.  A significant album for Barry Manilow, it finds the Brooklyn-born crooner taking on songs that were popular in his youth.  The project also marked Manilow's return to his former label, Arista, with the company's founder, Clive Davis, setting the singer up with 1950s pop classics much in the way that the savvy businessman steered Rod Stewart in the direction of jazzy standards in his successful "The Great American Songbook" project.  The album was an amazing hit in the United States.  It entered the Billboard 200 at No. 1, giving him the second chart-topping album of his career.  His only other No. 1 album was "Barry Manilow Live", in 1977.  This is also the highest-debuting album of his career, selling over 150,000 copies in its opening week and besting the No. 3 opening of "Ultimate Manilow" in 2002.

2:00 AM Paradise Cafe: 2:00 AM Paradise Cafe is the fourteenth album by singer-songwriter Barry Manilow.  The album was a radical departure from Manilow's previous work of highly polished pop.  Manilow wrote in the liner notes that the record's concept came to him in a dream.  Johnny Mercer's widow, Ginger, entrusted Manilow with a cache of Mercer's lyrics that had never been set to music.  Although Manilow used only Mercer's "When October Goes" for the project, he created an album of all original songs with a torchy, smokey jazz style.  He recruited veteran jazz musicians Bill Mays, Gerry Mulligan, Shelly Manne, Mundell Lowe, and George Duvivier.  Also enlisted for vocal duets were Mel Tormé and Sarah Vaughan.  The entire album was rehearsed for three days, then recorded entirely live (in one take) without overdubs at Westlake Studio 'C' in Los Angeles, California and released in 1984.

The Greatest Songs of the Seventies: The Greatest Songs of the Seventies is Barry Manilow's follow up to his previous album, "The Greatest Songs of the Sixties".  The album was released on September 18, 2007.  Album producer Clive Davis said about Manilow: "No one can reinvent the great classics better than Barry Manilow.  He breathes new life and vitality into these truly wonderful songs and they sound fresh and timeless.  We continue on the mission to bring to a new generation the great songs of a different era."  Davis has worked with Manilow since the 1970s and have been good friends.  The album was released under Arista Records.  It also features some of Manilow's hits in acoustic.

Paris Las Vegas: Paris Las Vegas is a hotel and casino located on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Caesars Entertainment Corporation.

Barry Manilow (1989 album): Barry Manilow is the sixth self-titled album released by singer and songwriter Barry Manilow.  Manilow released a total of six self-titled albums in his career: "Barry Manilow" (later re-released as "Barry Manilow I"), "Barry Manilow II", "Barry", "Manilow", and this album with the same title as his first.  The album was released in 1989, and reached Gold certification.  This album also represented a hint of future album releases... 95% of the songs were not written/co-written by Manilow, which had until that point been rare.  Manilow, known for being a composer, typically always stocked his albums with material he co-wrote with his celebrated lyricists.  After the release of this album, the 1990s dawned and a new era in his career began as he embarked on introducing contemporary audiences to pop music of the 1930s through the late 1940s.  This album is also one of his longest of original material, clocking in at nearly an hour.

The Feeling's Not Right Again: The Feeling's Not Right Again is a collection of previously recorded songs by Ray Stevens, released in 1979.  All of the selections were chosen from his studio albums that were recorded for Warner Bros.  Records.  Stevens had a total of five singles released by Warner Bros., but only three are featured on this collection; the rest of the selections are album tracks.  The first track, "I Need Your Help Barry Manilow," is a novelty single that made its first album appearance on this collection; both it and the title track are homages to singer-songwriter Barry Manilow, and the album's cover art is itself a spoof of Manilow's album "Tryin' to Get the Feeling". " I Need Your Help Barry Manilow" was a minor hit for Stevens, narrowly missing the top 40 of the "Billboard Hot 100" (Stevens's last appearance on the chart to date) and reaching #11 on the adult contemporary music charts.

Question: The Grestest Love Songs of All Time came out just before Barry Manilow started to play at a hotel owned by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "title",
        "release_date"
      ],
      "additionalProperties": false
    },
    "show_location": {
      "type": "object",
      "properties": {
        "hotel_name": {
          "type": "string"
        },
        "hotel_owner": {
          "type": "string"
        }
      },
      "required": [
        "hotel_name",
        "hotel_owner"
      ],
      "additionalProperties": false
    },
    "timing_description": {
      "type": "string"
    }
  },
  "required": [
    "album_details",
    "show_location",
    "timing_description"
  ],
  "additionalProperties": false
}
