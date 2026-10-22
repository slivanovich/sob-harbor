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
Look Who's Talking (song): "Look Who's Talking!"  is a song recorded by the Sweden-based musician and producer Dr. Alban.  It was released in February 1994 as the first single from his third studio album "Look Who's Talking".  The dance song was released in 1994 and became a hit reaching the top 10 in almost all European countries, except in France and UK.

Sing Hallelujah (Dr. Alban song): "Sing Hallelujah" is a 1992 song recorded by the Sweden-based musician and producer Dr. Alban.  It was the third single from his second studio album "One Love".  The song was released in 1993 and became a great hit reaching the top 10 in almost all European countries and managing no. 16 in the UK Singles Chart.  After "It's My Life", this was the second Dr Alban's hit which had an international scope.

ToyZ: ToyZ is the second studio album by German glam rock band Cinema Bizarre.  After their debut album, "Final Attraction" was a moderate hit, they began working on their second studio album.  The first single from the album is called "I Came 2 Party," featuring Space Cowboy.  Originally the first single was to be a song entitled "My Obsession," however this release was canceled due to fans taking advantage of a mistake on the part of iTunes.  When the single was put up two days too early, fans were able to download the track and the song quickly spread, resulting in an announcement from the band that "I Came 2 Party" would be released instead.  The album release date was also postponed until mid-August.  "My Obsession" was later released as the second single from the album.

Let the Beat Go On: "Let the Beat Go On" is a song recorded by the Sweden-based musician and producer Dr. Alban.  It was released in August 1994 as the third single from his third studio album "Look Who's Talking".  The chorus is sung by Nana Hedin and Jessica Folcker.  This Eurodance song was released at the end of 1994 and was charted in many European countries, peaking at number 21 on the European Hot 100 Singles.

Colour the World: "Colour the World" is a song by German production group Sash! .  It was released in 1999 via Mighty label.  This record is the fourth and final single from their second studio album "Life Goes On".  Dr. Alban performed the vocal part.  The song was a famous hit in a number of European countries and reached number 15 in the UK Singles chart.

Nuclear Furniture: Nuclear Furniture is an album by the American rock band Jefferson Starship.  It was the last album released by the band until 1998's "Windows of Heaven", and was also the final album by the band before the departure of leader Paul Kantner and the formation of the offshoot band Starship.  It was released in 1984 and spawned the Top 40 single "No Way Out", which was also the first single by any incarnation of the band to hit #1 on the Mainstream Rock Tracks chart.  The album itself reached #28.  Produced by Ron Nevison, the album was arranged with the help of Peter Wolf, who had worked with Grace Slick on her solo album, "Software".  Wolf also contributed keyboard and synthesizer work to the album, although not an official part of the band.  Peter Wolf (not the singer of the same name) and Ina Wolf also wrote the single "No Way Out", the first of many songs penned by the husband and wife duo that took "Starship" in a more commercial direction.  As the album was being recorded, Paul Kantner became frustrated with the album's direction.  Before the sessions came to a close, he stole the master tapes, put them in his car and drove around San Francisco for a few days and wouldn't bring them back until the band mixed the album in a way more to his liking.  Shortly after the release of the album, Kantner left the band, and he only appears in the first promotional video produced, "No Way Out."  After the departure of Kantner the band lost the "Jefferson" moniker and morphed into Starship; there would not be another studio album released under the Jefferson Starship name until after Kantner reformed the band in 1992.

Angel &amp; Khriz: Angel & Khriz are a Puerto Rican reggaeton duo, consisting of Angel Rivera Guzmán (Angel) and Christian Colón Rolon (Khriz).  Their high-impact performance on this first time out recording led to their sponsorship by Hector "El Father".  Through that relationship the duo recorded their first single, "Cazando Voy," which reached platinum status and earned them the reputation as "the MVP's of the year."  In 2004, they signed with MVP Records and toured extensively throughout South and Central America.  The success of their debut recording, Los MVP's, garnered the attention and an eventual distribution with Universal's Machete Music, a label targeting the ever-growing urban Latino audience.  Appearances in many U.S. cities to receptive crowds has earned the duo a reputation as one of reggaeton's most popular duos.  In 2005, their debut studio album "Los MVP" was released and featured the hit singles "Ven Baílalo" and "De Cazeria".  The album was certified Platinum by the United States Recording Industry Association of America (RIAA) and a special edition was released the following year.  The special edition of "Los MVP" featured their two singles "Fua" and "De Lao a Lao".  Performances at high-visibility events like opening Premios Juventud and closing the 2006 Latin Billboard Awards alongside Tito "El Bambino" and Wisin & Yandel continued to increase these budding artists' recognition and potential.  Almost three years later, in 2008, their second studio album, Showtime was released.  Singles featured on the album were "La Vecina" and "Na De Na".  This album was released by Machete Music.  Two years later, Da' Take Over, the duo's third studio album was released.  It featured the hit singles "Ayer La Vi" & "Me Enamoré".

It's My Life (Dr. Alban song): "It's My Life" is a song by the Nigerian-Swedish artist Dr. Alban.  It was released in April 1992 as the first single from his second studio album "One Love".

This Time I'm Free: "This Time I'm Free" is a song recorded by the Sweden-based musician and producer Dr. Alban.  It was released in 1995 as the first single from his fourth studio album "Born in Africa".  The chorus is sung by Martina Edoff.  This song charted in many European countries, peaking at number 2 in Finland, number 3 in Sweden and number 11 in Norway.  The black-and-white music video starts with the message "last year in Africa alone more than 12.000 people were held prisoner without charges - amnesty 1995".  In the end the message "freedom is a right and not a privilege" appear.

How Do You Do!: "How Do You Do!"  is a pop rock song by Swedish pop duo Roxette.  It was released as the lead single from their fourth studio album "Tourism" on 3 July 1992.  The song was a commercial success upon release, topping the national singles charts in Norway and Spain.  It also peaked at number two in several countries, including Austria, Belgium, Finland, Germany, the Netherlands, Sweden and Switzerland.  It was held off the top spot in many of these territories by Dr. Alban's "It's My Life".  The single was backed by several remixes created by Swedish production duo BomKrash, which consisted of Jacob Hellner and Carl-Michael Herlöfsson.

Question: Which duo backed the first single from Dr. Alban's second studio album released in April 1992?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album."
        },
        "type": {
          "type": "string",
          "description": "The type of album (e.g., studio album)."
        },
        "number": {
          "type": "integer",
          "description": "The sequential number of the album for the artist."
        }
      },
      "required": [
        "title",
        "type",
        "number"
      ],
      "additionalProperties": false
    },
    "single_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the single."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the single was released."
        },
        "release_month": {
          "type": "string",
          "description": "The month the single was released."
        },
        "order_in_album": {
          "type": "string",
          "description": "The order of the single from the album (e.g., 'first single')."
        }
      },
      "required": [
        "title",
        "release_year",
        "release_month",
        "order_in_album"
      ],
      "additionalProperties": false
    },
    "backing_duo_identified": {
      "type": "boolean",
      "description": "Indicates if a backing duo for this specific single was identified in the context."
    },
    "backing_duo_name": {
      "type": "string",
      "description": "The name of the duo that backed the single, if identified."
    }
  },
  "required": [
    "artist_name",
    "album_details",
    "single_details",
    "backing_duo_identified"
  ],
  "additionalProperties": false
}
