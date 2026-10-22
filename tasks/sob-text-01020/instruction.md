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
My Propeller: "My Propeller" is a song by the English indie rock band Arctic Monkeys.  It was released as the third single from the band's third studio album "Humbug", as announced on 1 February 2010.  Released on 22 March 2010, the single follows its two predecessors from "Humbug", "Crying Lightning" and "Cornerstone", with the 10" vinyl being sold exclusively at Oxfam charity stores.

Who the Fuck Are Arctic Monkeys?: Who the Fuck Are Arctic Monkeys?  was the second EP by the Sheffield indie rock band Arctic Monkeys, first released on 24 April 2006 (see 2006 in British music).  The EP includes "The View from the Afternoon", the opening track of their first album "Whatever People Say I Am, That's What I'm Not", and four other songs.

R U Mine?: "R U Mine?"  is a song by the English indie rock band Arctic Monkeys.  It features lyrics written by Arctic Monkeys vocalist and rhythm guitarist Alex Turner and bassist Nick O'Malley, as well as music composed by the entire band.  The song was released as a digital download in the United Kingdom on 27 February 2012 and was released physically for the Record Store Day on 21 April 2012 on a limited edition double A-side purple 7" vinyl along with new song "Electricity".  The vinyl was limited to a run of only 1750 copies.

Five Minutes with Arctic Monkeys: "Five Minutes with Arctic Monkeys" is the debut single by Sheffield band Arctic Monkeys.  Released on 30 May 2005, it featured a re-recording of fan favourite "Fake Tales of San Francisco" and new song and B-side "From the Ritz to the Rubble".  It was a limited release by Bang Bang Recordings – a label created by the band for the sole purpose of releasing the single.  The name, Bang Bang, was mooted as a replacement band name, on the basis that the name Arctic Monkeys sounded "silly".

I Bet You Look Good on the Dancefloor: "I Bet You Look Good on the Dancefloor" is a song by English rock band Arctic Monkeys.  The song was released through Domino Records as the band's first single from their debut studio album, "Whatever People Say I Am, That's What I'm Not" (2006).  It debuted at number one on the UK Singles Chart on 23 October 2005, and remains one of the band's best-known songs.

Humbug (album): Humbug is the third studio album by English indie rock band Arctic Monkeys, first released on 19 August 2009 by Domino Records.  The band started to write songs for the album towards the end of summer 2008, and finished it entirely in spring 2009.

Death Ramps: "Death Ramps" is an alias for British indie rock band Arctic Monkeys.  They usually go under this name in collaboration with Miles Kane and fellow Sheffield artist Richard Hawley, and have released five tracks, all B-sides to Arctic Monkeys singles.

Whatever People Say I Am, That's What I'm Not: Whatever People Say I Am, That's What I'm Not is the debut studio album by English rock band Arctic Monkeys, released on 23 January 2006 by Domino.  The album surpassed Elastica's self-titled album to become the fastest selling debut album in British music history, shifting over 360,000 copies in its first week, and remains the fastest selling debut album by a band.  It has since gone quintuple platinum in the UK.  It is the only album to feature Andy Nicholson as bass player before he was replaced by Nick O'Malley.

Cornerstone (song): "Cornerstone" is a song by the English indie rock band Arctic Monkeys, released as the second single from their third album "Humbug".  It was released on 16 November 2009.  Like the previous single "Crying Lightning", the vinyl was made available in Oxfam shops.  Alex Turner told "Uncut" magazine that he wrote this song, "one morning, quite quickly."  He added: "There's something to be said for writing in the morning.  At other points in the day you're a bit more defensive.  I saw it as a challenge to write something in a major key, but that wasn't cheesy."  It was originally written in the key of A Major.  In October 2013 it was sampled by the rapper Dom Kennedy for the song "Pleeze" on his album Get Home Safely.

Fake Tales of San Francisco: "Fake Tales of San Francisco" is a song by English indie rock band Arctic Monkeys originally released on the band's first EP "Five Minutes with Arctic Monkeys" in May 2005.  After being featured on the band's debut album "Whatever People Say I Am, That's What I'm Not", the song was released as a radio only single in the United States instead of "Leave Before the Lights Come On", which was released there at the end of October.  The song was also released in the Netherlands, where it reached number 31 on the Dutch Singles Chart.  The song was popular on alternative rock radio in the U.S. in late 2006, but ultimately did not chart on the "Billboard" Hot Modern Rock Tracks chart.

Question: What is the name of the album by the English rock band Arctic Monkeys that features the song Cornerstone

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The name of the song."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that performs the song."
    },
    "album_info": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the album the song is from."
        },
        "album_type": {
          "type": "string",
          "description": "The type of album (e.g., studio album, EP)."
        }
      },
      "required": [
        "album_title",
        "album_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_name",
    "band_name",
    "album_info"
  ],
  "additionalProperties": false
}
