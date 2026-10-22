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
Vic Ruggiero: Victor "Vic" Ruggiero, (also known as "Rugaroo", "Bad Vic" or "Lord Sluggo") is a musician, songwriter and producer from New York City who has played in reggae, blues, ska and rocksteady bands since the early 1990s, including The Slackers, Stubborn All-Stars, SKAndalous All Stars, Crazy Baldhead and The Silencers (not to be confused with the Scottish rock band The Silencers).  He has also performed with punk rock band Rancid, both live and in the studio.  He has released four solo acoustic albums and continues to tour and record worldwide.  Ruggiero is known primarily as a singer and organist, although he also plays piano, bass, banjo, cigar box guitar, guitar, harmonica and percussion.

Understanding New Jersey &amp; Living in Sin: Understanding New Jersey & Living in Sin is the first solo, acoustic album from The Slackers' keyboardist/lead singer Vic Ruggiero.  It was released in the US in 2001.  In 2006 it was released in Germany/Europe by Moanin'.  The reissued version reverses the order of the albums and, as a result, was retitled "Living in Sin & Understanding New Jersey"

SKAndalous All-Stars: The SKAndalous All-Stars are a ska band, composed of members of The Slackers, the Skatalites, Mephiskapheles, the Stubborn All-Stars, Agent 99, Ruder Than You, Sic & Mad, The Excalibur, Cocktaillica, The Hurtin' Buckaroos, Living Colour, Perfect Thyroid, the Cycle Sluts from Hell, and The Klezmatics, and is led by Slackers frontman Vic Ruggiero.  Considered one of the first ska supergroups, the Skandalous All Stars built their reputation on ska and reggae stylized versions of popular rock and pop tunes.  Their first two albums—"Hit Me", released in 1997, and "Punk Steady", released the following year—included dance-inspiring interpretations of songs by the Sex Pistols, The Clash, Blondie, Patti Smith, the Ramones, Kiss, Nirvana, Radiohead, Stevie Wonder, and White Zombie.  With their third album, "The Age of Insects", released in 1999, the group began focusing on the original songs of keyboardist and vocalist Ruggiero.

Lay Your Hands on Me (Thompson Twins song): "Lay Your Hands on Me" is a 1984 song by the British band Thompson Twins.  It was the first single to be released from their 1985 album "Here's to Future Days", and was released in the UK almost a year in advance of the album.  It was written by Tom Bailey, Alannah Currie, and Joe Leeway.  There are two main versions of the song, with various edits and remixes of the two.  The first version was produced by Alex Sadkin & Tom Bailey was released in late 1984 in Europe and Australia.  The 1985 version was a reworking co-produced by Nile Rodgers, adding electric guitar and a gospel choir and released as a single in the US (this version appeared on the album).  The single peaked at #13 in the UK, spending nine weeks on the chart.  The single fared better in America where it peaked at #6 on the US Billboard 100 and also peaked at #46 on the US Dance /Club Play Singles.

Alive at the Ladybug House: Alive at the Ladybug House is the second solo, acoustic album from The Slackers' keyboardist/lead singer, Vic Ruggiero.  It was released in 2004.

Tom Bailey (musician): Thomas Alexander Bailey (born 18 January 1956) is an English singer, songwriter, composer, multi-instrumentalist, and record producer.  Bailey came to prominence in the early 1980s as the lead vocalist for the new wave band Thompson Twins, which released five singles that entered the top ten charts in the United Kingdom during the 1980s, including Love On Your Side, We Are Detective, Hold Me Now, Doctor!  Doctor! , and You Take Me Up.  He was the only classic member of the band to have formal musical training.  From 1994, Bailey was also a member of its later incarnation, Babble, releasing two commercially unsuccessful studio albums.

Hamburguru: Hamburguru, is the third solo CD by The Slackers' organist and lead singer, Vic Ruggiero.  The album has been released on February 23, 2007.  It has only been released in Japan by the Japanese label "Ska In The World".  Several songs on the album have been previously released on Vic Ruggiero's demo CD, Top Secret Bounty and Clues.  Two Songs ("Lonely Nites" and "Innocent Girl") have been re-recorded in July 2007 for the album "Something in My Blindspot".

Crazy Baldhead Sound System: Crazy Baldhead is a side project of The Slackers headed by Jayson "Agent Jay" Nugent.  Crazy Baldhead plays an innovative style of music that mixed reggae, ska, dub, rock and dancehall.  Members of the band include Eddie Ocampo, Victor Rice, Vic Ruggiero, Dave Hillyard and Glen Pine.

Squares and Triangles: "Squares And Triangles" is the very first single released by Thompson Twins.  It was written when the band was a four-piece consisting of Tom Bailey, Pete Dodd, John Roog, and Chris Bell.  The single was originally released in three different colored sleeves (red/yellow, red/green, red/white).  In 1982, the single was re-released in a black/white sleeve as a free EP along with the album "Set" featuring "Weather Station", a track composed by Tom Bailey for an independent film called 'The Onlooker' (1982) and "Modern Plumbing".  "Modern Plumbing" was a song recorded in late 1979 by The Blankets, a project including Tom Bailey, John Hade, and Traci.  The track was used as the intro tape to the live shows for the first year or two of performing in London.

Top Secret Bountry and Clues: Top Secret Bountry and Clues, also known as Blues and Clues is a demo CD which is only being sold at shows of The Slackers' organist/lead singer, Vic Ruggiero.  The album was informally released in 2006 and resembles a mix of country and blues songs.  There is a US and a European version of the demo.

Question: Are Vic Ruggiero and Tom Bailey from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "origin_country": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "origin_country"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "origin_country": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "origin_country"
      ],
      "additionalProperties": false
    },
    "are_from_same_country": {
      "type": "boolean"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "are_from_same_country"
  ],
  "additionalProperties": false
}
