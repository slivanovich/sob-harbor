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
Band Aid (band): Band Aid is a charity supergroup featuring mainly British and Irish musicians and recording artists.  It was founded in 1984 by Bob Geldof and Midge Ure to raise money for anti-famine efforts in Ethiopia by releasing the song "Do They Know It's Christmas? " for the Christmas market that year.  On 25 November 1984, the song was recorded at Sarm West Studios in Notting Hill, London, and was released in the UK four days later.  The single surpassed the hopes of the producers to become the Christmas number one on that release.  Two subsequent re-recordings of the song to raise further money for charity also topped the charts.  The original was produced by Midge Ure.  The 12" version was mixed by Trevor Horn.  In November 2014, a new version of the song was recorded by artists under the name of Band Aid 30.

Band Aid 20: Band Aid 20 was the 2004 incarnation of the charity group Band Aid.  The group, which included Daniel Bedingfield, Justin Hawkins of The Darkness, Thom Yorke and Jonny Greenwood of Radiohead, Chris Martin of Coldplay, Bono of U2, and Paul McCartney, re-recorded the 1984 song "Do They Know It's Christmas? ", written by Band Aid organisers Bob Geldof and Midge Ure.

Live Aid: Live Aid was a dual-venue benefit concert held on 13 July 1985, and an ongoing music-based fundraising initiative.  The original event was organised by Bob Geldof and Midge Ure to raise funds for relief of the ongoing Ethiopian famine.  Billed as the "global jukebox", the event was held simultaneously at Wembley Stadium in London, England, United Kingdom (attended by 72,000 people) and John F. Kennedy Stadium in Philadelphia, Pennsylvania, United States (attended by about 100,000 people).

Tsunami Aid: Tsunami Aid: A Concert of Hope was a worldwide benefit held for the tsunami victims of the 2004 Indian Ocean earthquake.  It was broadcast on NBC and its affiliated networks of USA Network, Bravo, PAX, MSNBC, CNBC, Sci-Fi, Trio, Telemundo and other NBC Universal stations and was heard on any Clear Channel radio station.  The benefit was led by the actor George Clooney on January 15, 2005, and was similar to "" (set up after the September 11th, 2001 attacks).  Digital Media innovator Jay Samit enabled viewers to purchase digital downloads of the performances as a new way to raise money for the cause; including live recordings by Elton John, Madonna, Sheryl Crow, Eric Clapton and Roger Waters.  Taking a cue from Bob Geldof (the man who had organized the Live Aid concerts for African famine relief), it consisted of famous Hollywood entertainers and former American presidents George H.W. Bush and Bill Clinton.  It was two hours long with stories and entertainment from a huge array of Hollywood popstars notables that include Brad Pitt, Donald Trump, and much more.  It was estimated to raise at least five million dollars by the end of the broadcast.

Tears Are Not Enough: "Tears Are Not Enough" is a 1985 charity single recorded by a supergroup of Canadian artists, under the name Northern Lights, to raise funds for relief of the 1983–85 famine in Ethiopia.  It was one of a number of such supergroup singles recorded between December 1984 and April 1985, along with Band Aid's "Do They Know It's Christmas? " in the United Kingdom, USA for Africa's "We Are the World" in the United States, "Cantaré, cantarás" by a supergroup of Latin American and Spanish singers, and "Les Yeux de la faim" in French Canada.

Band Aid 30: Band Aid 30 is the 2014 incarnation of the charity supergroup Band Aid.  The group was announced on 10 November 2014 by Bob Geldof and Midge Ure, with Geldof stating that he took the step after the United Nations had contacted him, saying help was urgently needed to prevent the 2014 Ebola crisis in Western Africa spreading throughout the world.  As in previous incarnations, the group covered the track "Do They Know It's Christmas? ", written in 1984 by Geldof and Ure, this time to raise money towards the Ebola crisis in Western Africa.  The track has re-tweaked lyrics to reflect the current Ebola virus epidemic in West Africa with all proceeds going towards battling what Geldof described as a "particularly pernicious illness because it renders humans untouchable and that is sickening".

Do They Know It's Christmas?: "Do They Know It's Christmas?"  is a song written in 1984 by Bob Geldof and Midge Ure in reaction to television reports of the 1983–85 famine in Ethiopia.  It was first recorded in a single day on 25 November 1984 by Band Aid, a supergroup put together by Geldof and Ure and consisting mainly of the biggest British and Irish musical acts at the time.  The single was released in the United Kingdom on 3 December 1984 and aided by considerable publicity it entered the UK Singles Chart at number one and stayed there for five weeks, becoming the Christmas number one of 1984.  The record became the fastest selling single in UK chart history, selling a million copies in the first week alone and passing 3 million on the last day of 1984, on the way to becoming the biggest selling single of all time in the UK.  It held this title until 1997 when it was overtaken by Elton John's "Candle in the Wind 1997", released in tribute to Princess Diana following her death.  The original version of "Do They Know It's Christmas?"  has sold 3.8 million copies in the UK to date.

Put You in the Picture: "Put You in the Picture" is a song written by Midge Ure, and performed by his group PVC2, who comprised Ure on guitar and lead vocals, Kenny Hyslop on drums, Billy McIsaac on keyboards and Russell Webb on bass guitar.  The song was released on August 30, 1977 by Zoom Records, in an eponymous EP, which was the last single and recording of Midge Ure with the remaining members of Slik, who later resurged as Zones, with another singer and guitarist, Willie Gardner.

When Harvey Met Bob: When Harvey Met Bob is a 2010 television film, written by Joe Dunlop, dramatising the relationship between musician Bob Geldof and concert promoter Harvey Goldsmith as they organize the massive fundraising concert Live Aid in 1985.  Directed by Nicholas Renton, the film stars Domhnall Gleeson as Geldof and Ian Hart as Goldsmith.

Bob Geldof: Robert Frederick Zenon "Bob" Geldof, KBE (born 5 October 1951), is an Irish singer-songwriter, author, political activist and occasional actor.  He rose to prominence as the lead singer of the Irish rock band The Boomtown Rats in the late 1970s and early 1980s, alongside the punk rock movement.  The band had Number One hits with his compositions "Rat Trap" and "I Don't Like Mondays".  He co-wrote "Do They Know It's Christmas? ", one of the best-selling singles of all time, and starred in Pink Floyd's 1982 film "Pink Floyd – The Wall" as "Pink."

Question: Robert Frederick Zenon "Bob" Geldof, is an Irish singer-songwriter, author, political activist and occasional actor, and co-wrote "Do They Know It's Christmas?", a song written in 1984 by Bob Geldof and Midge Ure in reaction to television reports of the 1983–85 famine, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "famine_location": {
      "type": "string",
      "description": "The country where the famine occurred."
    },
    "famine_years": {
      "type": "string",
      "description": "The period during which the famine took place."
    },
    "song_inspired": {
      "type": "string",
      "description": "The title of the song written in reaction to the famine."
    },
    "song_writers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The individuals credited with writing the song."
    }
  },
  "required": [
    "famine_location",
    "famine_years",
    "song_inspired",
    "song_writers"
  ],
  "additionalProperties": false
}
