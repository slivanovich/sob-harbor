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
Les McKeown: Leslie Richard McKeown (born 12 November 1955) is a Scottish pop singer who was the lead singer of the Bay City Rollers during their most successful period.

Riot on Redchurch Street: Riot On Redchurch Street is an London-based musical drama directed by Trevor Miller and starring Sam Hazeldine, Alysson Paradis, Jesse Birdsall and Les McKeown.  The soundtrack includes four original songs written by Siobhan Fahey and is scheduled for international release, Summer 2012.

Takahiro Moriuchi: Takahiro Moriuchi (森内 貴寛 , Moriuchi Takahiro , born April 17, 1988 in Tokyo) , known professionally as Taka, is the lead vocalist of the Japanese rock band ONE OK ROCK.  Prior to this, he was in the boyband NEWS throughout 2003 until he left the group and the agency.  Taka is the lyricist and composer of his band.

One Ok Rock: One Ok Rock, stylized as ONE OK ROCK (pronounced in Japanese as "one o'clock"), is a Japanese rock band formed in Tokyo, Japan in 2005.  The band currently consists of Takahiro Moriuchi (vocals), Toru Yamashita (guitar/leader), Ryota Kohama (bass), and Tomoya Kanki (drums).

Don't Let the Music Die: "Don't Let the Music Die" is a pop ballad by the Bay City Rollers from their 1977 album "It's a Game".  The tune, written by Eric Faulkner and Stuart Wood, and featuring a lead vocal by Les McKeown, is a slow, dramatic ballad with a heavily-orchestrated arrangement and melancholy feel.  It was released as a 7" double A-side vinyl single (with "The Way I Feel Tonight") in Japan, but failed to make the charts.

Where Will I Be Now: "Where Will I Be Now" is a pop single by the Bay City Rollers from their 1978 album "Strangers in the Wind".  The tune, written by British songwriter Chris East and featuring a lead vocal by Les McKeown, is an uptempo song with a heavily-orchestrated disco-style arrangement.  It was released as a 7" vinyl single in Japan, Germany, and the United States.

5.....Go: 5...GO is an album by South Korean rock band F.T. Island.  It was released on 13 May 2015.  The album was released to celebrate the band's fifth anniversary in Japan.  The title track "Primavera" is a collaboration with Japanese rock singer Takahiro Moriuchi from One Ok Rock.

One Ok Rock discography: Japanese rock band One Ok Rock has released eight studio albums, two EPs, 22 singles, seven video albums, six cover versions, and 32 music videos.  One Ok Rock was formed in Tokyo, Japan in 2005, currently consists of Takahiro Moriuchi (vocals), Toru Yamashita (guitar/leader), Ryota Kohama (bass), and Tomoya Kanki (drums).

News (band): News, stylized as NEWS, is a four-member Japanese band consisting of Keiichiro Koyama, Takahisa Masuda, Shigeaki Kato and Yuya Tegoshi.  The group's name is an acronym based on the cardinal directions (North, East, West, South).  Formed in 2003 by Johnny Kitagawa as a nine-member group under the label Johnny's Entertainment, NEWS released a promotional single "NEWS Nippon" (News ニッポン , News Japan) , which was used for the World Cup of Volleyball Championships.  In 2004, Takahiro Moriuchi (present-day Taka of One Ok Rock) left the group and the remaining eight members released their debut single, "Kibō: Yell" (希望 ~Yell~ , Hope ~Yell~) , which debuted atop the Oricon charts.

It's a Game (Les McKeown album): It's A Game is an album by Les McKeown, released in 1989 with four corresponding singles released.  After the album, Dieter Bohlen released a cover of Blue System's song Nobody Makes Me Crazy (Like You Do) as a single, which did not appear on the album.

Question: Are Les McKeown and Takahiro Moriuchi from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_from_same_country": {
      "type": "boolean",
      "description": "Indicates whether both individuals are from the same country."
    },
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin for the first person."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin for the second person."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why they are or are not from the same country."
    }
  },
  "required": [
    "are_from_same_country",
    "person_1",
    "person_2",
    "reasoning"
  ],
  "additionalProperties": false
}
