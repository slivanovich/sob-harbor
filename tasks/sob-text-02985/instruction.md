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
Toru Yamashita: Toru Yamashita (山下 亨 , Yamashita Tōru ) (born December 7, 1988 in Osaka), better known by his stage name Toru, is a guitarist and leader in the Japanese rock band ONE OK ROCK.  He was in the hip-hop group HEADS along with Ryota Kohama from ONE OK ROCK before they disbanded in 2002.

One Ok Rock discography: Japanese rock band One Ok Rock has released eight studio albums, two EPs, 22 singles, seven video albums, six cover versions, and 32 music videos.  One Ok Rock was formed in Tokyo, Japan in 2005, currently consists of Takahiro Moriuchi (vocals), Toru Yamashita (guitar/leader), Ryota Kohama (bass), and Tomoya Kanki (drums).

Ryota Kohama: Ryota Kohama (小浜良太 , Kohama Ryōta ) (born 4 September 1989), better known as his stage name Ryota, is a bassist in the Japanese rock band ONE OK ROCK.  He was in the hip-hop group HEADS along with Toru Yamashita from ONE OK ROCK before they disbanded in 2002.

5.....Go: 5...GO is an album by South Korean rock band F.T. Island.  It was released on 13 May 2015.  The album was released to celebrate the band's fifth anniversary in Japan.  The title track "Primavera" is a collaboration with Japanese rock singer Takahiro Moriuchi from One Ok Rock.

Tomoya Kanki: Tomoya Kanki (神吉 智也 , Kanki Tomoya ) (born June 27, 1987 in Hyogo Prefecture, Japan, better known by his stage name Tomoya).  He played drums on ONE OK ROCK indie releases but did not officially join until 2007.  Tomoya came from ESP Musical Academy where he used to be a teacher.  He has the most curious hobbies among the band members and the eldest member of ONE OK ROCK.  He is the one who often updates the ONE OK ROCK blog.

Skyfall (One Ok Rock song): "Skyfall" is a limited CD single by Japanese rock band ONE OK ROCK.  It was released on February 18, 2017 under the A-Sketch label and sold only at venues of the "2017 ONE OK ROCK "Ambitions" Japan Tour".  It was not available at other stores, and sales were limited for each venue.

Into Another (band): Into Another is an American rock band formed in 1990 in New York City.  The original lineup consisted of vocalist Richie Birkenhead (formerly of Underdog and Youth of Today), drummer Drew Thomas (formerly of Bold), bassist Tony Bono (formerly of Whiplash) and guitarist Peter Moses.  Into Another performed their first show at New York's Pyramid Club, supporting White Zombie.  Their song "T.A.I.L." hit #39 on the U.S. Billboard Mainstream Rock Tracks chart in 1996.  The band broke up later that year due to intra-band tensions and a deteriorated relationship with Hollywood Records.  Bassist Tony Bono died in May 2002.

News (band): News, stylized as NEWS, is a four-member Japanese band consisting of Keiichiro Koyama, Takahisa Masuda, Shigeaki Kato and Yuya Tegoshi.  The group's name is an acronym based on the cardinal directions (North, East, West, South).  Formed in 2003 by Johnny Kitagawa as a nine-member group under the label Johnny's Entertainment, NEWS released a promotional single "NEWS Nippon" (News ニッポン , News Japan) , which was used for the World Cup of Volleyball Championships.  In 2004, Takahiro Moriuchi (present-day Taka of One Ok Rock) left the group and the remaining eight members released their debut single, "Kibō: Yell" (希望 ~Yell~ , Hope ~Yell~) , which debuted atop the Oricon charts.

One Ok Rock: One Ok Rock, stylized as ONE OK ROCK (pronounced in Japanese as "one o'clock"), is a Japanese rock band formed in Tokyo, Japan in 2005.  The band currently consists of Takahiro Moriuchi (vocals), Toru Yamashita (guitar/leader), Ryota Kohama (bass), and Tomoya Kanki (drums).

Jinsei×Boku=: Jinsei×Boku= (人生×僕= "Jinsei Kakete Boku wa", lit.  "Life Times Me Equals") is the sixth full-length album by the Japanese rock band, One Ok Rock.  It was released on March 6, 2013 and managed to reach first place on the Oricon weekly chart.  This album brought ONE OK ROCK to worldwide popularity, especially after the first single, "The Beginning", was selected as official soundtrack in the live action adaptation of "Rurouni Kenshin".  The song peaked at the #2 on the "Billboard" Japan Hot 100 and stayed for 45 weeks.  The next single, "Deeper Deeper/Nothing Helps", was featured on the "" ("Nothing Helps") game and used for Suzuki Swift TV commercials ("Deeper Deeper").

Question: Which band formed first, One Ok Rock or Into Another?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string"
          },
          "formation_year": {
            "type": "integer"
          }
        },
        "required": [
          "band_name",
          "formation_year"
        ],
        "additionalProperties": false
      }
    },
    "first_formed_band": {
      "type": "string"
    },
    "first_formed_year": {
      "type": "integer"
    }
  },
  "required": [
    "band_comparison",
    "first_formed_band",
    "first_formed_year"
  ],
  "additionalProperties": false
}
