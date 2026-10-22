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
Awake (Secondhand Serenade album): Awake is the debut album by American acoustic rock musician, John Vesely, under the pseudonym Secondhand Serenade.  The album was originally released as a demo, in 2005.  In late 2006, Secondhand Serenade signed to label Glassnote Records and re-released the album on January 31, 2007.

The Dandy Warhols Are Sound: The Dandy Warhols Are Sound is a studio album by American alternative rock band The Dandy Warhols.  It is the original mix of the band's 2003 album "Welcome to the Monkey House", by Grammy Award-winning soul music mixing engineer Russell Elevado.  It was released on July 14, 2009, through the band's own label Beat the World Records.

Horny as a Dandy: "Horny as a Dandy" is a mash-up of Mousse T.'s "Horny" and The Dandy Warhols' "Bohemian Like You".  It was released as a single in 2006.  It features vocals from Hot 'n' Juicy.  It peaked at number 17 on the UK Singles Chart.  Two versions of the song appear on the first CD single: the original mash-up version produced by Loo & Placido and a new version produced by Mousse T. featuring a re-recorded sample of "Bohemian Like You" with The Dandy Warhols providing the vocals and instrumentation.

Zia McCabe: Zia McCabe (born Aimee Springer on June 2, 1975) is a keyboard player, percussionist and bass guitarist, and member of American alternative rock band The Dandy Warhols.  She is also a solo DJ, and part of a six-piece country music band called Brush Prairie.  She graduated from Battle Ground High School in Battle Ground, Washington in 1993.  In 1995, with hardly any prior musical experience, Zia joined The Dandy Warhols.  In an interview, Zia said,

...Earth to the Dandy Warhols...: ...Earth to the Dandy Warhols... is the sixth studio album by American alternative rock band The Dandy Warhols, recorded in 2008 and released on May 19, 2008 and is the first album released on their self-founded Beat the World Records label, after leaving Capitol Records in 2007.

Fall for You (Secondhand Serenade song): "Fall for You" is a song by Secondhand Serenade, the solo project of John Vesely and it was the first single from Secondhand Serenade's second studio album "A Twist in My Story" (2008).  The single was released as a digital download on January 21, 2008, peaking, after receiving a lot of airplay in summer months, in September 2008, at No. 8 on the "Billboard" Pop 100 charts and No. 21 on the "Billboard" Hot 100 charts.

The Black Album/Come On Feel The Dandy Warhols: The Black Album/Come On Feel The Dandy Warhols is a 2004 double album released by American alternative band, The Dandy Warhols.  The two-disc set was released on their own Beat the World Records label.  Initially, the album was only available to purchase through the band's website.  It is now available to own via other sources.

The Dandy Warhols: The Dandy Warhols are an American alternative rock band, formed in Portland, Oregon in 1994 by singer-guitarist Courtney Taylor-Taylor and guitarist Peter Holmström.  They were joined by keyboardist Zia McCabe and drummer Eric Hedford.  Hedford left in 1998 and was replaced by Taylor-Taylor's cousin Brent DeBoer.  The band's name is a play on the name of American pop artist Andy Warhol.

...The Dandy Warhols Come Down: ...The Dandy Warhols Come Down is the second studio album by American rock band The Dandy Warhols.  It was recorded in 1996 and released on July 15, 1997 by record label Capitol.

Secondhand Serenade: Secondhand Serenade is an American rock band, led by vocalist, pianist and guitarist John Vesely.  Vesely has released four studio albums to date under the name Secondhand Serenade: "Awake" in 2007, "A Twist in My Story" in 2008, "Hear Me Now" in 2010, and "Undefeated" in 2014.  The debut album used multitrack recording to create the sound of a band using technology, while the second album took a different path, using a proper band and synthesizers to establish a more accomplished sound.

Question: Which band, Secondhand Serenade or The Dandy Warhols, formed in Portland, Oregon in 1994?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that matches the formation criteria."
    },
    "formed_in_portland_oregon_1994": {
      "type": "boolean",
      "description": "True if the band was formed in Portland, Oregon in 1994."
    },
    "formation_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the band was formed."
        },
        "location": {
          "type": "string",
          "description": "The city and state where the band was formed."
        }
      },
      "required": [
        "year",
        "location"
      ],
      "additionalProperties": false
    },
    "founding_members": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the band's founding members."
    }
  },
  "required": [
    "band_name",
    "formed_in_portland_oregon_1994",
    "formation_details",
    "founding_members"
  ],
  "additionalProperties": false
}
