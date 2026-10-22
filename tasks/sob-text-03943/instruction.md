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
Pearly-Dewdrops' Drops: "Pearly-Dewdrops' Drops" is a single by Scottish post-punk band Cocteau Twins, taken from their 1984 EP "The Spangle Maker".  The song was written by Cocteau Twins, and recorded at Rooster Studios in London.  It was their highest-charting single, peaking at No. 29 on the UK Singles Chart and No. 1 on the UK Indie Chart.

Headstones (band): Headstones are a Canadian punk-influenced alternative rock band that began in 1987 in Kingston and were active until 2003, subsequently reforming in 2011.  The band consists of vocalist Hugh Dillon, guitarist Trent Carr, and bassist Tim White.  They frequently sold out at small and mid-sized venues and were known for their high energy live shows, particularly the antics of Dillon, who interacted with his audience in a variety of ways more rock less super shock.  The songwriting tackled many serious and controversial topics.

Stars and Topsoil: Stars and Topsoil – A Collection (1982–1990) is a compilation album by the Scottish band Cocteau Twins, released on the 4AD label in October 2000.  The album featured tracks released during the group's time on 4AD between 1982 and 1990, covering every Cocteau Twins album from "Garlands" through "Heaven or Las Vegas".  The collection peaked at No. 63 on the UK Albums Chart.

The Box Set (Cocteau Twins): The Box Set (also known as Cocteau Twins Singles Collection ) is a 1991 collection of EPs by the Scottish band Cocteau Twins.  It collects their non-album releases up until that time.  It also contains a bonus disc including songs from throughout their history which have not been otherwise released on Cocteau Twins releases.

It'll End in Tears: It'll End in Tears is the first album released by 4AD collective This Mortal Coil, an umbrella title for a loose grouping of guest musicians and vocalists brought together by label boss Ivo Watts-Russell.  The album was released on 1 October 1984, and reached #38 on the UK Albums Chart.  It features many of the artists on the 4AD roster at the time, including Cocteau Twins, Colourbox, and Dead Can Dance; as well as key post-punk figure Howard Devoto, who sang "Holocaust", one of two covers of songs from the "Third/Sister Lovers" album by Big Star.  The other Alex Chilton-penned track, album opener "Kangaroo", was released as a single to promote the album.  Two key songs were performed by Elizabeth Fraser of Cocteau Twins, including Tim Buckley's "Song to the Siren", which reached #66 on the UK Charts when released as This Mortal Coil's debut single a year before the album.  The song remained on the UK Indie Chart for almost two years.  Fraser also performed on "Another Day" by Roy Harper.  4AD would go on to release two further albums under the name of This Mortal Coil: "Filigree & Shadow" (1986) and "Blood" (1991).

Cocteau Twins: Cocteau Twins were a Scottish rock band active from 1979 to 1997.  The original members were singer Elizabeth Fraser, guitarist Robin Guthrie, and bassist Will Heggie, who was replaced by multi-instrumentalist Simon Raymonde in 1983.  The group has earned much critical praise for its distinctive ethereal sound and the distinctive soprano vocals of Fraser, which often abandoned recognizable language altogether.  They were associated with the UK label 4AD for much of their career.

Four-Calendar Café: Four-Calendar Café is the seventh album by Scottish band Cocteau Twins.  It was originally released on 18 October 1993 on Fontana.  It distinguishes itself from the rest of the Twins' catalogue in two major areas: The sound is much more pop-oriented and less ambient than previous works, and vocalist Elizabeth Fraser's lyrics are more intelligible than usual.

Will Heggie: Will Heggie is a Scottish musician.  He co-founded the Cocteau Twins in 1980 with Robin Guthrie, and served as the bassist for them until 1983.  Immediately after departing the Cocteau Twins, he helped form Lowlife and played bass with them from 1983–1997.

The Moon and the Melodies: The Moon and the Melodies was an album resulting from the collaboration of the Scottish group Cocteau Twins and the American composer Harold Budd.  It was released by 4AD in November 1986.  The name "Cocteau Twins" did not appear on the release, which instead credited the band's three members (Elizabeth Fraser, Robin Guthrie and Simon Raymonde) and Budd individually.  The album's heavily treated guitar sounds and euphoric vocalising could be heard in the group's other work from the same period, such as the EP "Echoes in a Shallow Bay" and the album "Victorialand".  Budd's stylistic piano tonalities and phrasing on this project were echoed in his solo album "Lovely Thunder", released in the same year.  A version of the track "Memory Gongs" was released on "Lovely Thunder" as "Flowered Knife Shadows" and was dedicated to Raymonde.

Lullabies to Violaine: Lullabies to Violaine is a Cocteau Twins boxset released by 4AD Records in October 2005.  Comprising four CDs, the boxset collects the tracks from every Cocteau Twins EP from "Lullabies" to "Violaine".  It was also released as two separate double CD packs.

Question: who has had more members, Cocteau Twins or  Headstones

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first band being compared."
        },
        "member_count": {
          "type": "integer",
          "description": "The total number of distinct members the band has had."
        },
        "members": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the distinct members of the band."
        }
      },
      "required": [
        "name",
        "member_count",
        "members"
      ],
      "additionalProperties": false
    },
    "second_band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second band being compared."
        },
        "member_count": {
          "type": "integer",
          "description": "The total number of distinct members the band has had."
        },
        "members": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the distinct members of the band."
        }
      },
      "required": [
        "name",
        "member_count",
        "members"
      ],
      "additionalProperties": false
    },
    "band_with_more_members": {
      "type": "string",
      "description": "The name of the band that has had more members, or 'Equal' if both had the same number."
    },
    "more_members_count": {
      "type": "integer",
      "description": "The number of members for the band identified as having more, or the common count if 'Equal'."
    }
  },
  "required": [
    "first_band",
    "second_band",
    "band_with_more_members",
    "more_members_count"
  ],
  "additionalProperties": false
}
