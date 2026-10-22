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
Wisconsin Badgers: The Wisconsin Badgers are the athletic teams representing the University of Wisconsin–Madison (University of Wisconsin).  They compete as a member of the National Collegiate Athletic Association (NCAA) Division I level (Football Bowl Subdivision (FBS) sub-level), primarily competing in the Big Ten Conference for all sports since the 1896–97 season.  Men's sports include basketball, cross country, football, golf, ice hockey, rowing, soccer, swimming & diving, tennis, track & field and wrestling, while women's sports include basketball, cross country, golf, ice hockey, rowing, lightweight rowing, soccer, softball, swimming & diving, tennis, track & field and volleyball.  The women's ice hockey team competes in the Western Collegiate Hockey Association (WCHA), while the men's and lightweight women's crew team compete in the Eastern Association of Rowing Colleges (EARC).

Llanfyllin Town F.C.: Llanfyllin Town Football Club are a football club from Llanfyllin, Powys.  While the Llanfyllin Men's Senior team currently compete in the 5th tier of Welsh football and play in the Montgomeryshire Amateur League Division One, the club field an under 19's youth team in the Central Wales Youth League and the Ladies team compete in the Dave Smith North Powys League.

Raheny United F.C.: Raheny United Football Club (Irish: "Cumann Peile Ráth Éanna Aontaithe" ) is an Irish association football club based in Raheny, Dublin.  Raheny United was founded in 1994 following the amalgamation of Raheny Boys and Dunseedy United.  In 2016-17 their senior men's team compete in the Premier B division of the Athletic Union League.  An over–35s team compete in the Amateur Football League.  They also have 21 schoolboy teams competing in both the Dublin & District Schoolboy League and the North Dublin Schoolboys/Girls League.  The club however is perhaps best known for its senior women's team who in 2011–12 became founder members of the Women's National League.  They were league champions in both 2012–13 and 2013–14 and also competed in both the 2013–14 and the 2014–15 UEFA Women's Champions League.  In 2015 Raheny United's senior women's team merged with Shelbourne Ladies F.C..  This effectively saw Shelbourne take Raheny United's place in the WNL.The club currently cater for four senior teams, twenty schoolboy teams, and host their own youth academy every Saturday morning, making them one of the larger junior soccer clubs in Ireland.

Leicester Storm: Leicester Storm are an amateur community rugby league football club based in Leicester, England.  They compete in the Conference League South and their Academy Team compete in the 3v Sport Midlands Rugby League.  The club's home is Phoenix Park which is in the suburb of Saffron Lane, South-West Leicester, where they have played since 2006.  Leicester are one of the oldest clubs in the Rugby League Conference.

Ajax København: Ajax København is a handball club based in northern Copenhagen, Denmark, consisting of both a women's and a men's team.  As of the 2017-18 season, the women's team compete in Primo Tours Ligaen, the highest women's league in Denmark, whereas the men's team compete in the 1st Division.  Ajax København play their home matches in Bavnehøj-Hallen.

Delaware State Hornets football: The Delaware State Hornets football team compete in Division I FCS, and are full-members of the Mid-Eastern Athletic Conference.  They are a four-time conference champion and made their first-ever FCS playoff appearance in 2007.  They play at the 7,193-seat Alumni Stadium located in Dover, Delaware.  The facility opened in 1957 as a multi-purpose for football, and track and field.

Walsall F.C. Youth and Reserves: Walsall Football Club are represented at Reserve and Youth team level by the Walsall Development Squad and Walsall Academy.  The Development Squad currently compete in the Central League North-West Division and the Academy team compete in the Youth Alliance North-West Division.

Calvin Bird: James Calvin Bird (February 11, 1938 – June 19, 2013) was an American football player who played college football for the Kentucky Wildcats of the University of Kentucky and spent an off-season in the American Football League (AFL) with the New York Jets.

Kentucky Wildcats football: The Kentucky Wildcats football program represents the University of Kentucky in the sport of American football.  The Wildcats compete in the Football Bowl Subdivision (FBS) of the National Collegiate Athletic Association (NCAA) and the Eastern Division of the Southeastern Conference (SEC).

Georgia Southern Equestrian Team: The Georgia Southern Equestrian Team (GSUET) is a club sport available to students at Georgia Southern University.  The club develops an understanding in equestrian activities and horsemanship and unites collegiate horse owners, riders, and anyone interested in horses.  It introduces members to equine activities in the community.  Team members who join the Intercollegiate Horse Show Association (IHSA) compete with other IHSA team in horse shows hosted by different barns in the southeast.  Individuals and the team compete in Zone 5, Region 3 of the IHSA.  Each member takes two lessons a week.  The Georgia Southern Equestrian Team students are taught grooming, feeding, and health care skills.  All riding disciplines are presented and the facility provides well-trained horses for the riders.  The GSUET is funded mostly by its members' team fees.  However, each year the team is also allotted a budget from Georgia Southern's CRI (Campus Recreation and Intramurals).  Many of the saddles and other tack used by the team are purchased through CRI.  Team members pay for their own riding lessons, riding attire, show clothes, and entry fees for shows.

Question: In which conference does Calvin Bird's team compete?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player played for."
    },
    "team_competition_details": {
      "type": "object",
      "description": "Details about the team's competitive affiliations.",
      "properties": {
        "main_competition_organization": {
          "type": "string",
          "description": "The primary national collegiate athletic organization the team competes under."
        },
        "division_level": {
          "type": "string",
          "description": "The specific division level within the main competition organization."
        },
        "conference": {
          "type": "string",
          "description": "The specific athletic conference the team is a member of."
        },
        "conference_division": {
          "type": "string",
          "description": "The division within their specific athletic conference."
        }
      },
      "required": [
        "main_competition_organization",
        "division_level",
        "conference",
        "conference_division"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "team_name",
    "team_competition_details"
  ],
  "additionalProperties": false
}
