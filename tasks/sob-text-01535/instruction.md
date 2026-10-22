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
Richard Hines: Richard Hines (died 1851) was a Congressional Representative from North Carolina; born in Tarboro, North Carolina, birth date unknown; studied law; was admitted to the bar in 1816 and practiced in Raleigh, North Carolina; member of the State house of commons, 1824; elected to the Nineteenth Congress (March 4, 1825-March 3, 1827); unsuccessful candidate for reelection in 1826 to the Twentieth Congress; resumed the practice of law in Raleigh, N.C., and died there November 20, 1851; interment in the Old City Cemetery, Raleigh, N.C.

Congleton (UK Parliament constituency): Congleton is a constituency in Cheshire, represented in the House of Commons of the UK Parliament since 2010 by Fiona Bruce of the Conservative Party.

Thomas D. Singleton: Thomas Day Singleton (Birth date unknown – November 25, 1833) was a United States Representative from South Carolina.  He was born near Kingstree, South Carolina but his birth date is unknown.

Hippolytus (archbishop of Gniezno): Hippolytus or Hipolit (died c. 1027) was an early medieval archbishop of Gniezno.  His place and date of birth date are unknown but the medieval historian Jan Długosz claims that he was of noble birth and a Roman citizen.  Modern scholars generally agree that he was not Polish.

Aviation Maintenance Technician Day: Aviation Maintenance Technician Day is a United States day of recognition, observed on May 24, that recognizes the efforts of aviation maintenance professionals as well as the achievements of Charles Edward Taylor, the man who built the engine used to power the airplane of the Wright Brothers.  The date May 24 was selected to honor the birth date of Taylor.  The day of recognition is currently observed by 45 states in the United States.  On May 24, 2007, a United States House of Representatives resolution supporting the goals and ideals of a National Aviation Maintenance Technician Day was introduced.  Congressman Bob Filner of California was the sponsor of the resolution.  On April 30, 2008 the resolution passed by a voice vote.

Samuel Dickens: Samuel Dickens (died 1840) was a Congressional Representative from North Carolina; born near Roxboro in Person County, North Carolina, birth date unknown.  He was a member of the North Carolina state house of commons from 1813 to 1815, and in 1818.  He was elected as a Democratic-Republican to the Fourteenth Congress to fill the vacancy caused by the death of United States Representative Richard Stanford (December 2, 1816 – March 3, 1817).  He moved to Madison County, Tennessee in 1820 and died there in 1840.

John Taylor (14th Congress): John Taylor was a United States Representative from South Carolina.  His birth date is unknown.  Taylor was a member of the South Carolina House of Representatives, 1802–1805.  He was elected as a Republican to the Fourteenth Congress (March 4, 1815 – March 3, 1817) but was an unsuccessful candidate for reelection to the Fifteenth Congress in 1816 and for election to the Seventeenth Congress in 1820.  His death date is unknown.

Fiona Bruce (politician): Fiona Claire Bruce (born 26 March 1957) is a British Conservative Party politician who is the Member of Parliament for Congleton, elected at the 2010 general election, and then again in 2015.

Astro Boy (2003 TV series): Astro Boy (アストロボーイ・鉄腕アトム , Asutoro Bōi: Tetsuwan Atomu , lit.  "Astro Boy: Mighty Atom") is a remake of the 1960s anime series of the same name created by Osamu Tezuka, which was produced by his company, Tezuka Productions, Sony Pictures Entertainment Japan, Dentsu, and Fuji Television network.  It was also shown on Animax, who have broadcast the series across its respective networks worldwide, including Japan, Southeast Asia, South Asia, East Asia, and other regions.  It was created to celebrate the birth date of Atom/Astro Boy (as well as the 40th anniversary of the original TV series).  Under the original English name (instead of "Mighty Atom"), it kept the same classic art style as the original manga and anime, but was revisioned and modernized with more lush, high-quality, near-theatrical animation and visuals.  It combined the playfulness of the early anime with the darker, more serious and dramatic Science fiction themes of the manga and the 1980 series.  The anime broadcast in Japan on the same date as Atom's/Astro's birth in the manga (April 6, 2003) across Animax and Fuji Television.  It was directed by Kazuya Konaka and written by Chiaki J. Konaka at the beginning of the series.  Other writers included were Keiichi Hasegawa, Sadayuki Murai, Ai Ohta, Hirotoshi Kobayashi, Kenji Konuta, and Marc Handler, who was also executive story editor.

Tovma Artsruni: Tovma Artsruni (Armenian: Թովմա Արծրունի ; also known in English-language historiography as Thomas Artsruni; precise birth date and date of death unknown) was a ninth-century to tenth-century Armenian historian and author of the "History of the House of Artsrunik" (Armenian: Պատմություն Արծրունյաց Տան ).  Contrary to the given title, the four-volume work not only relates the history of Artsruni royal family, of which he was a member of, and its origins near Lake Van but also comprehensively covers the history of Armenia.

Question: What was the birth date of the 2010 electee to a Cheshire constituency in the House of Commons?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person elected."
    },
    "constituency_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the constituency."
        },
        "location_county": {
          "type": "string",
          "description": "The county where the constituency is located."
        }
      },
      "required": [
        "name",
        "location_county"
      ],
      "additionalProperties": false
    },
    "election_year": {
      "type": "integer",
      "description": "The year the person was elected."
    },
    "birth_date": {
      "type": "string",
      "description": "The full birth date of the person."
    },
    "birth_date_components": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The birth year."
        },
        "month": {
          "type": "string",
          "description": "The birth month."
        },
        "day": {
          "type": "integer",
          "description": "The birth day of the month."
        }
      },
      "required": [
        "year",
        "month",
        "day"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "constituency_details",
    "election_year",
    "birth_date",
    "birth_date_components"
  ],
  "additionalProperties": false
}
