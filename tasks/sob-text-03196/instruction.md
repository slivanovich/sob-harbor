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
Working for the Weekend: "Working for the Weekend" is a song by Canadian rock band Loverboy, from their second studio album "Get Lucky" (1981).  It was written by guitarist Paul Dean, vocalist Mike Reno and drummer Matt Frenette, and produced by Bruce Fairbairn and Dean, and released as the lead single from the album in October 1981.  It has more of a power pop feel than the other band's other songs, but this new sound proved to generate success; the song reached number 29 on the US "Billboard" Hot 100 chart, and number two on "Billboard"' s Mainstream Rock chart in January 1982.

Hard Core (Paul Dean album): Hard Core is the first solo album released by former Streetheart & Loverboy lead guitarist, founder, and main songwriter, Paul Dean from 1989.  The lead-off track, "Sword & Stone" was demoed by Kiss for their "Crazy Nights" album in 1987, and later additionally recorded by the German Rockers, Bonfire in 1989 for the film "Shocker" and accompanying soundtrack.  The Bryan Adams-penned "Draw the Line" was originally recorded by Ted Nugent with Brian Howe on lead vocals in 1984 on his "Penetrator" album.

Eric Friedman: Eric Charles "Erock" Friedman (born June 28, 1984) is an American musician and songwriter, best known as the current touring guitarist and backing vocalist for Creed, as well as Tremonti, which is fronted by Alter Bridge and Creed lead guitarist Mark Tremonti.  He played with the band on their 2009 United States reunion tour with Staind and their 2010 Tour with Skillet.  He is the former lead guitarist for the band Submersed and also the former lead guitarist for Daughters of Mara.  Submersed and Daughters of Mara both disbanded in 2008.  He also currently plays lead guitar and co writes for the rock band Hemme.  At the age of thirteen Friedman was the youngest guitarist at the time to be fully endorsed by Fender.  His first introduction to Mark Tremonti was at a NAMM show where his then manager introduced them both.  They subsequently jammed at one of the Rivera amp booths and noticed, that although they had different styles, (Tremonti being heavily influenced by metal and Friedman Blues), they both complemented each other.

Sum 41: Sum 41 is a Canadian rock band from Ajax, Ontario.  Originally called Kaspir, the band formed in 1996 and currently consists of lead vocalist/rhythm guitarist/keyboardist Deryck Whibley, lead guitarist/backing vocalist Dave Baksh, rhythm/lead guitarist/keyboardist/backing vocalist Tom Thacker, bassist/backing vocalist Jason McCaslin and drummer Frank Zummo.

Loverboy: Loverboy is a Canadian rock band formed in 1979 in Calgary, Alberta.  Loverboy's hit singles, particularly "Turn Me Loose" and "Working for the Weekend", have become arena rock staples and are still heard on many classic rock and classic hits radio stations across Canada.  The band is based in Vancouver.

When It's Over (Loverboy song): "When It's Over" was a song written by band members Paul Dean and Mike Reno, released by the rock band Loverboy from their album "Get Lucky" in 1981.  Relying heavily on synthesizers, the song became a Top 40 hit for the band when released as a single the following year, reaching #26 on the charts.

This Could Be the Night (Loverboy song): "This Could Be the Night" is a song written by Paul Dean, Mike Reno, Bill Wray and John Friga and recorded by the Canadian rock band Loverboy from their hit album, "Lovin' Every Minute of It", released in 1985.  The song contained much more of a style that represented 1980s power pop ballads than the rocking style for which the band had been known.  Released as a single in 1986, it reached the top ten on the "Billboard" Hot 100 singles chart.

Cosmic Dust (band): Cosmic Dust, also known as the Cosmic Dust Fusion Band, is an instrumental jazz band formed in 1990 by Jim Templeton.  The band was the first well-known group that guitarist Myles Kennedy played in.  The original lineup consisted of Jim Templeton on keyboard, Gary Edighoffer on saxophone, Clipper Anderson on double bass, Myles Kennedy on guitar, and Scott Reusser on drums.  Kennedy eventually left the band and went on to become the lead vocalist/lead guitarist for a jazz fusion group called Citizen Swing and later an alternative rock band called The Mayfield Four.  Kennedy is now fronting and playing guitar for the hard rock/alternative metal band Alter Bridge, which he helped form with Creed members Mark Tremonti, Scott Phillips, and Brian Marshall in 2004, and is also the lead vocalist for Slash's solo band on tour.

Paul Dean (guitarist): Paul Warren Dean (born February 19, 1946 in Vancouver, British Columbia) is the lead guitarist for the Canadian rock band Loverboy which reached huge fame in the early 1980s.

The Replacements (band): The Replacements were an American rock band formed in Minneapolis, Minnesota, in 1979.  Initially a punk rock band, they are considered pioneers of alternative rock.  The band was composed of the guitarist and vocalist Paul Westerberg, guitarist Bob Stinson, bass guitarist Tommy Stinson and drummer Chris Mars for most of its career.  Following several acclaimed albums, including "Let It Be" and "Tim", Bob Stinson left the band in 1986, and Slim Dunlap joined as lead guitarist.  Steve Foley replaced Mars in 1990.  Towards the end of the band's career, Westerberg exerted more control over the creative output.  The group disbanded in 1991, with the members eventually pursuing various projects.  A reunion was announced on October 3, 2012.  The Replacements never had significant commercial success, except for "I'll Be You", which hit number 1 on the "Billboard" Alt Rock chart, but they influenced numerous alternative rock acts.

Question: Paul Dean played as lead guitarist for a rock band formed where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the musician."
        },
        "role": {
          "type": "string",
          "description": "The role of the musician in the band."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "band_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band."
        },
        "formation_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the band was formed."
            },
            "province_state": {
              "type": "string",
              "description": "The province or state where the band was formed."
            }
          },
          "required": [
            "city",
            "province_state"
          ],
          "additionalProperties": false
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the band was formed."
        }
      },
      "required": [
        "name",
        "formation_location"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The combined city and province/state of the band's formation location."
    }
  },
  "required": [
    "musician_details",
    "band_details",
    "final_answer"
  ],
  "additionalProperties": false
}
