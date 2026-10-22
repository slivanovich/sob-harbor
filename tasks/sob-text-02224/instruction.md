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
Robert Ellis Orrall: Robert Ellis Orrall (born May 4, 1955) is an American singer, songwriter, and record producer.  Signed to RCA Records in 1980, Orrall debuted that year with the album "Fixation".  His first Top 40 single was "I Couldn't Say No", a duet with Carlene Carter.  By 1990, Orrall had found success as a songwriter, having penned Number One singles for Shenandoah and Clay Walker.  He returned to RCA in 1991 and charted the singles "Boom!  It Was Over" and "A Little Bit of Her Love", from his first country music album, "Flying Colors".  Orrall then joined frequent songwriting partner Curtis Wright in the CMA-nominated duo Orrall & Wright, recording one more album and charting two singles.  They split up in 1994, however, and Orrall returned to his solo career, writing singles for Reba McEntire, Taylor Swift, and Lindsay Lohan, as well as producing records for Swift, Be Your Own Pet, and Love and Theft.  He also performs and records as an indie rock musician in the band Monkey Bowl.

Next to You, Next to Me: "Next to You, Next to Me" is a song written by Robert Ellis Orrall and Curtis Wright, and recorded by American country music group Shenandoah.  It was released in June 1990 as the lead-off single from their album "Extra Mile".  It was a Number One hit in both the United States and Canada.  It is also the band's longest-lasting number 1, at three weeks.  As of 2006, no other single from Columbia had spent three weeks atop the country charts.

Look It Up: "Look It Up" is a song written by Robert Ellis Orrall and Angaleena Presley, and recorded by American country music artist Ashton Shepherd.  It was released in January 2011 as the lead-off single to her album "Where Country Grows".  The song was originally recorded by Australian country artist Jasmine Rae in 2008.

A Little Bit of Her Love: "A Little Bit of Her Love" is a song co-written and recorded by American country music artist Robert Ellis Orrall.  It was released in November 1993 as the second single from the album "Flying Colors".  The song reached #31 on the "Billboard" Hot Country Singles & Tracks chart.  The song was written by Orrall and Lonnie Wilson.

Orrall &amp; Wright: Orrall & Wright was an American country music duo composed of Robert Ellis Orrall and Curtis Wright.  Both members had recorded solo albums and had charted singles of their own prior to Orrall & Wright's inception.  As Orrall & Wright, they charted two more singles and recorded a self-titled album on the Giant label.

Curtis Wright: Curtis Blaine Wrightt Jr. (born June 6, 1955 in Huntingdon, Pennsylvania) is an American country music artist.  He made his debut in 1989 with the single "She's Got a Man on her Mind" on a branch of MCA Records, before recording a solo album in 1992 on Liberty Records.  By 1994, he and frequent songwriting partner Robert Ellis Orrall had formed a duo known as Orrall & Wright, which also recorded one major-label album.  Wright later succeeded Brent Lamb in 2002 as the lead vocalist for the band Shenandoah, until being replaced by Jimmy Yeary in 2007.  He has toured as a member of Pure Prairie League as well.

The Swing (song): "The Swing" is a song written by Robert Ellis Orrall and Bob Regan, and recorded by American country music artist James Bonamy.  It was released in March 1997 as the lead single from the album "Roots and Wings".  The song reached number 31 on the "Billboard" Hot Country Singles & Tracks chart and peaked at number 16 on the Canadian "RPM" Country Tracks chart.

Crazier (Taylor Swift song): "Crazier" is a song by American recording artist Taylor Swift.  The song was written by Swift and Robert Ellis Orrall and produced by Nathan Chapman with Swift's aid.  The song was featured in both the 2009 film "" and on its .  The song is a relaxed ballad with country qualities and lyrics that describe being in love.  Swift performed the song as herself during a cameo in the "Hannah Montana: The Movie"; this scene was taken from the film and released as a music video for "Crazier".  The song was premiered on Radio Disney and Disney Channel, the latter promoting the home release of the film.  The song charting at number seventeen on the "Billboard" Hot 100, sixty-four in the Australian Singles Chart, sixty-seven in the Canadian Hot 100, and one-hundred on the UK Singles Chart.

Boom! It Was Over: "Boom!  It Was Over" is a song co-written and recorded by American country music artist Robert Ellis Orrall.  It was released in November 1992 as the first single from the album "Flying Colors".  The song reached number 19 on the "Billboard" Hot Country Singles & Tracks chart.  The song was written by Orrall and Bill Lloyd.

Brandon Boyd: Brandon Charles Boyd (born February 15, 1976) is an American singer, songwriter, musician, author, and visual artist.  He is best known as the lead vocalist of the American Multi-Platinum rock band Incubus.

Question: Robert Ellis Orrall and Brandon Boyd, have which mutual occupations?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person."
    },
    "mutual_occupations": {
      "type": "array",
      "description": "A list of occupations shared by both individuals.",
      "items": {
        "type": "string"
      }
    },
    "person_1_occupations": {
      "type": "array",
      "description": "A list of all known occupations for the first person.",
      "items": {
        "type": "string"
      }
    },
    "person_2_occupations": {
      "type": "array",
      "description": "A list of all known occupations for the second person.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_1_name",
    "person_2_name",
    "mutual_occupations",
    "person_1_occupations",
    "person_2_occupations"
  ],
  "additionalProperties": false
}
