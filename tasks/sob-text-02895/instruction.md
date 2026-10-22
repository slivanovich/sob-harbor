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
Capitol Theatre (Wheeling, West Virginia): The Capitol Theatre (also known as the Capitol Music Hall) is the largest theatre in West Virginia and a landmark building in the national historic district of downtown Wheeling.  For many years, it has served as the home of Jamboree USA and the Wheeling Symphony Orchestra.  Jamboree USA, a Saturday night live country music show broadcast on WWVA 1170 AM from 1926 until 1977, was the second-longest running radio show in the United States, second only to the Grand Ole Opry.  The live music show annually drew hundreds of thousands of country music fans to Wheeling, where both local acts and nationally known celebrities such as Johnny Cash, Loretta Lynn, Merle Haggard and Charley Pride would perform.

Countdown (Dutch TV series): The Dutch music show Countdown was a popular music show from 1978 to the early 1990s, broadcast by the (in that time public) broadcasting system Veronica.  It ranked as the top music show in the whole of Europe.  Due to the popularity this show, the career of one of its hosts throughout the entire period, Adam Curry, rose like a star.  Other hosts included Simone Walraven, Jasper Faber, Erik de Zwart and Wessel van Diepen.

Hot Press: Hot Press is a fortnightly music and politics magazine based in Dublin, Ireland, founded in June 1977.  The magazine has been edited since its inception by Niall Stokes.  According to the Audit Bureau of Circulations, it had a circulation of 17,084 during 2014.

I'm a Loner: "I'm a Loner" (외톨이야 ; "Oetoriya") is a song by South Korean pop-rock idol band CNBLUE.  It is the debut and lead single to the band's first mini-album "Bluetory".  Written by Han Seong-ho and Amen, the punk-rock track was released under FNC Music on January 14, 2010.  Upon its release, CNBLUE achieved immediate commercial success; the song earned the band its first two music show wins on Korean Broadcasting System's (KBS) "Music Bank" and Seoul Broadcasting System's (SBS) "Inkigayo".  Unprecedented at the time, CNBLUE held the record for shortest period between debuting and earning a music show win for four and a half years.  The song also peaked at number two on the Gaon Digital Chart.

George Petros: George Petros (born George Lawrence Petros, January 11, 1955, Chicago, Illinois, United States) is an American art designer, author, editor, interviewer and illustrator.  From 1984 through 1992 he published and edited "EXIT", a punk-inspired art and science fiction magazine he founded with Adam Parfrey and Kim Seltzer.  From 1992 through 2000 he edited and art-directed "Seconds", an all-interview music and culture magazine founded by Steven Blush.  From 2000 through 2005 he was a contributing editor of "Juxtapoz", the low-brow art magazine founded by Robert Williams, and the senior editor of "Propaganda", a goth/industrial music and style magazine founded by Fred H. Berger.

Niall Stokes: Niall Stokes (born Dublin in 1951) is the award-winning editor of the long-running fortnightly Ireland music and political magazine "Hot Press" based in Dublin.  He has edited the magazine since 1977.  He has been a longstanding champion of Irish music, most famously U2 in the late 1970s and throughout the 1980s.  He was involved with The Music Show, an exhibition of the Irish music industry held in the RDS in October 2008.  He was Chairman of the Independent Radio and Television Commission (now the BCI) between 1993 and 1998.  He has written a book called "Into the Heart: The Stories Behind Every U2 Song".

The Music Show (Ireland): The Music Show was an annual event which took place in the RDS, Dublin on the first weekend of October each year.  The event combined live performances, music workshops and talks given by professionals within the music industry.  It had several high-profile sponsors, including "Hot Press", RTÉ 2fm, the "Irish Independent" and the "Sunday Independent".  RTÉ 2fm provided live radio coverage of the event.

Night Shift (Irish TV series): Night Shift is an Irish television music show.  Like its sister show "Day Shift", it was one of Channel 6's Irish shows.  It was launched with the network on Sunday, 30 March 2006.  "Night Shift" was transmitted late at night and sometimes early on weekend mornings.  The show was hosted by Michelle Doherty and featured the alternative music scene.  In 2006, "Night Shift" was voted the favourite music show by "Hot Press" magazine readers.  The last show aired on 31 December 2008.  Channel 6 was replaced by 3e on 1 January 2009.  No reason was given for the ending of the show.  It is rumoured that the show will be coming back in 2017 and will be presented by Dave Fanning but this has not been confirmed/denied by TV3.

Colin Irwin (journalist): Colin Irwin is a British music journalist.  Irwin was an assistant editor of "Melody Maker" in the 1970s and 1980s, before leaving in the summer of 1987 as the magazine moved in a different direction, and editor of "Number One" magazine in the late 1980s and early 1990s.  His book "In Search of the Craic" details a comic journey around Ireland seeking out pub music sessions and became a best-seller in Ireland.  Subsequent books were "In Search Of Albion", a similarly light-hearted journey around English traditions and rituals and "Sing When You're Winning", about the history and culture of terrace songs at football matches.  He's also reviewed music for "The Guardian", "Mojo", "The Daily Telegraph", "The Independent", "fRoots" and Spiral Earth and has been a Mercury Music Prize judge.  He reviews mainly singer-songwriters, folk rock, Celtic and traditional folk albums.  He has also presented music programmes on BBC Radio 2.  His play "The Corridor" has been performed in Surrey and Yorkshire.  Other plays he has written which have been performed on stage in different parts of the country include 'One Of Us Is Lying', 'When Barry Met Cally' and 'I Am The Way'.  In 2017, his theatrical music show, 'She Moved Through The Fair: The Legend Of Margaret Barry', co-written with Irish singer Mary McPartlan was successfully debuted in front of a sell-out audience at Glasgow's Tron Theatre as part of the Celtic Connections festival.

Violeta Riaubiškytė-Tarasovienė: Violeta Riaubiškytė-Tarasovienė (born 25 August 1974) is a famous Lithuanian singer and show host.  She used to be the co-host of a Lithuanian music show "Penktadienio muzikos šou" ("Friday Music Show") alongside Edmundas Kučinskas and also, and the co-host of a music show "Padainuokim!"  ("Let's Sing!")  alongside her husband Vilius Tarasovas.

Question: Which magazine founded in 1977 has sponsored "The Music Show" in Ireland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the magazine was founded."
    },
    "sponsored_event": {
      "type": "string",
      "description": "The name of the event sponsored by the magazine."
    },
    "magazine_location": {
      "type": "string",
      "description": "The city and country where the magazine is based."
    },
    "editor_name": {
      "type": "string",
      "description": "The name of the magazine's editor."
    }
  },
  "required": [
    "magazine_name",
    "founding_year",
    "sponsored_event",
    "magazine_location",
    "editor_name"
  ],
  "additionalProperties": false
}
