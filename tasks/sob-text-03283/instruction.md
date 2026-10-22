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
Babymetal: Babymetal (stylized as BABYMETAL) is a Japanese metal idol band.  Their line-up consists of Suzuka Nakamoto as "Su-metal", Yui Mizuno as "Yuimetal", and Moa Kikuchi as "Moametal".  The concept of the group is a fusion of the heavy metal and Japanese idol genres.  The three teenage girls and their band are managed by the Amuse talent agency.  Their vocals are backed by heavy metal instrumentation played by the Kami Band.  Babymetal released their eponymous debut album in February 2014.  Their second album "Metal Resistance" was released worldwide on  01, 2016 (2016--) .

Chicago XXVI: Live in Concert: Chicago XXVI: Live in Concert is a live album by the American band Chicago, their twenty-sixth album overall, released in 1999.  Their second live album to be released in the US, it was Chicago's first of the sort since 1971's "Chicago at Carnegie Hall" and 1972's "Live in Japan", though the band had released commercial VHS tapes of two concerts in the early 1990s.

Anika Moa discography: The discography of Anika Moa, a New Zealand pop singer-songwriter, consists of four studio albums, twelve solo singles, three charity singles, and fifteen music videos. Moa was a finalist in the 1998 national Smokefreerockquest, and was subsequently signed to record labels Warner Music and Atlantic Records.  She recorded her debut album, "Thinking Room", in New York City, which was released in 2001.  It focussed on the genre of pop, with elements of folk music, and hosted the singles "Youthful", "Good in My Head", "Falling in Love Again" and "Mother".  "Falling in Love Again" provided Moa with her first chart success in Australia, reaching number sixty-one on the Australian Singles Chart.  "Thinking Room" topped the New Zealand Albums Chart and was certified double platinum by the Recording Industry Association of New Zealand (RIANZ). " Stolen Hill", Moa's second studio effort, was released in 2005 and featured a darker tone, with Moa incorporating influences of rhythm and blues and swing music.  The album was certified gold by the RIANZ.

Live: Legend 1999 &amp; 1997 Apocalypse: Live: Legend 1999 & 1997 Apocalypse (stylized as "LIVE～LEGEND 1999&1997 APOCALYPSE") is the second live video release by the Japanese band Babymetal.  It contains two concerts.

Sasha, Benny y Erik: Sasha, Benny y Erik are a pop band from Mexico.  The group was formed by 3 former members of the Mexican pop group Timbiriche, consisting of Sasha Sokol, Benny Ibarra and Erik Rubin who are close friends in real life.  With much anticipation by their fans, Sasha, Benny and Erik released the live album "".  The project has enjoyed much success with a national tour that started in late 2012 and has continued through much of 2014.  The album has been certified triple platinum + gold in Mexico for sales exceeding 210,000 copies.  Originally, the band performed 2 concerts at the National Auditorium in Mexico City in April 2013, but due to demand, they did two more concerts at the venue in September of that same year.  In 2013, they released En Vivo desde el Auditorio Nacional, which went gold a few days after its release.  At the end of 2013, the album was officially recognized by AMPROFON as the second best-selling album in Mexico that year (after the album "Confidencias" by Alejandro Fernandez).  In late 2014, Sasha, Benny y Erik will release their first studio album "Vuelta al Sol" and release "Esta Noche" as their first single.  Next singles were "Todo tiene su lugar" ,"Japi" and "Punto de partida".  In 2015, they performed at National Auditorium twice ( two concerts in May and other two in November).  In early 2016, they will release a new live album with new songs and hits, performed with several guests.  First single "Lo Siento" featuring Pepe Aguilar, was released on February 19 in iTunes.  In May, "Entre Amigos" was released and the band announced the end of the project in December.  The album was certified as Gold some weeks later and they startred a farewell tour, which final performance will be on December 31.

MJ &amp; Friends: MJ & Friends were concerts held by American recording artist Michael Jackson in 1999, with numerous other performers as well.  The purpose of the tour was to raise funds for children in Kosovo, Africa and elsewhere.  Jackson gave two concerts during the tour.  The first one took place in Seoul, South Korea on June 25 and the second one was in Munich, Germany.  In an interview with Thomas Gottshalk, Jackson was joined by long-time collaborator Slash during the two concerts.

Anesthetize (Porcupine Tree): Anesthetize is the second live DVD by progressive rock band Porcupine Tree, released on 20 May 2010.  The Blu-ray edition was released on 15 June.  It is filmed in high definition and taken from two concerts given by Porcupine Tree at Tilburg, Netherlands on 15 and 16 October, at the end of the "Fear of a Blank Planet" tour in 2008.  The film is directed and edited by Lasse Hoile and the audio track is mixed in stereo and 5.1 Surround by Steven Wilson.

Suzuka Nakamoto: Suzuka Nakamoto (中元 すず香 , Nakamoto Suzuka , born December 20, 1997) , known by her stage names Suzuka and Su-metal, is a Japanese idol.  She is best known as the lead vocalist of three-piece kawaii metal band Babymetal.  She is represented by the talent agency Amuse, Inc. and has been a member of three musical groups formed by the company: Karen Girl's, Sakura Gakuin, and Babymetal.

0110111 – Quantum Physics &amp; A Horseshoe: 0110111 – Quantum Physics & A Horseshoe is the second live album and first live video album by Berlin-based indie punk band Bonaparte.  It was released by Staatsakt label in 2011, and contains live songs recorded while touring for their second album, "My Horse Likes You".  The album was released on DVD, double vinyl and digital download.

God Is in the T.V.: God Is in the T.V. is the second live video album by American rock band Marilyn Manson, released on November 2, 1999 on VHS, documenting the Beautiful Monsters Tour and Rock Is Dead Tour.  It features all 13 music videos the band spawned between July 1994 and November 1999 in reverse chronology, including uncensored bonus footage from the production of "The Dope Show" music video, as well as footage culled from various concerts across the world alongside backstage and behind-the-scenes clips.

Question: Who's line-up consists of Suzuka Nakamoto as "Su-metal", Yui Mizuno as "Yuimetal", and Moa Kikuchi as "Moametal", who released their second live video that contained two concerts ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "members": {
      "type": "array",
      "description": "List of band members with their real and stage names.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The real name of the band member."
          },
          "stage_name": {
            "type": "string",
            "description": "The stage name of the band member."
          }
        },
        "required": [
          "name",
          "stage_name"
        ],
        "additionalProperties": false
      }
    },
    "live_video_release": {
      "type": "object",
      "description": "Details about the band's live video release.",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the live video release."
        },
        "release_order": {
          "type": "integer",
          "description": "The sequential number of this live video release (e.g., 2 for second)."
        },
        "number_of_concerts": {
          "type": "integer",
          "description": "The total number of concerts featured in the live video release."
        }
      },
      "required": [
        "title",
        "release_order",
        "number_of_concerts"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "members",
    "live_video_release"
  ],
  "additionalProperties": false
}
