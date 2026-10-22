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
Billy Kinsley: William Ellis "Billy" Kinsley (born 28 November 1946, Anfield, Liverpool) is an English musician with The Merseybeats until 1966 (although he temporarily left the band both to form the Kinsleys) The group disbanded in January 1966 to resurface as a duo called The Merseys.  They recorded The McCoys' song "Sorrow" (also covered by David Bowie on his 1973 cover album, "Pin Ups") with the band before embarking on a solo career, where he recorded "Bye Bye Baby".  This song is not to be confused with a Four Seasons track of a similar title, but rather a typical Merseybeat tune.  Followed by the singles: "Annabella", and "You Make My Day".  Kinsley also undertook session work, which most notably included working for Apple Records (alongside George Harrison on at least one song for Jackie Lomax).  He also worked on the popular "Top of the Pops" record series, which contained anonymous cover versions of recent and current hit singles.  During this time he worked with fellow musician friend, Jimmy Campbell, and formed the band Rockin' Horse.  They recorded one album and toured England and Europe as the backing band for Chuck Berry.

Philippine Sports Stadium: The Philippine Sports Stadium, also known as New Era University (NEU) Stadium, is a football and track stadium at Ciudad de Victoria, a 140-hectare tourism enterprise zone in the towns of Bocaue and Santa Maria in Bulacan, Philippines.  The stadium was built right next to the Philippine Arena, the world's largest indoor arena.  The stadium is the largest football stadium in the Philippines with a maximum seating capacity of 25,000.  Its seating capacity is more than twice the seating capacity of the Rizal Memorial Stadium, the national stadium of the country which has a seating capacity of 12,000.

Los Angeles Memorial Coliseum: The Los Angeles Memorial Coliseum is an American sports stadium located in the Exposition Park neighborhood of Los Angeles, California.  The stadium serves as the home to the University of Southern California (USC) Trojans football team, and as the temporary home of the Los Angeles Rams of the National Football League (NFL).  The Coliseum was home to the Rams from 1946 to 1979, when they moved to Anaheim Stadium in Anaheim, California, and is serving as their home stadium again until the completion of Los Angeles Stadium at Hollywood Park in Inglewood, California.  The facility has a permanent seating capacity of 93,607 for USC football games, making it the largest football stadium in the Pac-12 Conference.  For Rams games, capacity is at 93,607, giving it the largest capacity in the NFL.

Gelora Bung Karno Stadium: The Gelora Bung Karno Main Stadium (formerly Gelora Senayan Main Stadium) is a multi-purpose stadium located within the Gelora Bung Karno Sports Complex, Gelora, Tanah Abang, Central Jakarta, Indonesia.  The stadium is named after Sukarno, Indonesia's first President.  It is mostly used for football matches and has a seating capacity of over 80.000 spectators, though it has been able to hold more than that during special matches.  The final of the 2007 AFC Asian Cup was held in this stadium.  This stadium is the 7th largest association football stadium in the world.

Anfield: Anfield is a football stadium in Anfield, Liverpool, England which has a seating capacity of 54,074 making it the sixth largest football stadium in England.  It has been the home of Liverpool F.C. since their formation in 1892.  It was originally the home of Everton F.C. from 1884 to 1891, before they moved to Goodison Park after a dispute with the club president.

Paul Brown Tiger Stadium: Paul Brown Tiger Stadium is a high school football stadium located in Massillon, Ohio.  It is primarily used for American football, and is the home field of the Massillon Washington High School Tigers football team.  The stadium has a seating capacity of 16,600 spectators, with a maximum capacity of over 19,000 when extra seating is brought in.  The stadium is named after former Tiger and noted football head coach, Paul Brown.

Kyle Field: Kyle Field is the football stadium located on the campus of Texas A&M University in College Station, Texas.  It has been the home to the Texas A&M Aggie football team in rudimentary form since 1904, and as a complete stadium since 1927.  It is known as the ""Home of the 12th Man"".  The seating capacity of 102,733 in 2015 makes the stadium the largest in the Southeastern Conference and the fourth largest stadium in the NCAA, fourth largest stadium in the United States, and the fifth largest non-racing stadium in the world.  Within the state of Texas, Kyle Field has the largest regular seating capacity, while AT&T Stadium has a larger overall capacity.

Salt Lake Stadium: Salt Lake Stadium, officially known as Vivekananda Yuba Bharati Krirangan (VYBK), is a multipurpose stadium in Bidhannagar, Kolkata, West Bengal, with a capacity of 66,687.  It is the largest stadium in India by capacity.  Before its renovation in 2011, it was the second largest football stadium in the world, having a seating capacity of 120,000.  Prior to the construction and opening of Rungrado May Day Stadium in 1989, it was the largest football stadium in the world.  The capacity of the stadium has been decreased from 85,000 to almost 67,000 for the FIFA U-17 World Cup.

Estadio Luis Franzini: The Estadio Luis Franzini (or Luis Franzini Stadium) is an outdoor football stadium located in Montevideo, Uruguay.  The stadium's maximum capacity is 18,000 people, and it is the home ground of Defensor Sporting.  The stadium was closed during the 1997 season for renovations.  It reopened on 16 August 1998 with the name "Nuevo Estadio Luis Franzini".  Renovations included a seating capacity increase and leveling of the playing area.  Previously, the land sloped to the west, toward the Rio de la Plata.

Seating capacity: Seating capacity is the number of people who can be seated in a specific space, in terms of both the physical space available, and limitations set by law.  Seating capacity can be used in the description of anything ranging from an automobile that seats two to a stadium that seats hundreds of thousands of people.  The largest sporting venue in the world, the Indianapolis Motor Speedway, has a permanent seating capacity for more than 235,000 people and infield seating that raises capacity to an approximate 400,000.

Question: What is the seating capacity of the football stadium located in Bill Kinsley birthplace?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person whose birthplace is being investigated."
        },
        "birthplace": {
          "type": "string",
          "description": "The specific location (city/area) where the person was born."
        }
      },
      "required": [
        "name",
        "birthplace"
      ],
      "additionalProperties": false
    },
    "stadium_in_birthplace": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the football stadium located in the person's birthplace."
        },
        "seating_capacity": {
          "type": "integer",
          "description": "The seating capacity of the identified stadium."
        }
      },
      "required": [
        "name",
        "seating_capacity"
      ],
      "additionalProperties": false
    },
    "stadium_location_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the stadium is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the stadium is located."
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_of_interest",
    "stadium_in_birthplace",
    "stadium_location_details"
  ],
  "additionalProperties": false
}
