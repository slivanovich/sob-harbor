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
Kenton Showcase: Kenton Showcase is an album by pianist and bandleader Stan Kenton recorded in early 1954 and originally released as two 10 inch LPs on Capitol, one each featuring compositions and arrangements by Bill Holman and Bill Russo, which were combined as a 12-inch LP in 1955.

Stan Kenton Presents Gabe Baltazar: Stan Kenton Presents Gabe Baltazar is an album by Gabe Baltazar.  It was the last recording by Stan Kenton's Creative World Records label prior to Kenton's death on August 25, 1979.  It was also the last of the "Stan Kenton presents..." series of albums (Bill Holman, Bill Russo, Bob Cooper, etc.); this recording presents the talent of the alto saxophonist and former Kenton band member Gabe Baltazar.  Though never reissued on CD the recording is critically acclaimed and does a good job highlighting the jazz talents of a legendary jazz artist (Baltazar) at the peak of his playing career.  He is backed up by a 17 piece big band on most cuts, a string section is added to one track.

Stan Kenton Plays for Today: Stan Kenton Plays for Today is an album by bandleader Stan Kenton recorded in 1966 by Capitol Records.

Rugolo Plays Kenton: Rugolo Plays Kenton (subtitled The Pete Rugolo Orchestra Plays Compositions Introduced by Stan Kenton) is an album by composer, arranger and conductor Pete Rugolo featuring performances of tunes associated with Stan Kenton recorded in 1958 and first released on the Mercury label.

Kenton Live from the Las Vegas Tropicana: Kenton Live from the Las Vegas Tropicana is a live album by bandleader and pianist Stan Kenton featuring a concert recorded at the Blue Room of the Tropicana Hotel in 1958 and released on the Capitol label.

Stan Kenton Band Clinics: Stan Kenton Band Clinics were summer programs founded by Stan Kenton in 1959.  Kenton conceived the idea out of concern that education of jazz and all its forms were not reaching teenagers who showed signs of interest in it.  He strongly felt that the survival of jazz depended heavily on the ability of leaders and artists in jazz community to educate a younger generation.

Tropicana Las Vegas: Tropicana Las Vegas is a hotel and casino on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Penn National Gaming and is a franchise of Hilton's DoubleTree chain.  It offers 1,467 rooms and a 50000 sqft gaming floor.  Tropicana Las Vegas also has 72000 sqft of convention and exhibit space.

Stan Kenton / Jean Turner: Stan Kenton / Jean Turner (full title "From the Creative World of Stan Kenton Comes the Exciting New Voice of Jean Turner") is an album by the Stan Kenton Orchestra with vocalist Jean Turner recorded in 1963 by Capitol Records.

Cuban Fire!: Cuban Fire!  is an album by Stan Kenton and his orchestra released in 1956 by Capitol Records.  This was Stan Kenton's big band's first full-length recording of Afro-Cuban-styled music.  The LP charted for four weeks in "Billboard" starting on September 15, 1956, peaking at #17.  The concept of the original 1956 recording centers on the "Cuban Fire!"  suite Kenton had commissioned from composer Johnny Richards.  The 1991 CD re-issue is augmented with one extra track from the 1956 sessions and five cuts recorded four years later by the first of Kenton's mellophonium orchestras.

Stan Kenton Plays Chicago: Stan Kenton Plays Chicago is a studio album by American jazz musician Stan Kenton and his orchestra, released on August 17, 1974, by Creative World Records.  Recording sessions for the album took place in Chicago on June 4, 5, 6, 1974.  The sessions are entirely based on the music of modern rock n' roll groups, in contrast to Kenton's earlier work which primarily featured swing with some progressive jazz leanings.

Question: Stan Kenton recorded Kenton Live from the Las Vegas Tropicana located in what town?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album mentioned in the question."
    },
    "venue_name": {
      "type": "string",
      "description": "The name of the venue where the album was recorded."
    },
    "location": {
      "type": "object",
      "properties": {
        "city_or_town": {
          "type": "string",
          "description": "The city or town where the venue is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the venue is located."
        }
      },
      "required": [
        "city_or_town",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_title",
    "venue_name",
    "location"
  ],
  "additionalProperties": false
}
