{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRestless Heart: Restless Heart is an American country music band established in 1984.  The band's longest-lasting lineup has consisted of Larry Stewart (lead vocals), John Dittrich (drums, background vocals), Paul Gregg (bass guitar, background vocals), Dave Innis (piano, keyboards, rhythm guitar, background vocals), and Greg Jennings (lead guitar, mandolin, background vocals).  Verlon Thompson was the band's original lead singer, but he was replaced by Stewart before the band signed to RCA Records Nashville.  Stewart departed for a solo career in 1992; during this time, Innis, Gregg, and Dittrich alternated as lead vocalists, until Innis also left.  The band was on hiatus from 1994 to 1998.  During this hiatus, Dittrich briefly recorded as one-third of The Buffalo Club, and Jennings joined Vince Gill's road band.  Stewart, Gregg, Dittrich, and Jennings reunited briefly in 1998 to record new material for a greatest hits album; they, along with Innis, reunited again in 2004, and this lineup has remained ever since.\n\nLove the One You're With: \"Love the One You're With\" is a song by folk rocker Stephen Stills.  It was released as the lead single from his debut self-titled studio album in November 1970.  The song, inspired by a remark Stills heard from musician Billy Preston, became his biggest hit single, peaking at No. 14 on the \"Billboard\" Hot 100 in early 1971.  David Crosby and Graham Nash, Stills' fellow members of Crosby, Stills & Nash, provide background vocals on the song.  The song was also covered by a number of artists, including The Isley Brothers, Bucks Fizz, and Luther Vandross.\n\nCountry Strong (song): \"Country Strong\" is a song written by Jennifer Hanson, Tony Martin and Mark Nesler.  It was recorded by singer Britni Hoover in 2007 for her debut album under the same name.  Then it was recorded again by actress Gwyneth Paltrow for the movie \"Country Strong\" in which Paltrow stars.  Vince Gill and Patty Griffin also provide background vocals for the song.  The song is included on the movie's soundtrack that was released on October 26, 2010.\n\nTake It Like a Man (Michelle Wright song): \"Take It Like a Man\" is a song written by Tony Haselden, and recorded by Canadian country music artist Michelle Wright.  It was released in February 1992 as the first single from Wright's album \"Now and Then\".  The song became Wright's first Number One on the Canadian \"RPM\" Country Tracks charts that year.  It was also her only top 10 hit on the \"Billboard\" Hot Country Singles & Tracks chart in the United States.  Country singer Lari White is featured on background vocals.\n\nDark Fantasy (song): \"Dark Fantasy\" is a song by American hip hop recording artist and producer Kanye West from his fifth studio album, \"My Beautiful Dark Twisted Fantasy\" (2010).  The song serves as the opening track of the album, and was written by West, Ernest Wilson, Jeff Bhasker, Mike Dean and Robert Diggs.  It features an opening narrative delivered by rapper Nicki Minaj, and singers Teyana Taylor and Justin Vernon contribute to the song's hook and provide background vocals.  The track is built around a sample of \"In High Places\" by Mike Oldfield (sung by Jon Anderson).  The song introduces several of the themes presented on the album and features numerous pop culture references, a gospel-inspired production style, and piano-driven composition.  The song received acclaim from music critics, who praised the song as a strong opener to \"My Beautiful Dark Twisted Fantasy\", complimenting West's vocal delivery and the song's production.\n\nLari White: Lari Michele White ( ; born May 13, 1965) is an American country music artist and actress.  She first gained national attention in 1988 as a winner on \"You Can Be a Star\", a talent competition which aired on The Nashville Network.  A recording contract with RCA Records Nashville followed a year later, producing three studio albums, a greatest hits package, and several chart singles, with three of her singles having reached Top Ten: \"That's My Baby\" and \"That's How You Know (When You're In Love)\" at No. 10, and \"Now I Know\" at No. 5.  A fourth studio album was released in 1998 on Lyric Street Records, followed by two more releases on White's own label, Skinny White Girl.  Overall, White has charted 12 times on the \"Billboard\" country music charts.\n\nCary Brothers: Cary Brothers is an American indie rock singer-songwriter originally from Nashville, Tennessee, United States.  After moving to Los Angeles and becoming a regular performer at the influential Hotel Cafe venue, Brothers first gained national attention with his song \"Blue Eyes\" on the Platinum-selling, Grammy-winning \"Garden State\" soundtrack.  As an independent artist, he has since toured worldwide, released two full-length records, and become one of the most-licensed artists in film and television.  In the electronic dance music world, Brothers has collaborated with Tiësto on a club remix of his song \"Ride\" and an original song for Tiesto's album \"Kaleidoscope\", and he co-wrote and sang the title tracks for the Cosmic Gate releases \"Wake Your Mind\" and \"Start to Feel\".\n\nBilly Dean: William Harold Dean Jr. (born April 2, 1962) is an American country music singer and songwriter.  Billy Dean first gained national attention after appearing on the television talent competition \"Star Search\".  Active as a recording artist since 1990, he has recorded a total of eight studio albums (of which the first three have been certified gold by the RIAA) and a greatest hits package which is also certified gold.  His studio albums have accounted for more than 20 hit singles on the \"Billboard\" country charts, including 11 Top Ten hits.  In 2000, he had a Billboard Number one as a guest artist along with Allison Kraus on Kenny Rogers' \"Buy Me a Rose\", and had two Number Ones on the \"RPM\" country charts in Canada.\n\nWhole Lotta Holes: \"Whole Lotta Holes\" is a song written by Jon Vezner and Don Henry, and recorded by American country music artist Kathy Mattea.  It was released in July 1991 as the second single from the album \"Time Passes By\".  The song reached #18 on the \"Billboard\" Hot Country Singles & Tracks chart.  The Roches provide background vocals.\n\nLittle Texas (band): Little Texas is an American country music band founded in Nashville, Tennessee, in 1988 by Tim Rushlow (lead vocals, rhythm guitar), Brady Seals (lead and background vocals, guitars, keyboards), Del Gray (drums), Porter Howell (lead guitar, background vocals), Dwayne O'Brien (rhythm guitar, lead and background vocals), and Duane Propes (bass guitar, background vocals).  Signed to Warner Bros.  Records in 1991, Little Texas released its debut album \"First Time for Everything\" that year.  The album's lead off single, \"Some Guys Have All the Love\", reached a peak of No. 8 on the \"Billboard\" Hot Country Singles & Tracks charts.  Little Texas continued to produce hit singles throughout the mid-1990s, including the Number One single \"My Love\" and six more top ten hits.  Their debut album earned a gold certification from the Recording Industry Association of America (RIAA), while 1993's \"Big Time\" was certified double platinum and 1994's \"Kick a Little\" was certified platinum.\n\nQuestion: What county music artist first gained national attention as a winner on \"You Can Be a Star\" and wen on to provide background vocals in 199 on the 1992 release of the song \"Take It Like a Man\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the country music artist.\"\n    },\n    \"attention_source\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"competition_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the talent competition where the artist first gained national attention.\"\n        },\n        \"year_gained_attention\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the artist first gained national attention from the competition.\"\n        }\n      },\n      \"required\": [\n        \"competition_name\",\n        \"year_gained_attention\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"background_vocal_contribution\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"song_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song on which the artist provided background vocals.\"\n        },\n        \"song_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the song.\"\n        },\n        \"main_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The main artist who recorded the song.\"\n        }\n      },\n      \"required\": [\n        \"song_title\",\n        \"song_release_year\",\n        \"main_artist\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"attention_source\",\n    \"background_vocal_contribution\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The full name of the country music artist."
      },
      "attention_source": {
        "type": "object",
        "properties": {
          "competition_name": {
            "type": "string",
            "description": "The name of the talent competition where the artist first gained national attention."
          },
          "year_gained_attention": {
            "type": "integer",
            "description": "The year the artist first gained national attention from the competition."
          }
        },
        "required": [
          "competition_name",
          "year_gained_attention"
        ],
        "additionalProperties": false
      },
      "background_vocal_contribution": {
        "type": "object",
        "properties": {
          "song_title": {
            "type": "string",
            "description": "The title of the song on which the artist provided background vocals."
          },
          "song_release_year": {
            "type": "integer",
            "description": "The release year of the song."
          },
          "main_artist": {
            "type": "string",
            "description": "The main artist who recorded the song."
          }
        },
        "required": [
          "song_title",
          "song_release_year",
          "main_artist"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "artist_name",
      "attention_source",
      "background_vocal_contribution"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
