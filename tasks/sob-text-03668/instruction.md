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
That Was Yesterday (Foreigner song): "That Was Yesterday" was the second single taken from the album "Agent Provocateur" by the band Foreigner.  This song was available in four versions, as a remixed single, a very popular extended remix, an orchestral version, and the original mix.  The song was written by Lou Gramm and Mick Jones, and the B-side "Two Different Worlds" is also of note for being the first solo-written Lou Gramm song to appear on a single.  The single reached number 12 on the "Billboard" Hot 100 chart, and also reached #4 on the Billboard Mainstream Rock chart and #24 on the Adult Contemporary chart.  It also reached the Top 40 in the UK (#28), the Netherlands (#19), Switzerland (#29) and Germany (#31).

Waiting for a Girl Like You: "Waiting for a Girl Like You" is a 1981 power ballad by the British-American rock band Foreigner.  The distinctive synthesizer theme was performed by the then-little-known Thomas Dolby.

Reaction to Action: "Reaction to Action" was the third single taken from the album "Agent Provocateur" by the band Foreigner, in the U.S. only.  This song was remixed for this release.  The song was written by Lou Gramm and Mick Jones, and the b-side, "She's Too Tough", a rockin' Elvis Presley-type song, is also featured on the European single release of "Growing Up the Hard Way".

Where the Wild Things Are (Agent Provocateur album): Where the Wild Things Are (Agent Provocateur album)

Growing Up the Hard Way: "Growing Up the Hard Way" was the fourth single taken from the album "Agent Provocateur" by the band Foreigner, and subsequently released only in Europe in May, 1985.  The song was written by Lou Gramm & Mick Jones, and the b-side, "She's Too Tough", a rockin' Elvis Presley-type song, is also featured on the American single release of "Reaction To Action".

Down on Love: "Down on Love" was the fifth and final single taken from the album "Agent Provocateur" by the band Foreigner, and primarily released only in the U.S. in September 1985.

Head Games (album): Head Games is the third studio album by the British-American rock band Foreigner, released on 10 September 1979 by Atlantic Records.  Recorded at Atlantic Studios in New York, with additional recording and whole mixing taking place at Cherokee Studios in Los Angeles, it was the only Foreigner album co-produced by Roy Thomas Baker, best known for working on Queen's classic albums.  It marked the first appearance of new bass guitarist Rick Wills who replaced Ed Gagliardi, and was the last album with founding members Ian McDonald and Al Greenwood who would leave the band after the recording.

I Want to Know What Love Is: "I Want to Know What Love Is" is a power ballad by the British-American rock band Foreigner.  It was released in November 1984 as the lead single from their fifth album, "Agent Provocateur".  The song hit number one in both the United Kingdom and the United States and is the group's biggest hit to date.  It remains one of the band's best-known songs and most enduring radio hits, charting in the top 25 in 2000, 2001, and 2002 on the "Billboard" Hot Adult Contemporary Recurrents chart.  "I Want to Know What Love Is" has continued to garner critical acclaim, and is listed as one of Rolling Stone Magazine's greatest songs of all time at #479.  The song is also featured in a number of films.

Agent Provocateur (album): Agent Provocateur is the fifth studio album by the British-American rock band Foreigner, released on December 7, 1984.  The album was the band's first and only number one album in the United Kingdom, and it reached the top 5 in the United States.  Although album sales were lower than their previous work in the U.S., it contains the band's biggest hit single, "I Want to Know What Love Is", which is their only #1 single in the UK and the U.S., staying at the top spot for three and two weeks respectively.  The follow-up single, "That Was Yesterday", also proved to be a sizeable hit, peaking at #12 in the U.S.  The album was certified Platinum in the UK by the BPI, and triple Platinum in the U.S. by the RIAA.

Foreigner (Foreigner album): Foreigner is the debut studio album by the British-American rock band Foreigner, released on March 8, 1977.  It spun off a barrage of hit singles, including "Feels Like the First Time", "Cold as Ice" and "Long, Long Way from Home".  It also features album tracks such as "Headknocker" and "Starrider", the latter of which features a rare lead vocal from lead guitarist and co-founder Mick Jones.  The first attempt at mixing the album was done at Sarm Studios, London, but dissatisfied with result the album was re-mixed at Atlantic Recording Studios by Mick Jones, Ian McDonald and Jimmy Douglass.

Question: What power ballad by the British-American rock band Foreigner was also in the Agent Provocateur album?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the power ballad song."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album the song is from."
    },
    "song_release_year": {
      "type": "integer",
      "description": "The year the song was released as a single."
    },
    "album_release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "chart_performance": {
      "type": "array",
      "description": "A list of chart performances for the song.",
      "items": {
        "type": "object",
        "properties": {
          "chart_name": {
            "type": "string",
            "description": "The name of the chart (e.g., United Kingdom, United States)."
          },
          "peak_position": {
            "type": "integer",
            "description": "The highest position reached on the chart."
          }
        },
        "required": [
          "chart_name",
          "peak_position"
        ],
        "additionalProperties": false
      }
    },
    "is_biggest_hit": {
      "type": "boolean",
      "description": "Indicates if this is the group's biggest hit to date."
    },
    "is_lead_single": {
      "type": "boolean",
      "description": "Indicates if the song was the lead single from the album."
    }
  },
  "required": [
    "song_title",
    "album_name",
    "song_release_year",
    "album_release_year",
    "chart_performance",
    "is_biggest_hit",
    "is_lead_single"
  ],
  "additionalProperties": false
}
