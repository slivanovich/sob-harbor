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
Promenade (Street Sweeper Social Club song): "Promenade" is the second single by rap rock supergroup Street Sweeper Social Club from their debut self-titled album.  The version that was released as a single differs from that on the album, the original version on the album is 2:31 in length whereas the extended version is 3:40 in length.  The extended version features a guitar solo by Tom Morello, the extended version is also on "The Ghetto Blaster EP", but is listed as the 'Guitar Fury remix'.

N.Flying: N.Flying (Korean: 엔플라잉 , Japanese: エヌフライング; short for New Flying which also means new wings or new escape.)  is a South Korean rap rock band formed by FNC Entertainment in 2013.  The band consists of Kwon Kwang-jin (bass, rap), Lee Seung-hyub (rhythm guitar, vocal, rap), Cha Hun (lead guitar, vocal), Kim Jae-hyun (drums) and Yoo Hwe-seung (vocal).  Their first release, "Basket" charted at number two on Oricon's weekly Indies chart in Japan.  Their fan club name is "N.Fia", a combination of the words “N.Flying” and “Utopia.”  It means that the band and their fans will fly together towards the utopia of their ideal music.

Deuce (singer): Aron Erlichman (born March 2, 1983), better known by his stage name Deuce (formerly known as "Tha Producer" ), is an American music producer, singer, songwriter, and rapper.  Brought to fame as a producer, singer-songwriter and one of the founding members of rap rock band Hollywood Undead, Deuce has since moved on to solo work through the label "Five Seven Music", a branch of Eleven Seven Music.  He is also involved in a movement with fellow rapper Truth (Vardan Aslanyan) called "Nine Lives" (often stylized as both "9LIVES" and "IX LIVES").  Deuce released his debut album of the same name on April 24, 2012, which sold 11,425 copies in its first week.  Deuce has also collaborated with artists Marc Bosserman, Ronnie Radke, Brokencyde and Blood on the Dance Floor in the past.

Ghetto Therapy: Ghetto Therapy is the first collaborative album by Latin rappers Sen Dog and Mellow Man Ace as The Reyes Brothers, released on June 13, 2006 via Latin Thugs Entertainment LLC.  The seventeen-track record features guest appearances by the likes of Cypress Hill, Warren G, Snoop Dogg, Bishop Lamont, Bishop Don Juan Magic, Slip Malota, Pop Duke, O. Brown, J Killa, Frank Lee White.

Sen Dog: Senen Reyes (born November 22, 1965), best known by his stage name Sen Dog, is a Cuban-American rapper and member of rap group Cypress Hill.  He has been developing a solo career in addition to his work with Cypress Hill, and headlines rap rock band SX-10.  As of 2017 he is currently performing in Powerflo.

The Ghetto Blaster EP: The Ghetto Blaster EP is the first EP from the rap rock supergroup Street Sweeper Social Club, released on August 10, 2010.  It features covers of "Paper Planes" by M.I.A. and "Mama Said Knock You Out" by LL Cool J as well as a remix of the band's second single "Promenade."  They also cover The Coup song "Everythang".  It has also been confirmed that the full touring band has recorded on the album.  Tom Morello spoke about the EP in a press release, saying that they shot for an interesting combination of groups.  "On The Ghetto Blaster EP we were shooting for a combo of the first Clash record and the Ohio Players greatest hits, interwoven with tractor trailer size riffs of course.  This record definitely has more of a 'band' feel than the first, and Boots’ lyrics and delivery have never been sharper."  Boots Riley has also said of the EP “We got a new EP that’s going to come out called The Ghetto Blaster EP.  [You can expect] hard, hard, hard music and some raw as lyrics on top.”

Underground Authority: Underground Authority (Bengali: আন্ডারগ্রাউন্ড অথরিটি is an alternative rock / rap rock band from India.  Formed in early 2010, in Kolkata, their music is flavoured by a blend of protest poetry, reggae, alternative rock, rap rock and hard rock.  The band is noted for their socio-political messages / Anti-capitalism agenda in their song lyrics and also for their "Music to express and not impress" quote.

Walk This Way: "Walk This Way" is a song by the American hard rock band Aerosmith.  Written by Steven Tyler and Joe Perry, the song was originally released as the second single from the 1975 album "Toys in the Attic".  It peaked at number 10 on the "Billboard" Hot 100 in early 1977, part of a string of successful hit singles for the band in the 1970s.  In addition to being one of the songs that helped break Aerosmith into the mainstream in the 1970s, it also helped revitalize their career in the 1980s when it was covered by rappers Run–D.M.C. on their 1986 album "Raising Hell".  This cover was a touchstone for the new musical subgenre of rap rock, or the melding of rock and hip hop.  It became an international hit and won both groups a Soul Train Music Award for Best Rap – Single in 1987.

Street Sweeper Social Club: Street Sweeper Social Club is an American rap rock supergroup, formed in Los Angeles, California in 2006.  The band primarily consists of guitarist Tom Morello of Rage Against the Machine and vocalist/emcee Boots Riley of The Coup.  The band had been testing songs out during Tom Morello's Nightwatchman tour and released an album on June 16, 2009.  Stanton Moore drummed for the group for the recording of the album although he did not join the band for the following tour.  Street Sweeper Social Club opened for Nine Inch Nails and Jane's Addiction in May 2009.  Street Sweeper Social Club describes itself as "more than a band, it's a social club."  Their 2010 EP "The Ghetto Blaster EP" includes covers of M.I.A. "Paper Planes" and LL Cool J's "Mama Said Knock You Out".

Trik Turner: Trik Turner is a rap rock band founded in Phoenix, Arizona in 1999.  The band is best known for their song "Friends and Family," which reached the top ten on the "Billboard" Modern Rock chart and received airplay on MTV, VH1 and adult contemporary television and radio formats in 2002.  They were the first band to ever have two different videos aired on MTV for the same song, "Friends and Family".  They made appearances on "Late Show with David Letterman", "Last Call with Carson Daly", "Late World with Zach" and "The Late Late Show with Craig Kilborn".  "Friends and Family" was also featured on the "Mr. Deeds" film soundtrack and "Black Sheep" was featured in the film, "You Got Served".  Although they were to go back into the studio, differences among band members led some to part ways.  The band was dropped from RCA Records.  They continued to tour and released a second album via their website, "Naming the Unidentified", in 2005, in this album they did not feature any rap metal songs.  it was just alternative rock songs, they did not use rap vocals in this album.

Question: Which of the rappers who collaborated on the album "Ghetto Therapy" headlines the rap rock band SX-10?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rapper_name": {
      "type": "string",
      "description": "The stage name of the rapper."
    },
    "collaborated_album": {
      "type": "string",
      "description": "The name of the album the rapper collaborated on."
    },
    "headlining_band": {
      "type": "string",
      "description": "The name of the rap rock band the rapper headlines."
    },
    "band_genre": {
      "type": "string",
      "description": "The genre of the headlining band."
    }
  },
  "required": [
    "rapper_name",
    "collaborated_album",
    "headlining_band",
    "band_genre"
  ],
  "additionalProperties": false
}
