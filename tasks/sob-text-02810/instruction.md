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
University of Canberra Capitals: The University of Canberra Capitals are an Australian professional women's basketball team competing in the Women's National Basketball League (WNBL).  The team is based in Canberra, Australian Capital Territory.  In 2014 the University of Canberra Union took control of the Capitals from Basketball ACT.  The University of Canberra is the current naming rights sponsor for the Capitals.

Ak-Chin Pavilion: Ak-Chin Pavilion (originally the Desert Sky Pavilion) is an amphitheater located in Phoenix, Arizona, which seats 8,106 under a pavilion roof and an additional 12,000 on a hillside behind the main stands .  It was originally known as Desert Sky Pavilion and opened on November 11, 1990 (Billy Joel was the venue's inaugural performer).  The current naming rights sponsor is the Ak-Chin Indian Community (the venue is not located on tribal land).  With a total capacity of 20,000, its capacity is higher than Talking Stick Resort Arena and Gila River Arena.  The amphitheater's season starts in April and closes in October.

SDCCU Stadium: SDCCU Stadium is a multi-purpose stadium in San Diego, California, United States.  The stadium opened in 1967 as San Diego Stadium and was later known for many years as Jack Murphy Stadium.  From 1997 to 2017, the stadium's naming rights were owned by Qualcomm, a San Diego-based telecommunications equipment company and the stadium was known as Qualcomm Stadium.  The naming rights expired on June 14, 2017 and the stadium was renamed in September 2017.  Currently the naming rights are owned by San Diego County Credit Union who paid $500,000 for the rights through December 31, 2018.

Talen Energy Stadium: Talen Energy Stadium (formerly known as PPL Park) is an American soccer-specific stadium located in Chester, Pennsylvania and is home to the Philadelphia Union of Major League Soccer.  The project is the result of combined commitments of $30 million from Delaware County and $47 million from the Commonwealth of Pennsylvania.  Talen Energy is the stadium's naming rights sponsor.

1965 Golden Fleece Cup: The 1965 VFL Golden Fleece Night Premiership was the Victorian Football League end of season cup competition played in September of the 1965 VFL Premiership Season.  Run as a knock-out tournament, it was contested by the eight VFL teams that failed to make the 1965 VFL finals series.  It was the tenth VFL Night Series competition.  Games were played at the Lake Oval, Albert Park, then the home ground of South Melbourne, as it was the only ground equipped to host night games.  This was the first time the Night Series cup had a naming rights sponsor in Golden Fleece petroleum products.  North Melbourne won its first night series cup defeating Carlton in the final by 40 points.

TDECU Stadium: John O'Quinn Field at TDECU Stadium is an American football stadium on the campus of the University of Houston.  The stadium serves as the home of the Houston Cougars football team, which represents the University of Houston in collegiate football.  TDECU Stadium was built on the former site of Robertson Stadium, which was the intermittent home of the school's football program since 1946.  Its official name is derived from Texas Dow Employees Credit Union (TDECU), the largest credit union in Houston, which purchased its naming rights in the largest-ever naming rights deal for a college football stadium.

Sports Authority Field at Mile High: Sports Authority Field at Mile High, previously known as Invesco Field at Mile High, and commonly known as Mile High or Mile High Stadium, is an American football stadium in Denver, Colorado.  The field is named after a sponsor and the stadium is named Mile High.  The stadium's primary tenant is the Denver Broncos of the National Football League (NFL).  The stadium opened in 2001 to replace Mile High Stadium.  The stadium was largely paid for by taxpayers in the Denver metropolitan area and the property is owned by a special taxing district.  More controversially, Invesco paid $120 million for the original naming rights, before Sports Authority secured the naming rights on August 16, 2011.

2016 Russell Athletic Bowl: The 2016 Russell Athletic Bowl was a post-season American college football bowl game played on December 28, 2016 at the Camping World Stadium in Orlando, Florida.  The 27th edition of the Russell Athletic Bowl featured the Miami Hurricanes of the Atlantic Coast Conference against the West Virginia Mountaineers of the Big 12 Conference.  It was one of the 2016–17 bowl games that concluded the 2016 FBS football season.  The game's naming rights sponsor is the Russell Athletic uniform company.

Courier Mail Piazza: The Courier Mail Piazza is a multi-purpose venue located in the South Bank Parklands in Brisbane, Australia.  The Courier-Mail has been the naming rights sponsor of the venue since 2013, prior to which it was known as the Suncorp Piazza and South Bank Piazza.

Philadelphia Union: The Philadelphia Union is an American professional soccer team based in Chester, Pennsylvania.  The Union competes in Major League Soccer (MLS) as a member club of the league's Eastern Conference.  The club began play in 2010 as an expansion team of the league.  The club plays their home matches at Talen Energy Stadium, a soccer-specific stadium located in Chester, Pennsylvania, on the banks of the Delaware River.  Jim Curtin is the Union's head coach.

Question: Who are the naming rights sponsor for the home stadium of the team Jim Curtin coaches?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    },
    "team_coached": {
      "type": "string",
      "description": "The name of the team coached by the individual."
    },
    "home_stadium_name": {
      "type": "string",
      "description": "The name of the home stadium for the team."
    },
    "stadium_location": {
      "type": "string",
      "description": "The location of the home stadium."
    },
    "stadium_naming_rights_sponsor": {
      "type": "string",
      "description": "The naming rights sponsor for the stadium."
    }
  },
  "required": [
    "coach_name",
    "team_coached",
    "home_stadium_name",
    "stadium_location",
    "stadium_naming_rights_sponsor"
  ],
  "additionalProperties": false
}
