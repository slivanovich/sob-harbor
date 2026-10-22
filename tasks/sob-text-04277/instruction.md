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
Love Remains the Same (song): "Love Remains the Same" is a song by British artist Gavin Rossdale.  It was released in May 2008 as the lead single from his album "WANDERlust".  It entered the "Billboard" Hot 100 at #76 and peaked at #27.  It unexpectedly became Rossdale's first Top-40 hit in the United States since 1995 when his former band Bush scored hits with "Comedown" and "Glycerine."  It has since become more successful than Gavin's biggest hits with Bush from the mid-1990s and is now his most successful track.

Love and Death: The Murder of Kurt Cobain: Love and Death: The Murder of Kurt Cobain, published by Simon & Schuster, is a collaborative investigative journalism book written by Ian Halperin and Max Wallace purporting to show that rock star Kurt Cobain, believed to have committed suicide, was in fact murdered, possibly at the behest of his wife Courtney Love.  It is a follow-up to the authors' 1998 bestseller on the same subject, "Who Killed Kurt Cobain?" .  The book is based on 30 hours of revealing audiotaped conversations, exclusively obtained by the authors, between Courtney Love's private investigator, Tom Grant, and her and Cobain's entertainment attorney, Rosemary Carroll, who both dispute the official finding of suicide and believe Cobain was in fact murdered.

Kurt Cobain: Montage of Heck: Kurt Cobain: Montage of Heck (also billed as Cobain: Montage of Heck) is a 2015 documentary film about Nirvana lead singer Kurt Cobain.  The film was directed by Brett Morgen and premiered at the 2015 Sundance Film Festival.  It received a limited theatrical release worldwide and premiered on television in the United States on HBO on April 24, 2015.  The documentary chronicles the life of Kurt Cobain from his birth in Aberdeen, Washington in 1967, through his troubled early family life and teenage years and rise to fame as front man of Nirvana, up to his death in April 1994 in Seattle at the age of 27.

Suicide of Kurt Cobain: On April 8, 1994, Kurt Cobain, the lead singer of the grunge band Nirvana, was found dead at his home, located at 171 Lake Washington Boulevard East in Seattle, Washington.  Forensic analysis at the time determined he had killed himself on April 5.  The Seattle Police Department incident report states: "Kurt Cobain was found with a shotgun across his body, had a visible head wound and there was a suicide note discovered nearby."  The King County Medical Examiner noted puncture wounds on the inside of both the right and left elbow.  Prior to his death, Cobain had checked out of a drug rehabilitation facility and had been reported as suicidal by his wife Courtney Love.

Teen Spirit: The Tribute to Kurt Cobain: Teen Spirit: The Tribute to Kurt Cobain is a documentary about Nirvana band leader Kurt Cobain.  Released in September 1996 it is significant as the first unofficial Kurt Cobain or Nirvana documentary to be available as a home video.

Gavin Rossdale: Gavin McGregor Rossdale (born 30 October 1965) is an English musician and actor, and the lead singer and rhythm guitarist of the rock band Bush.  He helped form Bush in 1992; upon its separation in 2002, he became the lead singer and guitarist for Institute, and later began a solo career.  When performing solo, Rossdale plays songs from his musical libraries.  He was ranked at 100 in the "Top 100 Heavy Metal Vocalists" by "Hit Parader".  In 2013 Rossdale received the British Academy's Ivor Novello Award for International Achievement.  In 2017, Rossdale became a coach on ITV's "The Voice UK".

Kurt Cobain: About a Son: Kurt Cobain About a Son is a documentary about Kurt Cobain that debuted at the 2006 Toronto International Film Festival.  It is directed by AJ Schnack.  It was produced by Sidetrack Films.  It features audio of interviews between Cobain and journalist Michael Azerrad done for the book "", set over ambient cinematography of the places which Kurt Cobain called his home, mainly Aberdeen, Olympia, and Seattle.  The film played at numerous film festivals, and was nominated for the 2007 Independent Spirit's Truer than Fiction Award.  The DVD, which was released by Shout!  Factory in February 2008, includes bonus interviews and commentary by Michael Azerrad and A.J. Schnack.  Shout!  Factory also put out the documentary's first Blu-ray edition on October 6, 2009.

Last Days (2005 film): Last Days is a 2005 American drama film directed, produced and written by Gus Van Sant.  It is a fictionalized account of the last days of a musician, loosely based on Kurt Cobain.  It was released to theaters in the United States on July 22, 2005 and was produced by HBO.  The film stars Michael Pitt as the character Blake, based on Kurt Cobain.  Lukas Haas, Asia Argento, Scott Patrick Green and Thadeus A. Thomas also star in the film.  This is the first film from Picturehouse, a joint venture between Time Warner's New Line Cinema and HBO Films subsidiaries to release art house, independent, foreign, and documentary films.  The film received mixed reviews from critics.  Though meant to be based on Kurt Cobain, it contradicts the factual evidence of Cobain's final days.

Kurt Cobain Memorial Park: Kurt Cobain Memorial Park, also called Kurt Cobain Landing, is the first official, full-scale memorial to Kurt Cobain in his hometown of Aberdeen, Washington.  A welcome sign to the city, placed in 2005, more than ten years after Cobain's death, obliquely says "come as you are" but does not mention him by name and was the first official recognition of Cobain.  The park, initially built in Felony Flats on city-owned land near his Aberdeen home in 2011, and maintained by local volunteers as Kurt Cobain Landing, was adopted by the city of Aberdeen in 2015, 20 years after his death.  As recently as 2011, a motion not to rename the adjacent Young Street Bridge after Cobain was applauded at a city council meeting.

Kurt Cobain: Kurt Donald Cobain (February 20, 1967 – April 5, 1994) was an American musician, artist, singer, songwriter, guitarist and poet.  Born in Aberdeen, Washington, Cobain formed the band Nirvana with Krist Novoselic in 1987 and established it as part of the Seattle music scene and grunge genre.  Nirvana's debut album "Bleach" was released on the independent record label Sub Pop in 1989.

Question: Who worked on TV more in 2017, Kurt Cobain or Gavin Rossdale?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_who_worked_on_tv": {
      "type": "string",
      "description": "The name of the person who worked on TV in the specified year."
    },
    "year_of_activity": {
      "type": "integer",
      "description": "The year the TV activity took place."
    },
    "tv_show_details": {
      "type": "object",
      "properties": {
        "show_name": {
          "type": "string",
          "description": "The name of the TV show."
        },
        "role": {
          "type": "string",
          "description": "The role the person had on the TV show."
        },
        "channel": {
          "type": "string",
          "description": "The TV channel the show aired on."
        }
      },
      "required": [
        "show_name",
        "role",
        "channel"
      ],
      "additionalProperties": false
    },
    "comparison_outcome": {
      "type": "string",
      "description": "A statement indicating who worked on TV more based on the context."
    }
  },
  "required": [
    "person_who_worked_on_tv",
    "year_of_activity",
    "tv_show_details",
    "comparison_outcome"
  ],
  "additionalProperties": false
}
