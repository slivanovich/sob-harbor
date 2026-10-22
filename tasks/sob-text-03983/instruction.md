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
Concrete Injection: Concrete Injection (sometimes stylized as CI) is an American Rock band from Minneapolis, formed in 2012.  The band consists of Sota James (vocals), Dylan Cash (guitar), Baylen Pocket (bass), and Cutty (drums).  Their first radio single titled "Devil's Crypt" from their Die Anyways record stayed in rotation on the Top 20 chart on Active Radio on Music World Radio for 8 weeks in 2014, peaking at #12.  Their second single, titled "Vulnerable Skin" remained on the Music World Radio charts for 27 weeks, peaking at #4. They also achieved the #1 band ranking on the Reverbnation metal/rock charts in the Midwest twice during 2014, 4 times in 2015, 5 times in 2016, and twice in 2017.  They were also a featured artist on V6 Radio and made the weekly top ten on the Highway Rock Radio 365 charts, reaching #7 in May, 2017.

Blue Cheer: Blue Cheer was an American rock band that initially performed and recorded in the late 1960s and early 1970s and was sporadically active until 2009.  Based in San Francisco, Blue Cheer played in a psychedelic blues rock style, and are also credited as being some of the earliest pioneers of heavy metal, with their cover of "Summertime Blues" sometimes cited as the first in the genre.  They have also been noted as influential in the development of genres as disparate as punk rock, stoner rock, doom metal, experimental rock, and grunge.

Kongreßhalle: The Kongreßhalle was a multi-purpose event facility located in Frankfurt, Germany.  As a music venue it hosted artists such as The Doors, Creedence Clearwater Revival, Uriah Heep, The Firm, Tina Turner and Procol Harum.

The Doughboys (band): The Doughboys are an American rock band from Plainfield, New Jersey, who were active in the mid-60s, and re-formed in 2000.  They have been active ever since, and have cut three albums of newly recorded material since their reunion.

Deep Six (song): "Deep Six" is a song by American rock band Marilyn Manson.  The song was released to digital outlets on December 16, 2014 as the second single from the band's ninth studio album, "The Pale Emperor" (2015).  A music video directed by Bart Hess was released on YouTube.  The song was a hit on American Active Rock radio, peaking at number eight on "Billboard"'s Mainstream Rock, becoming the band's highest peaking single ever on that chart.

The Gaunga Dyns: The Gaunga Dyns are an American rock band from New Orleans, Louisiana, who were active from 1965 through 1968 and who regrouped in 2013.  In 1967, they released two singles and a had a local hit with "Stick with Her".  In the intervening years their work has come to the attention of garage rock enthusiasts, particularly some of their bolder songs such as "Rebecca Rodifier", which is one of the earliest rock songs to address the topic of abortion, and "No One Cares", which employs odd time signatures and changes.  They reunited with most of the members from their best-known configuration for the Ponderosa Stomp festival in 2013 and have since been intermittently active with different lineups featuring guitarist Steve Staples and vocalist Beau Bremer.

Creedence Clearwater Revival: Creedence Clearwater Revival, often informally abbreviated to Creedence or CCR, was an American rock band active in the late 1960s and early 1970s.

Little Black Submarines: "Little Black Submarines" is a song by American rock band The Black Keys.  It is the fourth track from their 2011 studio album, "El Camino", and was released as the album's fourth single on October 8, 2012.  The song begins as a quiet acoustic ballad before transitioning to a loud, hard rock arrangement in the second half.  Critics praised the song and called it one of the highlights from "El Camino".  The song was a success on rock radio, reaching number two on the Alternative Songs chart in the US and the Alternative Rock and Active Rock charts in Canada.  The group filmed a music video with director Danny Clinch at the Springwater Supper Club and Lounge, a dive bar in Nashville, Tennessee.  "Little Black Submarines" was certified gold in America.

Rainbow (rock band): Rainbow (also known as Ritchie Blackmore's Rainbow or Blackmore's Rainbow) are a British rock band led by guitarist Ritchie Blackmore, active from 1975 to 1984, from 1993 to 1997, and from 2015 to the present.  They were originally established with Ronnie James Dio's American rock band Elf, but after their first album, Blackmore fired the backing members and continued with Dio until 1979.  Three British musicians joined in 1979, singer Graham Bonnet, keyboardist Don Airey, former Deep Purple bassist Roger Glover, and this line-up gave the band their commercial breakthrough with the single "Since You Been Gone".  Over the years Rainbow went through many line-up changes with no two studio albums featuring the same line-up.  Other lead singers Joe Lynn Turner and Doogie White would follow, and the project consisted of numerous backing musicians.  A pioneer to power metal, the band's early work primarily featured mystical lyrics with a neoclassical metal style, but went in a more streamlined, commercial direction following Dio's departure from the group.

3 Pill Morning: 3 Pill Morning (sometimes stylized as 3PM) is an American Rock / Hard Rock band from Minneapolis, formed in 2004.  The band consists of Jeff Stebbins (vocals), Jon Stephenson (guitar), Ryan Lee (bass) and Tom DuPree III (drums).  On October 1, 2008, the band released their debut album "The Side Effects of Chronic Ambition" independently.  Their first radio single "Loser" spawned from their EP "Take Control" and stayed in rotation on the Top 100 chart on Active Radio in the US for over 6 months in 2011.  On July 17, 2012, the band released their sophomore full-length studio album entitled "Black Tie Love Affair" on Page 2 Music distributed by eOne.  The music video for "Skin" was officially released on July 5, 2012.  The band's latest album "Never Look Back" was released on July 29, 2016 on Countdown Entertainment distributed by The Fuel Music.  The album recognized as the Billboard #15 Hard Rock Albums and #14 Heatseekers Albums for that week.

Question: When was the american rock band hosted at Kongreßhalle active? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the American rock band."
    },
    "band_origin": {
      "type": "string",
      "description": "The country of origin of the band."
    },
    "venue_name": {
      "type": "string",
      "description": "The name of the venue where the band was hosted."
    },
    "active_period": {
      "type": "string",
      "description": "The period during which the band was active."
    }
  },
  "required": [
    "band_name",
    "band_origin",
    "venue_name",
    "active_period"
  ],
  "additionalProperties": false
}
