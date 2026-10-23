{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPonderosa Campground: Ponderosa Campground is a United States Forest Service campground in the high country of Big Sur, on the central coast of California in the Los Padres National Forest.  The campground has 23 sites set in a high valley adjacent to the Nacimiento River, with a canopy of Ponderosa Pine, Oak, Madrone, and California Sycamore trees.  Each site includes a picnic table, fire ring, and pedestal grill.  The campground is on the Nacimiento-Fergusson Road (a famous motorcycling road), approximately 13 miles east of State Route 1 and 20 miles west of the city of Lockwood.\n\nBuddy Brown (musician): Buddy Brown is a traditional American country music singer-songwriter who was discovered as a YouTube sensation.  Brown was born on May 12, 1982 to Dan and Cheryl Brown in Madison, Mississippi, a suburb of Jackson.  When Brown was nine years old, his family decided to relocate to Orlando, Florida for his father’s career.  In 2005, he graduated from Mississippi State with a degree in Psychology.  On October 13, 2009, he released a cover of Easton Corbin’s \"A Little More Country Than That\" that went viral.  A year later, he opened up for country music legend, John Anderson in Wildwood, FL.  On July 4, 2012, he released his first album titled Mason Jar.  His fan base pushed his first full-length CD to No. 34 on the iTunes country chart without a record deal.  March 11, 2014, he released a self-titled EP, Buddy Brown.  On October 14, 2014, Buddy released his second EP, Keepin’ It Country.  This EP reached to No. 12 on the iTunes charts.  In January 2014, Billboard put Keepin’ It Country on their Heat Seekers Albums list.  USA Today published a story on Brown, labeling him as a \"YouTube Sensation.\"  His single \"Takin’ You Huntin’\" landed him a spot on the front page and an online feature in the Clarion Ledger.\n\nIngrid Croce: Ingrid Croce (born April 27, 1947) is an American author, singer-songwriter, and restaurateur.  She is the widow of singer-songwriter Jim Croce and the mother of singer-songwriter A. J. Croce.  Between 1964 and 1971, Ingrid and Jim Croce performed as a duo.  In 1969, Capitol Records released their album, \"Jim & Ingrid Croce\".  Their song, \"Age\", won a country music award in the late 1970s.\n\nSilinder Pardesi: Silinder Pardesi is a Bhangra singer, lyricist, and composer from Coventry, West Midlands, England.  He is the founder and lead singer of the highly acclaimed British Asian Bhangra band ‘The Pardesi Music Machine’.  In 1994 Silinder Pardesi moved onto pastures new and began his solo career.  Over the past 30 years Silinder Pardesi has released over twenty albums and collaborated with an array of artists including Rishi Rich and Neeru Bajwa.\n\nNacimiento Campground: Nacimiento Campground is a United States Forest Service campground in the high country of Big Sur, on the central coast of California in the Los Padres National Forest.  The campground has 8 sites set in a high valley adjacent to the Nacimiento River with a canopy of Oak trees.  Each site includes a picnic table, fire ring, and pedestal grill.  The campground is on the Nacimiento-Fergusson Road (a famous motorcycling road), approximately 11 miles east of State Route 1 and 22 miles west of the city of Lockwood.\n\nFelicity Urquhart: Felicity Ann Urquhart (born 4 May 1976) is an Australian country music singer-songwriter, and a TV and radio presenter.  Her single \"Big Black Cloud\", co-written with Randy Scruggs, reached No. 1 on Country Tracks National Top 30 Singles Chart in 2007.  She has won numerous awards including a Centenary Medal in 2001 \"For service to Australian society through country music\".  Urquhart married musician and producer Glen Hannah in March 2009.  She has been the host of country music show \"Saturday Night Country\" on Australian Broadcasting Corporation Local Radio since March 2010.\n\nRod Black (singer): Rod Black is a Canadian country rock singer-songwriter and the lead singer of hard rock band Jet Black Stare.  In 2014, Black launched a solo career with the release of the single \"Keepin' On\" to country radio.  It peaked at number 22 on the \"Billboard\" Canada Country chart.  Black was nominated at the 2015 Canadian Radio Music Awards for Best New Group or Solo Artist: Country for the song.  Black's second solo single, \"Long Gone\", was released in March 2015.  A music video for the song premiered in May.  At the 2015 British Columbia Country Music Association Awards, Black was nominated for Rising Star.\n\nMLB China Series: The Major League Baseball China Series, or MLB China Series, was two spring training games between the San Diego Padres and Los Angeles Dodgers played in the People's Republic of China.  It marked the first time Major League Baseball teams played in China, part an effort to popularize baseball in that country.  The games were played on March 15 and 16 at the now-demolished Wukesong Baseball Stadium in Beijing.  During the series, both teams visited the Great Wall of China and the Padres held a clinic for the students at Fengtai School.\n\nRosanne Cash discography: The discography of Rosanne Cash, an American singer-songwriter, consists of thirteen studio albums, six compilation albums, one tribute album, and 39 singles.  The daughter of Johnny Cash, Rosanne Cash recorded her self-titled debut album in 1978 under the German label Ariola.  After signing with Columbia Records in 1979, Cash's second studio album \"Right or Wrong\" was released.  Its lead single \"No Memories Hangin' Around\" (a duet with Bobby Bare) reached the Top 20 on the \"Billboard\" Hot Country Songs chart.  Cash's third studio release, \"Seven Year Ache\" (1981) gained major success when the title track peaked at number one on the \"Billboard\" Country chart, followed by \"My Baby Thinks He's a Train\" and \"Blue Moon with a Heartache,\" which also reached the top spot.  The album's follow-up effort, \"Somewhere in the Stars\" (1982) produced two Top 10 hits on the \"Billboard\" chart.  After a 3-year hiatus, Cash issued \"Rhythm & Romance\" in 1985, which reached #1 on the \"Billboard\" Top Country Albums list.  It spawned four Top 10 singles.  This included the number one single, \"I Don't Know Why You Don't Want Me,\" which won the Grammy Award for Best Female Country Vocal Performance in 1986.  Her sixth album, \"King's Record Shop\" was released in 1987.  The album peaked at number six on the country albums chart and certified gold in the United States.  The four singles released from \"King's Record Shop\" all reached number one on the \"Billboard\" Country chart between 1987 and 1988, including a cover of Johnny Cash's \"Tennessee Flat-Top Box.\"\n\nSinger-songwriter: Singer-songwriters are musicians who write, compose, and perform their own musical material, including lyrics and melodies.\n\nQuestion: Singer-songwriter Silinder Padres is from what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the singer-songwriter.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the artist is from.\"\n    },\n    \"origin_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city of origin for the artist.\"\n        },\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The region or county of origin for the artist.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"country_of_origin\",\n    \"origin_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the singer-songwriter."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the artist is from."
      },
      "origin_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city of origin for the artist."
          },
          "region": {
            "type": "string",
            "description": "The region or county of origin for the artist."
          }
        },
        "required": [
          "city",
          "region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "artist_name",
      "country_of_origin",
      "origin_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
