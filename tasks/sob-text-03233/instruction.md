{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHotter than Hell Tour (Kiss): Hotter than Hell Tour was the second tour of the American rock band Kiss.  The tour featured songs from their first album and their newly released second album, \"Hotter than Hell\", which was the album that the tour was in support of.  During this tour, the band used fire and the destruction of guitars as part of their show.  The January 31, 1975 show in San Francisco was filmed and later made available for public viewing.\n\nBig Daddy (album): Big Daddy is the tenth studio album by American singer-songwriter John Mellencamp, released in 1989 by Mercury Records.  It was his last album to be released under the name John Cougar Mellencamp, a combination of his real name and his original stage name of Johnny Cougar.  The album peaked at number seven on the \"Billboard\" 200 and contained the singles \"Pop Singer\" and \"Jackie Brown\", which peaked at No. 15 and 48, respectively, on the \"Billboard\" Hot 100.  A re-mastered version of the album was released on May 24, 2005, and contains a bonus acoustic version of \"Jackie Brown\".  Like \"The Lonesome Jubilee\", \"Big Daddy\" is folk-inspired as violins and fiddles (among other instruments) are significantly utilized on a number of tracks.  The album's lyrics largely take a serious tone and the album as a whole is regarded by some as Mellencamp's most reflective.\n\nHouse on Old Lonesome Road (song): \"House on Old Lonesome Road\" is a song written by Dave Gibson and Bernie Nelson, and recorded by American country music artist Conway Twitty.  It was released in August 1989 as the second single and title track from the album \"House on Old Lonesome Road\".  The song reached #19 on the \"Billboard\" Hot Country Singles & Tracks chart.\n\nAnother Way to Die (Disturbed song): \"Another Way to Die\" is a song by American heavy metal band Disturbed, released as the first single from their fifth studio album, \"Asylum\".  Airplay for the single began on the morning of June 14, 2010.  That same day, a lyric video was posted by the band on their official YouTube channel and was released as a digital download on June 15, 2010 via iTunes.  On August 31, 2010, an excerpt of the song played in a newly released second trailer for the 2011 Mortal Kombat game.\n\nRoddy Hart: Roddy Hart is a Scottish singer–songwriter from Glasgow.  He has released three solo records – \"Bookmarks\", \"Sign Language\" and \"Road of Bones\" – and one EP \"The Dylan EP\" (with Irish artist Gemma Hayes).  Hart now releases albums with his band The Lonesome Fire, the first of which was \"Roddy Hart & The Lonesome Fire\" produced by Patti Smith and Morrissey producer Danton Supple.  Released in late 2013 the album was nominated for the Scottish Album of the Year Award in April 2014.  Their second album - Swithering - was co-produced by Paul Savage (Mogwai, Emma Pollock, Admiral Fallow) and released in late 2016.  The band made their American network TV debut on The Late Late Show with Craig Ferguson on 17 February 2014 and proved so popular they were invited back the following week to perform a week long residency on the show.\n\nSibel Alaş: Sibel Alaş is a Turkish pop music singer.  She was born on 13 February 1973 in İzmit.  She graduated from American Culture and Literature Department in İstanbul University.  Her first hit was 'Adam' (Man) from her album of the same name in 1995.  She was both vocalist and dancer of Yonca Evcimik before solo career.  She released second album, Fem (Not opened rose in Turkish or short of female in English) in 1996.  She broke music career after releasing Çocuk (\"Child\" in Turkish) albüm in 1998 due to marrying with Zeki Aköz, who is her manager in 1996 and her disease, Aneurysm.  She released fourth album, \"Carpe Diem\" (\"Seize the day\" in Latin), in 2006.\n\nAnadilim Aşk: Anadilim Aşk (English: My Native Language is Love ) is Işın Karaca's debut album, it was released at 2001 with Power Records label.  All the songs are written by Sezen Aksu, except two of them co-written by Ali İlyas and Sezen Aksu.  The first video became \"Tutunamadım\".  The second video is shot for \"Başka Bahar\", which become very successful in music charts of Turkey.  After this success in Turkey, the song is chosen to represent Turkey in OGAE in 2002.  However, it became the last without getting any points in the contest.  The third video is shot for \"Aramıza Yollar\" by Lebanese director Waleed Nassif.  This video is the first video in High Definition format in Turkey.  Famous Turkish actor Toprak Sergen also starred in the video.  The fourth video is shot for \"Doğum Günün Kutlu Olsun Oğlum\", but it was not aired due to conflicts with her company.  The album sold-out quickly and released second time with addition of \"Tutunamadım Remix\".  In 2006, the album re-released with SM Gold label.\n\nCharlie, the Lonesome Cougar: Charlie, the Lonesome Cougar is a 1967 Walt Disney Productions adventure family film released by Buena Vista Distribution Company.  It was filmed at the Weyerhauser Mill in Enumclaw, Washington.\n\nMulan (1998 film): Mulan is a 1998 American animated musical action comedy-drama film produced by Walt Disney Feature Animation for Walt Disney Pictures.  It is based on the Chinese legend of Hua Mulan, and was Disney's 36th animated feature.  It was directed by Tony Bancroft and Barry Cook, with story by Robert D. San Souci and screenplay by Rita Hsiao, Philip LaZebnik, Chris Sanders, Eugenia Bostwick-Singer, and Raymond Singer.  Ming-Na, Eddie Murphy, Miguel Ferrer and B. D. Wong star in the English version, while Jackie Chan provided the voice of Captain Li Shang for the Chinese dubs of the film.  The film's plot takes place during the Han dynasty, where Fa Mulan, daughter of aged warrior Fa Zhou, impersonates a man to take her father's place during a general conscription to counter a Hun invasion.\n\nThe Lonesome Jubilee: The Lonesome Jubilee is the ninth studio album by American singer-songwriter John Mellencamp, credited as John Cougar Mellencamp.  The album was released by Mercury Records on August 24, 1987 (see 1987 in music).  Four singles were released from the album, the first two in 1987 and the last two in 1988.\n\nQuestion: What was released second Charlie, the Lonesome Cougar or Mulan?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comparison_entities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"release_year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"release_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"second_released_entity_name\": {\n      \"type\": \"string\"\n    },\n    \"release_year_difference_years\": {\n      \"type\": \"integer\"\n    }\n  },\n  \"required\": [\n    \"comparison_entities\",\n    \"second_released_entity_name\",\n    \"release_year_difference_years\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comparison_entities": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "release_year": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "release_year"
          ],
          "additionalProperties": false
        }
      },
      "second_released_entity_name": {
        "type": "string"
      },
      "release_year_difference_years": {
        "type": "integer"
      }
    },
    "required": [
      "comparison_entities",
      "second_released_entity_name",
      "release_year_difference_years"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
