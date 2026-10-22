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
Kasabian: Kasabian ( ) are an English rock band formed in Leicester in 1997.  The band's original members consisted of vocalist Tom Meighan, guitarist and vocalist Sergio Pizzorno, guitarist Chris Karloff, and bassist Chris Edwards.  The band's line-up was completed by drummer Ian Matthews in 2004 after a string of session drummers.  Karloff left the band in 2006 and founded a new band called Black Onassis.  Jay Mehler joined as touring lead guitarist in 2006.  Mehler left the band for Liam Gallagher's Beady Eye in 2013, to be replaced by Tim Carter.  In 2010 and 2014, Kasabian won the Q Awards for 'Best Act in the World Today', while they were also named "Best Live Act" at the 2014 Q Awards and the 2007 NME Awards.  The band's music is often described as "indie rock", but Pizzorno has said he "hates indie bands" and does not feel Kasabian fit into that category.

Jack Whitehall: Jack Peter Benedict Whitehall (born 7 July 1988) is an English comedian, television presenter and actor.  He is best known for his stand up comedy, for starring as JP in the TV series "Fresh Meat", and for playing Alfie Wickers in the TV series "Bad Education", which he also co-wrote.  Since 2012, he has been a regular panellist on the game show "A League of Their Own".  He also hosted "Backchat" with his father, Michael.

Glasvegas (album): Glasvegas is the debut studio album by the Scottish indie rock band Glasvegas, first released in the UK on 8 September 2008 by Columbia Records.  The album was produced by lead singer James Allan and Rich Costey (Muse, Franz Ferdinand).  The album sold copies in its first week of release and reached number 2 on the UK Albums Chart.  The album was nominated for Best International Album at the 2008 Swedish Rockbjörnen awards, Best Album at the 2009 NME Awards and the 2009 Mercury Prize.  On 25 September 2009 the album was certified Platinum by the BPI, and it has sold over 300,000 copies in the UK.

NME Awards 2012: The NME Awards 2012 were held in London, England, on 29 February 2012, at the Brixton Academy and was hosted by English comedian Jack Whitehall.  The nominations were announced exclusively on Zane Lowe's BBC Radio 1 show on 30 January 2012.  Arctic Monkeys had seven nominations, followed by Kasabian, who went on to win best British Band, Lana Del Rey and Muse with three apiece.

List of NME Award winners: This is a list of winners of NME Awards.

NME Awards 2017: The NME Awards 2017 were held in London, England, on 15 February 2017, at the Brixton Academy and was hosted by English comedian Huw Stephens.  Beyoncé led the nominations with five, followed by The 1975, Bastille, Christine And The Queens and Skepta with four nominations each.

NME Awards: The NME Awards is an annual music awards show in the United Kingdom, founded by the music magazine, "NME" ("New Musical Express").  The first awards show was held in 1953 as the NME Poll Winners Concerts, shortly after the founding of the magazine.  Though the accolades given are entirely genuine, the ceremony itself is usually carried out in a humorous and jovial manner, and have included categories in the past like "Villain of the year" and "Worst Record".  The trophies given to the winners resemble an extended middle finger.

Star Awards 2012: Star Awards 2012 (Chinese: 红星大奖 2012) was a double television award ceremony held in Singapore.  It is part of the annual Star Awards organised by MediaCorp for the two free-to-air channels, MediaCorp Channel 8 and MediaCorp Channel U.  Star Awards 2012 was telecasted 'LIVE' on Channel 8, on 22 April 2012 and 29 April 2012.  Both ceremonies commenced at 1900 hrs, where the results were announced.  The 1st ceremony was held at the MediaCorp TV Theatre while the 2nd ceremony was held at Marina Bay Sands.  In addition, Astro AEC (Malaysia) also broadcast the ceremony 'live' on 29 April 2012.

Peter McNulty (film editor): Peter McNulty is a film editor.  McNulty was co-nominated (with Leslie Jones) for the Chicago Film Critics Association Awards 2012, the San Diego Film Critics Society Awards 2012 and the Online Film Critics Society Awards 2012 for Best Editing for his work on "The Master".

Anthems (Pure Love album): Anthems is the debut album by British-American rock band Pure Love, released February 4, 2013.  The group formed in 2011 after the departure of lead singer Frank Carter from the hardcore punk band Gallows, after which he began sharing song ideas with Jim Carroll of The Hope Conspiracy and The Suicide File; the two had met when Gallows supported The Hope Conspiracy in 2006.  The group signed to Vertigo Records in February 2012 and began working with producer Gil Norton, playing a number of new songs in their debut performance at the NME Awards that February.  Prior to "Anthem"<nowiki>'</nowiki>s release, the band debuted several songs online as music videos and downloads.  The album was initially scheduled for release in October 2012 but was delayed to February 2013.

Question: What is the date of birth of the host of NME Awards 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_show_name": {
      "type": "string",
      "description": "The name of the award show."
    },
    "award_show_year": {
      "type": "integer",
      "description": "The year the award show was held."
    },
    "host_details": {
      "type": "object",
      "properties": {
        "host_name": {
          "type": "string",
          "description": "The name of the host of the award show."
        },
        "host_date_of_birth": {
          "type": "string",
          "description": "The date of birth of the host."
        }
      },
      "required": [
        "host_name",
        "host_date_of_birth"
      ],
      "additionalProperties": false
    },
    "date_of_birth_found": {
      "type": "boolean",
      "description": "Indicates whether the date of birth for the host was found in the context."
    }
  },
  "required": [
    "award_show_name",
    "award_show_year",
    "host_details",
    "date_of_birth_found"
  ],
  "additionalProperties": false
}
