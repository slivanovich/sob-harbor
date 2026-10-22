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
Progress Live: Progress Live (also known as the 20th Anniversary Tour) was the eighth concert tour by British pop group Take That.  The tour, sponsored by Samsung, supported their sixth studio album, "Progress" as they visited major cities in the UK and Europe.  It was the first tour to feature all five original members performing together in 15 years and the final tour to feature Jason Orange and Robbie Williams.  In its infancy, the tour accomplished many accolades including selling 1.34 million tickets in less than 24 hours.  The tour quickly became the biggest tour in the United Kingdom with demand for tickets a reported 30 times higher for Progress Live.

Robbie Williams: Robert Peter Williams (born 13 February 1974) is an English singer, songwriter and actor.  He was a member of the pop group Take That from 1990 to 1995 and again from 2009 to 2012.  He has also had commercial success as a solo artist.

Beautiful World Tour 2007: The Beautiful World Tour 2007 was the sixth concert tour for the British pop group Take That.  The tour ran from 11 October to 31 December 2007, with fifty stops in ten European countries.

Greatest Day (Take That song): "Greatest Day" is a song by British pop group Take That.  It was released through Polydor Records on 24 November 2008 as the lead single from their fifth studio album, "The Circus" (2008).  The song was written and produced by Take That and co-produced by John Shanks.

Higher Than Higher: "Higher Than Higher" is a song by British pop group Take That.  It was released through Polydor Records on 8 June 2015 as the third single from their seventh studio album, "III" (2014).  The song was written by Take That, Mattias Larsson, Robin Fredriksson, and Joe Janiak, and produced by Mattman & Robin and features Gary Barlow on lead vocals.

Let in the Sun: "Let in the Sun" is a song by British pop group Take That.  It was released through Polydor Records on 2 March 2015 as the second single from their seventh studio album, "III" (2014).  The song was written by Take That, Edvard Førre Erfjord, Gary Go, Cass Lowe, and Henrik Barman Michelsen, and produced by Stuart Price and features Gary Barlow on lead vocal.

Beautiful World (Take That album): Beautiful World is the fourth studio album from British pop group Take That.  The album was released in November 2006, and was the band's first studio album in 11 years, and was also the band's first album to be released as a four-piece, without Robbie Williams (who quit the band).  Five singles were released from the album: "Patience", "Shine", "I'd Wait for Life", the European-only single "Reach Out", and "Rule the World", which appeared on the deluxe tour edition.

Robbie Williams discography: The discography of Robbie Williams, an English singer-songwriter, consists of eleven studio albums, one live album, seven compilation albums, one extended play, ten video albums, fifty-nine singles (including six as a featured artist), six promotional singles and fifty-six music videos (including two as a featured artist).  Williams originally found success in the male pop group Take That, which he joined in 1990 following a successful audition: they released a series of UK number-one singles, including "Pray", "Relight My Fire", "Babe" and "Back for Good".  Williams left Take That in 1995 to pursue a solo career; the group disbanded the following year.

Let Me Entertain You Tour: The Let Me Entertain You Tour (also known as the Greatest Hits Tour) was the eleventh concert tour by British recording artist, Robbie Williams.  The tour begin March 2015 in Europe and continued into Asia and Australasia, with over 40 shows.  The tour grossed $27.1 million with 235,100 tickets sold.

Hey Boy (Take That song): "Hey Boy" is a song by British pop group Take That.  It was released through Polydor Records on 16 October 2015 as the fourth single from their seventh studio album, "III" (2014).  The song was written by Take That and produced by Greg Kurstin and features Mark Owen, Gary Barlow and Howard Donald on lead vocals.

Question: Which came first the let me entertain you tour or the pop group take that?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity being compared."
    },
    "entity_1_event_type": {
      "type": "string",
      "description": "The type of event for the first entity (e.g., formation, tour_start)."
    },
    "entity_1_year": {
      "type": "integer",
      "description": "The year the event for the first entity occurred."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity being compared."
    },
    "entity_2_event_type": {
      "type": "string",
      "description": "The type of event for the second entity (e.g., formation, tour_start)."
    },
    "entity_2_year": {
      "type": "integer",
      "description": "The year the event for the second entity occurred."
    },
    "first_event_name": {
      "type": "string",
      "description": "The name of the entity whose event occurred first."
    },
    "first_event_year": {
      "type": "integer",
      "description": "The year the first event occurred."
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement indicating which entity's event came first."
    }
  },
  "required": [
    "entity_1_name",
    "entity_1_event_type",
    "entity_1_year",
    "entity_2_name",
    "entity_2_event_type",
    "entity_2_year",
    "first_event_name",
    "first_event_year",
    "comparison_result"
  ],
  "additionalProperties": false
}
