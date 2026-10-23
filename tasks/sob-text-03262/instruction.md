{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGreatest Hits/Every Mile a Memory 2003–2008: Greatest Hits/Every Mile a Memory 2003–2008 is the first greatest hits album of country music singer Dierks Bentley.  It was released May 6, 2008 on Capitol Nashville.  His fourth album for Capitol Nashville, it includes his ten singles from his first three albums: 2003's \"Dierks Bentley\", 2005's \"Modern Day Drifter\", and 2006's \"Long Trip Alone\".  Two songs were newly recorded for this compilation: \"Sweet and Wild\" (a duet with Sarah Buxton) and \"With the Band\".  Also included here are live recordings of the album cuts \"So So Long\" (originally included on \"Modern Day Drifter\") and \"Wish It Would Break\" (originally included on \"Dierks Bentley\"), as well as live renditions of his singles \"Come a Little Closer\", \"Lot of Leavin' Left to Do\" and \"Free and Easy (Down the Road I Go)\".\n\nWaves (band): Waves was a New Zealand folk rock band that recorded a top-selling self-titled album in 1975 before disbanding in 1977.  Its lineup emerged from an acoustic trio, Rosewood, which originally included Geoff Chunn, who later joined Split Enz.  Despite making only sporadic live appearances—one of which was a double billing shared with Split Enz—their singles gained major airplay on Auckland radio and the \"Waves\" album reached No.7 on the New Zealand album charts, later becoming a sought-after collector's item.\n\nJames Reyne Live 99: Live 99 is a live album by Australian singer songwriter James Reyne.  The album was recorded in 1999, during the promotional tour of the album \"Design for Living\".  The album was originally included as a bonus disc on the limited edition of that album.  Following Reyne receiving the Medal of the Order of Australia (OAM) in 2014, the album was re-issued as a separate album.\n\n70 Volt Parade: 70 Volt Parade was Trey Anastasio's backing band in 2005, formed after the breakup of Phish in August of the previous year.  After writing and recording new material in late 2004 and early 2005, Anastasio began auditioning various musicians for his next project.  This band essentially replaced Anastasio's first backup band that was together in different forms from 1999 to 2004.  70 Volt Parade originally included Peter Chwazik on bass (later replaced by Tony Hall), Skeeto Valdez on drums (later replaced by Raymond Weber), Les Hall on guitar and keyboards, and Ray Paczkowski also on keyboards.  In 2006, with Les Hall out of the lineup, and a new musical focus for Anastasio, the 70 Volt Parade name was dropped.  \n\nList of Wolfmother members: Wolfmother are an Australian hard rock band from Sydney, New South Wales.  Formed in 2000, the band originally included vocalist and guitarist Andrew Stockdale, bassist and keyboardist Chris Ross, and drummer Myles Heskett, the three of whom had been jamming together for a number of years before the band's first public performance in 2004.  The group released their self-titled debut studio album \"Wolfmother\" in Australia in 2005, followed by international releases the following year, the songwriting for which was credited equally to all three band members.  The founding lineup remained until August 2008, when Ross and Heskett left the band due to \"irreconcilable personal and musical differences\".\n\nHappy Ever After (Ricki-Lee Coulter song): \"Happy Ever After\" is a song recorded by Australian singer and songwriter Ricki-Lee Coulter.  It was written by Coulter, David Schuler and Hal Linton.  The song was originally included on the digital extended play (EP) of Coulter's previous single \"All We Need Is Love\".  It was later released on 11 July 2014 as the second single from her fourth studio album, \"Dance in the Rain\".\n\nOutside Looking In: The Best of the Gin Blossoms: Outside Looking In: The Best of the Gin Blossoms is a greatest hits album by pop rock band Gin Blossoms.  It was released in 1999 on A&M Records.  It includes eleven songs from their previous two A&M studio albums, \"New Miserable Experience\" and \"Congratulations… I'm Sorry\".  The remaining three songs are from different sources.  \"Just South of Nowhere\" was originally included on the 1991 EP \"Up and Crumbling\".  The hit single \"Til I Hear It from You\" was originally found on the soundtrack of the 1995 movie \"Empire Records\".  \"Whitewash\" is a previously unreleased 1996 live recording of the song originally included on \"Congratulations… I'm Sorry\".\n\nRobbie Williams: Robert Peter Williams (born 13 February 1974) is an English singer, songwriter and actor.  He was a member of the pop group Take That from 1990 to 1995 and again from 2009 to 2012.  He has also had commercial success as a solo artist.\n\nMorbo (band): Morbo was a Mexican electronica/synthpop/ambient/alternative rock group formed by Juan Carlos Lozano.  Lozano was one of the four founding members of Moenia, which originally included Juan Carlos Lozano as lead vocalist on 1997's debut album 'Moenia' and its 1998 companion remix album 'Moenia Mixes'.  Despite the acclaimed success of 1997's Moenia and 1998's remix album, in itself a risky and previously-unheard of novelty in the Mexican music industry, and due to disagreements between Lozano, Jorge Soto and Alejandro 'Midi' Ortega as to the creative route Moenia should take, Lozano decided to leave Moenia as vocalist with original founding member Alfonso Pichardo returning as lead singer.  Lozano then formed the perhaps less commercial, still synth-oriented, but more guitar-centered Morbo, whose musical vision first came to fruition in 2001's eponymous \"Morbo\".\n\nTake That: Take That are an English pop music group formed in Manchester, England in 1990.  The group currently consists of Gary Barlow, Howard Donald and Mark Owen.  The original line-up also featured Jason Orange and Robbie Williams.  Barlow acts as the group's lead singer and primary songwriter, with Owen and Williams initially providing backing vocals and Donald and Orange serving primarily as dancers.Now though both Owen and Donald act as backing vocals.\n\nQuestion: Take That originally included the singer, songwriter and actor of what nationality as part of the lineup?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music group.\"\n    },\n    \"member_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific member in question.\"\n    },\n    \"member_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The professional roles of the band member.\"\n    },\n    \"member_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the band member.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"member_name\",\n    \"member_roles\",\n    \"member_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the music group."
      },
      "member_name": {
        "type": "string",
        "description": "The name of the specific member in question."
      },
      "member_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The professional roles of the band member."
      },
      "member_nationality": {
        "type": "string",
        "description": "The nationality of the band member."
      }
    },
    "required": [
      "band_name",
      "member_name",
      "member_roles",
      "member_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
