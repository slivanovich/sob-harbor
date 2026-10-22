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
New York Raining: "New York Raining" is a song from American rapper Charles Hamilton featuring vocals from British singer Rita Ora.  The track was released on March 18, 2015.  The track appears on the deluxe edition of the for Fox's TV series "Empire.

Hot Right Now: "Hot Right Now" is a single by British drum and bass producer DJ Fresh, released as the second single from his third studio album, "Nextlevelism".  British singer Rita Ora features on the single as the main vocalist.  The song also features as a bonus track on Ora's debut album, "Ora".  Released on 12 February 2012, the single debuted at the top of UK Singles Chart.  The Official Charts Company confirmed "Hot Right Now" as the UK's first ever drum and bass number one.

I Will Never Let You Down: "I Will Never Let You Down" is a song by British singer Rita Ora, released on 31 March 2014, through Roc Nation and Columbia Records.  The song debuted at number one on the UK Singles Chart, making it Ora's fourth overall UK number-one single (and third as a solo artist) within three years.

Body on Me (Rita Ora song): "Body on Me" is a song by British singer Rita Ora, featuring guest vocals by American recording artist Chris Brown.  The song was released on 7 August 2015.

Ed Sheeran: Edward Christopher Sheeran, {'1': ", '2': ", '3': ", '4': "} (born 17 February 1991) is an English singer-songwriter, guitarist, and record producer.  He was born in Halifax, West Yorkshire, and raised in Framlingham, Suffolk.  He attended the Academy of Contemporary Music in Guildford, Surrey, as an undergraduate from the age of 18 in 2009.  In early 2011, Sheeran independently released the extended play, "No. 5 Collaborations Project".  After signing with Asylum Records, his debut album, "+" (read as "plus"), was released on 9 September 2011 and has since been certified seven-times platinum in the UK.  The album contains the single "The A Team", which earned him the Ivor Novello Award for Best Song Musically and Lyrically.  In 2012, Sheeran won the Brit Awards for Best British Male Solo Artist and British Breakthrough Act.

Poison (Rita Ora song): "Poison" is a song by British singer Rita Ora.  The song was released on 18 May 2015, peaking at number three in the UK.

J Farell: Justin Farell Alamar (born April 23, 1982), better known as J Farell, is an American music producer from Cherry Hill, NJ.  He graduated from Rutgers University where he was first exposed to music production.  J Farell broke into the recording industry in 2010 and is best known for producing remixes for artists such as Kreayshawn, J. Cole, Roscoe Dash, Gorilla Zoe, Hyper Crush, Gotye, Driicky Graham, Rita Ora, Wiz Khalifa, Eva Simons, Bruno Mars, Ed Sheeran, and more.  He received his first official placement with Entertainment One for the remix of Gorilla Zoe's song "Twisted".  In March 2011, it debuted on Philadelphia's radio station Wired 96.5.  This remix was digitally released on iTunes by Atlantic Records on May 23, 2011.  J Farell first received widespread recognition on August 29, 2011 when his remix of Kreayshawn's single "Gucci Gucci" went viral on YouTube and gained over 7 million views in under 12 hours.  A week later, the video charted at #7 on YouTube's Top 100 Music Videos.  In 2013, Ed Sheeran spoke about J Farell's remix of his song The A Team with Ralphie Aversa on WPLJ's The Ralphie Radio Show.  J Farell began working on a collaboration project with Dj Beatstreet and Dj Suraci.  In May 2015, the trio formed the group Money Drop and, two months later, released their first collaborative single entitled Everything on Fleek.  With the help of Interscope Records in July 2015, J Farell landed the official remix of Good For You by Selena Gomez featuring A$AP Rocky.  In November 2015, J Farell collaborated with singer/songwriter Todd Carey and created a refreshed, doo-wop style remix of Todd's single "OMG".  On December 4, 2015, the official OMG Remix was released to a positive response on social media.  His work is noted by an announcer or a giggling woman saying the "J Farell" tagline in most of his recent music.

Coming Home (Sigma and Rita Ora song): "Coming Home" is a song by British drum and bass duo Sigma and British singer Rita Ora.  The song was released on 6 November 2015.

Sing (Ed Sheeran song): "Sing" is a song by English singer-songwriter, Ed Sheeran.  It was written by Sheeran and Pharrell Williams, who also produced it and provided uncredited background vocals.  The song was released on 7 April 2014, serving as the lead single from Sheeran's second studio album, "×" (2014).  The song became Sheeran's first UK number-one single and also topped the charts in Australia, New Zealand and Ireland.  It also peaked at No. 13 on the US "Billboard" Hot 100.

Your Song (Rita Ora song): "Your Song" is a song by British singer Rita Ora, with uncredited backing vocals from Ed Sheeran.  It was released on 26 May 2017, through Atlantic Records and Warner Music Group.  The song peaked at number 7 in the United Kingdom, becoming her ninth top-ten song overall.  The single also reached the top 20 in more than fifteen countries, including Belgium, Germany, Switzerland, Australia and New Zealand.

Question: "Your Song" is a song by British singer Rita Ora, with uncredited backing vocals from Ed Sheeran, is an English singer-songwriter, guitarist, and record producer, he attended which organization, in Guildford, Surrey? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "organization_attended": {
      "type": "string",
      "description": "The name of the organization the artist attended."
    },
    "organization_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the organization is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the organization is located."
        }
      },
      "required": [
        "city",
        "county"
      ],
      "additionalProperties": false
    },
    "attendance_role": {
      "type": "string",
      "description": "The role or status of the artist during attendance (e.g., undergraduate)."
    },
    "attendance_start_year": {
      "type": "integer",
      "description": "The year the artist started attending the organization."
    }
  },
  "required": [
    "artist_name",
    "organization_attended",
    "organization_location",
    "attendance_role",
    "attendance_start_year"
  ],
  "additionalProperties": false
}
