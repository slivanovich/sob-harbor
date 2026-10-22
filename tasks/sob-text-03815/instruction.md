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
One by One (Foo Fighters album): One by One is the fourth studio album by American rock band Foo Fighters, released on October 22, 2002 by RCA.  The album is the first to feature guitarist Chris Shiflett.  Production on the album was troubled, with initial recording sessions considered unsatisfying and raising tensions between the band members.  They eventually decided to redo the album from scratch during a two-week period at frontman Dave Grohl's home studio in Alexandria, Virginia.  The songs on the album, which include the successful singles "All My Life" and "Times Like These", have been noted for their introspective lyrics and a heavier and more aggressive sound compared to the band's earlier work, which Grohl said was intended to translate the energy of the Foo Fighters' live performances into a recording.

Wasting Light: Wasting Light is the seventh studio album by American rock band Foo Fighters.  It was released on April 12, 2011 on RCA Records, and is the first album to feature rhythm guitarist Pat Smear since "The Colour and the Shape" (1997), making the band a five piece with the album.  Wishing to capture the essence of the group's earlier work and avoid the artificiality of digital recording, frontman Dave Grohl arranged for the band to record in his garage in Encino, California using only analog equipment.  The sessions were supervised by producer Butch Vig, with whom Grohl had worked on Nirvana's "Nevermind".  Since the old equipment did not allow for many mistakes to be corrected in post-production, the band spent three weeks rehearsing the songs, and Vig had to relearn outdated editing techniques.  The band went for a heavier and rawer sound to contrast with the musical experiments from their previous albums, and most of the lyrics were written as Grohl reflected upon his life and possible future.  Guest musicians include Bob Mould, Krist Novoselic, Jessy Greene, Rami Jaffe and Fee Waybill.

List of Foo Fighters band members: Foo Fighters is an American alternative rock band formed by multi-instrumentalist and vocalist Dave Grohl in 1994.  After recording the album "Foo Fighters" alone, Grohl enlisted guitarist Pat Smear, bassist Nate Mendel and drummer William Goldsmith to join the band.  This lineup recorded the second Foo Fighters album, 1997's "The Colour and the Shape", although most of Goldsmith's drum recordings were removed and re-recorded by Grohl for the release, after he left the band due to creative tensions.  Goldsmith was replaced by Taylor Hawkins, and Franz Stahl replaced Smear after he also departed, although he only remained in the band for a short period and did not record an album with the group.  The group's third album, "There Is Nothing Left to Lose", featured Hawkins on drums and was released in 1999.

Foo Fighters: Sonic Highways: Sonic Highways is a 2014 American documentary miniseries directed by Dave Grohl and written by Mark Monroe.  The documentary was made concurrently with Foo Fighters' eighth album, "Sonic Highways", and was broadcast on HBO.  Grohl described the project as "a love letter to the history of American music".  Each of the eight episodes is presented as an exploration of the musical history of a different American city through a series of interviews by Grohl.  The group is also shown incorporating what they learned from the interviews into the writing and recording of a new song in or near that city.  The series debuted on October 17, 2014.

Dave Grohl: David Eric Grohl (born January 14, 1969) is an American rock musician, guitarist, singer, drummer, songwriter, record producer, and film director.  He is the former drummer of the grunge band Nirvana and the frontman and founder of the rock band Foo Fighters, of which he is the lead vocalist, rhythm and lead guitarist, and primary songwriter.

Echoes, Silence, Patience &amp; Grace: Echoes, Silence, Patience & Grace is the sixth studio album by rock band Foo Fighters, released on September 25, 2007 by RCA Records.  The album is noted for a blend of regular rock and acoustic tracks with shifting dynamics, which emerged from the variety of styles employed on the demos the band produced.  It also marks the second time the band worked with producer Gil Norton, whom frontman Dave Grohl brought to fully explore the potential of his compositions and have a record that sounded different from their previous work.  Grohl tried to focus on songs with messages that resonated on the audience, writing reflective lyrics which drew inspiration from the birth of his daughter.

Foo Fighters (album): Foo Fighters is the self-titled debut studio album by American hard rock band Foo Fighters, released on July 4, 1995, by Capitol Records through Dave Grohl's label Roswell.  Grohl wrote and recorded the entire album himself – with the exception of a guest guitar spot by Greg Dulli – with the assistance of producer Barrett Jones at Robert Lang Studios in Seattle, Washington, in 1994.  Grohl claimed he recorded the album just for fun, describing it as a cathartic experience to recover from the death of his Nirvana lead singer Kurt Cobain.

Mantra (Dave Grohl song): "Mantra" is a song by Dave Grohl, Josh Homme, and Trent Reznor from the 2013 album "", the soundtrack to the 2013 documentary "Sound City".  Grohl was joined by different artists for different tracks as Grohl's Sound City Players.  For "Mantra", the final track on the album, he was joined by Homme and Reznor.  Homme also appeared on two other tracks on the album, "Centipede" and "A Trick With No Sleeve".

These Days (Foo Fighters song): "These Days" is the third single, (fourth in the UK), from the American rock band Foo Fighters' seventh studio album "Wasting Light".  It was written by Dave Grohl and co-produced by Butch Vig.  Dave Grohl has stated that it is his favourite song that he has ever written.  On August 18, 2012, the Foo Fighters performed "These Days" at Pukkelpop, as a tribute to the people who died or were injured there a year earlier, due to a violent thunderstorm that raged over the festival grounds.

Probot: Probot was a heavy metal side project of ex-Nirvana drummer and Foo Fighters rhythm guitarist and lead-singer Dave Grohl.  Described by Grohl as "a death metal "Supernatural,"" the album mixes instrumentals recorded by Grohl himself with various metal singers whom the musician admired.  The album was released in February 2004 by Southern Lord Records.  It featured one single entitled "Centuries of Sin"/"The Emerald Law".

Question: What band are These Days and Dave Grohl associated with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "associated_band_name": {
      "type": "string",
      "description": "The name of the band associated with the entities."
    },
    "entities_associated": {
      "type": "array",
      "description": "A list of entities from the question that are associated with the band.",
      "items": {
        "type": "string"
      }
    },
    "dave_grohl_role_in_band": {
      "type": "array",
      "description": "Dave Grohl's roles within the associated band.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "associated_band_name",
    "entities_associated",
    "dave_grohl_role_in_band"
  ],
  "additionalProperties": false
}
