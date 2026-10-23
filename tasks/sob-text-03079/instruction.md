{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHand of Doom (Black Sabbath song): \"Hand of Doom\" is a song by the English heavy metal band Black Sabbath, originally appearing as the sixth song on their second album \"Paranoid\", released in 1970.  It has been performed in many of Black Sabbath's live concerts.  The lyrics were written by Geezer Butler while the music was written by the four members.  \"Hand of Doom\" is accepted as one of the best songs on the album by many fans of Black Sabbath.  It is the second longest song on the album behind \"War Pigs\".\n\nThe Black Sabbath Story, Vol. 2: The Black Sabbath Story Vol.  2 - 1978-1992 is a documentary video about the biography of the heavy metal band Black Sabbath.  It is the follow-up to \"The Black Sabbath Story Vol.  1 - 1970-1978\", and it's about their story from the leaving of Ozzy Osbourne to the recording of Dehumanizer, discussing the line-up changes Black Sabbath experienced during the period between 1978 and 1992.  In addition to comments by the storic members Geezer Butler and Tony Iommi, there are interviews with other people that have been in the band, like Ronnie James Dio, Ian Gillan, Cozy Powell and Vinny Appice.  There are also live clips and video clips of various songs.  In 2002 a DVD Version has been released, with 19 min of never-seen footage, not included in the previous VHS Version.\n\nThe End Tour: The End Tour was the farewell tour of the heavy metal band Black Sabbath, featuring founding members Ozzy Osbourne, Tony Iommi and Geezer Butler.  The tour concluded Sabbath's 40+ year career.  The final show was February 4, 2017, in their home city of Birmingham, UK.\n\nBlack Sabbath (album): Black Sabbath is the debut album by the English rock band Black Sabbath.  Released on 13 February 1970 in the United Kingdom and on 1 June 1970 in the United States, the album reached number eight on the UK Albums Charts and number 23 on the \"Billboard\" charts.  Although it was poorly received by most contemporary music critics at the time, \"Black Sabbath\" is now widely considered the first heavy metal album.\n\nBorn Again Tour 1983: The Born Again Tour 1983 was a global concert tour by in support of Black Sabbath's \"Born Again\" album.  Both the album and the tour were the only ones of Black Sabbath's to feature former Deep Purple frontman Ian Gillan on lead vocals.  Ex-Electric Light Orchestra drummer Bev Bevan was hired to replace Bill Ward, who had returned to the band for the recording of the album after a two-year hiatus, for the tour.  This was the final tour to feature original Black Sabbath bassist Geezer Butler until 1992's \"Dehumanizer\" tour.\n\nBorn Again (Black Sabbath album): Born Again is the eleventh studio album by English heavy metal band Black Sabbath, released in August 1983.  It is the only album the group recorded with lead vocalist Ian Gillan, best known for his work with Deep Purple.  It was also the last Black Sabbath album for nine years to feature original bassist Geezer Butler, and drummer Bill Ward, until he played the studio tracks on their 1998 live album \"Reunion\".  The album has received mixed to negative reviews from critics, but it was a commercial success upon its 1983 release, reaching No. 4 in the UK charts.  The album also hit the top 40 in the United States.\n\nSabbath Bloody Sabbath (song): \"Sabbath Bloody Sabbath\" is a song by British heavy metal band Black Sabbath.  It is the title track of the band's fifth album \"Sabbath Bloody Sabbath\".  It was released on the album in 1973.  The song is the opening track on the album.\n\nThe Collection (Black Sabbath album): The Collection is a compilation album released by English heavy metal band Black Sabbath in 1992.  The album was released on the label Castle, who released two CD versions of this album in the UK, both with the same cover art and songs.  The album includes greatest songs of Black Sabbath with Ozzy Osbourne prior to his dismissal in 1979, from the eponymous album to \"Never Say Die! \".  The album has 15 tracks, two from \"Black Sabbath\", two from \"Paranoid\", one from \"Master of Reality\", two from \"Black Sabbath Vol.  4\", two from \"Sabbath Bloody Sabbath\", two from \"Sabotage\", two from \"Technical Ecstasy\" and two from \"Never Say Die! \".\n\nThe End (EP): The End is an EP by English heavy metal band Black Sabbath, released on January 20, 2016.  It was only available at dates on their final tour The End.  The EP's first four tracks are unreleased songs from the \"13\" sessions, and the rest were recorded live on that album's tour in 2013–2014.\n\nOzzy Osbourne: John Michael \"Ozzy\" Osbourne (born 3 December 1948) is an English singer, songwriter, and actor.  He rose to prominence in the early 1970s as the lead vocalist of the heavy metal band Black Sabbath.  He was fired from Black Sabbath in 1979 and went on to have a successful solo career, releasing 11 studio albums, the first seven of which were all awarded multi-platinum certifications in the US.  Osbourne has since reunited with Black Sabbath on several occasions, recording the album \"13\" in 2013.  His longevity and success have earned him the informal title of \"Godfather of Heavy Metal\".\n\nQuestion: The End is an EP by English heavy metal band Black Sabbath, released on which date, it was only available at dates on their final tour The End Tour, the farewell tour of the heavy metal band Black Sabbath?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ep_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the EP.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that released the EP.\"\n    },\n    \"release_date\": {\n      \"type\": \"string\",\n      \"description\": \"The release date of the EP.\"\n    },\n    \"associated_tour\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the tour the EP was associated with.\"\n    },\n    \"tour_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the associated tour.\"\n    }\n  },\n  \"required\": [\n    \"ep_name\",\n    \"band_name\",\n    \"release_date\",\n    \"associated_tour\",\n    \"tour_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ep_name": {
        "type": "string",
        "description": "The name of the EP."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that released the EP."
      },
      "release_date": {
        "type": "string",
        "description": "The release date of the EP."
      },
      "associated_tour": {
        "type": "string",
        "description": "The name of the tour the EP was associated with."
      },
      "tour_description": {
        "type": "string",
        "description": "A description of the associated tour."
      }
    },
    "required": [
      "ep_name",
      "band_name",
      "release_date",
      "associated_tour",
      "tour_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
